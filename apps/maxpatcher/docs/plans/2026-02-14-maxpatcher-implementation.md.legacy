# MaxPatcher MVP Implementation Plan

> **REQUIRED SUB-SKILL:** Use the executing-plans skill or subagent-driven-development to implement this plan task-by-task.

**Goal:** Build the `maxpatcher` Python application, including CLI, Wrapper Logic, Validator, and Intelligence stubs, to enable isolated Max/MSP patch generation.

**Architecture:** A Python CLI tool that wraps a flattened internal fork of `MaxPyLang`. It uses subprocesses to execute user scripts in an isolated environment and enforces strict validation on the output.

**Tech Stack:** Python 3.11+, Click/Typer (or Argparse), Pytest, MaxPyLang (Internal).

---

## Phase 1: Scaffolding & Core Engine

### Task 1: Project Scaffolding & Configuration

**Files:**
- Create: `apps/maxpatcher/pyproject.toml`
- Create: `apps/maxpatcher/maxpatcher/__init__.py`
- Create: `apps/maxpatcher/maxpatcher/cli.py`
- Create: `apps/maxpatcher/tests/test_cli.py`

**Step 1: Define `pyproject.toml`**
- Define build system (setuptools/hatch).
- Define dependencies: `numpy`, `tabulate`.
- Define entry point: `maxpatcher = maxpatcher.cli:main`.

**Step 2: Create CLI Skeleton**
- Implement `cli.py` with a basic `main` function using `argparse` or `click`.
- Implement `new`, `build`, `validate`, `sync` commands as stubs.

**Step 3: Write Test for Entry Point**
- Create `tests/test_cli.py`.
- Test that `maxpatcher --help` returns exit code 0.

**Step 4: Commit**
- `git add apps/maxpatcher/`
- `git commit -m "feat(maxpatcher): initial scaffolding and cli stubs"`

### Task 2: Internal Engine Setup (MaxPyLang Fork)

**Files:**
- Move: `apps/maxpatcher/MaxPyLang/` -> `apps/maxpatcher/engine/maxpylang/`
- Modify: `apps/maxpatcher/engine/maxpylang/__init__.py` (if needed for import adjustments)

**Step 1: Move Library**
- Execute move command.
- Verify `apps/maxpatcher/engine/maxpylang/maxpatch.py` exists.

**Step 2: Verify Importability (Test)**
- Create `apps/maxpatcher/tests/test_engine.py`.
- Test: `import maxpylang` fails initially (because it's not in path).
- Test: Manually adding `engine/` to path allows import.

**Step 3: Commit**
- `git add apps/maxpatcher/engine`
- `git commit -m "refactor(maxpatcher): flatten maxpylang into internal engine"`

## Phase 2: The "New" Command

### Task 3: Implement `maxpatcher new`

**Files:**
- Modify: `apps/maxpatcher/maxpatcher/cli.py`
- Modify: `apps/maxpatcher/maxpatcher/core.py`
- Test: `apps/maxpatcher/tests/test_new.py`

**Step 1: Write Test**
- `test_new_project_creates_files`: Run `new mydevice`. Assert `projects/mydevice/.vibe.json` and `src/main.py` exist.

**Step 2: Implement Logic**
- In `cli.py`, parse `new <name>`.
- In `core.py`, implement `create_project(name)`.
- Write default `.vibe.json`.
- Write default `src/main.py` (Logic/Control blinker).

**Step 3: Run Test**
- Verify files are created.

**Step 4: Commit**
- `git commit -m "feat(maxpatcher): implement new command"`

## Phase 3: The Wrapper & Build Process

### Task 4: Vibe Helper Module

**Files:**
- Create: `apps/maxpatcher/maxpatcher/vibe.py`
- Test: `apps/maxpatcher/tests/test_vibe.py`

**Step 1: Write Test**
- `test_vibe_import`: Ensure it can be imported.
- `test_vibe_functions`: Test `make_ui_row` or similar helper.

**Step 2: Implement Vibe**
- Add `connect_stereo`, `make_ui_row`.

**Step 3: Commit**
- `git commit -m "feat(maxpatcher): add vibe helper module"`

### Task 5: Implement `maxpatcher build` (Subprocess & Env)

**Files:**
- Modify: `apps/maxpatcher/maxpatcher/cli.py`
- Modify: `apps/maxpatcher/maxpatcher/core.py`
- Test: `apps/maxpatcher/tests/test_build.py`

**Step 1: Write Test**
- `test_build_runs_script`: Mock a project. Run build. Assert script executed.
- `test_build_env`: Assert script can `import maxpylang` and `import vibe`.

**Step 2: Implement Logic**
- In `core.py`: `run_build(project_name)`.
- Read `.vibe.json`.
- Construct `PYTHONPATH` injecting `engine/` and `maxpatcher/`.
- `subprocess.run([sys.executable, src_path], env=env)`.

**Step 3: Run Test**
- Verify successful execution and environment availability.

**Step 4: Commit**
- `git commit -m "feat(maxpatcher): implement build command with subprocess isolation"`

## Phase 4: Validation & Intelligence

### Task 6: Validator (JSON Integrity)

**Files:**
- Create: `apps/maxpatcher/maxpatcher/validator.py`
- Modify: `apps/maxpatcher/maxpatcher/cli.py`
- Test: `apps/maxpatcher/tests/test_validator.py`

**Step 1: Write Test**
- `test_validate_valid_json`: Pass a good JSON. Return True.
- `test_validate_overlap`: Pass JSON with overlapping nodes. Return False + Error.

**Step 2: Implement Validator**
- `validate_patch(path)`.
- Load JSON.
- Check `patching_rect` collisions.
- Check for objects with 0 connections.

**Step 3: Wire to CLI**
- `maxpatcher validate <name>` calls this function.

**Step 4: Commit**
- `git commit -m "feat(maxpatcher): implement validator"`

### Task 7: Intelligence (Sync Stub & Global Cache)

**Files:**
- Create: `apps/maxpatcher/maxpatcher/intelligence.py`
- Modify: `apps/maxpatcher/maxpatcher/cli.py`

**Step 1: Implement Cache Manager**
- `IntelligenceCache`: Manages a JSON-based cache in `apps/maxpatcher/cache/objects/`.
- `sync_object(name)`: A stub that fetches metadata (inlets/outlets) and saves to the local cache.

**Step 2: Wire to CLI**
- `maxpatcher sync <project>`: Scans `src/main.py` for `p.add("object")` calls and ensures all used objects are in the global cache.

**Step 3: Commit**
- `git commit -m "feat(maxpatcher): implement intelligence sync and global caching strategy"`

---

## Phase 5: Refinement & Intelligence Integration (POST-MVP)

### Task 8: Refactor `vibe` Helper (High-level API)

**Goal:** Simplify object creation and connection to reduce boilerplate and errors, wrapping the `MaxPyLang` engine correctly.

**Step 1: Implement `vibe.Patcher` Class**
- Create `Patcher` class in `maxpatcher/vibe.py`.
- **Constructor**: Initialize `maxpylang.maxpatch.MaxPatch`.
- **Method `add(obj_text, **kwargs)`**:
    - Call engine's `place_obj`.
    - Handle coordinate management (initially just passing them through).
- **Method `link(src, dest, out_idx=0, in_idx=0)`**:
    - Validate `src` and `dest` are `MaxObject` instances.
    - Call engine's `connect((src.outs[out_idx], dest.ins[in_idx]))`.
- **Method `save(filename)`**: Wrapper for engine `save()`.

**Step 2: Update Smoke Test**
- Refactor `projects/smoke_test/src/main.py` to use the new `vibe.Patcher` API.

### Task 9: Implement Auto-Layout Strategy

**Goal:** Prevent overlapping objects by leveraging the engine's `place` logic or extending it in `vibe.Patcher`.

**Step 1: Integrate Engine Layouts**
- Update `Patcher.add()` to support a stateful layout cursor.
- By default, use `patch.place(..., spacing_type="grid")` to ensure objects are automatically arranged left-to-right, top-to-bottom.

**Step 2: Verify Layout**
- Build a patch with 5-10 objects and verify in Max/MSP that they are not stacked on top of each other.

### Task 10: Context7 Intelligence Integration

**Goal:** Replace the `sync` stub with actual Context7 queries.

**Step 1: Implement Context7 Tools**
- Use `context7_resolve_library_id` for "cycling74".
- Implement `context7_query_docs` to fetch object metadata (inlets, outlets, attributes).

**Step 2: Cache results**
- The `sync` command should write the fetched documentation somewhere to reduce the need for requerying via context7 api.

---

## Execution Handoff

**Plan complete and saved to `apps/maxpatcher/docs/plans/2026-02-14-maxpatcher-implementation.md`.**

**Options:**
1. **Subagent-Driven:** We execute task-by-task in this session.
2. **Parallel Session:** You open a new terminal/session to execute.

**Which approach?**
