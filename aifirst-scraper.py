"""
AIFirst.cz Technical Articles Scraper
Scrapuje české praktické články o vibe codingu a AI
"""

import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import os
import re


# === KONFIGURACE ===
BASE_URL = "https://www.aifirst.cz"
BLOG_URL = f"{BASE_URL}/clanky/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Educational Scraper)'
}
DELAY = 2
OUTPUT_DIR = r"C:\kb\aifirst"

# Klíčová slova pro filtrování (jen vibe coding a technical články)
KEYWORDS = ['vibe coding', 'claude code', 'cursor', 'ai nástroje', 'praktick', 'tutoriál', 'jak']


def get_page(url):
    """Stáhne HTML stránku"""
    try:
        print(f"  Stahuji: {url}")
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] {e}")
        return None


def is_relevant_article(title):
    """Zkontroluje, jestli článek je relevantní pro vibe coding"""
    title_lower = title.lower()
    return any(keyword in title_lower for keyword in KEYWORDS)


def scrape_blog_listing():
    """Scrapne seznam článků"""
    soup = get_page(BLOG_URL)
    if not soup:
        return []

    articles = []

    # Najdi všechny odkazy na články
    links = soup.find_all('a', href=True)

    for link in links:
        href = link.get('href', '')
        title = link.get_text(strip=True)

        # Filtruj pouze články z /clanky/ nebo podobné
        if not href or not title:
            continue

        # URL musí být článek (obsahuje nadpis v href nebo je pod /clanky/)
        if 'clanek' not in href.lower() and len(title) < 10:
            continue

        # Skip navigační odkazy
        if title.lower() in ['all', 'ai aktuality', 'tip na akci', 'minipřípadovky']:
            continue

        # Filtr relevantních článků
        if not is_relevant_article(title):
            continue

        # Absolutní URL
        if href.startswith('/'):
            full_url = BASE_URL + href
        elif href.startswith('http'):
            full_url = href
        else:
            continue

        # Přidej pouze pokud ještě není v seznamu
        if not any(a['url'] == full_url for a in articles):
            articles.append({
                'title': title,
                'url': full_url
            })

    # Filtr - pouze unique články
    seen = set()
    unique_articles = []
    for article in articles:
        if article['url'] not in seen:
            seen.add(article['url'])
            unique_articles.append(article)

    print(f"  [OK] Nalezeno {len(unique_articles)} relevantních článků")
    return unique_articles[:15]  # Max 15 článků


def scrape_article_detail(url):
    """Scrapne detail článku"""
    soup = get_page(url)
    if not soup:
        return None

    try:
        # Titulek
        title = ""
        title_tag = soup.find('h1') or soup.find('h2')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Hlavní obsah
        content = ""
        content_div = (
            soup.find('article') or
            soup.find('div', class_=lambda x: x and ('content' in str(x).lower() or 'post' in str(x).lower()))
        )

        if content_div:
            # Odstraň navigaci, formuláře atd.
            for tag in content_div.find_all(['nav', 'form', 'aside']):
                tag.decompose()

            paragraphs = content_div.find_all(['p', 'h2', 'h3', 'h4', 'li'])
            content = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        if not content or len(content) < 100:
            return None

        return {
            'title': title,
            'url': url,
            'content': content
        }

    except Exception as e:
        print(f"  [ERROR] Chyba při zpracování: {e}")
        return None


def scrape_all_articles():
    """Scrapne všechny relevantní články"""
    print("\n" + "="*60)
    print("SCRAPING: AIFirst.cz Technical Articles")
    print("="*60 + "\n")

    # Získej seznam
    print("Získávám seznam článků...")
    articles = scrape_blog_listing()

    if not articles:
        print("[WARNING] Žádné články nenalezeny")
        return []

    time.sleep(DELAY)

    # Scrapuj detaily
    print(f"\nStahuji detaily {len(articles)} článků...\n")

    for i, article in enumerate(articles, 1):
        print(f"[{i}/{len(articles)}] {article['title'][:60]}...")

        detail = scrape_article_detail(article['url'])
        if detail:
            article.update(detail)
            print(f"  [OK] Staženo ({len(detail['content'])} znaků)")
        else:
            print(f"  [ERROR] Selhalo")

        time.sleep(DELAY)

    # Filtruj pouze úspěšné
    successful = [a for a in articles if 'content' in a and a['content']]
    print(f"\n[OK] Úspěšně staženo: {len(successful)}/{len(articles)} článků")

    return successful


def save_to_kb(articles, output_dir=OUTPUT_DIR):
    """Uloží do KB"""
    os.makedirs(output_dir, exist_ok=True)

    files_created = []

    # Index
    index_content = [
        "# AIFirst.cz - České Technical Články\n\n",
        "*Praktické tutoriály a tipy o vibe coding a AI nástrojích v češtině*\n\n",
        f"*Scraped: {datetime.now().strftime('%Y-%m-%d')}*\n",
        f"*Source: {BLOG_URL}*\n\n",
        "## Články\n\n"
    ]

    for i, article in enumerate(articles, 1):
        # Filename z titulku
        safe_title = re.sub(r'[^\w\s-]', '', article['title'])
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        filename = f"{i:02d}_{safe_title[:50]}.md"

        filepath = os.path.join(output_dir, filename)

        # Markdown
        md_content = f"""---
title: {article['title']}
source: {article['url']}
scraped: {datetime.now().isoformat()}
---

# {article['title']}

{article['content']}

---

**Zdroj:** [{article['title']}]({article['url']})
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        files_created.append(filepath)

        # Do indexu
        index_content.append(f"{i}. [{article['title']}]({filename})\n")

    # Ulož index
    index_path = os.path.join(output_dir, 'INDEX.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(index_content))

    # README
    readme_content = f"""# AIFirst.cz - Technical Articles

Praktické české články o vibe codingu, AI nástrojích a tutoriálech.

**Source:** {BLOG_URL}

## Co je zahrnuto

{len(articles)} vybraných technical článků zaměřených na:
- Vibe coding prakticky
- Claude Code
- Cursor
- AI nástroje a workflow
- Praktické tutoriály

## Obsah

Viz [INDEX.md](INDEX.md) pro kompletní seznam.

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
    print("AIFirst.cz → KB Scraper\n")

    # Scrapuj
    articles = scrape_all_articles()

    if articles:
        # Ulož
        kb_path = save_to_kb(articles)

        print("\n" + "="*60)
        print("HOTOVO!")
        print("="*60)
        print(f"\nAIFirst KB: {kb_path}")
    else:
        print("\n[ERROR] Žádné články ke stažení")
