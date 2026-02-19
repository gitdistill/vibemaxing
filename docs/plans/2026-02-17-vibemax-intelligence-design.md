# Design: VibeMax Intelligence Extension

**Date:** 2026-02-17
**Status:** Design Phase
**Goal:** Create a Pi extension that empowers the agent to act as a "Max/MSP Expert" by providing deep access to Cycling '74 documentation, including objects, guides, tutorials, JS API, and the Live Object Model (LOM).

## 1. Overview

The `vibemax-intelligence` extension decouples the "research" capability from the `maxpatcher` builder. It serves as the primary interface for the agent to learn about Max/MSP concepts and technical details *before* designing or implementing solutions.

**Key Features:**
*   **Comprehensive Research:** Access to Objects, Guides, Tutorials, JS API, and LOM.
*   **Database Augmentation:** Ability to fetch object metadata and write it to the local `maxpylang` database (`apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`).
*   **Skill Integration:** A dedicated `SKILL.md` (content provided by user) teaches the agent how to navigate the documentation effectively.

## 2. Architecture

### Directory Structure
```text
.pi/extensions/vibemax-intelligence/
├── package.json          # Node dependencies
├── extension.json        # Pi extension manifest
├── src/
│   ├── context7.ts       # The Context7 API client
│   ├── researcher.ts     # Logic for querying docs (Objects, Guides, JS, LOM)
│   ├── augmenter.ts      # Logic for writing to maxpylang DB
│   └── util.ts           # JSON formatting
├── assets/
│   └── sitemap.json      # Structured map of docs.cycling74.com
└── SKILL.md              # Agent instructions (provided by user)
```

### Configuration
*   **API Key:** The extension will load the Context7 API key from the environment (`CONTEXT7_API_KEY`) or extension settings.

## 3. Tools Provided

### A. Research Tools (Read-Only)

1.  **`research_topic(query: string, section?: string) -> JSON`**
    *   **Description:** Searches for conceptual documentation, guides, and tutorials.
    *   **Arguments:**
        *   `query`: The search term (e.g., "gen~ codebox", "signal flow").
        *   `section`: Optional filter (e.g., "guides", "tutorials", "reference").
    *   **Returns:** Raw JSON content of the matching guide/tutorial.

2.  **`research_object(object_name: string) -> JSON`**
    *   **Description:** Retrieves technical reference for a specific Max object.
    *   **Arguments:** `object_name` (e.g., "poly~").
    *   **Returns:** Raw JSON (inlets, outlets, messages, attributes).

3.  **`research_js_api(method: string) -> JSON`**
    *   **Description:** Retrieves documentation for Max JavaScript API methods.
    *   **Arguments:** `method` (e.g., "Patcher.newdefault").
    *   **Returns:** Raw JSON description and signature.

4.  **`research_lom(path: string) -> JSON`**
    *   **Description:** Retrieves documentation for the Live Object Model.
    *   **Arguments:** `path` (e.g., "live_set tracks 0 devices 0").
    *   **Returns:** Raw JSON of properties and children.

5.  **`search_max_objects(query: string) -> List<String>`**
    *   **Description:** fuzzy search for object names.
    *   **Returns:** List of candidate names (e.g., `["poly~", "poly", "polybuffer~"]`).

### B. Augmentation Tools (Write)

1.  **`augment_max_db(object_name: string, category: string) -> String`**
    *   **Description:** Fetches object metadata and writes it to the local `maxpylang` database.
    *   **Arguments:**
        *   `object_name`: The exact name of the object (e.g., "poly~").
        *   `category`: The subfolder in `OBJ_INFO` (e.g., "max", "msp", "jitter").
    *   **Behavior:**
        *   Fetches metadata via `research_object`.
        *   Formats as `maxpylang` JSON.
        *   Writes to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{object_name}.json`.
        *   **Does NOT commit to git.**
    *   **Returns:** Success message with file path.

## 4. Skill Integration

The extension will include a `SKILL.md` that guides the agent's workflow.
*   **Content:** To be provided by the user.
*   **Focus:** Navigating the documentation hierarchy (Guides vs. Reference), understanding the LOM structure, and effective search strategies.

## 5. Caching Strategy (Persistence & Quota Protection)

To protect Context7 API quotas and ensure fast, offline-first responses, the extension implements a **Cache-First** logic.

*   **Storage Location:** `.pi/cache/vibemax-intelligence/` (JSON files organized by type/query).
*   **The "Check-Before-Query" Loop:**
    1.  **Intercept:** Every `research_*` call first hashes the query/parameters to generate a cache key.
    2.  **Lookup:** Check the local cache directory for a matching JSON file.
    3.  **Hit:** If found, return the cached JSON immediately (Zero API cost).
    4.  **Miss:** If not found:
        *   Execute the Context7 API request.
        *   Validate and format the response.
        *   **Persist:** Write the result to the local cache.
        *   Return the data to the agent.
*   **Data Integrity:** Since documentation for stable Max objects rarely changes, the cache is considered "Permanent" unless manually cleared by the user.

## 6. Next Steps
1.  **Implement Extension:** Scaffold the TypeScript project.
2.  **Populate SKILL.md:** User to provide the specific content.
3.  **Integrate:** Agent uses the new tools to assist with `maxpatcher` refactoring.
