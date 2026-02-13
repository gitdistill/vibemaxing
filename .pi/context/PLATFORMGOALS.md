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
*   **Cognitive Continuity:** Leverage "pi-superpowers" (a pi extension installed globally) to ensure the agent remembers context across sessions and tasks, eliminating the need to repeat "the plan".
*   **Strict Process Adherence:** Enforce the 7-step workflow (Brainstorm -> Finish) to prevent drift and ensure alignment.
*   **Tool Agency:** Give the agent robust CLI access to the `apps/` layer so it can actively participate in development.

### B. The Apps Layer (apps/)
*   **Context7 Integration:** Use the Context7 MCP bridge to provide the agent with real-time, high-fidelity Max/MSP and Cycling '74 documentation.
*   **Patcher Interaction:** Focus development on `maxpatcher` and `maxprober` to allow the agent to read, write, and debug Max patches directly.
*   **Format Transparency:** Solve the "Opaque Binary" problem of `.maxpat` files by robustly parsing them into readable formats (XML/JSON/Text).

## 3. Success Metrics

| Metric | Definition | Target |
| :--- | :--- | :--- |
| **Documentation Precision** | Ability to retrieve correct Max object attributes and JavaScript API methods via Context7. | 100% |
| **Patch Validity** | % of generated Max patches that open without corruption errors. | > 90% |
| **M4L Delivery** | Successful completion and functional validation of the planned Max for Live device. | 1 shipped device |
