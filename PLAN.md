# Plan: CycleScraper Sequential Refactor & Staged Execution

## Context
The initial concurrent scraping architecture (`crawler.arun_many()`) caused data corruption due to Next.js SPA state leakage across shared browser tabs. To fix this, we must process URLs sequentially. As verified by testing, using `await crawler.arun()` in a standard `for` loop guarantees strict isolation and completely eliminates the Next.js router collisions, which is the most robust approach for this specific SPA without introducing complex session management overhead.

Because sequential scraping takes much longer (~10-15 minutes for a full run), we need to support staged, modular execution (by section and sub-section) so developers can spot-check and debug without running the full suite. 

Furthermore, we need to decouple Knowledge Map generation from the scraping process. The sole purpose of the Knowledge Map is to provide a hierarchical Table of Contents that an expert agent can read to deterministically locate relevant documentation. (Note: For ~450 files, passing a structured JSON map to the agent is a highly effective, deterministic alternative to vector search/RAG, and is absolutely the right approach here).

## Approach
1. **Sequential Refactor**: Replace all instances of `arun_many()` with a standard `for` loop using `await crawler.arun()` in the processors to guarantee data integrity.
2. **CLI Staged Execution**: Implement `argparse` in `main.py` to allow running the scraper by section and sub-section.
3. **Sub-section Filtering**: Update each processor to optionally filter its task list based on the requested sub-section.
4. **Enhanced Frontmatter**: Processors will inject structural metadata (`section`, `group`, `kind`) directly into each Markdown file's frontmatter.
5. **Decouple Knowledge Map**: 
   - Scraping processors will *only* be responsible for fetching URLs, cleaning markdown, and saving files (with enriched frontmatter). 
   - A standalone `apps/cyclescraper/build_map.py` script will simply glob all `.md` files in `data/content/`, read their frontmatter to reconstruct the hierarchy, and output the final `knowledge-map.json`. This makes the map generation 100% independent of the scraping execution order.

## Files to Modify/Create
- `apps/cyclescraper/main.py`: Add `argparse` for `--section` and `--sub-section` flags. Remove knowledge map saving logic.
- `apps/cyclescraper/processors/user_guide.py`: Remove `arun_many()`, implement sequential processing, add filtering by group (e.g., `audio`). Update frontmatter to include `section: User Guide`, `group: <group_name>`, and `kind: guide`.
- `apps/cyclescraper/processors/api_ref.py`: Remove `arun_many()`, implement sequential processing, add filtering by API index (e.g., `lom`). Update frontmatter to include `section: API Reference`, `group: <api_id>`, and `kind: api-page`.
- `apps/cyclescraper/processors/learn.py`: Remove `arun_many()`, implement sequential processing, add filtering by series slug. Update frontmatter to include `section: Learn`, `group: <series_title>`, and `kind: tutorial`.
- **[New]** `apps/cyclescraper/build_map.py`: Standalone script to glob `data/content/**/*.md`, read frontmatter, and dynamically compile `knowledge-map.json`.

## Steps
- [x] **Step 1: CLI Configuration in `main.py`**
  - Add `argparse` with `--section` (choices: `userguide`, `apiref`, `learn`, `all`) and `--sub-section` (string).
  - Remove the global `knowledge_map` dictionary and `save_partial` logic.
- [x] **Step 2: Refactor `user_guide.py`**
  - Add `sub_section` filtering (match against group name).
  - Replace `arun_many` with sequential `for url in tasks: await crawler.arun(url)`.
  - Enrich frontmatter dictionary with `section`, `group`, and `kind`.
  - Remove `KnowledgeNode` creation.
- [x] **Step 3: Refactor `api_ref.py`**
  - Add `sub_section` filtering (match against `lom`, `js`, `nodeformax`).
  - Replace `arun_many` with sequential `for task in section_tasks: await crawler.arun(url)`.
  - Enrich frontmatter dictionary with `section`, `group`, and `kind`.
  - Remove `KnowledgeNode` creation.
- [x] **Step 4: Refactor `learn.py`**
  - Add `sub_section` filtering (match against series slug or title).
  - Enforce sequential `await crawler.arun()` for all article fetches.
  - Enrich frontmatter dictionary with `section`, `group`, and `kind`.
  - Remove `KnowledgeNode` creation.
- [x] **Step 5: Create `build_map.py`**
  - Write a script that uses `pathlib.Path.rglob('*.md')` to find all scraped documents.
  - Read YAML frontmatter from each file.
  - Group the files hierarchically by `section` -> `group` -> `file` and output to `knowledge-map.json`.

## Verification
- Run a subset: `python apps/cyclescraper/main.py --section apiref --sub-section nodeformax`.
- Verify 20 files are created correctly, sequentially, and contain the new structural frontmatter keys.
- Run `python apps/cyclescraper/build_map.py`.
- Check that `knowledge-map.json` contains ONLY the `nodeformax` nodes since those are the only files present on disk, successfully proving the decoupled architecture works.
