## Project: Vibemaxing Monorepo

**Goal:** Build a semi-autonomous development platform for Max/MSP patches and Max for Live devices using Context7 for technical intelligence.

**⚠️ CURRENT PHASE: DESIGN & BRAINSTORMING ONLY ⚠️**
*   **Status:** Architectural Design Refinement.
*   **Directive:** We are **NOT** ready to move to implementation. Do not write code. Do not start builds. Focus solely on refining design documents and verifying assumptions.

---

## 1. Architectural Framework

**Our monorepo is made up of 2 layers:**

1. **Agentic Layer (.pi/):** Contains context, skills, and extensions.
   *   **Context7 Extension:** Provides tools to query Cycling '74 documentation.
   *   **Library ID:** `/websites/cycling74`

2. **Apps Layer (apps/):** Discrete modules for patch manipulation.

| App | Role | Tech Stack |
| --- | --- | --- |
| **`maxpatcher`** | **Builder** | Python (Internal MaxPyLang Fork) |
| **`maxprober`** | **Analyzer** | MCP Server + Bash |

**Global Harness:** **Pi** (Terminal-based agentic harness).

---

## 2. Intelligence & Documentation (Context7)

The agent uses the **Context7 MCP** bridge to research Max/MSP objects, JavaScript APIs, and Live Object Model (LOM) details.

**Available Tools:**
*   `context7_resolve_library_id`: Resolves library names (e.g., "cycling74").
*   `context7_query_docs`: Retrieves documentation using the Library ID.

---

## 3. Core Workflow Pattern 

Leverage **pi-superpowers** skills:
1. **Brainstorm** `/skill:brainstorming`
2. **Isolate** `/skill:using-git-worktrees`
3. **Plan** `/skill:writing-plans`
4. **Execute** `/skill:executing-plans` or `/skill:subagent-driven-development`
5. **Verify** `/skill:verification-before-completion`
6. **Review** `/skill:requesting-code-review`
7. **Finish** `/skill:finishing-a-development-branch`

---

## 4. Strict Enforcement Rules (MANDATORY)

### I. Tool Usage & Token Economy
*   **NO RECURSIVE LS:** Use `tree -L 2` or `ls -F`.
*   **NO RECURSIVE GREP:** Always use `rg`.
*   **READ LIMITS:** Never `read` > 50KB or 2000 lines.

### II. Cognitive Safety
*   **CONTEXT7 FIRST:** Always search Context7 before assuming Max object behavior or JS API methods.
*   **STOP ON LOOPING:** If repeating output, STOP immediately.
*   **USER CONFIRMATION:** Operations > 10 files or 50KB require permission.

### III. Operational Philosophy
*   **STEP-BY-STEP:** Execute one step, report, then move to next.
*   **TRUST THE DISK:** Files and git state are the source of truth.

### IV. Version Control Hygiene (CRITICAL TOKEN SAFETY)
* **SILENCE IS GOLDEN:** For any `git add` or `git commit` involving >5 files, YOU MUST use the quiet flag (`-q` or `--quiet`) or redirect stdout to `/dev/null`.
    * *Bad:* `git add .` (Risks flooding context)
    * *Good:* `git add .` (If you are sure it's small) OR `git commit -q -m "message"`
* **NO COMPILER ARTIFACTS:** Before adding directories, check `.gitignore`. NEVER add `__pycache__`, `node_modules`, or `.DS_Store`.
* **VERIFY COMPACTLY:** Do not rely on `git commit` output to verify success.
    * After a quiet commit, verify with: `git log -1 --oneline` or `git status --short`.
* **LARGE OPS:** If moving/refactoring libraries, use `git mv` (which is often cleaner) or pipe output: `git add . > /dev/null && git status --short`.