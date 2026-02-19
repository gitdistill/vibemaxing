# Refactoring Plan: Decoupling Intelligence

**Date:** 2026-02-17
**Goal:** Transition `maxpatcher` from the "Integrated Context7" model (2026-02-14) to the "Decoupled Builder" model (2026-02-17).
**Executor:** Agent (Refactoring Specialist)

## 1. Context

We are shifting the platform architecture to make `maxpatcher` a deterministic, local-only builder. The previous design integrated `intelligence.py` to fetch object metadata from Context7. This logic is being moved to a global Pi extension (`.pi/extensions/vibemax-intelligence`).

**Current State (Legacy):**
*   `maxpatcher` contains `intelligence.py`.
*   `maxpatcher` has a `sync` command.
*   `maxpatcher` attempts to fetch data on build.

**Target State (New):**
*   `maxpatcher` has **NO** `intelligence.py`.
*   `maxpatcher` has **NO** `sync` command.
*   `maxpatcher` relies solely on `engine/maxpylang/data/OBJ_INFO`.
*   Missing objects trigger a warning suggesting the use of the `research_max` tool.

## 2. Migration Steps

### A. Remove Intelligence Logic
1.  **Delete** `apps/maxpatcher/maxpatcher/intelligence.py`.
2.  **Remove** any references to `intelligence` or `Context7` in `apps/maxpatcher/maxpatcher/cli.py`.
    *   Remove the `sync` command definition.
    *   Remove imports of `intelligence`.
3.  **Remove** references in `apps/maxpatcher/maxpatcher/vibe.py` (if any logic tried to call intelligence on `add()`).
4.  **Clean** `pyproject.toml` of any Context7-related dependencies (if added).

### B. Update Build Logic
1.  **Modify** `vibe.py` / `core.py`:
    *   When adding an object, check `maxpylang` data.
    *   If missing, log a warning: `Warning: Object '{name}' not found in local database. It may lack inlet/outlet validation. Run '@pi/research:augment {name}' to fix.`
    *   Do **NOT** crash. Allow the build to proceed with default "box" behavior (1 inlet, 1 outlet generic).

### C. Verify Determinism
1.  Run `maxpatcher build` on a project with standard objects (e.g., `cycle~`). It should succeed without network calls.
2.  Run `maxpatcher build` on a project with a fake object. It should warn but succeed.

## 3. Future Work (Out of Scope for this Refactor)
*   The creation of the `.pi/extensions/vibemax-intelligence` extension is a separate task (see `docs/plans/2026-02-17-architecture-evolution.md`).
*   This refactor strictly concerns cleaning up `maxpatcher`.
