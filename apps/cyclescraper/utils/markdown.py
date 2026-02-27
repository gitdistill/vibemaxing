import re

def clean_markdown(md_text: str) -> str:
    """
    Cleans up generated markdown by removing unwanted artifacts like empty anchor links,
    converting MathML annotations to KaTeX blocks, and ensuring absolute image URLs.
    """
    if not md_text:
        return ""
    
    # Remove empty markdown links: [](...) that are NOT images ![](...)
    # These often come from hidden anchor tags inside headings
    cleaned = re.sub(r'(?<!\!)\[\]\([^)]+\)', '', md_text)
    
    # Convert <annotation encoding="application/x-tex"> to $$ ... $$
    # Use re.DOTALL to match across newlines
    cleaned = re.sub(
        r'<annotation encoding="application/x-tex">(.*?)</annotation>',
        lambda m: f"$$ {m.group(1).strip()} $$",
        cleaned,
        flags=re.DOTALL
    )
    
    # Cleanup any lingering <math> or </math> tags if needed, or other math tags.
    # For now, just replacing the annotation is the most reliable way if raw TeX is present.
    
    # Ensure all image URLs are absolute (Crawl4AI absolute_urls might catch most, but just in case)
    # Match ![...](/images/...) and replace with ![...](https://docs.cycling74.com/images/...)
    cleaned = re.sub(
        r'!\[(.*?)\]\((/[^)]+)\)',
        r'![\1](https://docs.cycling74.com\2)',
        cleaned
    )
    
    # General relative link fallback for docs.cycling74.com just in case
    # This shouldn't affect much since Crawl4AI DefaultMarkdownGenerator(options={"absolute_urls": True}) is used,
    # but it's a good safety net for any links that slip through.
    cleaned = re.sub(
        r'(?<!!)\[(.*?)\]\((/[^)]+)\)',
        r'[\1](https://docs.cycling74.com\2)',
        cleaned
    )
    
    return cleaned
