import os
import json
import aiohttp
from pathlib import Path
from typing import Dict, Any, List
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from apps.cyclescraper.utils.crawler import get_base_config
from apps.cyclescraper.utils.files import write_markdown
from apps.cyclescraper.utils.markdown import clean_markdown

async def fetch_html_manually(url: str) -> str:
    """Fetches HTML using aiohttp for BeautifulSoup parsing."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
    except Exception as e:
        print(f"Error fetching manual HTML for {url}: {e}")
    return ""

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

async def process_user_guide(crawler: AsyncWebCrawler, seeds: Dict[str, Any], sub_section: str = None) -> None:
    """Logic for User Guide section."""
    print(f"Processing User Guide (Filtering for: {sub_section})..." if sub_section else "Processing User Guide...")
    
    user_guide_data = seeds["urlset"]["sections"]["User Guide"]
    
    # Prepare list of tasks
    tasks = []
    for group_name, group_data in user_guide_data.items():
        # Filtering logic
        if sub_section and sub_section.lower() not in group_name.lower():
            continue
            
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
        print("No User Guide pages found for the specified parameters.")
        return

    config = get_base_config()
    
    print(f"Processing {len(tasks)} User Guide pages sequentially...")
    
    for group_name, page_name, url in tasks:
        print(f"Scraping: {url}")
        
        # Fetch raw HTML manually to extract standard meta tags from <head>
        raw_html = await fetch_html_manually(url)
        meta = extract_metadata_from_html(raw_html, url)
        description = meta.get("description")
        title = meta.get("title") or page_name
        if title and " | Cycling '74 Documentation" in title:
            title = title.replace(" | Cycling '74 Documentation", "")
            
        # Run crawl4ai specifically targeted at the article content
        result = await crawler.arun(url, config=config)
        
        if not result.success:
            print(f"Failed to crawl {url}: {result.error_message}")
            continue
            
        slug, category = get_slug_and_category(url)
        
        # Define file path
        group_slug = group_name.lower().replace(" ", "_").replace("/", "_")
        file_path = Path(f"data/content/userguide/{group_slug}/{slug}.md")
        
        # Prepare frontmatter (Enriched for decoupled build_map.py)
        frontmatter = {
            "title": title,
            "description": description or "",
            "sourceUrl": url,
            "section": "User Guide",
            "group": group_name,
            "kind": "guide"
        }
        
        # Clean and write
        cleaned_md = clean_markdown(result.markdown)
        write_markdown(file_path, cleaned_md, frontmatter)

    print(f"User Guide processing complete.")

