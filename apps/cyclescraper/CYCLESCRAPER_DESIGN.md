# CycleScraper Design Document

**Status:** Draft
**Scope:** `apps/cyclescraper`
**Role:** Web ETL (Extract, Transform, Load) for Cycling '74 "Learn" Materials.

## 1. Overview
`cyclescraper` is a targeted web scraper designed to ingest tutorials, articles, and guides from the `docs.cycling74.com/learn/` section. It bypasses the need for complex crawling by leveraging the site's `sitemap.xml` and uses static HTML parsing (no headless browser) for speed and reliability.

**Output:** Clean Markdown files with YAML frontmatter, optimized for RAG (Retrieval-Augmented Generation) ingestion.

## 2. Architecture

### Tech Stack
*   **Language:** Python 3.x
*   **HTTP Client:** `requests` (Standard synchronous fetching)
*   **HTML Parsing:** `beautifulsoup4` (DOM traversal)
*   **Markdown Conversion:** `markdownify` (HTML to Markdown)
*   **CLI:** `argparse` (Standard library)

### Modules
1.  **`main.py`**: Entry point. Handles CLI arguments, orchestration, and logging.
2.  **`sitemap.py`**: Fetches and parses the XML sitemap to generate a target URL list.
3.  **`fetcher.py`**: Handles HTTP requests with retries, headers, and rate limiting.
4.  **`parser.py`**: The core logic. Takes HTML, extracts specific DOM elements, cleans noise, and produces a dictionary of data.
5.  **`asset_manager.py`**: Handles downloading images, hashing filenames (deduplication), and returning local paths.
6.  **`writer.py`**: Converts the dictionary to a Markdown string (with YAML frontmatter) and writes to disk.

## 3. Data Flow

1.  **Discovery:**
    *   Fetch `https://docs.cycling74.com/sitemap.xml`.
    *   Parse XML to find `<loc>` entries.
    *   **Filter:** Keep only URLs containing `/learn/articles/` (Series pages are excluded as they are typically index lists).

2.  **Ingestion (Loop):**
    *   Fetch URL.
    *   Check HTTP Status (200 OK).
    *   **Validation:** Check for "Soft 404" (e.g., page title "Page Not Found").

3.  **Extraction (DOM Mapping):**
    *   **Container:** `article.c74-article-content` (Primary content).
    *   **Title:** `h1` (First H1 inside the container or main wrapper).
    *   **Metadata:** Locate `.article_metaWrapper__...` for:
        *   `Kind` (e.g., Tutorial)
        *   `Author`
        *   `Contributors`
        *   **Series:** Check for "In this series" sidebar/breadcrumb and extract the Series Title if present.
    *   **Tags:** (If available in meta headers or footer categories).
    *   **Code Blocks:** Detect language from `class` (e.g., `language-js`, `language-c`) for syntax highlighting.

4.  **Transformation:**
    *   Convert HTML to Markdown.
    *   **Asset Handling (Mirroring):**
        *   Identify all `<img>` tags in the content.
        *   **Resolution:** Convert relative URLs to absolute URLs using the page's base URL.
        *   **Deduplication:** Generate a unique filename using the MD5 hash of the *absolute source URL* (e.g., `md5(url).webp`).
        *   **Check:** If file exists in `assets/`, skip download.
        *   **Rewrite:** Update Markdown image source to the local relative path (`./assets/<hash>.ext`).
    *   **Special Handling:**
        *   **Markdown Cleaning:** Configure `markdownify` to strip `class`, `id`, `style` attributes.
        *   **Explicit Removal:** Remove `<nav>`, `<header>`, `<footer>`, `<script>`, `<style>`, `<noscript>` tags *before* conversion.
        *   `<code>` / `<pre>`: **Preserve** `class` attributes here for language detection.
        *   Remove UI noise ("Download Content", "Open in Max" buttons).

5.  **Output:**
    *   File Name: `YYYY-MM-DD-slug.md` (or just `slug.md`).
    *   Location: `data/ingest/cyclescraper/` (configurable).

## 4. Output Schema (Markdown)

```markdown
---
title: "Getting Started with Jitter Geometry"
url: "https://docs.cycling74.com/learn/articles/geom-01/"
author: "Cycling '74"
kind: "Tutorial"
scraped_at: "2023-10-27T10:00:00Z"
tags: ["jitter", "geometry", "gl"]
---

# Getting Started with Jitter Geometry

The `jit.geom` family of objects...

## Making a Shape

[Content...]
```

## 5. Implementation Plan

### Phase 1: Skeleton & Discovery
*   Set up Python project structure.
*   Implement `sitemap.py` to prove we can list all target URLs.

### Phase 2: Extraction Prototype
*   Implement `fetcher.py` and `parser.py`.
*   Run against the local sample files (from `apps/cyclescraper/samples/`) to validate DOM selectors without network calls.

### Phase 3: Transformation & Output
*   Implement `writer.py`.
*   Tune `markdownify` settings to ensure Max/MSP code blocks look correct.

### Phase 4: CLI & Polish
*   Add CLI args:
    *   `--output-dir`: Custom path for markdown/assets (default: `data/ingest/cyclescraper`).
    *   `--dry-run`: Don't write files, just log.
    *   `--limit n`: Process only N items (dev mode).
    *   `--target-url`: Process specific URL (debugging).
*   Add logging.

## 6. Constraints & Safety
*   **Rate Limiting:** Enforce a polite delay (e.g., 1s) between requests.
*   **User Agent:** Identify as `VibeMaxingBot/1.0`.
*   **Validation:** If `article.c74-article-content` is missing, log error and skip (don't crash).
