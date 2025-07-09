#!/usr/bin/env python3
"""
Simple script to check for broken internal links in markdown files.
Usage: python check_links.py docs/
"""

import os
import re
import sys
from pathlib import Path

def find_markdown_files(directory):
    """Find all markdown files in directory."""
    return list(Path(directory).rglob("*.md"))

def extract_internal_links(content):
    """Extract internal markdown links from content."""
    # Match [text](link) where link doesn't start with http
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    links = []
    for match in re.finditer(pattern, content):
        link_text = match.group(1)
        link_url = match.group(2)
        # Skip external links
        if not (link_url.startswith('http') or link_url.startswith('mailto:')):
            links.append((link_text, link_url))
    return links

def resolve_link_path(current_file, link_url):
    """Resolve a relative link to absolute path."""
    current_dir = current_file.parent
    
    # Handle anchor links
    if '#' in link_url:
        link_url = link_url.split('#')[0]
        if not link_url:  # Just an anchor in current file
            return current_file
    
    # Resolve relative path
    if link_url.startswith('/'):
        # Absolute path from repo root
        return Path(link_url[1:])
    else:
        # Relative path
        return (current_dir / link_url).resolve()

def check_links(docs_dir):
    """Check all internal links in markdown files."""
    docs_path = Path(docs_dir)
    md_files = find_markdown_files(docs_path)
    broken_links = []
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = extract_internal_links(content)
        
        for link_text, link_url in links:
            target_path = resolve_link_path(md_file, link_url)
            
            # Check if target exists
            if not target_path.exists():
                broken_links.append({
                    'file': md_file,
                    'link_text': link_text,
                    'link_url': link_url,
                    'target_path': target_path
                })
    
    return broken_links

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_links.py <docs_directory>")
        sys.exit(1)
    
    docs_dir = sys.argv[1]
    if not os.path.isdir(docs_dir):
        print(f"Error: {docs_dir} is not a directory")
        sys.exit(1)
    
    broken_links = check_links(docs_dir)
    
    if not broken_links:
        print("✅ No broken internal links found!")
        return
    
    print(f"❌ Found {len(broken_links)} broken internal links:")
    print()
    
    for link in broken_links:
        print(f"File: {link['file']}")
        print(f"  Link: [{link['link_text']}]({link['link_url']})")
        print(f"  Target: {link['target_path']} (NOT FOUND)")
        print()

if __name__ == "__main__":
    main()