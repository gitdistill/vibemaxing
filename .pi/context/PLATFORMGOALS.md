---
description: High-level Platform Goals & Strategic Vision
---
# Platform Goals

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo)

## 1. The Vision: "The Competent Co-Architect"

We are building a development environment where the AI agent transcends the role of a simple code generator to become a **Senior Systems Architect** and **Max/MSP Consultant**. The primary goal is **Competency**: bridging the gap between generic LLM knowledge and the specific, complex reality of Max/MSP and Max for Live development.

### Core Roles

1.  **Discussion Partner & Co-Architect (Primary):**
    *   **Responsibility:** Deep research, architectural design, and "pre-flight" validation.
    *   **Activity:** The agent helps design system structures, data flows, and component interactions *before* implementation begins.
    *   **Source of Truth:** Architecture is defined in **Documentation** (`docs/plans/`, `docs/architecture/`), not implicitly in code.

2.  **Product Manager (Secondary):**
    *   **Responsibility:** Defining scope, breaking down epics, and tracking progress.

3.  **Pair Programmer & Builder (Supportive):**
    *   **Responsibility:** "Glue" work, implementation details, and generating "Scratchpad" patches.
    *   **Mode:** While the agent *can* implement full modules, it primarily uses `maxpatcher` to:
        *   Demonstrate a concept (Scratchpad).
        *   Generate specific, complex snippets for manual integration.
        *   Analyze or debug existing patches.

## 2. Architectural Principles

### A. Document-Driven Development
*   The **Specification** is the master record.
*   We do not start coding until the design is documented and validated against Max/MSP constraints.
*   The agent uses its tools to *verify* the spec (e.g., "Does this object support this message?") before the spec is finalized.

### B. Decoupled Intelligence
*   **Context7 (The Research Engine):** A standalone capability, not buried inside a builder tool.
*   **Access:** The agent can query Cycling '74 documentation, LOM references, and JS APIs at *any* stage (Brainstorming, Planning, Debugging).
*   **Goal:** Prevent hallucinations by fact-checking Max/MSP mechanics against the official docs.

### C. The Toolchain (`apps/`)
*   **`maxpatcher` (The Builder/Reasoner):** A bridge between Python reasoning and Max patch structure. Used to scaffold, generate snippets, and analyze patch files.
*   **`maxprober` (The Runtime verifier):** A debugging harness to verify that the built devices actually work as intended.

## 3. Success Metrics

| Metric | Definition | Target |
| :--- | :--- | :--- |
| **Architectural Validity** | Can the proposed design actually be built in Max? (Verified via Context7). | 100% |
| **Hallucination Rate** | Frequency of suggesting non-existent objects, messages, or attributes. | < 5% |
| **Snippet Utility** | Usefulness of generated "scratchpad" code in solving the immediate problem. | High |
