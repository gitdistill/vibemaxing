---
description: High-Level Platform Roadmap & Backlog
---
# Platform Plan

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## Phase 0: Foundation (Current)
*   [x] Scaffold `.pi/prompts/` (Workflow templates).
*   [x] Draft `.pi/context/PLATFORMGOALS.md`.
*   [x] Draft `.pi/context/PLATFORMARCH.md`.
*   [x] Stub `.pi/context/PLATFORMDEV.md` (Formal definition moved to Phase 1).

## Phase 1: Agentic Workflow Implementation
**Goal:** Build the `/commands` in Pi that unlock the core workflow pattern defined in `AGENTS.md`. The process of defining and building these commands *is* the definition of our development process (`PLATFORMDEV.md`).

**Commands:** `/dis` (formerly `/def`), `/doc`, `/plan`, `/ready`, `/engage`, `/reflect`

For each command, we will iteratively define the process:
1.  **Define:** Discussion session to establish behavior.
2.  **Spec:** Document requirements.
3.  **Plan:** Create implementation steps.
4.  **Author:** Create prompts/skills for the agent.

**Work Order:**
*   [ ] **Command: `/dis`** (Define, Spec, Plan, Author) -> *Enables structured discussion.*
*   [ ] **Command: `/doc`** (Define, Spec, Plan, Author) -> *Enables documenting decisions.*
*   [ ] **Command: `/plan`** (Define, Spec, Plan, Author) -> *Enables work planning.*
*   [ ] **Command: `/ready`** (Define, Spec, Plan, Author) -> *Enables task prioritization.*
*   [ ] **Command: `/engage`** (Define, Spec, Plan, Author) -> *Enables implementation.*
*   [ ] **Command: `/reflect`** (Define, Spec, Plan, Author) -> *Enables review and iteration.*

*Note: As each command is finalized, `PLATFORMDEV.md` will be updated to reflect the standard.*

## Phase 2: Agentic Tooling
**Goal:** Identify and build Pi tools (extensions or skills) needed for agentic coding workflows (agnostic to specific Apps).
*   [ ] Review workflow capabilities and gaps.
*   [ ] Identify necessary custom Pi Tools/Extensions.
*   [ ] Implement Agentic Tools.

## Phase 3: App Layer Definition & Implementation
**Goal:** Define and build the specific application modules using the workflow established in Phase 1.
*   [ ] `/dis` session for `cyclescraper` Goals & Spec.
*   [ ] `/dis` session for `maxpatcher` Goals & Spec.
*   [ ] `/dis` session for `maxrag` Goals & Spec.
*   [ ] `/dis` session for `maxdocsparser` Goals & Spec.
*   [ ] `/dis` session for `maxprober` Goals & Spec.

## Backlog / Discussion Queue
1.  **Data Flow Architecture:** Detailed session to map interactions between Pi, Beads, and Apps.
2.  **Beads Initialization:** When and how to initialize the global Beads tool in this repo.
