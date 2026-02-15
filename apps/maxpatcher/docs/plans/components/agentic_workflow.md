# Component Design: Agentic Workflow (Skills)

**Status:** Finalized
**Parent Design:** [2026-02-14-maxpatcher-design.md](../2026-02-14-maxpatcher-design.md)

## 1. Overview
This component defines how the Agent interacts with the `maxpatcher` toolchain. 

**Core Principle:** The workflow **strictly adheres** to the `pi-superpowers-plus` methodology defined in the root `AGENTS.md` and `PLATFORMSPEC.md`. We do not invent a separate "Max Developer" process; we apply standard skills to the Max domain.

## 2. The Superpowers Mapping
The agent operates by mapping standard `pi-superpowers` skills to MaxPatcher tasks.

| Phase | Superpower Skill | MaxPatcher Action |
| :--- | :--- | :--- |
| **1. Concept** | `/skill:brainstorming` | Query Context7 for "Conceptual Intelligence" (Tutorials/Guides). Define the device's purpose and "Vibe". |
| **2. Spec** | `/skill:writing-plans` | Create a `PLAN.md`. Decide on architecture (Logic vs. UI). |
| **3. Build** | `/skill:subagent-driven-development` | Run `maxpatcher new` and write `src/main.py`. |
| **4. Debug** | `/skill:systematic-debugging` | Analyze `maxpatcher build` errors. Run `maxpatcher sync <obj>` if technical metadata is missing. |
| **5. Verify** | `/skill:verification-before-completion` | **MANDATORY:** Run `maxpatcher validate <name>`. Build must succeed and pass all checks. |

## 3. Critical Rules

### A. The "Three Strikes" Rule (Error Handling)
If `maxpatcher build` fails **3 times in a row** with the same or related error:
1.  **STOP.** Do not attempt a 4th fix.
2.  **ASK THE USER.** Present the error summary and the failed strategies.
3.  *Rationale:* This prevents the agent from spiraling into a "hallucination loop" where it guesses at object attributes.

### B. Validation Gate
The `verification-before-completion` skill is **NOT SATISFIED** until:
1.  `maxpatcher build <name>` returns exit code 0.
2.  `maxpatcher validate <name>` returns exit code 0.
3.  `dist/<name>.maxpat` exists.

### C. Human-in-the-Loop
Adhering to `AGENTS.md`:
-   **Stage Transitions:** The agent must pause for user approval between **Plan** and **Execute**.
-   **Review:** The agent must pause for user approval before marking a task **Complete**.

## 4. Intelligence & Context (The Missing Link)
*   **Gap Identified:** The agent currently lacks a "Map" of the Context7 documentation library (e.g., knowing that "M4L Live Object Model" is distinct from "MSP Signal Processing").
*   **Solution (Future):** We will generate a **High-Level Index** of the docs with short descriptions and guidelines. This will be an artifact created in a future session.
*   **Current Workaround:** The agent must explicitly ask the user for "search keywords" if it is unsure which library to query during Brainstorming.

## 5. Artifact Management
Context management is handled by the standard `superpowers` artifacts:
-   **`docs/research/`:** Raw findings from Context7 (preserved for reference).
-   **`PLAN.md`:** The synthesized strategy (the source of truth for the coder).
-   **`src/main.py`:** The implementation.

The agent does not need to summarize research into a separate `spec.md` unless the `brainstorming` session naturally produces one.
