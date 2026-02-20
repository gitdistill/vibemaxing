---
description: High-Level Platform Roadmap & Backlog
---
# Platform Plan

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## Current Epic: Decoupled Intelligence (Target Architecture)
**Active Master Plan:** `docs/plans/2026-02-17-decoupled-architecture-master.md`

## Phase 1: Knowledge Infrastructure (Current Focus)
**Goal:** Transition to the "Co-Architect" model with separated research and building tools.

*   [x] **Design:** Consolidated Master Plan (`docs/plans/2026-02-17-decoupled-architecture-master.md`).
*   [ ] **Implementation (Part A):** Scaffold and build `.pi/extensions/vibemax-intelligence/` (TS Pi Extension).
*   [ ] **Implementation (Part B):** Refactor `maxpatcher` to remove `intelligence.py` and enforce local-only builds.

## Phase 2: Core Development Apps (In Progress)
**Goal:** Finalize the "Hands" for patch manipulation and debugging.
*   [x] MVP of `maxpatcher` (Builder).
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
