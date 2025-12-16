"""
Awesome Vibe Coding GitHub Scraper
Stahuje curated list best practices pro vibe coding
"""

import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from datetime import datetime
import os
import time


# === KONFIGURACE ===
GITHUB_REPOS = {
    "awesome-vibe-coding": "filipecalegario/awesome-vibe-coding",
    "awesome-vibe-coding-guide": "analyticalrohit/awesome-vibe-coding-guide"
}
OUTPUT_DIR = r"C:\kb\awesome-vibe-coding"
DELAY = 1


def download_readme(repo_url):
    """Stáhne README z GitHub repo"""
    raw_url = f"https://raw.githubusercontent.com/{repo_url}/main/README.md"

    # Zkus main branch
    try:
        print(f"  Stahuji README (main): {repo_url}")
        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()
        return response.text
    except:
        pass

    # Zkus master branch
    raw_url = f"https://raw.githubusercontent.com/{repo_url}/master/README.md"
    try:
        print(f"  Stahuji README (master): {repo_url}")
        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] {e}")
        return None


def scrape_all_repos():
    """Stáhne všechny README"""
    print("\n" + "="*60)
    print("SCRAPING: Awesome Vibe Coding Resources")
    print("="*60 + "\n")

    repos_data = []

    for name, repo_url in GITHUB_REPOS.items():
        print(f"[{name}]")

        content = download_readme(repo_url)
        if content:
            repos_data.append({
                'name': name,
                'repo_url': repo_url,
                'github_url': f"https://github.com/{repo_url}",
                'content': content
            })
            print(f"  [OK] Staženo ({len(content)} znaků)")
        else:
            print(f"  [ERROR] Nepodařilo se stáhnout")

        time.sleep(DELAY)

    return repos_data


def save_to_kb(repos_data, output_dir=OUTPUT_DIR):
    """Uloží do KB struktury"""
    os.makedirs(output_dir, exist_ok=True)

    # Každý repo do vlastního souboru
    files_created = []

    for repo in repos_data:
        filename = f"{repo['name']}.md"
        filepath = os.path.join(output_dir, filename)

        # Markdown s frontmatter
        md_content = f"""---
title: {repo['name'].replace('-', ' ').title()}
source: {repo['github_url']}
repo: {repo['repo_url']}
scraped: {datetime.now().isoformat()}
---

{repo['content']}

---

**Source:** [{repo['name']}]({repo['github_url']})
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        files_created.append(filepath)
        print(f"  Vytvořen: {filename}")

    # Index
    index_content = [
        "# Awesome Vibe Coding Resources\n\n",
        "*Curated lists of best practices, tools, and guides for vibe coding*\n\n",
        f"*Scraped: {datetime.now().strftime('%Y-%m-%d')}*\n\n",
        "## Contents\n\n"
    ]

    for repo in repos_data:
        filename = f"{repo['name']}.md"
        title = repo['name'].replace('-', ' ').title()
        index_content.append(f"- [{title}]({filename}) - {repo['github_url']}\n")

    index_content.append("\n## What is Vibe Coding?\n\n")
    index_content.append("Vibe coding is natural language-driven, AI-assisted software development ")
    index_content.append("where you describe what you want via prompts and AI helps turn that into working code.\n\n")
    index_content.append("## Key Concepts\n\n")
    index_content.append("- **Context Engineering**: Crafting environment with goals, constraints, examples\n")
    index_content.append("- **CLAUDE.md**: Project-wide rules and guidelines\n")
    index_content.append("- **INITIAL.md**: Clear feature requests\n")
    index_content.append("- **PRP Blueprints**: Prompt-Ready Patterns\n\n")

    index_path = os.path.join(output_dir, 'INDEX.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(index_content))

    # Main README
    readme_content = f"""# Awesome Vibe Coding

Curated collections of vibe coding resources, best practices, and guides.

## What's Included

This KB contains curated lists from leading vibe coding repositories:

1. **Awesome Vibe Coding** (filipecalegario) - Comprehensive list of tools, patterns, and resources
2. **Awesome Vibe Coding Guide** (analyticalrohit) - Best practices and tips for efficient AI-assisted coding

## How to Use

Browse [INDEX.md](INDEX.md) for all resources, or read individual files:

- [awesome-vibe-coding.md](awesome-vibe-coding.md) - Main curated list
- [awesome-vibe-coding-guide.md](awesome-vibe-coding-guide.md) - Practical guide

## Topics Covered

- Context engineering
- AI coding tools (Cursor, Aider, Claude Code, etc.)
- Best practices for prompting
- Project structure and organization
- Common patterns and anti-patterns

---

*Scraped: {datetime.now().strftime('%Y-%m-%d')}*
"""

    readme_path = os.path.join(output_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"\n[OK] Knowledge Base vytvořena:")
    print(f"  Složka: {output_dir}")
    print(f"  Soubory: {len(files_created)}")
    print(f"  Index: {index_path}")

    return output_dir


# === MAIN ===
if __name__ == "__main__":
    print("Awesome Vibe Coding → KB Scraper\n")

    # Scrapuj
    repos = scrape_all_repos()

    # Ulož do KB
    kb_path = save_to_kb(repos)

    print("\n" + "="*60)
    print("HOTOVO!")
    print("="*60)
    print(f"\nAwesome Vibe Coding KB: {kb_path}")
