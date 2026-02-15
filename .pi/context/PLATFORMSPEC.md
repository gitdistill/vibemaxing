---
description: Technical Specifications for Platform Extensions & Tools
---
# Platform Specification

**Context Scope:** `PLATFORM` (Vibemaxing Monorepo Infrastructure)

## 1. Context7 Extension Bridge
**Location:** `.pi/extensions/context7/`

### Purpose
Connects the Pi coding agent to the Context7 MCP server to provide high-fidelity documentation for Cycling '74 (Max/MSP, M4L, JS API).

### Architecture
- **Protocol:** Model Context Protocol (MCP).
- **Transport:** Stdio (Child Process).
- **Package:** `@upstash/context7-mcp`.
- **API:** Upstash Context7 REST API.

### Tool Definitions
#### `context7_resolve_library_id`
- **Description:** Resolves a library name (e.g., "cycling74") to a Context7 ID.
- **Parameters:**
  - `libraryName` (string): Search query for the library.
  - `query` (string): User intent.

#### `context7_query_docs`
- **Description:** Retrieves documentation snippets based on a query.
- **Parameters:**
  - `libraryId` (string): The resolved ID (e.g., `/websites/cycling74`).
  - `query` (string): The technical question or object name.

### Policy & Usage
- Agents must prioritize searching Context7 over guessing Max object attributes.
- **Lazy Lookup:** Query Context7 only when `MaxPyLang` reports a `PatchError: unknown obj` or local project metadata is missing.

## 2. Two-Tier Intelligence Architecture
Intelligence is split between **Conceptual Wisdom** and **Technical Grounding**.

### Tier 1: Conceptual Intelligence (The "How-To")
- **Source:** Tutorials, User Guides, and LOM Reference.
- **Mechanism:** Pi Skills (Brainstorming/Research phases).
- **Persistence:** Findings are saved as Markdown in `projects/<name>/docs/research/`.
- **Purpose:** Guides architectural decisions and ensures idiomatic Max patterns.

### Tier 2: Technical Intelligence (The "Reference")
- **Source:** Object Reference docs.
- **Mechanism:** `maxpatcher sync <obj>` command.
- **Persistence:** Findings are synthesized into JSON in a global store at `apps/maxpatcher/metadata/objects/`.
- **Conflict Resolution:** **Vibe Global Wins**. Synced metadata always overrides the native `MaxPyLang` definitions.
- **Purpose:** Grounding the `MaxPyLang` engine to ensure build integrity and correct wiring.

## 3. MaxPatcher Build System
The build system is the primary bridge between Python-based logic and Max JSON patches.

### Execution Model
- **Isolation:** Project scripts are executed via **Subprocess** to ensure environment purity and stable error capturing.
- **Feedback:** CLI provides **LLM-optimized summaries**. Raw tracebacks are suppressed by default to prevent agent context pollution.
- **Helper Layer:** The `vibe_utils` library provides high-level abstractions for idiomatic Max patterns (e.g., stereo connections, M4L signal routing).

### Validation & Quality Gate
- **Static Analysis:** Validation is performed on the generated `.maxpat` JSON without requiring a running Max instance.
- **Blocking Severity:** Validation failures result in a non-zero exit code, preventing the release of low-quality or broken artifacts.

## 4. Resource Management
- **Budgeting:** Context7 usage is capped at **1,000 requests per month**. 
- **Caching:** Mandatory caching for both tiers to prevent redundant token consumption.
- Session-based lifecycle: The MCP child process must terminate on `session_shutdown`.
