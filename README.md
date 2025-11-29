# KB - Moje znalostní báze pro AI

Osobní databáze materiálů, poznámek a zdrojů o AI, které sbírám pro svou práci jako AI Ambassador.

## 📁 Struktura

- `notes/` - Moje zpracované poznámky ve formátu Markdown
- `sources/` - Původní materiály (Word, Excel, PPT, PDF, videa)

## 📝 Jak přidat poznámku

Vytvoř nový .md soubor v `notes/` podle této šablony:

```markdown
---
title: Název materiálu
date: 2025-11-29
tags: tag1, tag2, tag3
source: URL nebo cesta k souboru
type: video/clanek/kurz/dokument
---

# Název

## Co jsem se naučil:
- Poznámka 1
- Poznámka 2
- Poznámka 3

## Jak to použiju:
Praktické využití v mé práci...

## Poznámky:
Vlastní postřehy a myšlenky...
```

## 🤖 Použití s AI nástroji

### Claude Code:
```bash
# Analyzuj videa a vytvoř poznámky
cd C:/kb
claude "Zpracuj video ze sources/ a vytvoř strukturovanou poznámku do notes/"

# Vyhledej v poznámkách
claude "Najdi všechny poznámky o prompt engineeringu"

# Vytvoř přehled
claude "Udělej přehled všech poznámek s tagem 'linkedin'"
```

### ChatGPT:
Nahraj soubory ze `sources/` a požádej o analýzu a vytvoření poznámek.

## 🏷️ Standardní tagy

- `ai-basics` - Základy AI
- `prompt-engineering` - Promptování
- `chatgpt` - ChatGPT specifické
- `claude` - Claude specifické
- `linkedin` - LinkedIn strategie
- `automation` - Automatizace
- `workshop` - Materiály z workshopů
- `case-study` - Případové studie
- `tools` - AI nástroje

## 📤 Nahrání na GitHub

1. Vytvoř nový repozitář na https://github.com/new
   - Název: kb
   - Popis: Znalostní báze pro AI materiály
   - Visibility: Private (nebo Public dle tvého výběru)
   - NEVYTVÁŘEJ README (už ho máš)

2. V terminálu v C:/kb/ spusť:
```bash
git remote add origin https://github.com/TVOJE-GITHUB-JMENO/kb.git
git branch -M main
git push -u origin main
```

3. Hotovo! Tvá kb je na GitHubu a připravená pro Cursor

## 📊 Statistiky

- Celkem poznámek: 0
- Celkem zdrojů: 0
- Poslední aktualizace: 2025-11-29
