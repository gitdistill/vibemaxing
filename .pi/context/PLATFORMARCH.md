---
description: High-level Platform Architecture & Constraints
---
# Platform Architecture

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## 1. System Design Pattern
**"The Brain and The Hands"**
The system is designed as a Hub-and-Spoke architecture where `.pi` (The Brain) orchestrates the execution of independent tools in `apps/` (The Hands).

### Layer 1: The Brain (.pi/)
*   **Role:** Context management, workflow enforcement, and user interface.
*   **Components:**
    *   **Pi:** The runtime environment (Coding Agent Harness).
    *   **Extensions/Skills/Prompts:** TBD

### Layer 2: The Hands (apps/)
*   **Role:** Domain-specific execution.
*   **Constraint:** These apps must not depend on Pi. They are invoked *by* Pi.
*   **Modules:**
    1.  **`cyclescraper`** (Input): Gathers external knowledge (Cycling '74 docs, forums).
    2.  **`maxdocsparser`** (Translation): Converts Max documentation/objects into LLM-friendly schemas.
    3.  **`maxrag`** (Memory): Vector store for documentation and past patches.
    4.  **`maxpatcher`** (Output): Generates/Modifies `.maxpat` JSON structures.
    5.  **`maxprober`** (Feedback): Runtime debugging via Node for Max.

## 2. Data Flow
*   **Status:** Pending Definition

## 3. Tech Stack & Constraints

### Global Constraints
*   **Local-First:** All tools and DBs must run locally. No cloud dependencies for core logic.
*   **Language Agnostic Interfaces:** Tools interact via CLI (STDIN/STDOUT), allowing `apps/` to use the best tool for the job.

### Technology Decisions
*   **Orchestration:** `Pi` (Node.js/Bun).
*   **App Stacks:** To be determined during individual app planning sessions.
*   **IPC:** CLI/STDIO (No long-running servers required for V1).
*   **Vector DB:** Placeholder (e.g., ChromaDB).

## 4. Directory Structure
```
/
├── .pi/                # Agentic Layer (Prompts, Skills, Context)
├── apps/               # Application Layer
│   ├── cyclescraper/
│   ├── maxdocsparser/
│   ├── maxrag/
│   ├── maxpatcher/
│   └── maxprober/
└── AGENTS.md           # Entry point / Meta-instructions
```
