## 4. Project: `maxpatcher`

**Role:** The Hands (Manipulation & Validation)
**Agent Grade:** **Grade 3 (Skill Library)**

### Description

A library to generate `.maxpat` files. The Agent never writes Python code directly in chat; it writes a **Spec File (JSON)** and runs this tool to compile it.

### Tech Stack

* **Interface:** Bash (`./scripts/build_patch.sh`)
* **Core Logic:** Python (Fork of `Barnard-PL-Labs/MaxPyLang`)

### Key Components

1. **Spec Reader:** Parses a high-level JSON description of the desired patch.
2. **Layout Engine:** A constraint solver that calculates object coordinates (Cursor system), removing the need for the Agent to do math.
3. **Static Validator:** Checks for illegal connections (Signal → Float) *before* saving. This is the first line of defense in the **Grade 4 Loop**.
4. **Snippet Injector:** Inserts pre-made chunks from `maxrag`.

### 🚀 Agent Kickoff Prompt

> "I am refactoring `maxpatcher`. We are moving to a 'Spec-First' workflow. Help me design the JSON schema for a patch definition and the `build_patch.sh` script that reads that JSON and calls the Python library to generate the file."

---