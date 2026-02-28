# CycleScraper 🚲

CycleScraper is a specialized documentation extraction tool designed to crawl and process Cycling '74's documentation (User Guide, API Reference, and Learn articles) into clean, LLM-ready Markdown with structured metadata.

## Overview

The scraper is built on top of [Crawl4AI](https://crawl4ai.com/) and is specifically tuned for the Cycling '74 website's Next.js SPA (Single Page Application) architecture. It uses a **sequential crawling strategy** to prevent content leakage and state corruption that often occurs with concurrent requests in SPA environments.

## Key Features

- **Sequential Execution**: Guarantees data integrity by processing one page at a time.
- **Smart Metadata Extraction**: Automatically pulls frontmatter descriptions and titles.
- **Seed-Based Discovery**: Uses `docs/seeds.json` as the source of truth for hierarchy and group-level metadata.
- **Structured Output**: Organized into `data/content/` subdirectories (`userguide`, `apiref`, `learn`).
- **Knowledge Map Generation**: `build_map.py` compiles all scraped content into a single `knowledge-map.json` for RAG or agentic use.

## Architecture

- **`main.py`**: Entry point and CLI orchestrator.
- **`processors/`**: Domain-specific logic for different doc sections (e.g., handling the specific HTML structure of Learn articles vs. API docs).
- **`utils/crawler.py`**: Centralized browser configuration and the sequential `arun` wrapper.
- **`models.py`**: Pydantic models for structured data.
- **`discovery.py`**: Utilities for initial URL discovery and seed generation.

## Usage

### Prerequisites
Ensure the virtual environment is set up and requirements are installed:
```bash
python -m venv venv
source venv/bin/activate
pip install -r apps/cyclescraper/requirements.txt
```

### Scraping Content
Scrape a specific section (e.g., API Reference):
```bash
python apps/cyclescraper/main.py --section apiref
```

Scrape a specific sub-section (e.g., Javascript API):
```bash
python apps/cyclescraper/main.py --section apiref --sub-section js
```

### Building the Knowledge Map
Once scraping is complete, generate the unified JSON map:
```bash
python apps/cyclescraper/build_map.py
```

## Data Schema
Each Markdown file includes YAML frontmatter:
```yaml
title: "Title"
description: "A brief summary of the content."
sourceUrl: "https://support.cycling74.com/..."
```
