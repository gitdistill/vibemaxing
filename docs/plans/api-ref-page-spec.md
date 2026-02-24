# API Reference Page Specification

## 1. Overview
Individual API reference pages provide technical details for the Live Object Model (LOM), Max JS API, and Node for Max. The structure varies between LOM (path-based) and JS/Node (signature-based).

## 2. Scraping Strategy

### 2.1. LOM Objects (`/apiref/lom/*`)
1. **Title**: `<h1>` text.
2. **Canonical Paths**: All `<pre>` blocks under the "Canonical Paths" `<h2>`.
3. **Hierarchy/Members**:
   - Iterate through sections: "Children", "Properties", "Functions".
   - For each `<h3>`:
     - **Name**: `<h3>` text.
     - **Metadata**:
       - `type`: `span.c74-api-type` (text or link).
       - `attributes`: List of `span.c74-tag` (e.g., `read-only`, `observe`).
     - **Description**: All sibling `<p>` tags until the next `<h3>` or `<h2>`.
     - **Parameters**: Parse the "Parameters: `name` [type]" text if present in the description.

### 2.2. JS / Node API (`/apiref/js/*`, `/apiref/nodeformax/*`)
1. **Title**: `<h1>` text (e.g., "function messnamed" or "class Buffer").
2. **Definition**: The first `<pre>` block (TypeScript syntax).
3. **Parameters**:
   - Locate the `<table>` immediately following the definition.
   - Extract columns: `Name`, `Type`, `Description`.
4. **Members (for Classes)**:
   - Identify Methods and Properties via `<h3>` headings.
   - For each member, extract its signature (`pre`), parameter table (`table`), and description (`p`).
5. **Examples**:
   - Extract `<h4>` headings and their following `<pre>` code blocks.

## 3. Data Output

### 3.1. File System
- **Path**: `apiref/[section]/[slug].md`

### 3.2. Knowledge Map (`knowledge-map.json`)
```json
{
  "title": "Chain",
  "type": "api-page",
  "section": "lom",
  "apiGroup": "API Objects",
  "filePath": "apiref/lom/chain.md",
  "description": "This class represents a group device chain in Live."
}
```
