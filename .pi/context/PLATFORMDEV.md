---
description: Platform Development Process & Guidelines
---
# Platform Development Guidelines

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## Core Workflow Pattern

Development for both the platform and individual apps follows a structured process leveraging the `pi-superpowers` extension. This process ensures rigor, quality, and maintainability.

### 1. Brainstorm
**Skill:** `brainstorming`
Refine the initial idea or requirement into a structured design document or specification. This phase explores intent and constraints before any code is written.

### 2. Isolate
**Skill:** `using-git-worktrees`
Create a clean, isolated workspace for the feature or fix. This prevents cross-contamination between tasks and ensures a stable environment.

### 3. Plan
**Skill:** `writing-plans`
Break down the design into bite-sized, actionable tasks. Plans should prioritize Test-Driven Development (TDD) and incremental implementation.

### 4. Execute
**Skills:** `executing-plans`, `subagent-driven-development`, `test-driven-development`
Work through the plan. Use TDD for all implementation. If bugs are encountered, use `systematic-debugging`.

### 5. Verify
**Skill:** `verification-before-completion`
Run all tests and verification commands to prove the implementation meets the requirements and doesn't break existing functionality. Evidence before assertions.

### 6. Review
**Skill:** `requesting-code-review`
Solicit feedback on the implementation. If receiving feedback, use `receiving-code-review` to process and verify suggestions.

### 7. Finish
**Skill:** `finishing-a-development-branch`
Complete the development by merging work, creating a PR, and cleaning up the workspace.

---

## Operational Principles

*   **User Responsibility:** Moving from one stage to the next is the responsibility of the user, NOT the agent.
*   **Execution over Simulation:** Do not attempt to mentally simulate complex decision trees. Execute the first step, report results, and proceed.
*   **Bias for Action:** If a decision is ambiguous, ask the user or try the most reversible action.
*   **Surgical Edits:** Use the `edit` tool for precise changes to existing code.
*   **TDD First:** Write tests before implementation. Verification is mandatory.
