# Plan: CycleScraper Implementation

Implement a specialized web scraper to transform Cycling '74 documentation into an agent-friendly Markdown knowledge base.

## Context
The `CycleScraper` tool is required to populate the `vibemax-intelligence` Pi extension with technical documentation, API references, and tutorials from `docs.cycling74.com`. It must produce a structured `knowledge-map.json` and a collection of Markdown files with YAML frontmatter.

## Approach
- **Core Engine**: Use `crawl4ai` for asynchronous crawling and high-quality HTML-to-Markdown conversion.
- **Source of Truth**: All scraping is driven by `docs/seeds.json`.
- **Concurrency**: Process URLs in batches to respect rate limits and manage resources.
- **Output**:
  - `data/content/`: Organized hierarchy of `.md` files.
  - `knowledge-map.json`: Hierarchical index for the agent.

## Files to Create
- `apps/cyclescraper/requirements.txt`: Dependencies (`crawl4ai`, `beautifulsoup4`, `pyyaml`, `pydantic`).
- `apps/cyclescraper/main.py`: Main orchestration script.
- `apps/cyclescraper/models.py`: Pydantic models for the knowledge map and configuration.
- `apps/cyclescraper/processors/`:
    - `user_guide.py`: Logic for User Guide section.
    - `api_ref.py`: Logic for API Reference (LOM, JS, Node).
    - `learn.py`: Logic for Learn section (Series and Articles).
- `apps/cyclescraper/utils/`:
    - `markdown.py`: Custom post-processing for math and images.
    - `crawler.py`: Crawl4AI configuration and wrapper (using `AsyncWebCrawler` and `CrawlerRunConfig`).
    - `files.py`: Directory and file management.

## Reuse
- `docs/seeds.json`: Entry points and static descriptions.
- `docs/*-spec.md`: Detailed selector logic and extraction patterns.

## Steps

### 1. Project Initialization
- [x] Create `apps/cyclescraper/` directory structure.
- [x] Create `requirements.txt` and install dependencies.
- [x] Initialize `crawl4ai` (e.g., `playwright install chromium`).

### 2. Core Infrastructure
- [x] Define data models in `models.py` (e.g., `KnowledgeNode`, `KnowledgeMap`).
- [x] Implement `utils/crawler.py` with standard `CrawlerRunConfig`:
    - `excluded_tags`: `header`, `nav`, `footer`, `aside`, `.sidebar`, `.cookie-banner`, `script`, `style`, `iframe`, `.blocks_anchorLink__kJCjR`, `.article_metaWrapper__ARyDO`.
    - `css_selector`: `.c74-article-content`.
    - `markdown_generator`: `DefaultMarkdownGenerator(options={"absolute_urls": True})`.
- [x] Implement `main.py` with `asyncio` and `seeds.json` loading.

### 3. Build & Unit Test Processors (No full scraping yet)
- [x] Implement `processors/user_guide.py`.
- [x] Implement `processors/api_ref.py` (including specialized selectors from `api-ref-page-spec.md` for signatures and parameter tables).
- [x] Implement `processors/learn.py`:
    - [x] Handle "See Also" and metadata extraction via `JsonCssExtractionStrategy`.
    - [x] Index parsing (`parse_learn_index`).
    - [x] Integrate `parse_series_page` into `discovery.py` to build actual `series` nodes in `seeds.json`.
    - [x] Map the articles discovered in `parse_series_page` to the list of URLs in `seeds.json` to organize the `page` nodes correctly under their respective `series` nodes.
    - [x] Run an integration test on a single series (e.g. `javascript-custom-drawing/`) and 1 of its articles to verify the proper nested structure (`section` -> `series` -> `page`) is serialized correctly without mock nodes.
- [x] Implement `processors/api_ref.py`:
    - [x] Move index parsing to `discovery.py` to pre-group API pages by their `apiGroup`.
    - [x] Update processor to use the structured hierarchy from `seeds.json`.
- [x] Implement `utils/markdown.py` to:
    - Ensure all math blocks (`<annotation encoding="application/x-tex">`) are converted to `$$ ... $$`.
    - Final check on absolute image URLs.
- [x] Implement Strategy & Concurrency logic: Use `arun_many` with a `Semaphore` or `max_concurrent=10`, configure `RetryConfig` (e.g., exponential backoff), and periodic saves to `knowledge-map.partial.json`.

### 4. Verification & Testing
- [x] **Dry Run**: Print the URLs that would be visited and the expected output paths.
- [x] **Unit Tests**: Test the metadata and content extraction on local HTML snapshots.
- [x] **Integration Test (User Guide)**: Run the scraper on a small subset (e.g., "Colors" group in User Guide) and verify output. Enable Crawl4AI caching (`cache_mode=CacheMode.ENABLED`) during tests.
- [x] **Integration Test (API Ref & Learn)**: Run a small subset of the API Reference (e.g. 1 LOM object) and Learn section (e.g. 1 article) to verify their distinct structures, specialized selectors, and knowledge map integration.
- [x] **Quality Check**: Manually inspect 5 random Markdown files for formatting and frontmatter.

### 5. Full Production Scrape
- [ ] **Discovery Update (Learn Section)**:
    - [ ] Refactor `apps/cyclescraper/discovery.py` to scrape the 6 Series landing pages.
    - [ ] Extract hierarchy: `Series -> Group (H2) -> Article (Title, URL, Blurb)`.
    - [ ] **Safety Mechanism**: Compare discovered URLs against the original flat `articles` list in `seeds.json`; any missing URLs go into `unmatched_articles`.
    - [ ] Update `docs/seeds.json` with the new nested structure.
- [ ] **Processor Update (Learn Section)**:
    - [ ] Refactor `apps/cyclescraper/processors/learn.py` to handle the 4-level hierarchy.
    - [ ] Ensure `KnowledgeNode` objects are created for Series and Groups.
    - [ ] Use pre-scraped titles and blurbs from `seeds.json` for article nodes.
- [X] **Calibration Pass**: Manually inspect 1 page of each type (User Guide, API Ref, Learn) to verify content extraction.
    - [X] Confirm "See Also" sections are kept (handled by default markdown generation).
- [X] **Infrastructure Upgrade**:
    - [x] Implement `BrowserConfig` with stealth/user-agent settings.
    - [x] Implement `wait_for` logic in `CrawlerRunConfig` to handle dynamic content.
    - [X] Refactor `process_api_ref` and `process_user_guide` to use `arun_many` for optimized batch processing (concurrency limits added).
- [ ] Remove final test limits/guards from all processors.
- [ ] **Execution**:
    - [ ] **Section 1: User Guide**: Scrape all pages grouped by the `seeds.json` structure. Generate Markdown files in `data/content/userguide/[group]/[slug].md`.
    - [ ] **Section 2: API Reference**: Scrape all pages for LOM, JS, and Node using the structured groups and descriptions from `seeds.json`.
    - [ ] **Section 3: Learn**: Scrape all articles nested within their respective series as defined in `seeds.json`. (No specific extraction strategy applied, using default markdown).
- [X] **Knowledge Map Consolidation**: Aggregate all results into the final `knowledge-map.json` ensuring no empty `children` fields.
- [ ] **Validation**: Verify that all `filePath` entries in `knowledge-map.json` exist on disk.
- [ ] **Completeness Check**: Final inspection of representative Markdown files from each section for formatting and metadata.
