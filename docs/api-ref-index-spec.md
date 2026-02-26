# API Reference Index Specification

## 1. Overview
API Reference Index pages (LOM, JS API, Node for Max) serve as the primary navigation hub for technical interfaces. They contain essential groupings (Classes, Objects, Functions) and short descriptions.

## 2. Scraping Strategy

### 2.1. Identification
- **URL Pattern**: `https://docs.cycling74.com/apiref/[section]/`
- **Main Container**: `article[class*="article_content"]`

### 2.2. Content Extraction
1. **Title**: Extract from `<h1>`.
2. **Overview**: Extract all paragraphs between the `<h1>` and the first `<h2>`.
3. **Grouped Items**:
   - Iterate through each `<h2>` (the Group Title).
   - Find the sibling `<table>` immediately following the `<h2>`.
   - For each row (`<tr>`) in the table:
     - **Title/Link**: Extract from the first `<td>`.
     - **Description**: Extract from the second `<td>`.
4. **Relationship Mapping**:
   - Each row is a child of the current index page.
   - Inherit the `<h2>` text as the `apiGroup` metadata.

## 3. Data Output

### 3.1. File System
- **Path**: `apiref/[section]/index.md`

### 3.2. Knowledge Map (`knowledge-map.json`)
```json
{
  "title": "Live Object Model",
  "type": "api-index",
  "section": "lom",
  "filePath": "apiref/lom/index.md",
  "children": [
    {
      "title": "Application",
      "apiGroup": "API Objects",
      "slug": "application",
      "filePath": "apiref/lom/application.md",
      "description": "This class represents the Live application..."
    }
  ]
}
```
