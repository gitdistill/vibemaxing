---
description: High-Level Platform Roadmap & Backlog
---
# Platform Plan

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## Phase 0: Foundation (Complete)
*   [x] Scaffold `.pi/prompts/` (Workflow templates).
*   [x] Draft `.pi/context/PLATFORMGOALS.md`.
*   [x] Draft `.pi/context/PLATFORMARCH.md`.
*   [x] Finalize `.pi/context/PLATFORMDEV.md` (Based on `pi-superpowers`).

## Phase 1: Knowledge Infrastructure (Complete)
**Goal:** Establish high-fidelity documentation retrieval without local RAG overhead.
*   [x] Research Context7 MCP integration.
*   [x] Implement Context7 TypeScript extension bridge.
*   [x] Verify retrieval of Cycling '74 documentation.
*   [x] Update Platform Architecture to reflect the removal of `cyclescraper`, `maxdocsparser`, and `maxrag`.

## Phase 2: Core Development Apps (In Progress)
**Goal:** Build the essential "Hands" for patch manipulation and debugging.
*   [ ] Brainstorming & Spec for `maxpatcher` (JSON-based patch generation).
*   [ ] Brainstorming & Spec for `maxprober` (Runtime debugging/Node for Max).

## Phase 3: First Device Implementation (Pending)
**Goal:** Deploy the full workflow (Brainstorm -> Finish) to create a functional Max for Live device.
*   [ ] Brainstorming for "Vibemaxing V1" Device.
*   [ ] Execute implementation using `maxpatcher` and Context7 intelligence.

## Backlog / Discussion Queue
- [ ] Investigate automatic `.maxpat` to JSON conversion for existing patches.
- [ ] Explore M4L specific API limitations in Context7.
