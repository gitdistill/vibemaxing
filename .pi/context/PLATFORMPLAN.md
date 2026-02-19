---
description: High-Level Platform Roadmap & Backlog
---
# Platform Plan

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## Phase 0: Foundation (Complete)
*   [x] Scaffold `.pi/prompts/` (Workflow templates).
*   [x] Draft `.pi/context/PLATFORMGOALS.md`.
*   [x] Draft `.pi/context/PLATFORMARCH.md`.

## Phase 1: Decoupled Intelligence (Current Focus)
**Goal:** Transition to the "Co-Architect" model with separated research and building tools.

*   [x] **Design:** Architecture Evolution (`docs/plans/2026-02-17-architecture-evolution.md`).
*   [x] **Design:** Intelligence Extension Spec (`docs/plans/2026-02-17-vibemax-intelligence-design.md`).
*   [ ] **Implementation:** Scaffold and build `.pi/extensions/vibemax-intelligence/`.
*   [ ] **Implementation:** Populate `SKILL.md` for the intelligence extension (User to provide content).
*   [ ] **Implementation:** Refactor `maxpatcher` to remove `intelligence.py` (`docs/plans/2026-02-17-maxpatcher-refactor.md`).

## Phase 2: Core Development Apps (In Progress)
**Goal:** Finalize the "Hands" for patch manipulation and debugging.
*   [x] MVP of `maxpatcher` (Builder).
*   [ ] Refactor/Clean up `maxpatcher` according to the new decoupled spec.
*   [ ] Finalize Spec for `maxprober` (Runtime debugging/Node for Max).

## Phase 3: First Device Implementation (Pending)
**Goal:** Deploy the full workflow (Brainstorm -> Finish) to create a functional Max for Live device.
*   [ ] Brainstorming for "Vibemaxing V1" Device.
*   [ ] Execute implementation using the new Co-Architect workflow.

## Backlog / Discussion Queue
- [ ] Investigate automatic `.maxpat` to JSON conversion for existing patches.
- [x] Explore M4L specific API limitations in Context7.
- [ ] add context7 agentic api request logging 
- [ ] migrate to pi superpowers plus
