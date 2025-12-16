"""
Anthropic Cookbook GitHub Scraper
Stahuje klíčové Jupyter notebooks a převádí je do Markdown pro KB
"""

import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
import json
import time
from datetime import datetime
import os
import re


# === KONFIGURACE ===
GITHUB_REPO = "anthropics/claude-cookbooks"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"
OUTPUT_DIR = r"C:\kb\anthropic-cookbook"
DELAY = 1

# Klíčové soubory ke stažení (vybrané pro vibe coding)
KEY_FILES = {
    "getting_started": [
        "multimodal/getting_started_with_vision.ipynb",
        "tool_use/calculator_tool.ipynb",
    ],
    "agents": [
        "patterns/agents/README.md",
        "tool_use/customer_service_agent.ipynb",
    ],
    "skills": [
        "skills/README.md",
    ],
    "advanced": [
        "misc/prompt_caching.ipynb",
        "misc/building_evals.ipynb",
        "extended_thinking/guide.ipynb",
    ],
    "rag": [
        "capabilities/retrieval_augmented_generation/00_index.ipynb",
    ],
    "multimodal": [
        "multimodal/reading_charts_graphs_powerpoints.ipynb",
    ]
}


def download_file(path):
    """Stáhne raw soubor z GitHubu"""
    url = f"{RAW_BASE}/{path}"
    try:
        print(f"  Stahuji: {path}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] {e}")
        return None


def convert_notebook_to_markdown(notebook_json):
    """Převede Jupyter notebook (.ipynb) do Markdown"""
    try:
        nb = json.loads(notebook_json)
    except json.JSONDecodeError:
        return None

    markdown_parts = []

    for cell in nb.get('cells', []):
        cell_type = cell.get('cell_type')
        source = cell.get('source', [])

        # Spojit source (může být list nebo string)
        if isinstance(source, list):
            content = ''.join(source)
        else:
            content = source

        if not content.strip():
            continue

        if cell_type == 'markdown':
            # Markdown cell - přímo přidej
            markdown_parts.append(content + '\n\n')

        elif cell_type == 'code':
            # Code cell - wrap do code blocku
            # Detekuj jazyk (většinou Python)
            lang = 'python'
            markdown_parts.append(f"```{lang}\n{content}\n```\n\n")

            # Pokud má outputs, přidej je taky
            outputs = cell.get('outputs', [])
            for output in outputs:
                # Text output
                if 'text' in output:
                    text = output['text']
                    if isinstance(text, list):
                        text = ''.join(text)
                    markdown_parts.append(f"**Output:**\n```\n{text}\n```\n\n")

                # Data output (např. obrázky - jen poznámka)
                elif 'data' in output:
                    if 'image/png' in output['data']:
                        markdown_parts.append("*[Image output - see original notebook]*\n\n")
                    elif 'text/plain' in output['data']:
                        text = output['data']['text/plain']
                        if isinstance(text, list):
                            text = ''.join(text)
                        markdown_parts.append(f"```\n{text}\n```\n\n")

    return ''.join(markdown_parts)


def process_file(path, category):
    """Zpracuje jeden soubor (notebook nebo markdown)"""
    content = download_file(path)
    if not content:
        return None

    # Určíme typ souboru
    is_notebook = path.endswith('.ipynb')
    is_markdown = path.endswith('.md')

    filename = os.path.basename(path)
    title = filename.replace('.ipynb', '').replace('.md', '').replace('_', ' ').title()

    if is_notebook:
        # Převeď notebook do markdown
        markdown_content = convert_notebook_to_markdown(content)
        if not markdown_content:
            print(f"  [ERROR] Nepodařilo se převést notebook")
            return None
        final_content = markdown_content
        filename_out = filename.replace('.ipynb', '.md')

    elif is_markdown:
        # Markdown soubor - vezmi přímo
        final_content = content
        filename_out = filename

    else:
        print(f"  [WARNING] Nepodporovaný typ souboru")
        return None

    return {
        'title': title,
        'path': path,
        'category': category,
        'filename': filename_out,
        'content': final_content,
        'github_url': f"https://github.com/{GITHUB_REPO}/blob/main/{path}"
    }


def scrape_all_files():
    """Stáhne všechny klíčové soubory"""
    print("\n" + "="*60)
    print("SCRAPING: Anthropic Cookbook (GitHub)")
    print("="*60 + "\n")

    all_files = {}
    total = sum(len(files) for files in KEY_FILES.values())
    current = 0

    for category, files in KEY_FILES.items():
        print(f"\n[KATEGORIE: {category.upper()}]")
        all_files[category] = []

        for path in files:
            current += 1
            print(f"[{current}/{total}] {path}")

            file_data = process_file(path, category)
            if file_data:
                all_files[category].append(file_data)
                print(f"  [OK] Zpracováno ({len(file_data['content'])} znaků)")
            else:
                print(f"  [ERROR] Selhalo")

            time.sleep(DELAY)

    return all_files


def save_as_markdown_kb(data, output_dir=OUTPUT_DIR):
    """Uloží do KB struktury"""
    os.makedirs(output_dir, exist_ok=True)

    # Index
    index_content = [
        "# Anthropic Cookbook - Practical Examples\n\n",
        f"*Scraped from: https://github.com/{GITHUB_REPO}*\n",
        f"*Date: {datetime.now().strftime('%Y-%m-%d')}*\n\n",
        "Practical Jupyter notebooks and guides for working with Claude.\n\n",
        "## Contents\n\n"
    ]

    files_created = []

    for category, files in data.items():
        if not files:
            continue

        category_dir = os.path.join(output_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        index_content.append(f"### {category.replace('_', ' ').title()}\n\n")

        for file_data in files:
            filepath = os.path.join(category_dir, file_data['filename'])

            # Markdown s frontmatter
            md_content = f"""---
title: {file_data['title']}
source: {file_data['github_url']}
category: {category}
original: {file_data['path']}
scraped: {datetime.now().isoformat()}
---

# {file_data['title']}

{file_data['content']}

---

**Source:** [{file_data['title']}]({file_data['github_url']})
"""

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            files_created.append(filepath)

            # Do indexu
            rel_path = os.path.relpath(filepath, output_dir).replace('\\', '/')
            index_content.append(f"- [{file_data['title']}]({rel_path})\n")

        index_content.append("\n")

    # Ulož index
    index_path = os.path.join(output_dir, 'INDEX.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(index_content))

    # Main README
    readme_content = f"""# Anthropic Cookbook

Practical examples and notebooks for working with Claude AI.

**Source:** https://github.com/{GITHUB_REPO}

## What's included

This KB contains selected notebooks converted to Markdown:
- Getting Started examples
- Agent patterns
- Skills demonstrations
- Advanced techniques (prompt caching, evals, extended thinking)
- RAG (Retrieval Augmented Generation)
- Multimodal examples

## How to use

1. Browse [INDEX.md](INDEX.md) for all examples
2. Each file is a converted Jupyter notebook with:
   - Code examples
   - Explanations
   - Outputs (where applicable)

## Original Repository

For the full collection with runnable notebooks:
https://github.com/{GITHUB_REPO}

To run notebooks locally:
```bash
git clone https://github.com/{GITHUB_REPO}
cd claude-cookbooks
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements-dev.txt
jupyter notebook
```

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
    print("Anthropic Cookbook → KB Scraper")
    print(f"Output: {OUTPUT_DIR}\n")

    # Scrapuj
    files = scrape_all_files()

    # Ulož do KB
    kb_path = save_as_markdown_kb(files)

    print("\n" + "="*60)
    print("HOTOVO!")
    print("="*60)
    print(f"\nAnthopic Cookbook KB: {kb_path}")
