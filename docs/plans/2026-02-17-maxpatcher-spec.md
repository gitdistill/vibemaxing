# Technical Spec: MaxPatcher (Decoupled Builder)

**Status:** Active Reference (Target Architecture: 2026-02-17)
**Goal:** A fast, deterministic Max/MSP patch builder (Python) with zero network dependencies.

## 1. Core Logic

### A. Vibe Coordinator (`vibe.py`)
*   **Data Lookup:** Queries the local `maxpylang/data/OBJ_INFO` database to validate object definitions and port counts.
*   **Missing Object Handling:** If an object is not found in the local database:
    1.  **Stop Build:** Immediately halt the build process.
    2.  **Error Code:** Emit a specific error: `[MISSING_OBJECT: {name}]`.
    3.  **Instruction:** Provide a recovery hint: `Run '@pi/research:augment_max_db {name}' to add this object to the local database.`
*   **Constraint:** No network requests. All `intelligence.py` and Context7 logic must be removed.

### B. CLI (`maxpatcher`)
*   `new <name>`: Scaffolds a project folder structure.
*   `build <name>`: Executes Python source scripts into Max patches (`.maxpat`).
*   `validate <name>`: Static analysis for JSON integrity, connection orphans, and object collisions.
*   **REMOVAL:** The `sync` command is deprecated and must be removed. Use the `vibemax-intelligence` extension for database augmentation.

### C. Validator (`validator.py`)
*   **Static Analysis:** Parses generated `.maxpat` files without running the Max environment.
*   **Failure Gates:** Fails builds on JSON corruption or disconnected inlets/outlets.
*   **Collision Detection:** Identifies overlapping objects in the patch UI layout.

## 2. Directories
*   **Core Engine:** `apps/maxpatcher/engine/maxpylang/`.
*   **Knowledge Base:** `engine/maxpylang/data/OBJ_INFO/` (organized by: `max`, `msp`, `jitter`).

## 3. Standard Workflow
1.  **Research:** Use `research_topic` or `research_object` via the Intelligence Extension to verify designs.
2.  **Build:** `maxpatcher build`.
3.  **Error Recovery:** If a `[MISSING_OBJECT]` error occurs, run `augment_max_db` and rebuild.
