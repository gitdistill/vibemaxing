### Context
The `build_map.py` script generates the final `knowledge-map.json`, but currently, higher-level non-page fields (sections and groups) are lacking meaningful `description`, `sourceUrl`, and proper `title` fields. 

The user wants to use `docs/seeds.json` to enrich the metadata for groups across all three sections:
- **Learn:** Use series `title`, `description`, and `url` from `seeds.json`.
- **API Reference:** Map the existing group slugs (`"js"`, `"lom"`, `"nodeformax"`) to their full titles (`"Javascript API"`, `"Live Object Model"`, `"Node for Max"`) and extract `description` and `index` (as `sourceUrl`) from `seeds.json`.
- **User Guide:** Use the description already present in `seeds.json` for each User Guide group.
- **Top-level Sections:** Add top-level descriptions for the 3 main sections (Learn, API Reference, User Guide).

### Approach
1. **Load `seeds.json`:** Add a helper in `build_map.py` to parse `docs/seeds.json`.
2. **Enrich Group Nodes:** Before creating a `KnowledgeNode` of type `group`, look up its metadata:
   - For `Learn`, iterate over `urlset.sections["Learn"]["series"]` to find the matching title.
   - For `API Reference`, map `"js"`, `"lom"`, and `"nodeformax"` to the keys in `urlset.sections["API Reference"]` to get the metadata.
   - For `User Guide`, look up the group name directly in `urlset.sections["User Guide"]`.
3. **Enrich Section Nodes:** Hardcode appropriate top-level descriptions for the 3 main sections ("Learn", "API Reference", "User Guide") instead of generic fallbacks.

### Files to modify
- `apps/cyclescraper/build_map.py`

### Reuse
- `json` and `Path` are already used/available in `build_map.py`.
- No new models needed; `KnowledgeNode` already supports `title`, `description`, and `sourceUrl`.

### Steps
- [x] Modify `apps/cyclescraper/build_map.py` to load `docs/seeds.json` into memory.
- [x] Add helper functions to fetch metadata for Learn, API Reference, and User Guide groups based on their name/slug.
- [x] Update the section & group node creation loops to fetch and use this metadata for `title`, `description`, and `sourceUrl`.
- [x] Add static top-level descriptions for "Learn", "API Reference", and "User Guide".
- [x] Run `python apps/cyclescraper/build_map.py` to verify the resulting `knowledge-map.json` contains the enriched fields.

### Verification
- Ensure `python apps/cyclescraper/build_map.py` runs without errors.
- Inspect `data/knowledge-map.json` to verify that `type: "group"` and `type: "section"` nodes have populated `description` and `sourceUrl` (where applicable) and correct titles.
