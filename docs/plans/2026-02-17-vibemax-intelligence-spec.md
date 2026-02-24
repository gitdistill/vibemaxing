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
*   **Export:** `Context7Client` (Class)
*   **Library ID:** `/websites/cycling74` (Verified).
*   **Base URL:** `https://context7.com/api/v2/`
*   **Authentication:** Header `Authorization: Bearer <CONTEXT7_API_KEY>`
*   **Primary Method:** `getContext(query: string)`
    *   **Endpoint:** `GET /context`
    *   **Params:** `libraryId=/websites/cycling74`, `query=<search_term>`, `type=json`
<verify task="incorrect, this is also mentioned below">    
    *   **Response Handling:** Parses `codeSnippets` (for object structure) and `infoSnippets` (for description).
</verify>

### B. Cache Manager (`src/cache.ts`)
*   **Directory:** `.pi/cache/vibemax-intelligence/`.
*   **Key Strategy:** MD5 Hash of the normalized query string (e.g., `md5("object:poly~")`).
*   **Logic:** Check cache -> Hit (return JSON) -> Miss (fetch API -> write cache -> return JSON).

### C. Augmenter (`src/augmenter.ts`)
   *   **Dependency:** Receives an instance of `Context7Client`.
   *   **Data Source:** Calls `Context7Client.getContext(object_name)` to retrieve the raw JSON.
   *   **Logic:**
    1.  Fetch raw data.
    2.  Transform Context7 JSON into the `maxpylang` schema.
    3.  Write to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`.   

### D. Navigation Provider (`src/navigation.ts`)
*   **Asset:** `assets/navigation.json` (A comprehensive, taxonomic map).
    *   **Purpose:** Provides a static, pre-processed map of the Cycling '74 documentation hierarchy to aid the agent in discovery and browsing. This asset is loaded once by the extension.
    *   **Schema Design:** Refer to `docs/plans/2026-02-21-navigation-map-design.md` for the detailed structure of `assets/navigation.json`.

*   **Requirement:** Identify "Landing Page" URLs (e.g., `/userguide/audio/`) and return their index/overview content to facilitate high-level browsing.


## 5. Tools (Agent API)

### A. `research_max(query: string) -> JSON`
*   **Description:** The primary research tool. Queries the Context7 documentation engine for Max/MSP/Jitter.
*   **Behavior:**
    *   Calls `client.getContext(query)`.

<verify task="property names and uses are incorrect, need to validate with real responses">
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

*   **Goal:** Enable "Research-First Development" by mapping user intent to the specific Cycling '74 documentation hierarchy.

### A. Documentation Router (Decision Tree)
Before querying, determine the *type* of knowledge required:
1.  **Technical Verification:** Need input/output specs for a specific object? -> **Use Object Reference**.
2.  **Conceptual Understanding:** Need to understand a system (e.g., "How MC works")? -> **Use User Guide** *(TBD)*.
3.  **Scripting & Control:** Need to control Live or write JS? -> **Use API Reference** *(TBD)*.
4.  **Workflow Patterns:** Need a recipe for a task? -> **Use Tutorials** *(TBD)*.

### B. Workflow: Object Reference (Technical Verification)
*   **Trigger:** You have a specific object name (e.g., `cycle~`, `jit.world`) and need to validate it for a patch.
*   **Tool:** `research_max(query=object_name)`
*   **Required Extraction:**
    You must extract and confirm the following 6 data points from the response:
    1.  **Description:** What does the object strictly do?
    2.  **Arguments:** What creation arguments are required vs. optional?
    3.  **Attributes:** What properties can be set (e.g., `@mode`, `@dim`)?
    4.  **Inlets & Messages:** 
        *   How many inlets? 
        *   What *specific* messages (e.g., `bang`, `float`, `list`) does each inlet accept?
    5.  **Outlets:** What data/signal comes out of which outlet?
    6.  **Related Objects:** What objects are listed in "See Also" for alternatives?
*   **Verification Step:**
    *   *Before* adding the object to a plan, ask: "Do the inlets/outlets match my signal flow requirements?"
    *   If the object lacks a required inlet/message, you MUST find an alternative from the "Related Objects" list.

### C. Workflow: Discovery & Search
*   **Goal:** Move from a fuzzy intent (e.g., "I need to distort a signal") to a specific list of candidate objects or concepts.

1.  **Consult Navigation Map (Static Asset)**
    *   **Action:** Read `assets/navigation.json` to understand the high-level documentation structure.
    *   **Decision:**
        *   **Browsing:** If the intent maps to a known category (e.g., "Audio -> Dynamics"), use the *Browsing* path.
        *   **Search:** If the intent is specific but not in the map (e.g., "granular synthesis"), use the *Search* path.

2.  **Path A: Browsing (Category Exploration)**
    *   **Tool:** `get_navigation(path)`
    *   **Input:** A specific path from the navigation map (e.g., `user_guide/Audio`).
    *   **Output:** A list of sub-categories or articles/objects in that section.
    *   **Refinement:** If the list is too broad, drill down further (e.g., `user_guide/Audio/Dynamics`).

3.  **Path B: Search (Keyword Lookup)**
    *   **Tool:** `search_docs(query)`
    *   **Input:** A specific keyword or phrase (e.g., "granular synthesis").
    *   **Output:** A mixed list of high-relevance matches across all documentation types (User Guide, Reference, Tutorials).

4.  **Selection & Reading**
    *   **Action:** Select the most relevant result (Guide for concepts, Object for implementation).
    *   **Tool:** `read_doc(url)` (formerly `research_max`).
    *   **Output:** The full content of the selected document.

### D. Workflow: Conceptual & Architectural (Guides & Tutorials)
*   **Goal:** Build a correct mental model of the subsystem (Audio, Control, Jitter, etc.) to act as a **Senior Systems Architect**.
*   **Scope:** Covers both *User Guide* (broad concepts) and *Tutorials* (specific patterns/recipes).
*   **Trigger:**
    *   System-level questions (e.g., "How does the Jitter matrix system work?").
    *   Architectural decisions (e.g., "Should I use `poly~` or `mc.` for this?").
    *   Pattern discovery (e.g., "What is the standard way to handle MPE in Max?").
*   **Method:**
    1.  **Identify Domain:** Use the *Discovery* workflow to find the relevant "Book" (e.g., "User Guide -> MC" or "Jitter Tutorials -> Geometry").
    2.  **Read Deeply:** Call `read_doc(url)` on the overview or specific article.
    3.  **Extract Architectural Rules:**
        *   **Data Flow:** How do signals/messages move? (e.g., Right-to-Left order, Scheduler vs Audio thread).
        *   **State Management:** Where is state stored? (e.g., `pattr`, `dict`, object attributes).
        *   **Idioms:** What is the "Max way" to do this? (e.g., using `trigger` to ensure execution order).
        *   **Constraints:** What are the hard limits? (e.g., "Gen~ cannot allocate memory dynamically").
*   **Outcome:** A high-level **Design Strategy** that respects these constraints, formulated *before* selecting specific objects for the patch.

### E. Workflow: API Reference (LOM & JS)
*(Section Pending - Will define structure for LOM, JS, Node)*

### D. Workflow: API Reference (LOM & JS)
*(Section Pending - Will define structure for LOM, JS, Node)*

### E. Workflow: Tutorials (Patterns)
*(Section Pending - Will define structure for Max, MSP, Jitter tutorials)*


## 7. User Interface (TUI)
*   **Context:** Tools and functions utilize the `ExtensionContext` (referred to as `ctx`) provided by the Pi harness.
*   **Notifications:** Use `ctx.ui.notify` to report successful cache hits or new documentation fetches.
*   **Progress Indicators:** Use `ctx.ui.setWorkingMessage` during active network requests to the Context7 API to provide visual feedback in the status bar.

## 8. Error Handling
The extension maps Context7 API responses to actionable feedback via the Pi TUI.

*   **401 Unauthorized:** Invalid `CONTEXT7_API_KEY`. Notify user via `ctx.ui.notify` and halt.
*   **429 Too Many Requests:** Rate limit exceeded. Notify user of the wait time (from `Retry-After` header) via `ctx.ui.notify`.
*   **400 Bad Request:** Malformed query. Log internal error for debugging.
*   **500/503 Server Errors:** Transient failure. Implement exponential backoff retry (up to 3 times) before failing.
*   **File System Errors:** Report specific path and permission issues if `augment_max_db` fails to write metadata.

## 9. File Structure
*   `package.json`
*   `src/index.ts` (Entry point)
*   `src/client.ts` (Context7 interaction)
*   `src/cache.ts` (Persistence)
*   `src/navigation.ts` (Hierarchy browser)
*   `src/augmenter.ts` (Local DB writer)
*   `src/tools.ts` (Tool definitions)
*   `assets/navigation.json` (The semantic map)
