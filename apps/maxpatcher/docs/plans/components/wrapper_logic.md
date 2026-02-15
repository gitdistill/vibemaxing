# Component Design: Wrapper Logic

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
The Wrapper Logic (`core.py`) manages the execution of project scripts and the runtime configuration of the `MaxPyLang` engine.

## 2. Decisions
1.  **Execution Mode:** Project scripts will be run as a **subprocess**. This ensures clean isolation and provides a clear boundary for LLM error capturing.
2.  **Engine Strategy:** **Internal Fork**. We will flatten `MaxPyLang` into `apps/maxpatcher/engine/`, removing its git history. It is now our internal engine.
3.  **Strict CLI Entry:** The `maxpatcher build` command is the *only* supported way to execute project scripts. Direct execution (`python main.py`) is not supported.
4.  **Helper Library (`vibe`):** We will implement a helper module `vibe.py` (exposed as `import vibe`) to provide higher-level abstractions.
5.  **Output Handling:** **Buffering & Summarization**. Subprocess output is captured; the CLI then presents a "Success" message or an "LLM-Optimized Error Summary".

## 3. Implementation Detail: Environment Injection
To ensure `import maxpylang` and `import vibe` work seamlessly, the Wrapper (`core.py`) configures the subprocess environment:

```python
env = os.environ.copy()
# Add the internal engine and the wrapper package root to PYTHONPATH
# - engine/: allows `import maxpylang`
# - maxpatcher/: allows `import vibe` (if vibe.py is adjacent to core.py)
env["PYTHONPATH"] = f"{APP_ROOT}/engine:{APP_ROOT}/maxpatcher:{env.get('PYTHONPATH', '')}"
```

## 4. Vibe Utils (The `vibe` module)
Exposed as `import vibe`.
- `vibe.connect_stereo(src, dest)`
- `vibe.make_ui_row([objs])`
- `vibe.setup_m4l_midi()`

## 5. Dependencies
The internal engine requires:
- `numpy>=1.22.0`
- `tabulate` (used by MaxPyLang for reporting)
These must be added to `apps/maxpatcher/pyproject.toml`.
