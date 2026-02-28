import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin
from typing import List, Dict, Any

async def fetch_html(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=15) as response:
                if response.status == 200:
                    return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return ""

async def discover_series(series_url: str):
    """Parses a series page to get its title, description, and article hierarchy."""
    print(f"Discovering: {series_url}")
    html = await fetch_html(series_url)
    if not html:
        return None
        
    soup = BeautifulSoup(html, 'lxml')
    article_tag = soup.find('article')
    
    if not article_tag:
        print(f"No <article> tag found on {series_url}")
        return None

    # Extract Title
    h1 = article_tag.find('h1')
    title = h1.get_text(strip=True) if h1 else ""
    
    # Extract Description (Overview)
    overview_paras = []
    if h1:
        curr = h1.find_next_sibling()
        while curr and curr.name not in ['h2', 'ul']:
            if curr.name == 'p':
                overview_paras.append(curr.get_text(strip=True))
            curr = curr.find_next_sibling()
    overview = " ".join(overview_paras)

    # Extract Articles grouped by H2 headings
    groups = []
    
    # Find all H2s in the article
    h2s = article_tag.find_all('h2')
    for h2 in h2s:
        group_name = h2.get_text(strip=True)
        articles_in_group = []
        
        # The articles are in the next sibling UL
        ul = h2.find_next_sibling('ul')
        if ul:
            for li in ul.find_all('li', recursive=False):
                a_tag = li.find('a', href=True)
                if a_tag:
                    article_title = a_tag.get_text(strip=True)
                    href = a_tag['href']
                    full_url = urljoin(series_url, href)
                    if not full_url.endswith('/'):
                        full_url += '/'
                    
                    # Description is usually text following the <a> in the <li>
                    # We remove the title from the li text and clean up
                    li_text = li.get_text(strip=True)
                    description = li_text.replace(article_title, "").strip()
                    # Clean leading dashes/whitespace
                    description = description.lstrip('—').lstrip('-').strip()
                    
                    articles_in_group.append({
                        "title": article_title,
                        "url": full_url,
                        "description": description
                    })
        
        if articles_in_group:
            groups.append({
                "name": group_name,
                "articles": articles_in_group
            })
                
    return {
        "title": title,
        "url": series_url,
        "description": overview,
        "groups": groups
    }

async def discover_api_ref(index_url: str, section_name: str) -> List[Dict[str, Any]]:
    """Crawls an API index URL and extracts descriptions and groups from tables."""
    print(f"Discovering API Index for {section_name}: {index_url}")
    html = await fetch_html(index_url)
    if not html:
        return []

    soup = BeautifulSoup(html, 'lxml')
    groups = {}

    # Find the main article content container
    article = soup.find('article') or soup

    # Find all h2s (groups) and their sibling tables
    for h2 in article.find_all('h2'):
        group_name = h2.get_text(strip=True)
        # Find next sibling table
        nxt = h2.find_next_sibling()
        while nxt and nxt.name not in ['h2', 'table']:
            nxt = nxt.find_next_sibling()
        
        if nxt and nxt.name == 'table':
            articles_in_group = []
            for row in nxt.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) >= 2:
                    link_tag = cols[0].find('a')
                    if link_tag and link_tag.has_attr('href'):
                        href = link_tag['href']
                        
                        # Determine slug from the href.
                        # For Node for Max, real slug is often the last part of the path, 
                        # even if nested inside a query param like /apiref/nodeformax/?source=.../max_env/
                        if '/' in href:
                            # Split by '/' and ignore empty strings and query param garbage
                            parts = [p for p in href.split('/') if p and not p.startswith('?source=')]
                            if parts:
                                slug = parts[-1]
                                # Ensure we don't accidentally keep the '?' if it was attached to the last part
                                if '?' in slug:
                                    slug = slug.split('?')[0]
                            else:
                                slug = ""
                        else:
                            slug = href.strip('/')

                        if slug:
                            full_url = urljoin(index_url, slug)
                            if not full_url.endswith('/'):
                                full_url += '/'
                        else:
                            full_url = index_url
                        
                        desc = cols[1].get_text(strip=True)
                        
                        articles_in_group.append({
                            "url": full_url,
                            "description": desc
                        })
            
            if articles_in_group:
                groups[group_name] = articles_in_group

    # Convert to list of group objects
    return [{"group": name, "pages": pages} for name, pages in groups.items()]

async def main():
    seeds_path = Path("docs/seeds.json")
    with open(seeds_path, 'r') as f:
        seeds = json.load(f)
        
    # 1. Discover Learn Section
    learn_section = seeds["urlset"]["sections"]["Learn"]
    # Capture current state to preserve existing data if already structured
    current_series = learn_section.get("series", [])
    
    series_urls = []
    for item in current_series:
        url = item if isinstance(item, str) else item.get("url")
        if url:
            series_urls.append(url)
    
    if not series_urls:
        # Fallback if series list is missing or empty
        series_urls = [
            "https://docs.cycling74.com/learn/series/javascript-custom-drawing/",
            "https://docs.cycling74.com/learn/series/jitter-tutorials/",
            "https://docs.cycling74.com/learn/series/jitter_geometry/",
            "https://docs.cycling74.com/learn/series/max-tutorials/",
            "https://docs.cycling74.com/learn/series/msp-tutorials/",
            "https://docs.cycling74.com/learn/series/polish-your-pixels/"
        ]

    new_series_data = []
    discovered_urls = set()
    
    for url in series_urls:
        data = await discover_series(url)
        if data:
            new_series_data.append(data)
            for group in data["groups"]:
                for art in group["articles"]:
                    discovered_urls.add(art["url"])
    
    seeds["urlset"]["sections"]["Learn"]["series"] = new_series_data

    # 2. Discover API Reference Section
    api_ref_section = seeds["urlset"]["sections"]["API Reference"]
    for section_name, section_data in api_ref_section.items():
        index_url = section_data.get("index")
        pages = section_data.get("pages", [])
        
        # If pages is a flat list of strings, it needs discovery
        # Or if it's already a list of dicts, we refresh it
        if pages and (isinstance(pages[0], str) or (isinstance(pages[0], dict) and "group" in pages[0])):
            structured_groups = await discover_api_ref(index_url, section_name)
            if structured_groups:
                seeds["urlset"]["sections"]["API Reference"][section_name]["pages"] = structured_groups
                print(f"Updated {section_name} with {len(structured_groups)} groups.")
    
    with open(seeds_path, 'w') as f:
        json.dump(seeds, f, indent=4)
        
    print(f"Updated {seeds_path} with structured data.")

if __name__ == "__main__":
    asyncio.run(main())
