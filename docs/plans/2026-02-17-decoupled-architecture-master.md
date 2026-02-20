# MASTER PLAN: Decoupled Intelligence & Co-Architect Platform

**Date:** 2026-02-17
**Status:** Canonical (Supersedes all previous Feb 17 documents)
**Primary Goal:** Move Context7 logic out of `maxpatcher` into a dedicated Pi Extension to enable a "Research First, Build Second" workflow.

---

## 1. Target Architecture

### A. The "Researcher" (Pi Extension)
*   **Technical Spec:** `docs/plans/2026-02-17-vibemax-intelligence-spec.md`
*   **Location:** `.pi/extensions/vibemax-intelligence/`
*   **Tech:** **Pi Extension (TypeScript/JavaScript)**. 
    *   *Note: Do NOT build an MCP server. This must be a native Pi extension using the Pi SDK.*
*   **Role:** Agent-facing data pipe. Returns **Raw JSON** for the agent to reason about.
*   **Key Tools:**
    *   `research_max(query, section)`: Fetches raw JSON from Context7 (Objects, Guides, JS, LOM).
    *   `augment_max_db(object_name, category)`: Fetches object metadata and writes it to `apps/maxpatcher/engine/maxpylang/data/OBJ_INFO/`.
*   **Caching:** Mandatory "Cache-First" logic. Check `.pi/cache/vibemax-intelligence/` before hitting API.

### B. The "Builder" (MaxPatcher)
*   **Technical Spec:** `docs/plans/2026-02-17-maxpatcher-spec.md`
*   **Location:** `apps/maxpatcher/`
*   **Role:** Deterministic Python builder.
*   **Constraint:** **Zero Network Calls.** No Context7, no `intelligence.py`.
*   **Data:** Strictly consumes local `maxpylang/data/OBJ_INFO`.
*   **Behavior:** Missing objects trigger a warning: `[MISSING_OBJECT: {name}]`. Agent should then call `augment_max_db` via the extension.

---

## 2. Sequence of Operations (MANDATORY ORDER)

### Phase 1: The Intelligence Extension (Migration)
*Do NOT delete MaxPatcher logic yet.*
1.  **Scaffold:** Create `.pi/extensions/vibemax-intelligence/`.
2.  **Extract:** Copy the Context7 API logic from `apps/maxpatcher/maxpatcher/intelligence.py` into the extension's TS source.
3.  **Implement:** Build the tools (`research_max`, `augment_max_db`) with the Cache-First logic.
4.  **Verify:** Ensure the extension can query docs and successfully write a JSON file to the `maxpylang` data directory.

### Phase 2: MaxPatcher Refactor (Cleanup)
*Only start after Phase 1 is verified.*
1.  **Delete:** Remove `apps/maxpatcher/maxpatcher/intelligence.py`.
2.  **Prune CLI:** Remove the `sync` command from `cli.py`.
3.  **Update Vibe:** Refactor `vibe.py` to use the local DB only and emit the `[MISSING_OBJECT]` warning.
4.  **Cleanup:** Remove any Context7 dependencies from `pyproject.toml`.

### Phase 3: Platform Integration
1.  **Skill:** Populate the `SKILL.md` (content provided by user) in the extension.
2.  **Handoff:** Update `AGENTS.md` to point to the new tools.

---

## 3. Technology Guardrails (FOR AGENTS)
*   **NO MCP SERVERS:** This platform uses Pi Extensions.
*   **JSON ONLY:** Research tools return Raw JSON for agent reasoning.
*   **LOCAL ENGINE:** `maxpylang` is the local source of truth for objects.
