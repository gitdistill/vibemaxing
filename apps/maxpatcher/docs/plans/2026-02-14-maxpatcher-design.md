# Design: MaxPatcher Build System

> **⚠️ DEPRECATED: This design has been superseded by the "Decoupled Intelligence" architecture.**
> **Please refer to `apps/maxpatcher/docs/plans/2026-02-17-maxpatcher-design.md` for the current canonical design.**
> **For migration instructions, see `apps/maxpatcher/docs/plans/2026-02-17-maxpatcher-refactor.md`.**

**Date:** 2026-02-14
**Status:** Deprecated (Historical Reference Only)

> **IMPORTANT:** We are currently decomposing this high-level design into specific component architectures. Detailed specs and critical design questions for each module are located in:
> `apps/maxpatcher/docs/plans/components/`
>
> **Active Design Files:**
> - [CLI Component](components/cli.md)
> - [Wrapper Logic Component](components/wrapper_logic.md)
> - [Validator Component](components/validator.md)
> - [Intelligence Component](components/intelligence.md)
> - [Agentic Workflow Component](components/agentic_workflow.md)
> - [Testing Strategy](components/testing_strategy.md)

## 1. Overview

The `maxpatcher` app serves as the **Builder** component of the Vibemaxing platform. It provides a structured Python environment for generating Max/MSP patches (`.maxpat`) using the `MaxPyLang` library.

**Goal:** Create a thin wrapper around `MaxPyLang` that standardizes project structure, handles build artifacts, and provides basic validation for generated patches.

**Project Isolation:** Each project in the `projects/` directory is strictly isolated. Projects do not share source code or metadata, ensuring that changes to one device do not affect others.

## 2. Architecture

### Directory Structure

```text
/
├── apps/
│   └── maxpatcher/          # The Builder App
│       ├── engine/          # The Core Engine (Flattened MaxPyLang)
│       │   └── maxpylang/   # The Python Package
│       │       ├── data/    # The Knowledge Base (Target for Sync)
│       │       │   └── OBJ_INFO/
│       ├── maxpatcher/      # The Wrapper Package
│       │   ├── __init__.py
│       │   ├── cli.py       # Entry point (new, build)
│       │   ├── core.py      # Logic for scaffolding/building
│       │   ├── validator.py # JSON/integrity checks
│       │   ├── intelligence.py # Context7 manager & engine patcher
│       │   └── vibe.py      # The `vibe` helper module (exposed to user)
│       ├── tests/           # Unit tests for the wrapper
│       ├── pyproject.toml   # Dependencies & Metadata
│       └── README.md
├── projects/                # User Land (Your Devices)
│   ├── <project_name>/
│   │   ├── src/             # Python Source (The Truth)
│   │   │   └── main.py
│   │   ├── dist/            # Generated Artifacts
│   │       └── <project_name>.maxpat
│   │   └── .vibe.json       # Project Configuration
└── .pi/                     # Agent Context
```

### Core Components

1.  **CLI (`maxpatcher`):**
    *   `new <name>`: Scaffolds a project folder structure.
    *   `build <name>`: Executes the source script via subprocess.
    *   `validate <name>`: Checks the generated `.maxpat` for integrity.
    *   `sync <obj>`: Fetches object metadata from Context7 and patches the Engine directly.

2.  **Wrapper Logic (`core.py`):**
    *   **Subprocess Execution:** Runs user scripts in an isolated process.
    *   **Path Management:** Simply ensures `apps/maxpatcher/engine` is in the `PYTHONPATH` so the user script can `import maxpylang`.
    *   **Helper Injection:** Ensures `import vibe` works by exposing `apps/maxpatcher/maxpatcher/vibe.py`.
    *   **Output Handling:** Buffers stdout/stderr and parses them into LLM-friendly summaries.

3.  **Validator (`validator.py`):**
    *   **Static Analysis:** Parses `.maxpat` JSON without running Max.
    *   **Blocking Gates:** Fails build on JSON errors, unknown objects, or zero-connection orphans.
    *   **Collision Detection:** Reports specific coordinates of overlapping objects.

4.  **Vibe Coordinator (`vibe.py`):**
    *   **High-Level API:** Provides the `vibe.Patcher` class which wraps `MaxPatch`.
    *   **Auto-Layout:** Implements a stateful layout engine (defaulting to grid/flow) to prevent overlapping objects.
    *   **Intelligent Linking:** Simplifies connections (e.g., `patch.link(a, b)` instead of `patch.connect((a.outs[0], b.ins[0]))`).

5.  **Intelligence Manager (`intelligence.py`):**
    *   **Context7 Bridge:** Manages API quotas and fetches documentation using the Context7 library ID `/websites/cycling74`.
    *   **Global Cache Strategy:** Instead of patching the engine data directly (which can be fragile), `intelligence.py` maintains a persistent JSON cache in `apps/maxpatcher/cache/objects/`.
    *   **Runtime Integration:** The `vibe.Patcher` API queries this cache during `add()` and `link()` calls to provide real-time validation of inlet/outlet indices and object existence.
    *   **Sync Logic:** The `maxpatcher sync <project>` command performs static analysis on the project's source code to identify all Max objects used and ensures their metadata is present in the cache.

## 3. Workflow

1.  **Setup:** Run `pip install -e apps/maxpatcher` once to install the tool and dependencies.
2.  **Scaffold:** User runs `maxpatcher new my_device`.
3.  **Develop:** User/Agent edits `projects/my_device/src/main.py`.
4.  **Build:** User runs `maxpatcher build my_device`.
    *   Wrapper executes `main.py`.
    *   Wrapper moves/ensures output is in `dist/`.
5.  **Verify:** User runs `maxpatcher validate my_device`.
    *   System checks file integrity and structure.

## 4. Implementation Plan

removed for context management.

## 5. Future Considerations
-   **Pi Extension:** Dedicated Pi skills/tools (e.g., `/skill:vibemax-builder`) to automate the "Build-Validate-Resolve" loop. Requires future brainstorming.
-   **Library:** Extract common patterns into `apps/maxpatcher/lib/`.
