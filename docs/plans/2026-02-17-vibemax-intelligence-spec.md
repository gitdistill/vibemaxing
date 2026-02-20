# Technical Spec: VibeMax Intelligence Extension

**Status:** Active Reference (See Master Plan for Sequence)
**Goal:** Pi extension (TS/JS) providing deep documentation access and DB augmentation.

## 1. Tool Definitions

### A. Research Tools (Read-Only)
*   **`research_topic(query: string, section?: string) -> JSON`**: Conceptual guides/tutorials.
*   **`research_object(object_name: string) -> JSON`**: Technical reference (inlets, outlets, messages, attributes).
*   **`research_js_api(method: string) -> JSON`**: Max JavaScript API methods.
*   **`research_lom(path: string) -> JSON`**: Live Object Model paths and properties.
*   **`search_max_objects(query: string) -> List<String>`**: Fuzzy search for candidate names.

### B. Augmentation Tools (Write)
*   **`augment_max_db(object_name: string, category: string) -> String`**:
    *   Fetches metadata via `research_object`.
    *   Formats as `maxpylang` JSON.
    *   Writes to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{object_name}.json`.

## 2. Caching (Cache-First Logic)
*   **Storage:** `.pi/cache/vibemax-intelligence/`.
*   **Behavior:** Check cache before API call. Persist all new responses. Cache is permanent unless manually cleared.

## 3. Configuration
*   **API Key:** `CONTEXT7_API_KEY` (from environment or extension settings).
*   **Sitemap:** Extension includes `assets/sitemap.json` for hierarchical browsing.
