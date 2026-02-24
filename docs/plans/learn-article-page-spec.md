# Learn Article Page Specification

## 1. Overview
The **Article Page** is the terminal node of the Learn section. It contains the actual tutorial content, images, code examples, and relationships to other articles or objects.

## 2. Scraping Strategy

### 2.1. Identification
- **URL Pattern**: `https://docs.cycling74.com/learn/articles/[slug]`
- **Main Container**: `<article class="article_content__OHg47 c74-article-content">` (Note: Use class substring match `[class*="article_content"]`).

### 2.2. Content Extraction
0. **SEO Metadata (Head)**:
   - **Description**: Extract from `<meta name="description">` or `<meta property="og:description">`.
   - **OG Title**: Extract from `<meta property="og:title">` (often cleaner than `<title>`).
1. **Title**: Extract from the `<h1>` inside the article container.
2. **Main Body**:
   - Extract the HTML within the article container.
   - **Exclude**:
     - The initial `<h1>` (saved as title).
     - Anchor links next to headings (`.blocks_anchorLink__kJCjR`).
     - The metadata footer (`.article_metaWrapper__ARyDO`).
   - **Images**: Keep `src` as absolute URLs to `https://docs.cycling74.com`.
   - **Links**: 
     - Rewrite `/learn/articles/[slug]` to `./[slug].md`.
     - Rewrite `/learn/series/[slug]` to `../series/[slug]/index.md`.
     - Keep `/reference/*` as absolute URLs.

### 2.3. Relationship Extraction ("See Also")
- **Target**: Find any `<h2>` with ID `see-also` or `explore-further`.
- **Logic**:
  - Capture all `<a>` tags within the sibling list (`<ul>`) or paragraph immediately following the heading.
  - Store as an array of objects: `{ text: string, url: string, type: "article" | "series" | "reference" | "external" }`.

### 2.4. Metadata Extraction
- **Location**: `.article_metaWrapper__ARyDO`.
- **Logic**: Iterate over `<dl>` elements.
  - `dt` -> Key (lowercase, e.g., "kind", "author").
  - `dd` -> Value.

## 3. Data Output

### 3.1. File System
- **Path**: `learn/articles/[slug].md`
- **Format**: Clean Markdown with code fences.

### 3.2. Knowledge Map (`knowledge-map.json`)
```json
{
  "title": "Article Title",
  "type": "article",
  "slug": "article-slug",
  "filePath": "learn/articles/article-slug.md",
  "sourceUrl": "https://docs.cycling74.com/learn/articles/article-slug",
  "metadata": {
    "kind": "Tutorial",
    "author": "Cycling '74"
  },
  "seeAlso": [
    { "text": "Related Topic", "url": "...", "type": "article" }
  ]
}
```
