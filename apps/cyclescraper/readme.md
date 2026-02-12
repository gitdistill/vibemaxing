## 1. Project: `cyclescraper`

**Role:** Data Ingestion (ETL)
**Agent Grade:** **Grade 1 (Script)** – Deterministic execution.

### Description

A robust web scraper targeted specifically at the Cycling '74 documentation ecosystem. It handles the nuances between Max, MSP, Jitter, and Max for Live web documentation structures.

### Tech Stack

* **Interface:** Bash (`./scripts/scrape_docs.sh`)
* **Core Logic:** Python (`Playwright`, `BeautifulSoup4`)
* **Target:** `docs.cycling74.com` (Reference, Tutorials, Vignettes)
* **Output:** Markdown files with YAML frontmatter (Clean text for RAG).

### Key Components

1. **The Crawler:** Recursive crawler with depth control (CLI argument driven).
2. **Section Classifier:** Distinguishes between API refs, Tutorials, and Concepts.
3. **Jitter/M4L Normalizer:** Specific parsers for the differing DOM structures of Jitter vs MSP.
4. **Change Detector:** Hash-comparison to only scrape updated pages.

### 🚀 Agent Kickoff Prompt

> "I am starting `cyclescraper`. Help me build a Python script wrapped in a Bash executable. It needs to scrape `docs.cycling74.com` and output clean Markdown. The Agent must be able to run it via `./scripts/scrape_docs.sh --target [section]`."

---