## 3. Project: `maxrag`

**Role:** The Brain (Knowledge Retrieval)
**Agent Grade:** **Grade 3 (Tool)** – The Agent's reference library.

### Description

The central library. It hosts the vector database.

* **For Agents:** Accessed via CLI scripts to keep context lightweight.
* **For Humans:** Accessed via MCP Server (in Cursor/Claude Desktop) for interactive research.

### Tech Stack

* **Interface:** Bash (`./scripts/ask_docs.sh`) & MCP Protocol
* **Database:** `ChromaDB` (Local)

### Key Components

1. **The Indexer:** Watcher script that updates the vector store from `maxdocsparser` output.
2. **CLI Query Tool:** A simple script that takes a query string and prints the answer to `stdout`.
3. **MCP Wrapper:** A lightweight server layer that wraps the CLI tools for IDE integration.

### 🚀 Agent Kickoff Prompt

> "I am building `maxrag`. We need a dual interface: a Python CLI for the Agent scripts, and an MCP server wrapper for my IDE. Help me design the `ChromaDB` schema to store 'Narrated Snippets' and the `./scripts/ask_docs.sh` entry point."

---