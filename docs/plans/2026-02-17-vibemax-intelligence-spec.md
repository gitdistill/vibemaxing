# Technical Spec: VibeMax Intelligence Extension

**Status:** Active Reference (See Master Plan for Sequence)
**Goal:** Pi extension (TS/JS) providing deep documentation access and DB augmentation.

## 1. Tool Definitions

### A. Research Tools (Read-Only)
*   **`research_topic(query: string, section?: string) -> JSON`**: Fetches raw JSON content for conceptual guides, tutorials, or LOM/JS references.
*   **`research_object(object_name: string) -> JSON`**: Retrieves technical reference (inlets, outlets, messages, attributes) for a specific Max object.
*   **`search_objects(query: string) -> List<String>`**: 
    *   **Logic:** Fuzzy search for object names. 
    *   **The "List & Pick" Rule:** If a query is ambiguous (e.g., "poly"), this tool returns all candidates. The agent/user MUST then use a specific name from this list for `augment_max_db`.

### B. Augmentation Tools (Write)
*   **`augment_max_db(object_name: string, category: string) -> String`**:
    *   **Requirement:** Requires an exact `object_name` (validated via `search_objects`).
    *   **Action:** Fetches metadata via `research_object`, formats as `maxpylang` JSON, and writes to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{object_name}.json`.
    *   **Local Only:** Does NOT perform git commits.

## 2. Caching (Cache-First Logic)
*   **Storage:** `.pi/cache/vibemax-intelligence/`.
*   **Behavior:** Check cache before API call. Persist all new responses. Cache is permanent unless manually cleared.

## 3. Configuration & Assets
*   **API Key:** `CONTEXT7_API_KEY` (from environment or extension settings).
*   **Sitemap:** Extension includes `assets/sitemap.json` (provided by user) for hierarchical browsing of docs.cycling74.com.
*   **Skill Integration:** Includes `SKILL.md` (content provided by user) with specific navigation instructions.
