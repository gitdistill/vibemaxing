import asyncio
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator, CacheMode
from apps.cyclescraper.utils.crawler import get_base_config

async def main():
    async with AsyncWebCrawler() as crawler:
        # Use our standard config with selector
        config = get_base_config()
        url = "https://docs.cycling74.com/userguide/color_palette/"
        results = await crawler.arun_many([url], config=config)
        result = results[0]
        if result.success:
            print("Successfully fetched.")
            # Use BeautifulSoup to find description in the whole HTML
            print(f"Cleaned HTML length: {len(result.cleaned_html or '')}")
            print(f"Raw HTML length: {len(result.html or '')}")
            soup = BeautifulSoup(result.html, 'lxml')
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            desc = desc_tag.get('content') if desc_tag else "NOT FOUND"
            print(f"Manual Description: {desc}")
            
            og_title_tag = soup.find('meta', attrs={'property': 'og:title'})
            og_title = og_title_tag.get('content') if og_title_tag else "NOT FOUND"
            print(f"Manual OG Title: {og_title}")
            
            print(f"Metadata: {result.metadata}")
        else:
            print(f"Failed: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
