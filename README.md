# Vibemaxing Monorepo

**Vibemaxing** is a semi-autonomous development platform for Max/MSP patches and Max for Live devices. It leverages **Context7** for technical intelligence to bridge the gap between generic LLM knowledge and the complex reality of Max/MSP development.

## 🎯 Vision: The Competent Co-Architect

We are building a system where the AI agent acts as a **Senior Systems Architect**, not just a code generator.
*   **Decoupled Intelligence:** Research happens *before* implementation.
*   **Document-Driven:** The specification is the source of truth.
*   **Local-First:** The builder tools are deterministic and work offline, relying on a local database that is augmented on-demand.

---

## 🏗 Architecture: "The Brain and The Hands"

The system uses a Hub-and-Spoke architecture:

### 1. The Brain (`.pi/`)
*   **Role:** Orchestration, research, and workflow enforcement.
*   **Components:**
    *   **Pi:** The runtime environment.
    *   **Vibemax Intelligence Extension:** A bridge to the **Context7 MCP** documentation engine (Cycling '74 docs).
    *   **Skills:** Specialized workflows for brainstorming, planning, and debugging.

### 2. The Hands (`apps/`)
Discrete, domain-specific modules that execute tasks.
*   **`maxpatcher` (The Builder):** A Python-based builder that owns a flattened fork of `MaxPyLang`. It compiles Python scripts into `.maxpat` files using *only* local metadata.
*   **`maxprober` (The Analyzer):** (Future) A runtime debugging harness.

### 3. User Land (`projects/`)
Isolated environments for specific devices or patches.
*   **Structure:** `src/` (Python source), `dist/` (Generated Max patches), `docs/` (Research notes).

---

## 🧩 Core Components

### `vibemax-intelligence` (Extension)
*   **Location:** `.pi/extensions/vibemax-intelligence/`
*   **Purpose:** The "Researcher." It queries Cycling '74 documentation via Context7.
*   **Tools:**
    *   `research_max(query)`: Fetches raw JSON documentation for objects, guides, or LOM.
    *   `augment_max_db(object, category)`: Fetches object metadata and writes it to `maxpatcher`'s local database.

### `cyclescraper` (Script)
WIP

### `maxpatcher` (App)
*   **Location:** `apps/maxpatcher/`
*   **Purpose:** The "Builder." Converts Python logic into Max patches.
*   **Constraint:** **Zero Network Connectivity.** It halts if an object is unknown.
*   **Recovery:** If `maxpatcher` fails with `[MISSING_OBJECT]`, the agent uses `augment_max_db` to teach it the new object, then rebuilds.

---

## 📂 Directory Structure

```text
/
├── .pi/                     # Agentic Layer
│   ├── extensions/
│   │   └── vibemax-intelligence/ # Context7 Bridge
│   ├── context/             # Platform Documentation
│   └── skills/              # Workflow definitions
├── apps/                    # Application Layer
│   ├── maxpatcher/          # Python Builder (Offline)
│   └── maxprober/           # Runtime Debugger
├── projects/                # User Projects
│   └── my-device/
│       ├── src/             # Python logic
│       └── dist/            # Compiled .maxpat
├── docs/                    # Specs & Implementation Plans
│                
└── AGENTS.md                # Meta-instructions for the Agent
```
