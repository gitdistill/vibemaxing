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
    <!-- *   **Context7 Extension:** MCP bridge providing the agent with the "Context7" library of Cycling '74 documentation. -->
    *   **Extensions/Skills/Prompts:** Project-specific logic and workflow enforcement.

### Layer 2: The Hands (apps/)
*   **Role:** Domain-specific execution for Max/MSP.
*   **Modules:**
    1.  **`maxpatcher`** (Output): A Python-based Builder. Owns a flattened fork of the `MaxPyLang` engine.
    2.  **`maxprober`** (Feedback): Runtime debugging via Node for Max. (DEFERRED for future iteration)

### Layer 3: User Land (projects/)
*   **Role:** Isolated development environments for specific Max devices or patches.
*   **Structure:** Contains `src/` (Python source) and `dist/` (Generated .maxpat). Configuration via `.vibe.json`.

## 2. Documentation Retrieval Stack

### Layer 1: CycleScraper (apps/cyclescraper/)
*   **Role:** Specialized documentation extraction for Cycling '74's Next.js SPA.
*   **Engine:** Crawl4AI with a sequential crawling strategy to prevent state leakage.
*   **Output:** Clean Markdown with YAML frontmatter in `data/content/`.

### Layer 2: Knowledge Map
*   **Tool:** `apps/cyclescraper/build_map.py`
*   **Role:** Aggregates scraped files into a structured `knowledge-map.json` using `docs/seeds.json` as the source of truth for hierarchy and metadata.
*   **Purpose:** Provides a unified context for agents.

### Layer 3: Context7 Pi Extension
TBD

## 3. Tech Stack & Constraints

### Global Constraints
*   **Local-First Development:** Development of Max patches and M4L devices happens locally.
*   **Lazy Intelligence:** Agents must prioritize local metadata and only query external documentation when encountering "Unknown Objects".

### Technology Decisions
*   **Orchestration:** `Pi` (Node.js/Bun).
*   **App Stacks:** Node.js, Python (Crawl4AI/Pydantic), or MaxPyLang.
*   **Knowledge Layer:** Scraped Markdown + Knowledge Map JSON.

## 4. Directory Structure
```
/
├── .pi/                # Agentic Layer (Prompts, Skills, Context, Extensions)
├── apps/               # Application Layer
│   ├── cyclescraper/   # Documentation Scraping Engine
│   ├── maxpatcher/
│   └── maxprober/
├── data/               # Persistent Data
│   ├── content/        # Scraped Documentation (Markdown)
│   └── knowledge-map.json
├── docs/               # Specifications and Seed Data
└── AGENTS.md           # Entry point / Meta-instructions
```
