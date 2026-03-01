# Plan for maxpert Skill (v1)

## Context
Implement the `maxpert` Pi Skill (v1), fulfilling the "Competent Co-Architect" role. This skill defines the agent's identity as a Vibemax expert and provides clear workflows for using the local knowledge base (`search_docs.py`) and object library (`OBJ_INFO`) to ensure architectural integrity and minimize hallucinations.

## Approach
1.  **Identity:** Establish `maxpert` as the "Vibemax Co-Architect," prioritizing idiomatic Max/MSP/Jitter/LOM implementation.
2.  **Workflow (RAG):** Mandate the use of `python3 apps/cyclescraper/search_docs.py` when an architectural decision is needed or when the agent is unsure about specific Max idioms.
3.  **Local-First Object Verification:** Instruct the agent to check the local object library in `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{category}/{object_name}.json` before proposing code.
4.  **Balance:** Use "Context over directives" to explain *why* checking local documentation is critical for system stability (e.g., matching the Max/MSP version of the project).
5.  **Exclusions:** v1 explicitly excludes fallback to Context7/API lookups.

## Files to modify
- `.pi/skills/maxpert/SKILL.md` (New file)

## Reuse
- **`apps/cyclescraper/search_docs.py`**: The primary tool for navigating the knowledge base.
- **`apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`**: The source of truth for existing object definitions.

## Steps
- [ ] Create directory `.pi/skills/maxpert/`.
- [ ] Draft `SKILL.md` with:
    - [ ] **Frontmatter**: `name: maxpert`, `description: Professional Max/MSP/Jitter/LOM architect. Provides idiomatic structural guidance and validates object mechanics using local knowledge.`
    - [ ] **Identity & Role**: Define the "Maxpert" persona as a senior-level technical partner who values clarity, efficiency, and robustness in Max patching.
    - [ ] **Philosophy**: Emphasis on "Understand the Idiom" (reading guides before implementation) and "Trust but Verify" (checking `OBJ_INFO` before proposing code).
    - [ ] **Workflow: Deep Research**: Mandate using `python3 apps/cyclescraper/search_docs.py` for queries involving concepts like "signal routing," "matrix management," or "Ableton Live integration."
    - [ ] **Workflow: Object Grounding**: Instruct the agent to locate object definitions in `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/{max|msp|jit}/<name>.json` to ensure accurate inlet/outlet and attribute usage.
    - [ ] **Workflow: Hallucination Defense**: Direct the agent to state when a specific technique or object is NOT found in the local knowledge base instead of guessing.
- [ ] Validate the skill for conciseness and appropriate triggers.

## Verification
- Invoke the skill explicitly with `/skill:maxpert` (once implemented and reloaded).
- Ask the agent: "How should I handle state management between multiple abstractions?" and observe if it uses `search_docs.py` to find guides first.
- Ask the agent: "What are the attributes for the `coll` object?" and observe if it searches `OBJ_INFO/max/coll.json` first.
