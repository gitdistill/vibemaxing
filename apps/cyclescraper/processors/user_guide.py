import os
import json
from pathlib import Path
from typing import Dict, Any, List
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from apps.cyclescraper.utils.crawler import get_base_config
from apps.cyclescraper.utils.files import write_markdown
from apps.cyclescraper.utils.markdown import clean_markdown
from apps.cyclescraper.models import KnowledgeNode

def extract_metadata_from_html(html: str, url: str) -> Dict[str, str]:
    """Extracts metadata from the Crawl4AI HTML result."""
    try:
        soup = BeautifulSoup(html, 'lxml')
        desc_tag = soup.find('meta', attrs={'name': 'description'}) or \
                   soup.find('meta', attrs={'property': 'og:description'})
        
        title_tag = soup.find('meta', attrs={'property': 'og:title'}) or \
                    soup.find('title')
                    
        return {
            "description": desc_tag.get('content') if desc_tag else None,
            "title": title_tag.get('content') if title_tag and title_tag.name == 'meta' else (title_tag.text if title_tag else None)
        }
    except Exception as e:
        print(f"Error parsing metadata for {url}: {e}")
    return {"description": None, "title": None}

def get_slug_and_category(url: str):
    """
    Extracts slug and category from URL.
    Pattern: https://docs.cycling74.com/userguide/[category]/[slug]
    Valid categories: mc, gen, jitter, lua, m4l
    """
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split('/') if p]
    
    # path_parts typically starts with 'userguide'
    if not path_parts or len(path_parts) < 1:
        return "index", None
        
    relevant_parts = path_parts[1:] if path_parts[0] == 'userguide' else path_parts
    
    if not relevant_parts:
        return "index", None
        
    valid_categories = {'mc', 'gen', 'jitter', 'lua', 'm4l'}
    
    if relevant_parts[0] in valid_categories:
        category = relevant_parts[0]
        slug = relevant_parts[1] if len(relevant_parts) > 1 else "index"
    else:
        category = None
        slug = relevant_parts[0]
        
    # Clean up slug (remove trailing slashes or empty strings)
    if not slug:
        slug = "index"
        
    return slug, category

async def process_user_guide(crawler: AsyncWebCrawler, seeds: Dict[str, Any]) -> List[KnowledgeNode]:
    """Logic for User Guide section."""
    print("Processing User Guide...")
    
    user_guide_data = seeds["urlset"]["sections"]["User Guide"]
    nodes = []
    
    # Prepare list of tasks
    tasks = []
    for group_name, group_data in user_guide_data.items():
        pages = group_data.get("pages", {})
        for page_name, url in pages.items():
            tasks.append((group_name, page_name, url))

    # --- CALIBRATION OVERRIDE ---
    calibration_urls_str = os.getenv("CALIBRATION_URLS")
    if calibration_urls_str:
        calibration_urls = [url.strip() for url in calibration_urls_str.split(',')]
        original_task_count = len(tasks)
        tasks = [task for task in tasks if task[2] in calibration_urls]
        print(f"--- Calibration Mode: Found {len(tasks)} of {original_task_count} User Guide pages to process. ---")
    # ---------------------------

    if not tasks:
        print("No User Guide pages to process.")
        return []

    section_node = KnowledgeNode(
        title="User Guide",
        type="section",
        slug="userguide",
        sourceUrl="https://docs.cycling74.com/userguide/",
        description="Conceptual guides and overviews",
        children=[]
    )
    
    # Process in batches using arun_many
    config = get_base_config()
    urls = [t[2] for t in tasks]
    
    print(f"Batch crawling {len(urls)} User Guide pages...")
    results = await crawler.arun_many(urls, config=config, max_concurrent=5)
    
    # Combine results
    combined_results = []
    for i, (group_name, page_name, url) in enumerate(tasks):
        result = results[i]
        
        if not result.success:
            print(f"Failed to crawl {url}: {result.error_message}")
            continue
            
        slug, category = get_slug_and_category(url)
        
        # Metadata cleanup from HTML
        meta = extract_metadata_from_html(result.html, url)
        description = meta.get("description")
        title = meta.get("title") or page_name
        if title and " | Cycling '74 Documentation" in title:
            title = title.replace(" | Cycling '74 Documentation", "")
        
        # Define file path
        group_slug = group_name.lower().replace(" ", "_").replace("/", "_")
        file_path = Path(f"data/content/userguide/{group_slug}/{slug}.md")
        
        # Prepare frontmatter
        frontmatter = {
            "title": title,
            "description": description or "",
            "sourceUrl": url
        }
        
        # Clean and write
        cleaned_md = clean_markdown(result.markdown)
        write_markdown(file_path, cleaned_md, frontmatter)
        
        combined_results.append({
            "group_name": group_name,
            "node": KnowledgeNode(
                title=title,
                type="page",
                kind="guide",
                slug=slug,
                filePath=str(file_path),
                sourceUrl=url,
                description=description or ""
            )
        })

    # Group results
    groups = {}
    for r in combined_results:
        if r:
            gname = r["group_name"]
            if gname not in groups:
                group_data = user_guide_data.get(gname, {})
                group_slug = gname.lower().replace(" ", "_").replace("/", "_")
                groups[gname] = KnowledgeNode(
                    title=gname,
                    type="group",
                    slug=group_slug,
                    sourceUrl="", # Typically groups don't have a specific URL in userguide unless defined
                    description=group_data.get("description", ""),
                    children=[]
                )
            groups[gname].children.append(r["node"])
            
    section_node.children = list(groups.values())
    if not section_node.children:
        section_node.children = None
        
    return [section_node]
