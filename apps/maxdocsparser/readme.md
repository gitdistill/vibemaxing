## 2. Project: `maxdocsparser`

**Role:** Semantic Parsing (The "Translator")
**Agent Grade:** **Grade 1 (Pipeline)** – Deterministic parsing logic.

### Description

A specialized parser that ingests local Max application files (`.maxhelp`, `.maxref.xml`). Crucially, it converts visual patch logic into textual narratives so the Agent can "read" how objects connect.

### Tech Stack

* **Interface:** Bash (`./scripts/ingest_knowledge.sh`)
* **Core Logic:** Python (using `maxpatcher` for parsing)

### Key Components

1. **Cluster Detector:** Identifies unconnected "islands" of objects in help files.
2. **Spatial-Semantic Linker:** Geometric heuristic linking "Comment" boxes to nearby "Objects." (If a comment is within 50px, it belongs to that object).
3. **Graph-to-Text Narrator:** Generates descriptions like *"A phasor~ connects to cycle~..."*
4. **Snippet Exporter:** Saves parsed islands as atomic text chunks for the RAG.

### 🚀 Agent Kickoff Prompt

> "I am building `maxdocsparser`. I need a 'Spatial-Semantic Linker' that reads Max JSON and links comments to nearby objects. Help me write the Python logic and the Bash wrapper so I can run `./scripts/ingest_knowledge.sh` to parse my local Max folder."

---