# Technical Spec: MaxPatcher (Decoupled Builder)

**Status:** Active Reference (See Master Plan for Sequence)
**Goal:** Pure Python builder with zero network dependencies.

## 1. Components

### A. CLI (`maxpatcher`)
*   `new <name>`: Scaffolds a project folder structure.
*   `build <name>`: Executes user source in isolated subprocess.
*   `validate <name>`: JSON/integrity checks.
*   **REMOVAL:** The `sync` command is removed. Use the intelligence extension's `augment_max_db` instead.

### B. Vibe Coordinator (`vibe.py`)
*   **Data Lookup:** Queries `maxpylang/data/OBJ_INFO` to validate object names and port counts.
*   **The "FAIL-FAST" Rule:** If an object is not found in the local DB:
    1.  **Stop Build:** Do **NOT** proceed with a generic box definition.
    2.  **Emit Error:** Log a specific error: `[MISSING_OBJECT: {name}]`.
    3.  **Instruction:** Provide a recovery hint: `Run '@pi/research:augment_max_db {name}' to add this object to the local database before rebuilding.`
*   **Constraint:** Zero external network calls or `intelligence.py` calls.

### C. Validator (`validator.py`)
*   **Static Analysis:** Parses `.maxpat` JSON without running Max.
*   **Blocking Gates:** Fails build on JSON corruption or zero-connection orphans.
*   **Collision Detection:** Reports specific coordinates of overlapping objects.

## 2. Dependencies
*   **Engine:** `apps/maxpatcher/engine/maxpylang/`.
*   **Knowledge Base:** `engine/maxpylang/data/OBJ_INFO/`.

## 3. Workflow
1.  **Research (Optional):** Agent uses `research_topic` or `research_object` to verify logic.
2.  **Augment (Optional):** Agent uses `augment_max_db` to update local knowledge if `maxpatcher build` fails.
3.  **Build:** `maxpatcher build`. Builder uses local knowledge only.
