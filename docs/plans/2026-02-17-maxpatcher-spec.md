# Technical Spec: MaxPatcher (Decoupled Builder)

**Status:** Active Reference (See Master Plan for Sequence)
**Goal:** Pure Python builder with zero network dependencies.

## 1. Components

### A. CLI (`maxpatcher`)
*   `new <name>`: Scaffolds a project folder structure.
*   `build <name>`: Executes user source in isolated subprocess.
*   `validate <name>`: JSON/integrity checks.
*   **REMOVAL:** `sync` command is removed. Use `@pi/research:augment` instead.

### B. Vibe Coordinator (`vibe.py`)
*   **Data Lookup:** Queries `maxpylang/data/OBJ_INFO` to validate object names and port counts.
*   **Missing Object Warning:** If object is not found in local DB:
    *   Emit warning: `[MISSING_OBJECT: {name}]`.
    *   Proceed with build using a generic "box" definition (1 inlet, 1 outlet).
    *   **Do NOT** call any external APIs.

### C. Validator (`validator.py`)
*   **Static Analysis:** Parses `.maxpat` JSON without running Max.
*   **Blocking Gates:** Fails build on JSON corruption or zero-connection orphans.
*   **Collision Detection:** Reports specific coordinates of overlapping objects.

## 2. Dependencies
*   **Engine:** `apps/maxpatcher/engine/maxpylang/`.
*   **Knowledge Base:** `engine/maxpylang/data/OBJ_INFO/`.

## 3. Workflow
1.  **Research (Optional):** Agent uses `research_max` to verify logic.
2.  **Augment (Optional):** Agent uses `augment_max_db` to update local knowledge.
3.  **Build:** `maxpatcher build`. Builder uses local knowledge only.
