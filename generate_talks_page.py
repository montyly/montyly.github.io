#!/usr/bin/env python3
"""
Generate talks.md page for the business website from talks.yaml

This script fetches talks.yaml from the publications repo and generates
a Jekyll-compatible markdown page for the business website.

Usage:
    python generate_talks_page.py

The script expects talks.yaml to be in the current directory (downloaded by GitHub Action).
"""

import yaml
from pathlib import Path


# Base URL for linking to slides in the publications repo
PUBLICATIONS_BASE_URL = "https://github.com/montyly/publications/blob/main/"


def make_link(text: str, path: str, base_url: str = PUBLICATIONS_BASE_URL) -> str:
    """Create a markdown link."""
    if path:
        # Handle paths that might have spaces
        return f"[{text}]({base_url}{path})"
    return text


def generate_presentations_section(presentations: list) -> str:
    """Generate the presentations section."""
    lines = [
        "## Conference Talks\n",
        "Invited talks and presentations at major blockchain and security conferences.\n",
    ]
    
    # Group by year
    by_year = {}
    for pres in presentations:
        year = pres['year']
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(pres)
    
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"\n### {year}\n")
        
        for pres in by_year[year]:
            title = pres['title']
            conference = pres['conference']
            
            # Build the entry
            if pres.get('slides_path'):
                entry = f"- **{title}** — {conference}"
                entry += f" ([slides]({PUBLICATIONS_BASE_URL}{pres['slides_path']}))"
            else:
                entry = f"- **{title}** — {conference}"
            
            if pres.get('video_url'):
                entry += f" ([video]({pres['video_url']}))"
            
            if pres.get('invited'):
                entry += " *(invited)*"
            
            lines.append(entry)
    
    return "\n".join(lines)


def generate_workshops_section(workshops: list) -> str:
    """Generate the workshops section."""
    lines = [
        "\n\n## Workshops\n",
        "Hands-on workshops on smart contract security, fuzzing, and static analysis.\n",
    ]
    
    # Group by year
    by_year = {}
    for ws in workshops:
        year = ws['year']
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(ws)
    
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"\n### {year}\n")
        
        for ws in by_year[year]:
            title = ws['title']
            conference = ws['conference']
            
            # Build the entry
            if ws.get('slides_path'):
                entry = f"- **{title}** — {conference}"
                entry += f" ([slides]({PUBLICATIONS_BASE_URL}{ws['slides_path']}))"
            else:
                entry = f"- **{title}** — {conference}"
            
            if ws.get('exercises_path'):
                entry += f" ([exercises]({PUBLICATIONS_BASE_URL}{ws['exercises_path']}))"
            
            lines.append(entry)
    
    return "\n".join(lines)


def generate_academic_section(conferences: list) -> str:
    """Generate the academic publications section."""
    lines = [
        "\n\n## Academic Publications\n",
        "Peer-reviewed research papers on program analysis, symbolic execution, and smart contract security.\n",
    ]
    
    for conf in conferences:
        title = conf['title']
        conference = conf['conference']
        authors = conf['authors']
        
        # Build the entry
        if conf.get('paper_path'):
            entry = f"- **{title}** — {conference}"
            entry += f" ([paper]({PUBLICATIONS_BASE_URL}{conf['paper_path']}))"
        else:
            entry = f"- **{title}** — {conference}"
        
        if conf.get('slides_path'):
            entry += f" ([slides]({PUBLICATIONS_BASE_URL}{conf['slides_path']}))"
        
        entry += f"\n  - *{authors}*"
        
        lines.append(entry)
    
    return "\n".join(lines)


def generate_podcasts_section(podcasts: list) -> str:
    """Generate the podcasts/panels section."""
    lines = [
        "\n\n## Podcasts & Panels\n",
    ]
    
    # Group by year
    by_year = {}
    for pod in podcasts:
        year = pod['year']
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(pod)
    
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"\n### {year}\n")
        
        for pod in by_year[year]:
            title = pod['title']
            pod_type = pod['type']
            url = pod.get('url', '')
            event = pod.get('event', '')
            
            if url:
                entry = f"- [{title}]({url})"
            else:
                entry = f"- {title}"
            
            entry += f" — {pod_type}"
            
            if event:
                entry += f" ({event})"
            
            lines.append(entry)
    
    return "\n".join(lines)


def generate_talks_page(data: dict) -> str:
    """Generate the complete talks.md page."""
    
    # Jekyll front matter with navigation style
    header = """---
layout: default
title: Talks & Publications
permalink: /talks/
---

<style>
.nav-tabs {
  display: flex;
  margin-bottom: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.95em;
  overflow: hidden;
  width: fit-content;
}

.nav-tabs a {
  padding: 8px 16px;
  text-decoration: none;
  color: #0366d6;
  background: #f8f8f8;
  border-right: 1px solid #ccc;
  flex: 1;
  text-align: center;
}

.nav-tabs a:last-child {
  border-right: none;
}

.nav-tabs a.active {
  background: white;
  font-weight: bold;
}
</style>

<div class="nav-tabs">
  <a href="/">Home</a>
  <a href="/blog">Blog</a>
  <a href="/talks/" class="active">Talks</a>
  <a href="/portfolio/">Portfolio</a>
  <a href="/about/">About</a>
</div>

# Talks & Publications

A collection of my conference presentations, workshops, academic papers, and podcast appearances.

For the complete list with all materials, see the [publications repository](https://github.com/montyly/publications).

"""
    
    presentations = generate_presentations_section(data['industrial_presentations'])
    workshops = generate_workshops_section(data['industrial_workshops'])
    academic = generate_academic_section(data['academic_conferences'])
    podcasts = generate_podcasts_section(data['podcasts_panels'])
    
    footer = """

---

*This page is auto-generated from the [publications repository](https://github.com/montyly/publications).*
"""
    
    return header + presentations + workshops + academic + podcasts + footer


def main():
    yaml_path = Path("talks.yaml")
    output_path = Path("talks.md")
    
    if not yaml_path.exists():
        print(f"Error: {yaml_path} not found")
        return 1
    
    # Load YAML data
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Generate talks page
    content = generate_talks_page(data)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {output_path}")
    return 0


if __name__ == "__main__":
    exit(main())
