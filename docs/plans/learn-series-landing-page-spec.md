# Series Landing Page Specification

## 1. Goals
*   Extract **Series Title**.
*   Extract **Series Overview Content** (if present).
*   Extract an **Ordered List of Articles**, including:
    *   Category Name (if articles are grouped).
    *   Article Title.
    *   Article Description.
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
- [Article Title 1](local/path/to/article1.md) - Article Description 1
- [Article Title 2](local/path/to/article2.md) - Article Description 2

## [Category Name 2 - if present]
- [Article Title 3](local/path/to/article3.md) - Article Description 3
```

### `data/content/learn/series/<series-slug>/metadata.json`
This file will contain a structured JSON representation of the series and its articles for programmatic access.
```json
{
  "title": "[Series Title]",
  "overview": "[Series Overview Content]",
  "url": "https://docs.cycling74.com/learn/series/<series-slug>/",
  "articles": [
    {
      "category": "[Category Name 1]", // Null if no category
      "title": "Article Title 1",
      "description": "Article Description 1",
      "url": "https://docs.cycling74.com/learn/articles/article1/",
      "path": "learn/articles/article1.md" // Local path
    },
    {
      "category": "[Category Name 1]",
      "title": "Article Title 2",
      "description": "Article Description 2",
      "url": "https://docs.cycling74.com/learn/articles/article2/",
      "path": "learn/articles/article2.md"
    }
  ]
}
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
    *   **Full Text:** Text content of the `<a>` tag (e.g., "Basics — Getting MIDI input and output").
    *   **Parsing `Full Text`:**
        *   Split the `Full Text` by the first occurrence of "—".
        *   The part before "—" is the **Article Title**.
        *   The part after "—" is the **Article Description**.
        *   If "—" is not present, the entire `Full Text` is the **Article Title**, and the **Article Description** is empty.

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
            *   Parse the `<a>` tag's text content into Article Title and Article Description using the "—" delimiter logic.
            *   Add an article object `{ category, title, description, url, path }` to the list. The `path` will be generated during the link rewriting phase.
4.  **Output Generation:**
    *   **`index.md`**: Assemble using Markdown formatting: Series Title, Overview, and then categorized lists of articles.
    *   **`metadata.json`**: Populate the JSON structure with the extracted Series Title, Overview, URL, and the list of articles. The `articles` array in JSON will include the `category` for each entry.

## 6. Edge Cases
*   **No Series Overview:** If no `<p>` tags are found meeting the criteria, the `overview` field will be an empty string/null.
*   **No Categories:** If a series has no `h2` elements, all articles will be categorized under null/empty string. The Markdown output will be a flat list.
*   **"Title — Description" Parsing:** The parsing logic must be resilient to variations in the article link text.

