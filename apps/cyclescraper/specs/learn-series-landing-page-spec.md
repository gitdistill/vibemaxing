# Series Landing Page Specification

## 1. Goals
*   Extract **Series Title**.
*   Extract **Series Overview Content** (if present).
*   Extract an **Ordered List of Articles**, including:
    *   Category Name (if articles are grouped).
    *   Article Title.
    *   Article Link.

## 2. Target URLs
`https://docs.cycling74.com/learn/series/<series-slug>/`
(e.g., `https://docs.cycling74.com/learn/series/jitter_geometry/`, `https://docs.cycling74.com/learn/series/msp-tutorials/`)

## 3. Output Files

### `data/content/learn/series/<series-slug>/index.md`
This file will contain a Markdown representation of the series overview and its articles.
```markdown
# [Series Title]

[Series Overview Content - if present]

## [Category Name 1 - if present]
- [Article Title 1](https://docs.cycling74.com/learn/articles/article1/)
- [Article Title 2](https://docs.cycling74.com/learn/articles/article2/)

## [Category Name 2 - if present]
- [Article Title 3](https://docs.cycling74.com/learn/articles/article3/)
```

## 4. DOM Selectors & Strategy (Dynamic Class Strategy)

*   **Main Content Area:** `article[class*="c74-article-content"]`
    *   This will be the primary container for all content extraction on these pages.

*   **Series Title:** `h1`
    *   Found directly within the `Main Content Area`.

*   **Series Overview:**
    *   `p` tags that are direct siblings of the `h1` and appear *before* the first `h2` (category heading) or `ul` (article list).
    *   Concatenate the text content of these paragraphs.

*   **Article Categories:** `h2`
    *   Text content defines the category name (e.g., "MIDI", "Data"). These `h2` elements act as logical grouping for subsequent articles.

*   **Article List Items:** `ul > li > a`
    *   These `ul` elements will either be direct siblings of the `h1` (for flat lists) or immediately follow an `h2` (for categorized lists).
    *   **URL:** `href` attribute of the `<a>` tag.
    *   **Title**: The text content of the `<a>` tag.
    *   **Description**: **DEPRECATED**. Article descriptions must be extracted from the article page's `<meta name="description">` instead of splitting the link text.

## 5. Execution Logic

1.  **Fetch:** Fetch the series landing page URL.
2.  **Extract Series Info:**
    *   Identify `h1` for the Series Title.
    *   Collect all `<p>` tags between the `h1` and the first `h2` or `ul` to form the Series Overview.
3.  **Extract Article Structure:**
    *   Initialize an empty list for articles.
    *   Iterate through children of the `Main Content Area`.
    *   Maintain a `currentCategory` variable (initially null).
    *   If an `h2` element is encountered, update `currentCategory` with its text content.
    *   If a `ul` element is encountered:
        *   For each `li > a` within this `ul`:
            *   Extract the `href` attribute (Article URL).
            *   Extract the `<a>` tag's text content as the Article Title.
            *   Add an article object `{ category, title, url }` to the list.
4.  **Output Generation:**
    *   **`index.md`**: Assemble using Markdown formatting: Series Title, Overview, and then categorized lists of articles.

## 6. Edge Cases
*   **No Series Overview:** If no `<p>` tags are found meeting the criteria, the `overview` field will be an empty string/null.
*   **No Categories:** If a series has no `h2` elements, all articles will be categorized under null/empty string. The Markdown output will be a flat list.
*   **"Title — Description" Parsing:** The parsing logic must be resilient to variations in the article link text.

