import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, List
from apps.cyclescraper.models import KnowledgeNode, KnowledgeMap

def parse_markdown_file(path: Path) -> Dict[str, Any]:
    """Parses frontmatter from a markdown file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    return frontmatter
                except yaml.YAMLError as exc:
                    print(f"Error parsing frontmatter in {path}: {exc}")
    except Exception as e:
        print(f"Error reading {path}: {e}")
    return {}

def build_knowledge_map():
    content_dir = Path("data/content")
    if not content_dir.exists():
        print(f"Content directory {content_dir} not found. Run main.py first.")
        return

    # hierarchy[section][group] = [pages]
    hierarchy = {}

    print(f"Scanning {content_dir} for markdown files...")
    
    count = 0
    for md_file in content_dir.rglob("*.md"):
        # Skip index files if they don't have frontmatter (though our scrapers should add it)
        meta = parse_markdown_file(md_file)
        if not meta:
            continue
            
        section = meta.get("section")
        group = meta.get("group")
        
        if not section or not group:
            continue
            
        title = meta.get("title", md_file.stem)
        description = meta.get("description", "")
        source_url = meta.get("sourceUrl", "")
        kind = meta.get("kind", "page")
        
        if section not in hierarchy:
            hierarchy[section] = {}
        
        if group not in hierarchy[section]:
            hierarchy[section][group] = []
            
        hierarchy[section][group].append(KnowledgeNode(
            title=title,
            type="page",
            kind=kind,
            slug=md_file.stem,
            filePath=str(md_file),
            sourceUrl=source_url,
            description=description
        ))
        count += 1

    if not hierarchy:
        print("No valid markdown files found with required frontmatter (section, group).")
        return

    # Convert hierarchy to KnowledgeNode structure
    section_nodes = []
    for section_name, groups in hierarchy.items():
        group_nodes = []
        for group_name, pages in groups.items():
            # Sort pages by title
            pages.sort(key=lambda x: x.title)
            
            group_nodes.append(KnowledgeNode(
                title=group_name,
                type="group",
                slug=group_name.lower().replace(" ", "_"),
                sourceUrl="",
                description=f"{group_name} in {section_name}",
                children=pages
            ))
        
        # Sort groups by title
        group_nodes.sort(key=lambda x: x.title)
        
        section_nodes.append(KnowledgeNode(
            title=section_name,
            type="section",
            slug=section_name.lower().replace(" ", ""),
            sourceUrl="",
            description=f"Documentation section: {section_name}",
            children=group_nodes
        ))

    # Sort sections by title
    section_nodes.sort(key=lambda x: x.title)

    knowledge_map = KnowledgeMap(nodes=section_nodes)
    
    output_path = "data/knowledge-map.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_map.model_dump(exclude_none=True), f, indent=2)
    
    print(f"Knowledge map written to {output_path} with {len(section_nodes)} sections and {count} total pages.")

if __name__ == "__main__":
    build_knowledge_map()
