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
- Use `limit` and `offset` logic if large amounts of documentation are returned (handled via the bridge).
- Session-based lifecycle: The MCP child process must terminate on `session_shutdown`.
