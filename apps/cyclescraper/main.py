import asyncio
import argparse
import os
from pathlib import Path
from typing import Dict, Any

from crawl4ai import AsyncWebCrawler
from apps.cyclescraper.utils.crawler import get_browser_config
from apps.cyclescraper.utils.files import load_seeds
from apps.cyclescraper.processors.user_guide import process_user_guide
from apps.cyclescraper.processors.api_ref import process_api_ref
from apps.cyclescraper.processors.learn import process_learn

async def main():
    """Main orchestration script for CycleScraper."""
    parser = argparse.ArgumentParser(description="CycleScraper - Cycling '74 Docs Scraper")
    parser.add_argument("--section", choices=["userguide", "apiref", "learn", "all"], default="all",
                        help="Which section of the documentation to scrape.")
    parser.add_argument("--sub-section", type=str, default=None,
                        help="Optional sub-section to filter (e.g. 'audio', 'nodeformax', 'javascript-custom-drawing').")
    args = parser.parse_args()

    # Ensure data/content exists
    os.makedirs("data/content", exist_ok=True)
    
    # Load seeds configuration
    seeds = load_seeds()
    
    print(f"Starting CycleScraper (Section: {args.section}, Sub-section: {args.sub_section})...")
    
    async with AsyncWebCrawler(config=get_browser_config()) as crawler:
        try:
            if args.section in ["userguide", "all"]:
                await process_user_guide(crawler, seeds, sub_section=args.sub_section)
            
            if args.section in ["apiref", "all"]:
                await process_api_ref(crawler, seeds, sub_section=args.sub_section)
            
            if args.section in ["learn", "all"]:
                await process_learn(crawler, seeds, sub_section=args.sub_section)
            
        except Exception as e:
            print(f"Scrape interrupted: {e}")
            raise
            
        print("CycleScraper execution complete. Run build_map.py to generate data/knowledge-map.json.")

if __name__ == "__main__":
    asyncio.run(main())

