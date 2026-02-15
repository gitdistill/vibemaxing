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

### Task 7: Intelligence (Sync Stub)

**Files:**
- Create: `apps/maxpatcher/maxpatcher/intelligence.py`
- Modify: `apps/maxpatcher/maxpatcher/cli.py`

**Step 1: Implement Stub**
- `sync_object(name)`: Print "Searching Context7 for {name}..." (Mock implementation for MVP).

**Step 2: Wire to CLI**
- `maxpatcher sync <name>`.

**Step 3: Commit**
- `git commit -m "feat(maxpatcher): implement intelligence sync stub"`

---

## Execution Handoff

**Plan complete and saved to `apps/maxpatcher/docs/plans/2026-02-14-maxpatcher-implementation.md`.**

**Options:**
1. **Subagent-Driven:** We execute task-by-task in this session.
2. **Parallel Session:** You open a new terminal/session to execute.

**Which approach?**
