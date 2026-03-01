The role of this file is to describe common mistakes and
confusion points that agents might encounter as they work in
this project. If you ever encounter something in the project
that surprises you, please alert the developer working with you
and indicate that this is the case in the agents.md file to help
prevent future agents from having the same issue.

---

## 4. Strict Enforcement Rules (MANDATORY)

### Tool Usage & Token Economy
*   **NO RECURSIVE LS:** Use `tree -L 2` or `ls -F`.
*   **NO RECURSIVE GREP:** Always use `rg`.

### Cognitive Safety
*   **USER CONFIRMATION:** Operations > 10 files require permission.

### Version Control Hygiene (CRITICAL TOKEN SAFETY)
* **SILENCE IS GOLDEN:** For any `git add` or `git commit` involving >5 files, YOU MUST use the quiet flag (`-q` or `--quiet`)
* **VERIFY COMPACTLY:** Do not rely on `git commit` output to verify success.
    * After a quiet commit, verify with: `git log -1 --oneline` or `git status --short`.

## Do not blindly create files at the root directory of the project. Identify the appropriate folder given the current context.

_notes_
- Python 3 is installed via homebrew and is also managed by virtual environments: `./venv/`

- While scanning code, if anything looks off (bad/dead code, poor naming, refactor opportunity, or VISION misalignment), immediately log a stand-alone entry in `./BACKLOG.md` so it can be picked up, prioritized, and acted on later.