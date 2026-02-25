# Component Design: CLI

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
The CLI is the primary entry point for both human developers and agentic "Junior Programmers." It must provide clear feedback and support the project lifecycle (`new`, `build`, `validate`).

## 2. Interface Definition
- **Binary Name:** `maxpatcher`
- **Commands:**
    - `new <name>`: Scaffolds a project.
    - `build <name>`: Executes the source script.
    - `validate <name>`: Runs integrity and intelligence checks.

## 3. Decisions
1. **Verb Granularity:** `build` and `validate` will remain **separate** commands. This allows the agent to build a patch, inspect it, and then choose to validate it or run it in Max without mandatory overhead.
2. **Error Feedback:** CLI will provide **LLM-optimized summaries** for failures (e.g., "Error: Object 'cycl' not found. Did you mean 'cycle~'?"). Raw tracebacks will be available via a `--verbose` flag.
3. **Scaffold Boilerplate:** The default `main.py` will generate a basic **Logic/Control** patch:
   - `metro 500` -> `counter` -> `button`.
   - This avoids MSP/DSP complexities while providing a clear visual "smoke test" (blinking button).
4. **Configuration:** Project-level settings (paths, dist directories) will be stored in a **`.vibe.json`** file within the project root.

## 4. Project Structure (Scaffolded by `new`)
The command `maxpatcher new <name>` creates the following structure:
```
projects/<name>/
├── .vibe.json       # Project Configuration
├── README.md        # Generated documentation template
├── src/
│   └── main.py      # Entry point (imports maxpylang)
└── dist/            # Output directory (gitignored)
```

## 5. Configuration Schema (`.vibe.json`)
Minimal configuration file to define project metadata and build settings.
```json
{
  "name": "my-device",
  "version": "0.0.1",
  "type": "max-patch", // or "m4l-device"
  "paths": {
    "src": "src/main.py",
    "dist": "dist/"
  }
}
```

## 6. Remaining Questions
1. Does the CLI need to handle auto-discovery of the Max application path for "Open in Max" functionality? -> *Deferred to future iteration.*
