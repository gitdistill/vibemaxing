# Component Design: Testing Strategy

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
This document defines how we verify the correctness of the `maxpatcher` tool. The strategy prioritizes **Integration Testing** of the CLI and **Snapshot Testing** of the generated artifacts.

## 2. Core Decisions

### A. Integration-First (CLI)
Instead of unit-testing every internal function, we treat the `maxpatcher` binary as a "Black Box."
*   **Test Harness:** We will use `pytest` with a fixture that creates a temporary directory.
*   **Workflow:**
    1.  `maxpatcher new test_project`
    2.  Write a known `main.py` into that folder.
    3.  `maxpatcher build test_project`
    4.  Assert exit code is 0.
    5.  Assert `dist/test_project.maxpat` exists.

### B. Context7 Mocks (Data)
Since cycling74 documentation changes rarely, we will **NOT** hit the live API during tests.
*   **Mechanism:** We will cache "Gold Standard" JSON responses for common objects (`cycle~`, `patcher`, `m4l.api`) in `tests/fixtures/context7/`.
*   **Implementation:** The test suite will mock the `context7_query_docs` tool integration to return these local files instead of making network calls.

### C. Snapshot Testing (Artifacts)
To ensure the Layout Engine isn't silently broken:
*   **Gold Masters:** We commit "perfect" `.maxpat` files for specific test cases to the repo.
*   **Comparison:** The test builds a fresh patch and performs a strict JSON comparison against the Master.
*   **Tolerance:** Zero. Any change in connection order, patcher coordinates, or object ID generation sequence causes a failure.

### D. Subprocess Isolation
We affirm the decision to use **Subprocesses** for user code execution.
*   **Why?** It guarantees that user scripts (which modify `sys.path` and import heavy libs) cannot pollute the Builder's memory space or crash the test runner.
*   **Testing Approach:** We verify behavior by inspecting `stdout`, `stderr`, and `exit_code`.
    *   *Success Case:* Assert `stdout` contains "Build Successful".
    *   *Failure Case:* Create a `main.py` with a syntax error. Assert `stderr` contains our "LLM-Optimized" summary, not just a raw traceback.

## 3. Test Structure
```text
apps/maxpatcher/tests/
├── fixtures/
│   ├── context7/          # Cached API responses
│   │   ├── cycle~.json
│   │   └── api.json
│   └── snapshots/         # Gold Master .maxpat files
│       └── basic_osc.maxpat
├── integration/
│   ├── test_cli_new.py    # Tests scaffolding
│   ├── test_cli_build.py  # Tests subprocess execution
│   └── test_validator.py  # Tests the checker logic
└── unit/
    └── test_parser.py     # (Optional) specific logic tests
```

## 4. CI/CD Requirements
*   Tests must run in a standard Python environment.
*   No Max/MSP installation required (due to Static Analysis approach).
