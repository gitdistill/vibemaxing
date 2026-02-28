# Learn Landing Page Specification

**Target URL:** `https://docs.cycling74.com/learn/`

## 1. Goals
1.  **Extract Series Metadata:** Get the title, description, and link for the core tutorial series for inclusion in the `knowledge-map.json`.
2.  **Generate Output:** `data/content/learn/index.md` (Human-readable overview).

## 2. DOM Selectors & Strategy

### 2.1. Core Series (The Grid)
*   **Container:** `div[class*="featuredGrid_grid"]`
*   **Item:** `div[class*="featuredGrid_gridItem"]`
    *   **Link:** `a` (Extract `href`)
    *   **Title:** `div[class*="featuredGrid_gridItemTitle"]` (Text content)
    *   **Description:** `p[class*="featuredGrid_gridItemDescription"]` (Text content)

## 3. Execution Logic
1.  **Series Extraction:**
    *   Fetch base URL.
    *   Parse `Series Container`.
    *   Extract items to build the `series` nodes in `knowledge-map.json`.
2.  **Article Orchestration:**
    *   The scraper should iterate through article URLs defined in `docs/seeds.json` -> `urlset.sections["Learn"]["articles"]` rather than discovering them via pagination.

## 4. Output Data Models

### `learn/index.md`
```markdown
# Learn Max

## Core Series
- **[Max Tutorials](https://docs.cycling74.com/learn/series/max-tutorials/)**: Core Max tutorial series...
...
```
