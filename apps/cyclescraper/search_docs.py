#!/usr/bin/env python3
import json
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any

# Assuming script is run from project root, or handles relative paths
KNOWLEDGE_MAP_PATH = Path("data/knowledge-map.json")
FAILED_SEARCH_LOG = Path("data/failed_searches.log")

def log_failed_search(query_str: str):
    """Logs searches that returned 0 results."""
    try:
        FAILED_SEARCH_LOG.parent.mkdir(parents=True, exist_ok=True)
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FAILED_SEARCH_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {query_str}\n")
    except Exception as e:
        print(f"Warning: Could not log failed search: {e}", file=sys.stderr)

def load_knowledge_map() -> Dict[str, Any]:
    if not KNOWLEDGE_MAP_PATH.exists():
        print(f"Error: Could not find {KNOWLEDGE_MAP_PATH}. Please ensure you are running from the project root.", file=sys.stderr)
        sys.exit(1)
    
    with open(KNOWLEDGE_MAP_PATH, "r", encoding="utf-8") as f:
        # Note on minification: The ~200KB JSON file loads in <5ms.
        # Minifying it might save 50KB on disk but offers negligible memory or speed improvements in Python.
        return json.load(f)

def find_matches(nodes: List[Dict[str, Any]], keywords: List[str], results: List[Dict[str, Any]], max_results: int = 15):
    for node in nodes:
        if len(results) >= max_results:
            return
            
        title = node.get("title", "").lower()
        description = node.get("description", "").lower()
        tags = " ".join(node.get("tags", [])).lower() if isinstance(node.get("tags"), list) else ""
        filePath = str(node.get("filePath", "")).lower()
        slug = node.get("slug", "").lower()
        
        searchable_text = f"{title} {description} {tags} {filePath} {slug}"
        
        # Check if ALL keywords are in the searchable text
        if all(kw in searchable_text for kw in keywords):
            # Only return actual files, not groups/sections
            if node.get("filePath"):
                results.append(node)
                
        # Recursively check children
        if "children" in node and isinstance(node["children"], list):
            find_matches(node["children"], keywords, results, max_results)

def main():
    parser = argparse.ArgumentParser(description="Search the local Vibemax knowledge base.")
    parser.add_argument("query", nargs="+", help="Keywords to search for")
    parser.add_argument("--limit", type=int, default=15, help="Maximum number of results to return")
    args = parser.parse_args()
    
    keywords = []
    for q in args.query:
        keywords.extend(q.lower().split())
    
    data = load_knowledge_map()
    nodes = data.get("nodes", [])
    
    results = []
    find_matches(nodes, keywords, results, max_results=args.limit)
    
    if not results:
        query_str = ' '.join(keywords)
        print(f"No results found for: {query_str}")
        log_failed_search(query_str)
        return
        
    print(f"Found {len(results)} matches for: {' '.join(keywords)}\n")
    for i, res in enumerate(results, 1):
        print(f"[{i}] {res.get('title')}")
        if res.get('description'):
            print(f"    Description: {res.get('description')}")
        print(f"    Path: {res.get('filePath')}\n")

if __name__ == "__main__":
    main()
