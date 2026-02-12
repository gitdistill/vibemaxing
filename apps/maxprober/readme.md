## 5. Project: `maxprober`

**Role:** The Debugger (Runtime Analysis)
**Agent Grade:** **Grade 4 (Feedback Mechanism)**

### Description

A focused tool for **Runtime Inspection**. It does *not* write patches. It uses a Node.js script inside Max to expose the engine's state to the Agent via terminal commands. This tool enables the **Closed Loop** validation.

### Tech Stack

* **Interface:** Bash (`./scripts/probe_runtime.sh`)
* **Core Logic:** `Node.js` (inside Max `node.script`) + `curl`

### Key Components

1. **Node Bridge:** A script running inside Max that listens for HTTP requests.
2. **Console Reader:** Fetches the Max Window error logs (e.g., "Stack Overflow").
3. **Signal Spy:** Uses `snapshot~` to report RMS amplitude at specific outlets.
4. **Bash Client:** A script that sends `curl` commands to the Node bridge and prints the result to `stdout`.

### 🚀 Agent Kickoff Prompt

> "I am building `maxprober`. I need to fork the 'Max-MCP' concept but strip it down to a read-only debugger. Help me write a `node.script` for Max that exposes the Max Console and Signal levels via a local HTTP server, controllable by a Bash script."

---
