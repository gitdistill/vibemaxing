import asyncio
import json
import os
from pathlib import Path
from typing import Dict, Any

from crawl4ai import AsyncWebCrawler
from apps.cyclescraper.utils.crawler import get_browser_config
from apps.cyclescraper.utils.files import load_seeds, write_knowledge_map
from apps.cyclescraper.processors.user_guide import process_user_guide
from apps.cyclescraper.processors.api_ref import process_api_ref
from apps.cyclescraper.processors.learn import process_learn

def save_partial(knowledge_map: Dict[str, Any]):
    """Periodically save progress."""
    write_knowledge_map("knowledge-map.partial.json", knowledge_map)
    print("Saved partial knowledge map.")

async def main():
    """Main orchestration script for CycleScraper."""
    # Ensure data/content exists
    os.makedirs("data/content", exist_ok=True)
    
    # Load seeds configuration
    seeds = load_seeds()
    
    # Initialize knowledge map structure
    knowledge_map = {
        "version": "1.0.0",
        "nodes": []
    }
    
    # Concurrency and Retry configs are typically handled per process or globally in crawler init.
    # In Crawl4AI, arun_many handles concurrent crawls, but since we have custom processing 
    # and metadata extraction around the crawl, we use asyncio.Semaphore(10) inside processors.
    
    print("Starting CycleScraper (Building Processors & Architecture)...")
    
    # Setting max_concurrent for the AsyncWebCrawler.
    # arun_many will respect this concurrency.
    async with AsyncWebCrawler(config=get_browser_config()) as crawler:
        try:
            # 1. User Guide
            nodes_ug = await process_user_guide(crawler, seeds)
            knowledge_map["nodes"].extend([node.model_dump(exclude_none=True) for node in nodes_ug])
            save_partial(knowledge_map)
            
            # 2. API Reference
            nodes_api = await process_api_ref(crawler, seeds)
            knowledge_map["nodes"].extend([node.model_dump(exclude_none=True) for node in nodes_api])
            save_partial(knowledge_map)
            
            # 3. Learn
            nodes_learn = await process_learn(crawler, seeds)
            knowledge_map["nodes"].extend([node.model_dump(exclude_none=True) for node in nodes_learn])
            save_partial(knowledge_map)
            
        except Exception as e:
            print(f"Scrape interrupted: {e}")
            save_partial(knowledge_map)
            raise
            
        print("CycleScraper architecture setup complete.")
        write_knowledge_map("knowledge-map.json", knowledge_map)
        
        # Remove partial save on success
        if os.path.exists("knowledge-map.partial.json"):
            os.remove("knowledge-map.partial.json")

if __name__ == "__main__":
    asyncio.run(main())

