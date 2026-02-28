from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator, CacheMode, BrowserConfig
from typing import Optional, List

# Standard excluded tags to keep the Markdown clean
# Note: excluded_tags only supports standard HTML tags, NOT CSS selectors.
EXCLUDED_TAGS = [
    "nav", "footer", "aside", "script", "style", "iframe", "header"
]

def get_browser_config() -> BrowserConfig:
    """Returns a robust browser configuration with stealth settings."""
    return BrowserConfig(
        headless=True,
        viewport_width=1280,
        viewport_height=1024,
        # Standard user agent to avoid bot detection
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        # Use random_user_agent=True if we hit blocks, but static is safer for now
    )

def get_base_config() -> CrawlerRunConfig:
    """Standard configuration for most Cycling '74 documentation pages."""
    return CrawlerRunConfig(
        css_selector="article.c74-article-content",
        excluded_tags=EXCLUDED_TAGS,
        markdown_generator=DefaultMarkdownGenerator(
            options={
                "absolute_urls": True,
                "escape_html": False  # We want to keep some HTML like tables if Markdown fails
            }
        ),
        cache_mode=CacheMode.BYPASS,
        verbose=False, # SILENCE IS GOLDEN
        wait_for="css:article.c74-article-content", # Wait for the main content to be present
        # Increase timeout for complex pages
        page_timeout=60000 
    )

def get_metadata_strategy():
    """NOT NEEDED: result.metadata has what we need."""
    return None

async def get_crawler():
    """Returns an instance of the AsyncWebCrawler."""
    return AsyncWebCrawler(config=get_browser_config())

