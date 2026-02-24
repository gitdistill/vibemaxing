# CycleScraper Design Document

## 1. Overview
**CycleScraper** is a specialized, run-once web scraper designed to transform the [Cycling '74 documentation](https://docs.cycling74.com) into an agent-friendly knowledge base. The output will serve as the foundational dataset for the `vibemax-intelligence` Pi extension, enabling agents to query Max/MSP technical concepts, API details, and tutorials without live network access.

## 2. Scope & Targets
The scraper targets specific sections of `docs.cycling74.com` while explicitly excluding others handled by separate tools.

### In Scope
1.  **User Guide** (`/userguide/`):
    *   Conceptual guides and overviews grouped by topic (Audio, MIDI, Gen, etc.).
    *   Target: `https://docs.cycling74.com/userguide/*`
2.  **API Reference** (`/apiref/`):
    *   **Live Object Model (LOM)**: Hierarchy of Live objects.
    *   **Max JS API**: JavaScript classes and functions.
    *   **Node for Max**: Node.js API integration.
    *   Target: `https://docs.cycling74.com/apiref/*`
3.  **Learn** (`/learn/`):
    *   Tutorial series (Max, MSP, Jitter, etc.).
    *   Target: `https://docs.cycling74.com/learn/*`

### Out of Scope
*   **Object Reference** (`/reference/`): The 1800+ individual object pages (e.g., `cycle~`, `jit.world`) are handled by the `maxpylang` internal database tool and the context7 pi extension.

## 3. Data Model

### 3.1. Knowledge Map (`knowledge-map.json`)
A hierarchical JSON tree representing the **logical structure** of the documentation. This is the primary index for the agent.

*   **Common Fields**: `title`, `type` (category, guide, api-index, api-page, series, article), `slug`, `filePath` (relative to content root), `sourceUrl`, `description`.
*   **Specialized Fields**:
    *   `group`: Navigational group (User Guide).
    *   `category`: Structural category (User Guide - e.g., `gen`).
    *   `section`: API section (`lom`, `js`, `nodeformax`).
    *   `apiGroup`: Grouping within API index (e.g., "Classes", "Functions").
    *   `series`: Series name (Learn).
    *   `canonicalPaths`: Array of LOM paths (LOM Objects).

**Example Structure:**
```json
{
  "title": "Cycling '74 Documentation",
  "children": [
    {
      "title": "User Guide",
      "type": "category",
      "children": [
        {
          "title": "Audio",
          "type": "category",
          "children": [
             { 
               "title": "MSP Basics",
               "type": "guide",
               "group": "Audio",
               "filePath": "userguide/audio/msp-basics.md",
               "sourceUrl": "https://docs.cycling74.com/userguide/msp_basics"
             }
          ]
        }
      ]
    },
    {
      "title": "API Reference",
      "type": "category",
      "children": [
        {
          "title": "Live Object Model",
          "type": "api-index",
          "section": "lom",
          "children": [
             { 
               "title": "Song", 
               "type": "api-page",
               "apiGroup": "API Objects", 
               "canonicalPaths": ["live_set"],
               "filePath": "apiref/lom/song.md" 
             }
          ]
        }
      ]
    },
    {
      "title": "Learn",
      "type": "category",
      "children": [
        {
          "title": "Max Data Tutorials",
          "type": "series",
          "children": [
            {
              "title": "01: Hello Data",
              "type": "article",
              "series": "Max Data Tutorials",
              "filePath": "learn/max-data-tutorials/01-hello-data.md"
            }
          ]
        }
      ]
    }
  ]
}
```

### 3.2. Content Store (`data/content/`)
A directory structure containing clean, readable **Markdown** files.
*   **Format**: Standard Markdown (`.md`).
*   **Code**: Fenced code blocks with language identifiers.
*   **Math**: Raw TeX preserved in KaTeX blocks where possible.
*   **Images**: Kept as absolute URLs to `docs.cycling74.com` (for now).

**Organization**:
*   `data/content/userguide/[group]/[slug].md`
*   `data/content/apiref/[section]/[slug].md`
*   `data/content/learn/[series]/[slug].md`

## 4. Architecture & Workflow

### 4.1. Input: Seed Configuration (`config/seeds.json`)
The "Source of Truth" driving the scraper strategies.

*   **Strategies**:
    1.  **LearnSeriesCrawl**: 
        *   Input: Landing page URL (e.g., `/learn/`).
        *   Action: Extract series titles and links from the main table/grid. Crawl each series index to find articles.
    2.  **UserGuideGrouped**: 
        *   Input: JSON structure defining Groups (Audio, MIDI) and their lists of URLs.
        *   Action: Process each URL, assigning it to the defined Group folder and metadata.
    3.  **ApiIndexCrawl**: 
        *   Input: Index URLs (`/apiref/lom/`, `/apiref/js/`, `/apiref/nodeformax/`).
        *   Action: Parse the grouped tables (Classes, Functions) to find child pages. Extract "Description" from the table for metadata.

### 4.2. Processing Pipeline (`src/processor.ts`)
The core logic for transforming raw HTML.

1.  **Router**: Dispatches URL to the correct Page Processor based on pattern.
2.  **Page Processors**:
    *   `UserGuideProcessor`: Handles grouping, KaTeX, and relative linking.
        *   See: [User Guide Page Spec](user-guide-page-spec.md)
    *   `ApiRefProcessor`: Handles LOM hierarchy (canonical paths, properties) and JS definitions (signatures, parameter tables).
        *   See: [API Index Spec](api-ref-index-spec.md)
        *   See: [API Page Spec](api-ref-page-spec.md)
    *   `LearnProcessor`: Handles Series navigation and relationships.
        *   See: [Learn Landing Page Spec](learn-landing-page-spec.md)
        *   See: [Series Landing Page Spec](learn-series-landing-page-spec.md)
        *   See: [Learn Article Spec](learn-article-page-spec.md)

    **Key Selectors Reference:**
    *   **User Guide**: `article[class*="article_content"]` (Main), `annotation[encoding="application/x-tex"]` (Math).
    *   **API (LOM)**: `h2:contains("Canonical Paths") + pre` (Paths), `h3` + `span.c74-api-type` (Members).
    *   **API (JS)**: `pre:first-of-type` (Signature), `h2:contains("Classes") + table` (Index), `h3` + `pre` + `table` (Methods).
    *   **Learn**: `div.series_grid` (Series Index), `div.article_metaWrapper` (Metadata), `h2#see-also` (Relationships).

3.  **Common Transforms**:
    *   **Clean**: Remove sidebars, headers, footers using `cheerio`.
    *   **Markdown**: Convert HTML to MD using `turndown`.
    *   **Link Rewriting**: Convert internal links to relative file paths.
    *   **Metadata**: Extract SEO description and OpenGraph tags.

### 4.3. Tech Stack
*   **Runtime**: Node.js / TypeScript.
*   **Libraries**:
    *   `cheerio`: HTML parsing.
    *   `turndown`: HTML to Markdown.
    *   `axios`: HTTP client with rate limiting.
    *   `p-limit`: Concurrency control.

## 5. Execution Strategy
1.  **Initialize**: `npm install` dependencies.
2.  **Configure**: Populate `config/seeds.json` with the User Guide groups and API/Learn entry points.
3.  **Run**: `npm start`.
4.  **Verify**: Inspect `knowledge-map.json` and generated Markdown.
5.  **Deploy**: Move `data/content` and `knowledge-map.json` to the `vibemax-intelligence` extension.

## 6. Next Steps - Implementation Phase
1.  **Repository Setup**: 
    *   Initialize `cyclescraper` in a dedicated directory.
    *   Install dependencies (`axios`, `cheerio`, `turndown`, `p-limit`).
2.  **Configuration**:
    *   Create `config/seeds.json` with the "User Guide" group hierarchy.
3.  **Core Processors**:
    *   Scaffold `src/processors/BaseProcessor.ts`.
    *   Implement `UserGuideProcessor`, `ApiRefProcessor`, `LearnProcessor` using the specific Selectors defined in 4.2.
4.  **Integration**:
    *   Write `src/main.ts` to orchestrate the pipeline.
    *   Run test scrapes on sample pages (using cached files or live requests with politeness).
5.  **Output**:
    *   Generate `knowledge-map.json` and Markdown files.
    *   Package for `vibemax-intelligence`.
