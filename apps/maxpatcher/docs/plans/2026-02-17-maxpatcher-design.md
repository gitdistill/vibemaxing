# Design: MaxPatcher (Decoupled Builder)

**Date:** 2026-02-17
**Status:** Canonical Design (Supersedes 2026-02-14)
**Goal:** A fast, deterministic Max/MSP patch builder with zero external dependencies.

## 1. Overview

The `maxpatcher` app is a pure Python builder that transforms Python scripts (`main.py`) into Max patches (`.maxpat`). It operates strictly on local data, ensuring builds are fast, reproducible, and offline-capable.

**Key Principle:** All "Intelligence" (research, documentation lookup, database augmentation) is externalized to the Agent/Platform level via `.pi/extensions/vibemax-intelligence`. `maxpatcher` simply consumes the data provided by that extension.

## 2. Architecture

### Directory Structure

```text
/
├── apps/
│   └── maxpatcher/          # The Builder App
│       ├── engine/          # The Core Engine (Flattened MaxPyLang)
│       │   └── maxpylang/   # The Python Package
│       │       ├── data/    # The Knowledge Base (Augmented by Extension)
│       │       │   └── OBJ_INFO/
│       ├── maxpatcher/      # The Wrapper Package
│       │   ├── __init__.py
│       │   ├── cli.py       # Entry point (new, build, validate)
│       │   ├── core.py      # Logic for scaffolding/building
│       │   ├── validator.py # JSON/integrity checks
│       │   └── vibe.py      # The `vibe` helper module (exposed to user)
│       ├── tests/           # Unit tests for the wrapper
│       ├── pyproject.toml   # Dependencies & Metadata
│       └── README.md
```

### Core Components

1.  **CLI (`maxpatcher`):**
    *   `new <name>`: Scaffolds a project folder structure.
    *   `build <name>`: Executes the source script via subprocess.
    *   `validate <name>`: Checks the generated `.maxpat` for integrity.
    *   **Removed:** `sync` command (replaced by `@pi/research:augment`).

2.  **Wrapper Logic (`core.py`):**
    *   **Subprocess Execution:** Runs user scripts in an isolated process.
    *   **Path Management:** Simply ensures `apps/maxpatcher/engine` is in the `PYTHONPATH` so the user script can `import maxpylang`.
    *   **Helper Injection:** Ensures `import vibe` works by exposing `apps/maxpatcher/maxpatcher/vibe.py`.
    *   **Output Handling:** Buffers stdout/stderr and parses them into LLM-friendly summaries.

3.  **Vibe Coordinator (`vibe.py`):**
    *   **High-Level API:** Provides the `vibe.Patcher` class which wraps `MaxPatch`.
    *   **Data Lookup:** Queries `maxpylang/data/OBJ_INFO` to validate object names and inlet/outlet counts.
    *   **Missing Object Handling:** If an object is not found in the DB:
        *   Log a warning: `Warning: Object '{name}' not found. Using default inlet/outlet counts.`
        *   Proceed with build using a generic "box" definition (1 inlet, 1 outlet).
        *   Does **NOT** crash or attempt network fetch.

4.  **Validator (`validator.py`):**
    *   **Static Analysis:** Parses `.maxpat` JSON without running Max.
    *   **Blocking Gates:** Fails build on JSON errors or zero-connection orphans.
    *   **Collision Detection:** Reports specific coordinates of overlapping objects.

## 3. Workflow

1.  **Research (Optional):** Agent uses `@pi/research:research_max` to understand object usage.
2.  **Augment (Optional):** Agent uses `@pi/research:augment_max_db` to add new object definitions to `maxpylang/data/OBJ_INFO`.
3.  **Develop:** User/Agent edits `projects/my_device/src/main.py`.
4.  **Build:** User runs `maxpatcher build my_device`.
    *   Builder uses local data only.
5.  **Verify:** User runs `maxpatcher validate my_device`.
