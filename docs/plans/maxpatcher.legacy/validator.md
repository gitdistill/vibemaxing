# Component Design: Validator

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
The Validator ensures that the generated `.maxpat` is both a valid JSON file and a logically sound Max patcher.

## 2. Decisions
1. **Analysis Type:** **Static Analysis**. The validator parses the generated `.maxpat` JSON file directly. It does NOT require a running instance of Max/MSP, ensuring it can run in CI/CD or headless environments.
2. **Severity:** **Blocking**. A validation failure results in a non-zero exit code. A build is not "Successful" until it passes validation.
3. **Strictness Policy:** "Unknown Objects" will trigger a **Failure**. This forces the agent to use the `sync` command to grounding the engine before the build is considered complete.
4. **Orphan Policy:** **Hard Failure for Total Orphans**. Any object with zero (0) incoming or outgoing connections will trigger a blocking error. Objects with partial connections (e.g., an inlet patched but not an outlet) are permitted.
5. **Auto-Fixing:** **No Auto-Fix**. The validator will strictly report layout issues (like overlaps) without modifying the output. This prevents desync between the Python source and the generated `.maxpat`.

## 3. Core Validation Rules
- **JSON Integrity:** Validates structure and syntax.
- **Intelligence Check:** Cross-references objects against the Engine's known metadata.
- **Logical Validation:** Detects phantom connections or ports that don't exist on the object.
- **Orphan Detection:** Blocks build if an object has 0 total connections.
- **Collision Detection:** Checks `patching_rect` values to ensure objects aren't stacked directly on top of each other.
    *   **Error Format:** `Collision Error: Object 'cycle~' (id: obj-1) at [100, 100] overlaps with 'dac~' (id: obj-2) at [100, 100]. Please adjust coordinates.`
    *   This explicit coordinate feedback allows the Agent to fix the Python source code deterministically.

## 4. Remaining Questions
1. **Vibe Rules (The "High-Quality" Spec):** Postponed. We will define idiomatic patterns (layout, color-coding, documentation) as the platform evolves.
