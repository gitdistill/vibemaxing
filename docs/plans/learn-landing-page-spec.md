# Learn Landing Page Specification

**Target URL:** `https://docs.cycling74.com/learn/`

## 1. Goals
1.  **Extract Series Metadata:** Get the title, description, and link for the 6 core tutorial series.
2.  **Extract Article Metadata:** Get the title, description, link, and tags for all available articles.
3.  **Generate Dual Output:**
    *   `data/content/learn/index.md` (Human-readable overview).
    *   `data/content/learn/metadata.json` (Structured data for search/filtering).

## 2. DOM Selectors & Strategy

### 2.1. Core Series (The Grid)
*   **Container:** `div[class*="featuredGrid_grid"]`
*   **Item:** `div[class*="featuredGrid_gridItem"]`
    *   **Link:** `a` (Extract `href`)
    *   **Title:** `div[class*="featuredGrid_gridItemTitle"]` (Text content)
    *   **Description:** `p[class*="featuredGrid_gridItemDescription"]` (Text content)

### 2.2. Articles (The Table)
*   **Target URL (Force Tags):** `https://docs.cycling74.com/learn/?categories=analysis&categories=audio&categories=communication&categories=javascript&categories=max&categories=midi&categories=synthesis&categories=user+interface`
*   **Pagination:** Iterate `page=1` to `page=25` (or until empty).
*   **Container:** `div[class*="articlesTable_table"]` (Implied from class names)
*   **Row/Item:** `tr` or `div[class*="articlesTable_row"]`
    *   **Title:** `[class*="articlesTable_title"]`
    *   **Intro:** `[class*="articlesTable_intro"]`
    *   **Tags:** `[class*="articlesTable_categories"]` (Only visible when filter applied)

## 3. Execution Logic
1.  **Series Extraction:**
    *   Fetch base URL.
    *   Parse `Series Container`.
    *   Extract top 6 items.
2.  **Article Extraction (Pagination Loop):**
    *   **Loop:** `page=1` to `page=25`.
    *   **Stop Condition:** No articles found in table OR page limit reached.
    *   **Processing:**
        *   For each row, extract Title, Intro, Tags.
        *   Convert relative links to absolute/local paths.
    *   **Rate Limiting:** 500ms delay between requests.

## 4. Output Data Models

### `learn/index.md`
```markdown
# Learn Max

## Core Series
- **[Max Tutorials](./max-tutorials/index.md)**: Core Max tutorial series...
- **[MSP Tutorials](./msp-tutorials/index.md)**: Signal processing tutorial series...
...

## All Articles
(List of all articles with links)
```

### `learn/metadata.json`
```json
{
  "series": [
    { "title": "Max Tutorials", "description": "...", "path": "learn/series/max-tutorials/" }
  ],
  "articles": [
    {
      "title": "Hello World",
      "intro": "First steps in Max",
      "tags": ["max", "basics"],
      "url": "https://docs.cycling74.com/learn/articles/..."
    }
  ]
}
```
