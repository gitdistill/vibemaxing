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

## 4. Vibe Patcher Coordinator (vibe.py)
To bridge the gap between low-level engine operations and high-level agentic patch generation, `vibe.py` provides the `vibe.Patcher` class.

### Key API Patterns:
- **`vibe.Patcher()`**: Inherits from or wraps `MaxPatch`. Manages default template discovery and output paths.
- **`Patcher.add(obj_spec, **kwargs)`**:
    - Wraps `place_obj` or `place`.
    - Automatically manages the internal `_curr_position` (cursor) using a configurable layout strategy (default: "flow" or "grid").
    - Supports named parameters for common object attributes (e.g., `frequency=440` -> `cycle~ 440`).
- **`Patcher.link(src, dest, out_idx=0, in_idx=0)`**:
    - Simplifies `patch.connect((src.outs[out_idx], dest.ins[in_idx]))`.
- **`Patcher.link_stereo(src, dest)`**:
    - High-level helper for dual-mono/stereo connections.

### Layout Implementation:
- The `vibe.Patcher` will default to using `spacing_type="grid"` with `spacing=[80.0, 80.0]` if no coordinates are provided, ensuring no overlaps occur during automated builds.

## 5. Dependencies
The internal engine requires:
- `numpy>=1.22.0`
- `tabulate` (used by MaxPyLang for reporting)
These must be added to `apps/maxpatcher/pyproject.toml`.
