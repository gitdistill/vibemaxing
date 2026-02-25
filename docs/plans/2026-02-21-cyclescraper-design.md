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
    *   **Live Object Model (LOM)**: Index of LOM objects and detailed pages (Canonical Paths, Children, Properties, Functions).
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

*   **Nodes**:
    *   `root`: The top-level container.
    *   `section`: Major divisions (`User Guide`, `API Reference`, `Learn`).
    *   `group`: Navigational groupings (e.g., "Audio" in User Guide, "Classes" in API).
    *   `series`: Specific tutorial series (e.g., "Max Data Tutorials").
    *   `page`: The actual content nodes (Articles, API Pages, Guides).

*   **Fields**:
    *   `title`: Display title.
    *   `type`: `section` | `group` | `series` | `page`.
    *   `kind`: Specific content subtype (e.g., `api-index`, `lom-object`, `js-class`).
    *   `slug`: URL-friendly identifier.
    *   `filePath`: Relative path to the `.md` file (only for `page` type).
    *   `sourceUrl`: Original web URL.
    *   `description`: **Required**. Short summary for agent context. The source of this description depends on the domain:
        *   **User Guide Groups**: Provided statically in `docs/seeds.json`.
        *   **API Reference (LOM, JS, Node)**: Extracted from the descriptive text in the Index Tables on the root API pages.
        *   **Learn Series**: Extracted from the text beneath each series card on the `/learn/` landing page.
        *   **Pages/Articles**: Extracted from the page's `<meta name="description">`.
    *   `children`: Array of child nodes.

**Example Structure:**
```json
{
  "title": "Cycling '74 Documentation",
  "type": "root",
  "children": [
    {
      "title": "User Guide",
      "type": "section",
      "children": [
        {
          "title": "Audio",
          "type": "group",
          "children": [
             { 
               "title": "MSP Basics",
               "type": "page",
               "kind": "guide",
               "filePath": "userguide/audio/msp-basics.md",
               "sourceUrl": "https://docs.cycling74.com/userguide/msp_basics",
               "description": "Introduction to digital audio concepts in MSP."
             }
          ]
        }
      ]
    },
    {
      "title": "API Reference",
      "type": "section",
      "children": [
        {
          "title": "Live Object Model",
          "type": "group",
          "kind": "api-index",
          "sourceUrl": "https://docs.cycling74.com/apiref/lom/",
          "description": "Index of Live Object Model classes.",
          "children": [
             { 
               "title": "Song", 
               "type": "page",
               "kind": "lom-object",
               "description": "Represents a Live Set.",
               "filePath": "apiref/lom/song.md" 
             }
          ]
        }
      ]
    },
    {
      "title": "Learn",
      "type": "section",
      "children": [
        {
          "title": "Max Data Tutorials",
          "type": "series",
          "sourceUrl": "https://docs.cycling74.com/learn/max-data-tutorials/",
          "description": "Tutorials for working with data dictionaries in Max.",
          "children": [
            {
              "title": "01: Hello Data",
              "type": "page",
              "kind": "article",
              "filePath": "learn/max-data-tutorials/01-hello-data.md",
              "description": "Getting started with the dict object."
            }
          ]
        }
      ]
    }
  ]
}
```

<comment feedback="concerned about learn page desc vs meta tag"></comment>

### 3.2. Content Store (`data/content/`)
A directory structure containing clean, readable **Markdown** files.
*   **Format**: Standard Markdown (`.md`).
*   **Frontmatter**: Every file MUST start with YAML frontmatter containing:
    *   `title`: Page title.
    *   `description`: Short summary (Always extracted from the page's `<meta name="description">` tag, regardless of section).
    *   `sourceUrl`: Original URL.
    *   `tags`: Keywords (if available).
*   **Code**: Fenced code blocks with language identifiers.
*   **Math**: Raw TeX preserved in KaTeX blocks where possible.
*   **Images**: Relative image paths in HTML (e.g., `/images/foo_hash.webp`) are converted to **absolute URLs** by prepending the domain (e.g., `https://docs.cycling74.com/images/foo_hash.webp`). The hash/build-id in the filename is preserved to ensure the link points to the correct version of the asset.

**Organization**:
*   `data/content/userguide/[group]/[slug].md`
*   `data/content/apiref/[section]/[slug].md`
*   `data/content/learn/[series]/[slug].md`

## 4. Scraping Strategies & Specifications

This section defines the high-level approach for each content domain. The detailed logic for traversing indices, selecting content, and extracting metadata is strictly defined in the referenced **Specification Files**. The Scraper Implementation must adhere to these specs.

### 4.0 The Seed Configuration (`docs/seeds.json`)
The entire scraping process is driven by `docs/seeds.json`, which acts as the unified source of truth for the documentation structure and entry points. It contains a `urlset.sections` object that defines the three major domains:
1.  **User Guide**: Contains a fully defined map of thematic Groups (e.g., "Audio", "Gen") along with their predefined agentic descriptions and the static list of all page URLs belonging to each group.
2.  **API Reference**: Contains predefined descriptions and the root index URLs for the LOM, JS API, and Node for Max API. It also includes an array of individual page URLs for verification or direct scraping.
3.  **Learn**: Contains the landing page URL (`/learn/`), as well as arrays of all known series and article URLs.

The scraper uses this file to orchestrate its workflow, minimizing the need to "discover" links via deep crawling when the explicit list is already provided.

### 4.1. User Guide Strategy
*   **Goal**: Transform a provided list of URLs into a structured hierarchy of concept guides.
*   **Input**: `docs/seeds.json` -> `urlset.sections["User Guide"]`.
*   **Process**:
    1.  **Iterate**: Loop through the configured Groups and URLs.
    2.  **Scrape**: Visit each URL.
    3.  **Extract**: Parse the content, titles, and metadata.
    4.  **Map**: Create `guide` nodes in `knowledge-map.json` under the appropriate Group, utilizing the predefined Group description and the page's `<meta name="description">`.
*   **Specification**:
    *   **[User Guide Page Spec](user-guide-page-spec.md)**: Defines selector logic for content extraction and metadata scraping.

### 4.2. API Reference Strategy
*   **Goal**: Build a complete index and content store for LOM, JS, and Node for Max APIs.
*   **Input**: `docs/seeds.json` -> `urlset.sections["API Reference"]`.
*   **Process**:
    1.  **Index Crawl**: For each API section (LOM, JS, Node for Max), parse its `index` page to extract the descriptions from the index table rows.
    2.  **Child Scrape**: Visit each URL defined in the `pages` array to extract the API definition (signatures, properties, methods).
*   **Specifications**:
    *   **[API Index Spec](api-ref-index-spec.md)**: Defines how to parse the index tables to build the navigation tree and capture descriptions.
    *   **[API Page Spec](api-ref-page-spec.md)**: Defines how to extract detailed API signatures, property tables, and method descriptions.

### 4.3. Learn Strategy
*   **Goal**: capture the hierarchy of "Learn" (Section) -> "Series" (e.g. Tutorials) -> "Articles".
*   **Input**: `docs/seeds.json` -> `urlset.sections["Learn"]`.
*   **Process**:
    1.  **Landing Crawl**: Use the `index` URL to parse the `/learn/` landing page to extract all available Series titles and descriptions.
    2.  **Series Processing**: For each series URL in the `series` array, visit the page to build the sequential hierarchy of articles.
    3.  **Article Scrape**: Iterate through the URLs in the `articles` array to extract tutorial content and establish "See Also" relationships.
*   **Specifications**:
    *   **[Learn Landing Page Spec](learn-landing-page-spec.md)**: Logic for the main `/learn/` page.
    *   **[Series Landing Page Spec](learn-series-landing-page-spec.md)**: Logic for Series indices.
    *   **[Learn Article Spec](learn-article-page-spec.md)**: Logic for individual tutorials.

### 4.4. Common Transformation Rules
These rules apply globally across all processors unless overridden by a specific spec.

1.  **HTML Cleaning (Cheerio)**
    *   **Remove Elements**: `nav`, `footer`, `.sidebar`, `.cookie-banner`, `script`, `style`, `iframe`, `.blocks_anchorLink__kJCjR` (heading anchors), `.article_metaWrapper__ARyDO` (footer meta).
    *   **Unwrap**: Remove wrapping `div`s that add no semantic value if they break Markdown flow.

2.  **Link Rewriting**
    *   **Internal Links**: Convert `href` starting with `/` (e.g., `/learn/series/foo`) to relative file paths (e.g., `../series/foo.md`).
    *   **External/Reference**: Keep absolute URLs for domains other than `docs.cycling74.com` OR for paths under `/reference/` (Max Object Reference).
    *   **Anchors**: Preserve fragment identifiers (`#foo`) when rewriting.

3.  **Image Handling**
    *   **Logic**: Convert relative paths to absolute URLs to ensure validity without local hosting.
    *   **Pattern**: `src="/images/hash.webp"` -> `src="https://docs.cycling74.com/images/hash.webp"`.
    *   **Query Params**: Strip strictly unnecessary query params if they don't affect the asset (e.g., tracking), but preserve signatures/versions if part of the filename.

4.  **Markdown Conversion (Turndown)**
    *   **Code Blocks**: Use `turndown-plugin-gfm` to preserve fenced code blocks with language detection (`javascript`, `json`).
    *   **Tables**: Ensure GFM table support is enabled.
    *   **Math**: Preserve `<annotation encoding="application/x-tex">` content as `$$ ... $$` blocks for KaTeX compatibility.

### 4.5. Tech Stack
*   **Runtime**: Node.js / TypeScript.
*   **Libraries**:
    *   `cheerio`: HTML parsing / DOM manipulation.
    *   `turndown`: HTML to Markdown conversion (with GFM plugin).
    *   `axios`: HTTP client with rate limiting/retry logic.
    *   `p-limit`: Concurrency control for polite scraping.

## 5. Execution Strategy
1.  **Initialize**: `npm install` dependencies.
2.  **Configure**: Load the user-provided `docs/seeds.json` file as the unified entry point.
3.  **Run**: `npm start`.
4.  **Verify**: Inspect `knowledge-map.json` and generated Markdown.
5.  **Deploy**: Move `data/content` and `knowledge-map.json` to the `vibemax-intelligence` extension.

## 6. Next Steps - Implementation Phase
1.  **Repository Setup**: 
    *   Initialize `cyclescraper` in a dedicated directory.
    *   Install dependencies (`axios`, `cheerio`, `turndown`, `p-limit`).
2.  **Configuration**:
    *   Load and validate the `docs/seeds.json` structure.
3.  **Core Processors**:
    *   Scaffold `src/processors/BaseProcessor.ts`.
    *   Implement `UserGuideProcessor`, `ApiRefProcessor`, `LearnProcessor` using the specific Selectors defined in 4.2.
4.  **Integration**:
    *   Write `src/main.ts` to orchestrate the pipeline.
    *   Run test scrapes on sample pages (using cached files or live requests with politeness).
5.  **Output**:
    *   Generate `knowledge-map.json` and Markdown files.
    *   Package for `vibemax-intelligence`.
