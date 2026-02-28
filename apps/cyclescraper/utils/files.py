import json
import asyncio
from typing import List, Dict, Any
from pathlib import Path

def load_seeds(path: str = "docs/seeds.json") -> Dict[str, Any]:
    """Loads the main seeds configuration file."""
    with open(path, "r") as f:
        return json.load(f)

def write_markdown(path: Path, content: str, frontmatter: Dict[str, Any]):
    """Writes a Markdown file with YAML frontmatter."""
    import yaml
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Sanitize description to collapse newlines/extra whitespace from HTML extraction
    if "description" in frontmatter and isinstance(frontmatter["description"], str):
        frontmatter["description"] = " ".join(frontmatter["description"].split())

    with open(path, "w") as f:
        f.write("---\n")
        # width=float('inf') prevents PyYAML from inserting its own line wraps
        yaml.dump(frontmatter, f, default_flow_style=False, width=float('inf'))
        f.write("---\n\n")
        f.write(content)

def write_knowledge_map(path: str, data: Dict[str, Any]):
    """Writes the full hierarchical index to knowledge-map.json."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
