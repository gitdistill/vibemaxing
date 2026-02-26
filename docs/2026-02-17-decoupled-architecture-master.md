# MASTER PLAN: Decoupled Intelligence & Co-Architect Platform

**Date:** 2026-02-17
**Status:** Canonical (Supersedes all previous Feb 17 documents)
**Primary Goal:** Transition the Vibemaxing monorepo to a "Co-Architect" model by decoupling documentation research and database augmentation from the patch builder.

---

## 1. Target Architecture

### A. The "Researcher" (Pi Extension)
*   **Technical Spec:** `docs/plans/2026-02-17-vibemax-intelligence-spec.md`
*   **Location:** `.pi/extensions/vibemax-intelligence/`
*   **Tech:** **Pi Extension (TypeScript/JavaScript)**.
*   **Role:** Agent-facing data interface for Cycling '74 documentation (Objects, Guides, JS, LOM). Returns **Raw JSON** for agent reasoning.
*   **Key Capabilities:** Documentation lookup (Cache-First) and `maxpylang` database augmentation.

### B. The "Builder" (MaxPatcher)
*   **Technical Spec:** `docs/plans/2026-02-17-maxpatcher-spec.md`
*   **Location:** `apps/maxpatcher/`
*   **Role:** Deterministic Python builder for `.maxpat` generation.
*   **Constraint:** **Zero Network Connectivity.** Must rely exclusively on the local `maxpylang` object database.

---

## 2. Execution Sequence (MANDATORY)

### Phase 1: Intelligence Extension (Migration)
1.  **Scaffold:** Create `.pi/extensions/vibemax-intelligence/` and load the extending pi skill.
2.  **Migrate Logic:** Extract the Context7 API client logic from the existing `apps/maxpatcher/maxpatcher/intelligence.py`.
3.  **Implement Tools:** Build `research_topic`, `research_object`, and `augment_max_db` as defined in the Technical Spec.
4.  **Verification:** Confirm the extension successfully writes a valid object JSON to the `maxpylang` data directory.

### Phase 2: MaxPatcher Refactor (Decoupling)
1.  **Cleanup:** Delete `apps/maxpatcher/maxpatcher/intelligence.py` and remove Context7-related dependencies from `pyproject.toml`.
2.  **CLI Update:** Remove the `sync` command from `maxpatcher/cli.py`.
3.  **Validation Logic:** Refactor `vibe.py` to stop builds and emit `[MISSING_OBJECT: {name}]` when an unknown object is encountered.

---

## 3. Core Guardrails
*   **No MCP Servers:** Use the native Pi Extension API only.
*   **Strict Local Database:** MaxPatcher must never perform documentation lookups; it only consumes what is in the local `OBJ_INFO` directories.
