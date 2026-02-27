import asyncio
import os
import aiohttp
from pathlib import Path
from typing import Dict, Any, List
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler
from apps.cyclescraper.utils.crawler import get_base_config
from apps.cyclescraper.utils.files import write_markdown
from apps.cyclescraper.utils.markdown import clean_markdown
from apps.cyclescraper.models import KnowledgeNode

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

def extract_metadata_from_api_page(html: str, section: str) -> Dict[str, Any]:
    """Applies specialized selectors from api-ref-page-spec.md"""
    soup = BeautifulSoup(html, 'lxml')
    meta = {}
    
    # Title from h1
    h1 = soup.find('h1')
    meta["title"] = h1.get_text(strip=True) if h1 else None
    
    if section == "lom":
        # LOM specialized logic
        paths = []
        # Find h2 with "Canonical Paths"
        paths_h2 = soup.find('h2', string=lambda t: t and 'Canonical Paths' in t)
        if paths_h2:
            nxt = paths_h2.find_next_sibling()
            while nxt and nxt.name not in ['h2']:
                if nxt.name == 'pre':
                    paths.append(nxt.get_text(strip=True))
                nxt = nxt.find_next_sibling()
        meta["canonical_paths"] = paths
    else:
        # JS and Node for Max specialized logic
        # First pre block usually contains the definition/signature
        first_pre = soup.find('pre')
        meta["signature"] = first_pre.get_text(strip=True) if first_pre else None
        
    return meta

async def process_api_ref(crawler: AsyncWebCrawler, seeds: Dict[str, Any]) -> List[KnowledgeNode]:
    """Logic for API Reference section."""
    print("Processing API Reference...")
    
    api_ref_data = seeds.get("urlset", {}).get("sections", {}).get("API Reference", {})
    nodes = []
    
    config = get_base_config()

    # --- CALIBRATION OVERRIDE ---
    calibration_urls_str = os.getenv("CALIBRATION_URLS")
    calibration_mode = bool(calibration_urls_str)
    calibration_urls = []
    if calibration_mode:
        calibration_urls = [url.strip() for url in calibration_urls_str.split(',')]
        print(f"--- Calibration Mode: Filtering for API Reference pages. ---")
    # ---------------------------
    
    for section_name, section_data in api_ref_data.items():
        groups_data = section_data.get("pages", [])

        if calibration_mode:
            # Filter the groups_data to only include groups that contain a calibration URL
            filtered_groups_data = []
            for group_info in groups_data:
                # Filter pages within this group
                # Fix: Check if page is dict or string
                group_pages = group_info.get("pages", [])
                filtered_pages = []
                for p in group_pages:
                    p_url = p["url"] if isinstance(p, dict) else p
                    if p_url in calibration_urls:
                        filtered_pages.append(p)
                
                if filtered_pages:
                    # If pages are found, create a new group object with only those pages
                    new_group_info = group_info.copy()
                    new_group_info["pages"] = filtered_pages
                    filtered_groups_data.append(new_group_info)
            groups_data = filtered_groups_data # Overwrite with the filtered list
        
        if not groups_data:
            continue # Skip this section if no pages are left after filtering

        print(f"Processing section: {section_name}")
        index_url = section_data.get("index")
        
        # Determine short section identifier
        if "LOM" in section_name or "Live Object Model" in section_name:
            section_id = "lom"
        elif "JS" in section_name or "Javascript" in section_name:
            section_id = "js"
        elif "Node" in section_name:
            section_id = "nodeformax"
        else:
            section_id = section_name.lower().replace(" ", "")
            
        section_node = KnowledgeNode(
            title=section_name,
            type="section",
            kind="api-index",
            slug=section_id,
            filePath=f"apiref/{section_id}/index.md",
            sourceUrl=index_url,
            description=section_data.get("description", "")
        )
        nodes.append(section_node)
        
        group_nodes = {}
        
        # Flatten all pages in this section for batch processing
        section_tasks = []
        for group_info in groups_data:
            grp_name = group_info.get("group", "General")
            for page_data in group_info.get("pages", []):
                p_url = page_data["url"] if isinstance(page_data, dict) else page_data
                p_desc = page_data.get("description", "") if isinstance(page_data, dict) else ""
                section_tasks.append({
                    "url": p_url,
                    "description": p_desc,
                    "group": grp_name
                })
        
        if section_tasks:
            print(f"Batch crawling {len(section_tasks)} pages for API {section_id}...")
            urls = [t["url"] for t in section_tasks]
            results = await crawler.arun_many(urls, config=config, max_concurrent=5)
            
            for i, task in enumerate(section_tasks):
                url = task["url"]
                description = task["description"]
                grp_name = task["group"]
                result = results[i]
                
                if not result.success:
                    print(f"Failed to crawl {url}: {result.error_message}")
                    continue
                    
                path_parts = [p for p in urlparse(url).path.split('/') if p]
                slug = path_parts[-1] if path_parts else "index"
                
                # Apply specialized selectors
                page_meta = extract_metadata_from_api_page(result.html, section_id)
                title = page_meta.get("title") or slug
                
                # File path
                file_path = Path(f"data/content/apiref/{section_id}/{slug}.md")
                
                # Frontmatter
                frontmatter = {
                    "title": title,
                    "description": description or "",
                    "sourceUrl": url
                }
                
                # Write
                cleaned_md = clean_markdown(result.markdown)
                write_markdown(file_path, cleaned_md, frontmatter)
                
                if grp_name not in group_nodes:
                    group_nodes[grp_name] = KnowledgeNode(
                        title=grp_name,
                        type="group",
                        slug=grp_name.lower().replace(" ", "_"),
                        sourceUrl="",
                        description=f"{grp_name} for {section_name}",
                        children=[]
                    )
                
                group_nodes[grp_name].children.append(KnowledgeNode(
                    title=title,
                    type="page",
                    kind="api-page",
                    slug=slug,
                    filePath=str(file_path),
                    sourceUrl=url,
                    description=description or ""
                ))
            
            valid_groups = [g for g in group_nodes.values() if g.children]
            section_node.children = valid_groups if valid_groups else None
            
    return nodes
