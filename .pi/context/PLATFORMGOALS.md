---
description: High-level Platform Goals & Success Metrics
---
# Platform Goals

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## 1. Strategic Vision
**The "Co-Architect" Relationship**
We are building a development environment where the AI agent transcends the role of a simple code generator to become a multifaceted partner:
*   **Pair Programmer:** Writing and debugging code alongside the human.
*   **Product Manager:** helping define scope and track progress.
*   **Discussion Partner:** exploring ideas and trade-offs.
*   **Contributing Developer:** handling "glue" work and implementation details.
*   **Co-Architect:** designing system structures and data flows.

The platform does not aim to replace the human artist but to empower them by handling parsing, git state, scaffolding, and logic debugging.

## 2. Key Objectives

### A. The Agentic Layer (.pi)
*   **Cognitive Continuity:** Leverage "Beads" (external global tool) to ensure the agent remembers context across sessions and tasks, eliminating the need to repeat "the plan".
*   **Strict Process Adherence:** Enforce the 6-step workflow (`/dis` -> `/reflect`) to prevent drift and ensure alignment.
*   **Tool Agency:** Give the agent robust CLI access to the `apps/` layer so it can actively participate in development.

### B. The Apps Layer (apps/)
*   **Modularity:** The 5 core apps (`cyclescraper`, `maxdocsparser`, `maxrag`, `maxpatcher`, `maxprober`) constitute the complete V1 toolset. Each must function as a standalone CLI tool first.
*   **Format Transparency:** Solve the "Opaque Binary" problem of `.maxpat` files by robustly parsing them into readable formats (XML/JSON/Text).

## 3. Success Metrics

| Metric | Definition | Target |
| :--- | :--- | :--- |
| **Context Retention** | Ability of the agent to recall a decision made in `/dis` during the `/engage` phase without re-reading chat history (relying on Beads/Docs). | 100% |
| **Patch Validity** | % of generated Max patches that open without corruption errors. | > 90% |
| **M4L Delivery** | Successful completion and functional validation of the planned Max for Live device. | 1 shipped device |
