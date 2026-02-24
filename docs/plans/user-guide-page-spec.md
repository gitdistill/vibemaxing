# User Guide Page Specification

## 1. Overview
User Guide pages provide conceptual documentation for Max. While structurally similar to Learn Articles, they are organized into logical groups (Audio, MIDI, etc.) defined in the scraper's seed configuration rather than the URL structure.

## 2. Scraping Strategy

### 2.1. Identification
- **URL Pattern**: `https://docs.cycling74.com/userguide/*`
- **Category Detection**: 
  - If the URL matches `https://docs.cycling74.com/userguide/[category]/[slug]`, extract `[category]` (one of: `mc`, `gen`, `jitter`, `lua`, `m4l`).
  - Otherwise, `category` is `null`.
- **Group Detection**:
  - The `group` name is provided by the scraper's `seeds.json` configuration for the current URL.

### 2.2. Content Extraction
1. **SEO Metadata (Head)**:
   - **Description**: Extract from `<meta name="description">`.
   - **OG Title**: Extract from `<meta property="og:title">`.
2. **Title**: Extract from the `<h1>` inside the article container.
3. **Main Body**:
   - Extract HTML within the article container.
   - **Exclude**:
     - The initial `<h1>`.
     - Heading anchor links (`.blocks_anchorLink__kJCjR`).
   - **Math (KaTeX)**: If possible, extract the raw TeX from `<annotation encoding="application/x-tex">` to ensure math remains readable for agents.
   - **Images/Figures**: Preserve `<figure>` and `<figcaption>` blocks. Keep `src` as absolute URLs.

### 2.3. Link Rewriting
- **Rule**: All internal links must be relative to the file's location in the local content store.
- **User Guide Links**: Rewrite to point to the local `.md` file in its respective group folder.
- **Reference Links**: Keep as absolute URLs to `docs.cycling74.com/reference/*`.

## 3. Data Output

### 3.1. File System
- **Path**: `userguide/[group-name]/[slug].md`
  - *Note: `group-name` is derived from the `seeds.json` mapping.*

### 3.2. Knowledge Map (`knowledge-map.json`)
```json
{
  "title": "Page Title",
  "type": "guide",
  "group": "Logical Group Name (e.g., Audio)",
  "category": "URL Category (e.g., gen or null)",
  "slug": "page-slug",
  "filePath": "userguide/audio/page-slug.md",
  "sourceUrl": "https://docs.cycling74.com/userguide/gen/page-slug",
  "description": "SEO description text"
}
```
