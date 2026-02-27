import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json

SERIES_URLS = [
    "https://docs.cycling74.com/learn/series/javascript-custom-drawing/",
    "https://docs.cycling74.com/learn/series/jitter-tutorials/",
    "https://docs.cycling74.com/learn/series/jitter_geometry/",
    "https://docs.cycling74.com/learn/series/max-tutorials/",
    "https://docs.cycling74.com/learn/series/msp-tutorials/",
    "https://docs.cycling74.com/learn/series/polish-your-pixels/"
]

async def inspect_series(url):
    print(f"\n--- Investigating: {url} ---")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            article = soup.find('article')
            
            if not article:
                print("No <article> tag found!")
                return

            # Print H1
            h1 = article.find('h1')
            if h1:
                print(f"Title (H1): {h1.get_text(strip=True)}")

            # Find all H2s and the first few items in the following UL
            h2s = article.find_all('h2')
            for h2 in h2s:
                group_name = h2.get_text(strip=True)
                print(f"\n  Group (H2): {group_name}")
                
                # Find the next UL
                ul = h2.find_next_sibling('ul')
                if ul:
                    items = ul.find_all('li', recursive=False)
                    print(f"    Found {len(items)} articles in this group.")
                    # Show first item as sample
                    if items:
                        li = items[0]
                        a = li.find('a', href=True)
                        if a:
                            title = a.get_text(strip=True)
                            url_path = a['href']
                            # Look for description - often text following the <a> or in a <p>
                            desc = li.get_text(strip=True).replace(title, "").strip()
                            print(f"    Sample Article: {title}")
                            print(f"    Sample URL: {url_path}")
                            print(f"    Sample Blurb: {desc[:100]}...")

if __name__ == "__main__":
    for url in SERIES_URLS:
        asyncio.run(inspect_series(url))
