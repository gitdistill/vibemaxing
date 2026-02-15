# Component Design: Intelligence

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
The Intelligence module (`intelligence.py`) bridges the gap between the library's local knowledge and the external Context7 technical documentation.

## 2. Key Responsibilities
- **Context7 Management:** Handling the 1000-request limit and API calls.
- **Engine Patching:** Writing JSON schemas directly into the `MaxPyLang` internal library (`apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`).
- **Knowledge Synthesis:** Converting Context7 data into `MaxPyLang` compatible JSON.

## 3. Decisions
1.  **Engine Strategy:** **Absorb & Own**. We flatten `MaxPyLang` into `apps/maxpatcher/engine/`.
2.  **Metadata Synchronization:** The command `maxpatcher sync <obj>` fetches technical metadata from Context7 and writes it directly into the engine's `data/OBJ_INFO/` directory. This permanently upgrades the engine for all projects.
3.  **Strict Duty Separation:** 
    - **CLI (`maxpatcher`):** Responsible only for **Technical Intelligence** (JSON schemas, inlets/outlets).
    - **Agent/Skill:** Responsible for **Conceptual Intelligence** (Tutorials, User Guides, Patterns).
4.  **Explicit Sync Only:** Syncing only happens when the technical build requires it (lazy loading) or the user explicitly runs the command.
5. **Exit Codes & Error Handling:**
   - `CODE_MISSING_REF`: Object unknown. **Action:** Run `maxpatcher sync <obj>`.
   - `CODE_API_LIMIT`: Context7 limit reached. **Action:** Stop/Notify.
   - `CODE_NOT_FOUND`: Object not in docs. **Action:** Fix typo.

## 4. Holistic Intelligence (Architecture)
The Intelligence module serves the **Builder (Engine Grounding)**. It focuses on the **Reference** docs to ensure the Engine knows how to write valid patches.

The **Conceptual Grounding** (Tutorials/Guides) is handled entirely at the Agent/Skill layer.

## 5. Remaining Questions
1. **Metadata Versioning:** Should the `sync` command attempt to preserve the original engine data as a fallback? (Currently: No, we assume Context7 is the source of truth).
