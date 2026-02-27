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
from apps.cyclescraper.models import KnowledgeNode

async def process_learn(crawler: AsyncWebCrawler, seeds: Dict[str, Any]) -> List[KnowledgeNode]:
    """Logic for Learn section."""
    learn_data = seeds.get("urlset", {}).get("sections", {}).get("Learn", {})
    index_url = learn_data.get("index")
    series_list = learn_data.get("series", [])

    if not series_list:
        print("No Learn articles to process.")
        return []

    print("Processing Learn section...")
    
    # Create the root section node
    section_node = KnowledgeNode(
        title="Learn",
        type="section",
        kind="index",
        slug="learn",
        filePath="learn/index.md",
        sourceUrl=index_url,
        description="Tutorial series and articles for learning Max, MSP, Jitter, and more.",
        children=[]
    )
    
    # --- CALIBRATION OVERRIDE ---
    calibration_urls_str = os.getenv("CALIBRATION_URLS")
    calibration_mode = bool(calibration_urls_str)
    calibration_urls = []
    if calibration_mode:
        calibration_urls = [url.strip() for url in calibration_urls_str.split(',')]
        print(f"--- Calibration Mode: Filtering for Learn articles. ---")
    # ---------------------------

    # Count total articles and filter if in calibration mode
    total_articles = 0
    filtered_series_list = []
    
    for s_info in series_list:
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
                total_articles += len(articles)
        
        if series_groups:
            new_s = s_info.copy()
            new_s["groups"] = series_groups
            filtered_series_list.append(new_s)

    series_list = filtered_series_list
    completed_articles = 0
    
    # Process each series
    for series_info in series_list:
        series_slug = series_info["url"].split('/')[-2] if series_info["url"].endswith('/') else series_info["url"].split('/')[-1]
        
        series_node = KnowledgeNode(
            title=series_info["title"],
            type="series",
            slug=series_slug,
            sourceUrl=series_info["url"],
            description=series_info["description"],
            children=[]
        )
        
        groups = series_info.get("groups", [])

        for group in groups:
            group_name = group["name"]
            articles = group.get("articles", [])
            
            if not articles:
                continue
                
            article_urls = [a["url"] for a in articles]
            print(f"Batch crawling {len(article_urls)} articles for series: {series_info['title']} - Group: {group_name}")
            
            # Base config for Learn articles
            article_config = get_base_config()
            results = await crawler.arun_many(article_urls, config=article_config, max_concurrent=5)
            
            group_node = KnowledgeNode(
                title=group_name,
                type="group",
                slug=group_name.lower().replace(" ", "_"),
                sourceUrl="",
                description=f"{group_name} in {series_info['title']}",
                children=[]
            )

            for i, article_meta in enumerate(articles):
                url = article_meta["url"]
                result = results[i]
                
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
                
                # Prepare frontmatter
                frontmatter = {
                    "title": title,
                    "description": description,
                    "sourceUrl": url
                }
                
                # Write markdown
                cleaned_md = clean_markdown(result.markdown)
                write_markdown(file_path, cleaned_md, frontmatter)
                
                completed_articles += 1
                if completed_articles % 10 == 0 or completed_articles == total_articles:
                    print(f"Learn Progress: {completed_articles}/{total_articles} articles")

                group_node.children.append(KnowledgeNode(
                    title=title,
                    type="page",
                    kind="article",
                    slug=slug,
                    filePath=str(file_path),
                    sourceUrl=url,
                    description=description
                ))
            
            if group_node.children:
                series_node.children.append(group_node)
            
        if series_node.children:
            section_node.children.append(series_node)

    if not section_node.children:
        section_node.children = None

    return [section_node]
