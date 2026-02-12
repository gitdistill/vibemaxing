## Project: Vibemaxing Monorepo

**Goal:** Build a semi-autonomous (mix of human in and out of the loop) development platform for Max/MSP patches and Max for Live devices.

---

## 1. Architectural Framework

**Our monorepo is made up of 2 layers:**

1. An agentic layer contained in `.pi/`, made up of context, skills, tools, prompts and extensions specific to the development of the agentic development platform infrastructure.

2. An apps layer contained in `apps/` where 5 discrete application modules reside.

| App | Role | Tech Stack (unvalidated) |
| --- | --- | --- |
| **`cyclescraper`** | **Web ETL** | Python, Exa |
| **`maxdocsparser`** | **Local Parser** | Python, MaxPyLang |
| **`maxrag`** | **Memory/RAG** | ChromaDB, MCP |
| **`maxpatcher`** | **Builder** | Python (fork + wrapper) |
| **`maxprober`** | **Debugger** | Node.js (inside Max) |

**In addition to these 2 layers we have the following global component**

**Pi:** a minimal terminal based agentic coding harness, with only basic defaults in place.

**With these layers and harness we create max devices each in their own dedicated directory**

For now we are only focused on developing the supporting apps inidiviually, and the finally we will implement our first max device.

---

## 2. Core Workflow Pattern 

For both platform and app development we leverage the pi-superpowers extension which provides the user a set of skills for each stage of the development process: 

1. **Brainstorm** `/skill:brainstorming` refines your idea into a design document
2. **Isolate** `/skill:using-git-worktrees` creates a clean workspace
3. **Plan** `/skill:writing-plans` breaks work into bite-sized TDD tasks
4. **Execute** `/skill:executing-plans` or `/skill:subagent-driven-development` works through the plan
5. **Verify** `/skill:verification-before-completion` proves it works
6. **Review** `/skill:requesting-code-review` catches issues
7. **Finish** `/skill:finishing-a-development-branch` merges or creates a PR

_!!IMPORTANT!!: moving from one stage the next is the responsibilty of the user NOT the agent._

---

## 3. Project Context & Artifact Schema

To maintain context window efficiency, you are aware of the following artifact themes but must not read them on load. Access these files only when their specific contents are required for the current task.

**Naming Convention:**
Artifacts follow the pattern `{SCOPE}{SUFFIX}.md`
* **SCOPE:** `PLATFORM` (Global) or `{APPNAME}` (e.g., `cyclescraper`, `maxrag`)
* **SUFFIX:** Maps to the themes below.

**Artifact Themes:**

| Suffix | Theme | Content Definition |
| :--- | :--- | :--- |
| **`...GOALS.md`** | **Objectives** | Project goals, key objectives, and success metrics. |
| **`...ARCH`** | **Architecture** | System design, data flow, tech stack, and rigid constraints. |
| **`...DEV.md`** | **Process** | Development guidelines, quality gates, and supporting tooling setup. |
| **`...SPEC.md`** | **Requirements** | Functional specifications and technical requirements. |
| **`...PLAN.md`** | **Roadmap** | Phased workplan, current phase summary, and high-level backlog. |

**Retrieval Instruction:**
Do not `cat` or read these files preemptively. You will be instructed on when to load specific artifacts based on user input and the immediate context of the request.

---

## 4. Operational Guidelines

**Token Economy & Tool Usage:**
*   **Search:** Always use `rg` (ripgrep) instead of `grep`. `rg` respects `.gitignore` and ignores `node_modules` by default, preventing token usage explosions.
*   **Reading:** When reading files, prefer specific paths. If reading huge logs or data files, use `limit` and `offset`.

**Cognitive Safety & Stability (CRITICAL):**
*   **Documentation Reading:** **NEVER** read full documentation files (`node_modules/**/*.md`, `.pi/skills/**/*.md`) unless explicitly instructed.
*   **Use Surgical Tools:** Use `grep` or `read` with `limit`/`offset` to extract specific syntax/answers. Reading >50KB of documentation destabilizes context and causes loops.
*   **Stop Condition:** If you find yourself repeating output or looping, **STOP IMMEDIATELY** and ask for clarification.

**Operational Philosophy: Execution over Simulation**
*   **Do Not Simulate:** Do not attempt to mentally simulate complex decision trees (e.g., skill logic) to their conclusion.
*   **Step-by-Step Execution:** Execute the first step, report the result, and *then* ask for the next step.
*   **State Management:** Trust files and logs to hold state. Do not try to hold the entire "potential future" in your context window.
*   **Bias for Action:** If a decision is ambiguous, ask the user or try the most reversible action. Do not loop trying to find the "perfect" path.