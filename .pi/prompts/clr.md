---
description: Clarify through discussion - Troubleshoot, Define, Evaluate, Investigate, Align
---
# Clarify Stage

**Goal:** Establish clarity and alignment through discussion before any documentation or implementation begins.

**Context to Load:**
- Identify and read any relevant `*GOALS.md` files in the current scope.

**Input:** "$@"

## Workflow Logic

1. **Analyze Input:**
   - If input is empty, ask: "What are we discussing?" and wait for response.
   - If input is present, categorize the discussion type based on keywords:

   **Type: Troubleshoot** (Keywords: *troubleshoot*)
   - *Goal:* Identify and validate a bug or issue.
   - *Loop:* Investigate logs/behavior, hypothesize cause.
   - *End:* User validates the bug -> Update Task/Beads (if available) or summarize for `doc` stage.

   **Type: Define Problem** (Keywords: *define*, *problem statement*)
   - *Goal:* Articulate the problem clearly.
   - *Loop:* Ask probing questions to narrow scope.
   - *End:* User approves problem statement -> Update `...GOALS.md`.

   **Type: Evaluate Solution** (Keywords: *solution*, *evaluate*)
   - *Goal:* Decide on a technical approach.
   - *Loop:* Propose/compare options (trade-offs).
   - *End:* User decides -> Update `...ARCH.md` or `...SPEC.md`.

   **Type: Investigate/Analyze** (Keywords: *investigate*, *analyze*)
   - *Goal:* Gather context or feasibility data.
   - *Loop:* Read files, search (if available), analyze structure.
   - *End:* User reviews analysis -> Update relevant docs.

   **Type: Alignment** (Keywords: *alignment*, *not aligned*, *misalignment*)
   - *Goal:* Resolve confusion or sync mental models.
   - *Loop:* Clarify assumptions, re-state understanding.
   - *End:* Alignment reached -> Update relevant docs.

   **Fallback:**
   - If input doesn't match above, infer intent.
   - If inference fails, ask the user for clarification.

## Rules of Engagement

1. **Pattern:** Loop [`<Interview/Analysis>` <-> `<Propose>`] until explicit `<Human Approval>`, then proceed to `<Action>`.
2. **Constraints:**
   - **NO** implementation code.
   - **NO** editing code files.
   - **ONLY** edit Markdown (`.md`) files or create tasks (if tools allow).
3. **Completion:**
   - This stage is a continuous loop. Do not move to the next stage until the user explicitly issues a command (e.g., `/doc`, `/plan`) or says "we are done".
4. **Tools:**
   - Use read-only bash tools (`ls`, `grep`, `cat` via `read`) to investigate.
   - Use web search if available/necessary.

## Immediate Action
Start the discussion based on the input: "$@".
