# Vibe Coding Knowledge Base

> Personal curated collection of vibe coding documentation, best practices, and practical examples

[![Auto-Update](https://github.com/matouspetrzela-pixel/kb/actions/workflows/update-kb.yml/badge.svg)](https://github.com/matouspetrzela-pixel/kb/actions/workflows/update-kb.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is this?

A comprehensive, auto-updating knowledge base for AI-assisted development (vibe coding). Contains scraped documentation, practical examples, and personal notes.

**Total:** 31+ files | ~272 KB | 4 sources | Auto-updated weekly

## Contents

### 1. Claude Code Documentation
**Path:** `claude-code/` | **Size:** ~138 KB | **Files:** 15

Official Claude Code docs including:
- MCP (Model Context Protocol) integration
- Hooks system (28KB of API reference!)
- CLI commands and slash commands
- Configuration and settings

[Browse →](claude-code/INDEX.md)

### 2. Anthropic Cookbook
**Path:** `anthropic-cookbook/` | **Size:** ~78 KB | **Files:** 8

Practical Jupyter notebooks (converted to Markdown):
- Getting started with Vision
- Agent patterns
- Prompt caching (90% cost reduction!)
- Building evals

[Browse →](anthropic-cookbook/INDEX.md)

### 3. Awesome Vibe Coding
**Path:** `awesome-vibe-coding/` | **Size:** ~20 KB | **Files:** 2

Curated lists from the community:
- Best practices for context engineering
- Tool comparisons (Cursor, Claude Code, Aider)
- 1500+ GitHub repos referenced

[Browse →](awesome-vibe-coding/INDEX.md)

### 4. AIFirst.cz (Czech)
**Path:** `aifirst/` | **Size:** ~36 KB | **Files:** 6

Practical Czech tutorials:
- Vibe coding in practice
- Cursor 2.0 revolution
- Claude Code + Figma integration via MCP

[Browse →](aifirst/INDEX.md)

## How to Use

### Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/matouspetrzela-pixel/kb.git
   cd kb
   ```

2. **Browse locally:**
   - Open in VS Code, Obsidian, or any Markdown editor
   - Use `Ctrl+Shift+F` for full-text search

3. **Search via grep:**
   ```bash
   # Find all mentions of "hooks"
   grep -r "hooks" claude-code/

   # Find Python code examples
   grep -r "```python" .
   ```

### Use with Claude Code

Add to your `.claude/CLAUDE.md`:

```markdown
## Knowledge Base

I have a local vibe coding KB containing:
- Claude Code documentation (hooks, MCP, plugins)
- Anthropic Cookbook practical examples
- Best practices from Awesome Vibe Coding
- Czech tutorials from AIFirst

Reference these when I need help with vibe coding tools.
```

## Auto-Updates

This KB **automatically updates every Sunday at 3 AM UTC** via GitHub Actions.

Manual update:
```bash
python claude-code-scraper.py
python anthropic-cookbook-scraper.py
python awesome-vibe-coding-scraper.py
python aifirst-scraper.py
```

Or trigger via GitHub: **Actions** → **Update Knowledge Base** → **Run workflow**

## Structure

```
kb/
├── README.md                    # This file
├── claude-code/                 # Claude Code official docs
├── anthropic-cookbook/          # Practical notebooks
├── awesome-vibe-coding/         # Community best practices
├── aifirst/                     # Czech tutorials
├── notes/                       # Personal notes (gitignored)
├── .github/workflows/           # Auto-update actions
└── *-scraper.py                 # Update scripts
```

## Contributing

This is a **personal knowledge base**, but feel free to:
- Fork for your own use
- Suggest new sources via Issues
- Share your own KB structure

## Scrapers

Each source has its own scraper:
- `claude-code-scraper.py` → Scrapes code.claude.com/docs
- `anthropic-cookbook-scraper.py` → GitHub notebooks → Markdown
- `awesome-vibe-coding-scraper.py` → Curated READMEs
- `aifirst-scraper.py` → Czech blog articles

## License

MIT - Feel free to use and adapt

## Credits

Built with:
- [Claude Code](https://code.claude.com) - AI coding assistant
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Web scraping
- [GitHub Actions](https://github.com/features/actions) - Auto-updates

---

**Last updated:** 2025-12-15 (auto-updates weekly)

*Generated and maintained with Claude Code*
