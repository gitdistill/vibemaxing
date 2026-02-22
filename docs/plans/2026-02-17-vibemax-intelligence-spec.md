# Extension Design Outline (Proposed)

## 1. Extension Identity

*   **Name:** `vibemax-intelligence`
*   **Location:** `.pi/extensions/vibemax-intelligence/`
*   **Entry Point:** `src/index.ts`
*   **Capabilities:**
    *   **Research Tools:** Query Context7 for Max/MSP docs.
    *   **Augmentation:** Write to local `maxpylang` database.

## 2. Environment

*   **Required Variable:** `CONTEXT7_API_KEY`
    *   **Source:** Loaded from the agent's environment or `.env` file.
    *   **Usage:** Authenticates requests to the Context7 documentation service.

## 3. Lifecycle Management

*   **Activation (`activate`):**
    *   **Cache Initialization:** Ensure the local cache directory `.pi/cache/vibemax-intelligence/` exists.

## 4. Core Components

### A. Context7 Client (`src/client.ts`)
*   **Library ID:** `/websites/cycling74` (Verified).
*   **Base URL:** `https://context7.com/api/v2/`
*   **Authentication:** Header `Authorization: Bearer <CONTEXT7_API_KEY>`

<verify task="check c7 api docs for all">
*   **Primary Method:** `getContext(query: string)`
    *   **Endpoint:** `GET /context`
    *   **Params:** `libraryId=/websites/cycling74`, `query=<search_term>`, `type=json`
    *   **Response Handling:** Parses `codeSnippets` (for object structure) and `infoSnippets` (for description).
</verify>

### B. Cache Manager (`src/cache.ts`)
*   **Directory:** `.pi/cache/vibemax-intelligence/`.

<verify task="clarify why md5 hash, are there other ways?">
*   **Key Strategy:** Hash the query + type (e.g., `md5("object:poly~")`).
</verify>

*   **Logic:** Check cache -> Hit (return JSON) -> Miss (fetch API -> write cache -> return JSON).

### C. Augmenter (`src/augmenter.ts`)

<verify task="naming">
*   **Data Source:** Uses `Context7Client` to get raw object JSON.
</verify>

*   **Format:** Converts raw JSON -> `maxpylang` schema.
*   **Destination:** `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{name}.json`.

### D. Navigation Provider (`src/navigation.ts`)
<verify task="schema design">
*   **Asset:** `assets/navigation.json` (A comprehensive, taxonomic map).
</verify>
<verify task="innaccurate url">
*   **Requirement:** Identify "Landing Page" URLs (e.g., `/userguide/audio/`) and return their index/overview content to facilitate high-level browsing.
</verify>

## 5. Tools (Agent API)

### A. `research_max(query: string) -> JSON`
*   **Description:** The primary research tool. Queries the Context7 documentation engine for Max/MSP/Jitter.
*   **Behavior:**
    *   Calls `client.getContext(query)`.

<verify task="validate property names and inferred values">
    *   Returns the raw JSON response containing `codeSnippets` (technical examples) and `infoSnippets` (guides/descriptions).
    *   **Caching:** Hashes the query key and checks local cache before network call.
</verify>

### B. `augment_max_db(object_name: string, category: string) -> String`
*   **Description:** Writes object metadata to the local `maxpylang` database.
*   **Arguments:**
    *   `object_name`: Exact object name (e.g., `poly~`).
    *   `category`: Subfolder in `OBJ_INFO` (e.g., `max`, `msp`, `jitter`).
*   **Process:**
    1.  Calls `research_max(object_name)` internally to get the object's JSON.
    2.  Parses the JSON to extract inlets, outlets, and messages.
    3.  Writes to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{object_name}.json`.

<verify task="examples and/or schema">
### C. `get_navigation(path?: string, filter?: string) -> JSON`
*   **Description:** Returns the documentation hierarchy or specific branch of the Cycling '74 website.
*   **Arguments:**
    *   `path`: The semantic path (e.g., `user_guide/Audio`).
    *   `filter`: Optional filter for `package` (e.g., `MC`) or `kind` (e.g., `Gen DSP Operator`).
*   **Usage:**
    *   No path: Returns top-level buckets.
    *   With path: Returns specific articles and their canonical URLs.
    *   With filter: Returns only entries matching the specified package or kind.
</verify>

## 6. Skill Integration (`SKILL.md`)

*   **Goal:** Establish a rigorous research-before-implementation workflow.

### Research Methodology

<verify task="verify steps, mappings, examples, consider redoing">
1.  **Structured Discovery (Taxonomy First)**
    *   **Requirement:** Do not guess search terms. Use `get_navigation(path)` to locate the correct documentation "Bucket," "Package," or "Series."
    *   **Mapping:**
        *   **Live/M4L:** Use `reference/api/LOM`.
        *   **DSP/Gen:** Use `reference/objects/packages/Gen`.
        *   **Jitter:** Use `reference/objects/packages/Jitter`.
2.  **Behavioral Research (Concepts & Patterns)**
    *   **Action:** Call `research_max(url)` on relevant *User Guide* or *Learn* articles found in step 1.
    *   **Goal:** Understand design patterns (e.g., "How to handle polyphony voice allocation") before selecting objects.
    *   **Cross-Reference:** Identify all objects listed in the "See Also" section of these articles.
3.  **Technical Research (Object Specs)**
    *   **Action:** Call `research_max(object_name)` for every identified object.
    *   **Goal:** Retrieve exact inlet/outlet counts, argument types, and messages.
    *   **Constraint:** You must use this raw technical data to validate your patching plan.
4.  **Architectural Verification**
    *   **Requirement:** Compare your proposed patch design against the technical specs.
    *   **Pivot:** If an object lacks a required message or inlet, you must revise your architecture *before* writing any code.
</verify>

5.  **Augmentation**
    *   **Action:** If a required object is missing from the local database, call `augment_max_db`.
    *   **Categorization:**
        *   Ends with `~` -> `msp`
        *   Starts with `jit.` -> `jitter`
        *   Otherwise -> `max`

</verify task="what is ctx? what are these props?">
## 7. User Interface (TUI)
*   **Notifications:** Show `ctx.ui.notify` on successful cache hits or new fetches.
*   **Progress:** Use `ctx.ui.setWorkingMessage` during network calls.
</verify>

</verify task="design error codes">
## 8. Error Handling
*   **Context7 Errors:** Map 404/429 codes to user-friendly notifications.
*   **File System:** Handle write permission errors gracefully.
</verify>

## 9. File Structure
*   `package.json`
*   `src/index.ts` (Entry point)
*   `src/client.ts` (Context7 interaction)
*   `src/cache.ts` (Persistence)
*   `src/navigation.ts` (Hierarchy browser)
*   `src/augmenter.ts` (Local DB writer)
*   `src/tools.ts` (Tool definitions)
*   `assets/navigation.json` (The semantic map)
