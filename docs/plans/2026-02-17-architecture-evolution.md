# Architecture Evolution: Decoupled Intelligence & The "Co-Architect" Platform

**Date:** 2026-02-17
**Status:** Brainstorming -> Implementation
**Goal:** Refactor the Vibemaxing monorepo to support a "Co-Architect" AI agent by decoupling the intelligence layer from the builder layer.

## 1. Core Principles

1.  **Platform Purpose:** The platform is a "Computer-Aided Design (CAD)" system for Max/MSP. The agent is a Senior Architect who uses tools to verify designs before implementation.
2.  **Decoupled Intelligence:** `Context7` integration is moved out of `maxpatcher` and into a global Pi extension (`.pi/extensions/vibemax-intelligence`).
3.  **Deterministic Building:** `maxpatcher` (the builder) is purely local, relying on its internal `maxpylang` database. It never makes network calls.
4.  **Research & Augmentation:** The intelligence extension is responsible for:
    *   **Researching:** Answering "How do I use `poly~`?" or "What is the LOM path for a clip?"
    *   **Augmenting:** Fetching metadata for missing objects and writing new JSON definitions to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`.

## 2. Component Architecture

### A. The Researcher (`.pi/extensions/vibemax-intelligence`)
*   **Type:** Pi Extension (TypeScript/JavaScript).
*   **Tools Provided:**
    *   `research_max <query>`: Queries Context7 for documentation, summarizes usage, and returns Markdown.
    *   `augment_max_db <object_name>`: Fetches object metadata (inlets, outlets, attributes) and writes a new JSON file to the appropriate `maxpylang` data directory (`max`, `msp`, or `jitter`).
*   **Responsibilities:**
    *   Caching responses to avoid excessive API calls.
    *   Rate limiting to respect Context7 quotas.
    *   Formatting output for human/agent readability.

### B. The Builder (`apps/maxpatcher`)
*   **Type:** Python Application.
*   **Responsibilities:**
    *   **Scaffold:** Create new project structures.
    *   **Build:** Compile Python source (`main.py`) into Max patches (`.maxpat`).
    *   **Validate:** Check patch integrity using local rules.
*   **Data Source:** `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`.
*   **Logic:**
    *   If an object is found in the DB, use its definition.
    *   If an object is missing, warn the user and suggest using the `research_max` tool to add it.
    *   **REMOVE:** The `intelligence.py` module and all `context7` dependencies.

### C. The Verifier (`apps/maxprober`)
*   **Type:** Runtime Debugger (MCP Server).
*   **Responsibilities:**
    *   Connect to running Max instances via UDP/OSC.
    *   Verify signal flow and attribute values at runtime.

## 3. Migration Plan

1.  **Phase 1: Decoupling**
    *   Create `.pi/extensions/vibemax-intelligence/`.
    *   Move `context7` logic from `apps/maxpatcher/maxpatcher/intelligence.py` to the new extension.
    *   Remove `intelligence.py` from `maxpatcher`.

2.  **Phase 2: Extension Development**
    *   Implement `research_max` tool (TS).
    *   Implement `augment_max_db` tool (TS).
    *   Add caching and rate limiting.

3.  **Phase 3: Builder Refactoring**
    *   Update `maxpatcher` to rely solely on local data.
    *   Add friendly error messages for missing objects ("Object 'xyz' not found. Run 'research_max xyz' to add it.").

## 4. Documentation Strategy

*   **Source of Truth:** Architecture is defined in `docs/plans/` and `docs/architecture/`.
*   **Workflow:**
    1.  **Brainstorm:** Discuss ideas with the agent (using `research_max` to verify facts).
    2.  **Plan:** Write a design doc.
    3.  **Build:** Use `maxpatcher` to implement the design.
    4.  **Verify:** Use `maxprober` to test the result.
