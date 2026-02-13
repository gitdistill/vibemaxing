---
description: High-level Platform Architecture & Constraints
---
# Platform Architecture

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## 1. System Design Pattern
**"The Brain and The Hands"**
The system is designed as a Hub-and-Spoke architecture where `.pi` (The Brain) orchestrates the execution of documentation retrieval and development tools.

### Layer 1: The Brain (.pi/)
*   **Role:** Context management, workflow enforcement, and user interface.
*   **Components:**
    *   **Pi:** The runtime environment (Coding Agent Harness).
    *   **Context7 Extension:** MCP bridge providing the agent with the "Context7" library of Cycling '74 documentation.
    *   **Extensions/Skills/Prompts:** Project-specific logic and workflow enforcement.

### Layer 2: The Hands (apps/)
*   **Role:** Domain-specific execution for Max/MSP.
*   **Constraint:** These apps must not depend on Pi. They are invoked *by* Pi.
*   **Modules:**
    1.  **`maxpatcher`** (Output): Generates/Modifies `.maxpat` JSON structures.
    2.  **`maxprober`** (Feedback): Runtime debugging via Node for Max.

## 2. Documentation Retrieval Stack
Instead of a custom scraping stack, we utilize **Context7 MCP**:
*   **Connection:** Bridge extension located at `.pi/extensions/context7/`.
*   **Source:** Cycling '74 Documentation (Library ID: `/websites/cycling74`).
*   **Tools:**
    *   `context7_resolve_library_id`: To find library IDs.
    *   `context7_query_docs`: For specific object/API retrieval.

## 3. Tech Stack & Constraints

### Global Constraints
*   **Local-First Development:** Development of Max patches and M4L devices happens locally.
*   **Agentic Intelligence:** Rely on Context7 for high-fidelity technical specs instead of local scraping.

### Technology Decisions
*   **Orchestration:** `Pi` (Node.js/Bun).
*   **App Stacks:** Node.js, Python, or MaxPyLang.
*   **Knowledge Layer:** Context7 MCP.

## 4. Directory Structure
```
/
├── .pi/                # Agentic Layer (Prompts, Skills, Context, Extensions)
│   ├── extensions/
│   │   └── context7/   # Context7 MCP Bridge
├── apps/               # Application Layer
│   ├── maxpatcher/
│   └── maxprober/
└── AGENTS.md           # Entry point / Meta-instructions
```
