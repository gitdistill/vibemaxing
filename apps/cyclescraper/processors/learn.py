import asyncio
import os
import aiohttp
from pathlib import Path
from typing import Dict, Any, List
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

from crawl4ai import AsyncWebCrawler
from apps.cyclescraper.utils.crawler import get_base_config
from apps.cyclescraper.utils.files import write_markdown
from apps.cyclescraper.utils.markdown import clean_markdown

async def process_learn(crawler: AsyncWebCrawler, seeds: Dict[str, Any], sub_section: str = None) -> None:
    """Logic for Learn section."""
    learn_data = seeds.get("urlset", {}).get("sections", {}).get("Learn", {})
    series_list = learn_data.get("series", [])

    if not series_list:
        print("No Learn articles to process.")
        return

    print(f"Processing Learn section (Filtering for: {sub_section})..." if sub_section else "Processing Learn section...")
    
    # --- CALIBRATION OVERRIDE ---
    calibration_urls_str = os.getenv("CALIBRATION_URLS")
    calibration_mode = bool(calibration_urls_str)
    calibration_urls = []
    if calibration_mode:
        calibration_urls = [url.strip() for url in calibration_urls_str.split(',')]
        print(f"--- Calibration Mode: Filtering for Learn articles. ---")
    # ---------------------------

    # Count total articles and filter if in calibration mode or sub-section
    filtered_series_list = []
    
    for s_info in series_list:
        series_slug = s_info["url"].rstrip('/').split('/')[-1]
        
        # Filtering logic
        if sub_section and sub_section.lower() not in series_slug.lower() and sub_section.lower() not in s_info["title"].lower():
            continue

        series_groups = []
        for g_info in s_info.get("groups", []):
            articles = g_info.get("articles", [])
            if calibration_mode:
                articles = [a for a in articles if a["url"] in calibration_urls]
            
            if articles:
                series_groups.append({
                    "name": g_info["name"],
                    "articles": articles
                })
        
        if series_groups:
            new_s = s_info.copy()
            new_s["groups"] = series_groups
            new_s["slug"] = series_slug
            filtered_series_list.append(new_s)

    series_list = filtered_series_list
    
    if not series_list:
        print("No Learn series found for the specified parameters.")
        return

    # Base config for Learn articles
    article_config = get_base_config()
    
    # Process each series
    for series_info in series_list:
        series_title = series_info["title"]
        series_slug = series_info["slug"]
        groups = series_info.get("groups", [])

        print(f"Processing Series: {series_title} ({series_slug})")

        for group in groups:
            group_name = group["name"]
            articles = group.get("articles", [])
            
            if not articles:
                continue
                
            print(f"Processing {len(articles)} articles sequentially for Group: {group_name}")
            
            for article_meta in articles:
                url = article_meta["url"]
                
                print(f"Scraping: {url}")
                result = await crawler.arun(url, config=article_config)
                
                if not result.success:
                    print(f"Failed to crawl {url}: {result.error_message}")
                    continue
                
                # Get slug from URL
                path_parts = [p for p in urlparse(url).path.split('/') if p]
                slug = path_parts[-1] if path_parts else "index"
                
                # Use metadata from seeds.json (populated during discovery)
                title = article_meta.get("title", slug)
                description = article_meta.get("description", "")
                
                # File path
                file_path = Path(f"data/content/learn/articles/{slug}.md")
                
                # Prepare frontmatter (Enriched)
                frontmatter = {
                    "title": title,
                    "description": description,
                    "sourceUrl": url,
                    "section": "Learn",
                    "group": series_title,
                    "kind": "tutorial"
                }
                
                # Write markdown
                cleaned_md = clean_markdown(result.markdown)
                write_markdown(file_path, cleaned_md, frontmatter)
                
    print("Learn processing complete.")

