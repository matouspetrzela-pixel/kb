---
title: Návod na práci s dokumenty v Cursoru
date: 2025-11-29
tags: cursor, dokumenty, návod, workflow
source: Vlastní materiál
type: dokument
status: prostudováno
---

# Návod: Práce s dokumenty v Cursoru

## Úvod

Tento návod vám ukáže, jak efektivně pracovat s dokumenty v Cursoru.
Dozvíte se, kde najít informace, jak používat klíčové funkce a jak
automatizovat rutinní úkoly při práci s textovými soubory, markdown
dokumenty a projekty.

## Co najdete v tomto návodu

- 🎯 Tři hlavní režimy práce s AI (Chat, Composer, Edit Mode)

- 📌 @ Symboly - jak poskytovat kontext agentovi

- 🗂️ Jak pracovat s více soubory současně

- ✏️ Jak upravovat a vytvářet dokumenty

- 🔄 Jak automatizovat rutinní úkoly

- 📊 Jak pracovat s různými formáty (Markdown, CSV, JSON)

- 🎯 Praktické příklady pro běžné úkoly

- 💡 Tipy a triky pro efektivní práci

## 1. Základy: Otevření projektu a práce s dokumenty

### Otevření složky s dokumenty

**Metoda 1: Přetažení (nejjednodušší)**

1.  Otevřete Cursor

2.  Přetáhněte složku s dokumenty do okna Cursoru

3.  V levém panelu uvidíte všechny soubory

**Metoda 2: Přes menu**

1.  File → Open Folder\...

2.  Vyberte složku s dokumenty

3.  Potvrďte výběr

**Metoda 3: Otevření jednotlivého souboru**

1.  File → Open File\...

2.  Vyberte soubor (např. .md, .txt, .json)

\[Screenshot: Otevření projektu v Cursoru\]

### Jaké formáty můžete otevřít?

Cursor podporuje všechny textové formáty:

- **Markdown** (.md) - dokumentace, poznámky

- **Textové soubory** (.txt) - jednoduché dokumenty

- **JSON** (.json) - strukturovaná data

- **CSV** (.csv) - tabulková data

- **YAML** (.yaml, .yml) - konfigurační soubory

- **XML** (.xml) - strukturované dokumenty

## 2. Jak efektivně používat Cursor: Tři hlavní režimy

Cursor nabízí tři různé režimy práce s AI. Každý režim má své specifické
použití a je důležité vědět, kdy který použít.

### Ask Mode (Chat) - Cmd/Ctrl+L

**Kdy použít:**

- Porozumění kódu a učení

- Plánování přístupu k úkolu

- Získání vysvětlení a konzultací

- Když potřebujete poradit, ale nechcete automatické změny

**Charakteristika:**

- Read-only, nemodifikuje kód automaticky

- Ideální pro začátečníky

- Bezpečné prostředí pro experimentování

- Konzultační režim - dostáváte odpovědi, ale změny musíte aplikovat
  sami

**Příklady použití pro dokumenty:**

\"Vysvětli, co obsahuje tento dokument\"

\"Jak bych měl přistoupit k organizaci těchto poznámek?\"

\"Jaké jsou best practices pro strukturování Markdown dokumentace?\"

\"Jaký formát by byl nejlepší pro tyto data?\"

\[Screenshot: Chat režim v Cursoru\]

### Agent Mode (Composer) - Cmd/Ctrl+I

**Kdy použít:**

- Aktivní vývoj a úpravy dokumentů

- Práce s více soubory současně

- Komplexní změny napříč projektem

- Automatizace rutinních úkolů

- Když chcete, aby AI aktivně pracovalo s vašimi soubory

**Charakteristika:**

- Může modifikovat dokumenty přímo

- Vytváří nové soubory automaticky

- Spouští příkazy v terminálu (pokud je povoleno)

- Až 25 tool calls pro iterativní zlepšování

- Automatické funkce:

  - Vyhledává relevantní kontext (@Recommended)

  - Vytváří checkpointy před změnami

  - Iteruje na chybách automaticky

**Příklady použití pro dokumenty:**

\"Vytvoř souhrn ze všech markdown souborů v této složce\"

\"Organizuj dokumenty do složek podle témat\"

\"Převeď všechny CSV soubory na Markdown tabulky\"

\"Oprav formátování ve všech dokumentech\"

\[Screenshot: Composer režim v Cursoru\]

### Edit Mode - Vybrat text + Cmd/Ctrl+K

**Kdy použít:**

- Malé, přesné úpravy v dokumentu

- Rychlé změny na místě

- Úpravy vybraného textu

- Když nepotřebujete pracovat s více soubory

**Charakteristika:**

- Inline úpravy vybraného textu

- Nejrychlejší pro drobné změny

- Okamžité výsledky

**Příklady použití pro dokumenty:**

Vyberte text a stiskněte Ctrl+K, pak zadejte:

\"Změň tento text na formálnější tón\"

\"Přidej více detailů k této sekci\"

\"Zkrátí tento odstavec\"

\"Přepiš tuto část tak, aby byla jasnější\"

\[Screenshot: Edit Mode v Cursoru\]

### Který režim použít?

**Použijte Chat (Ctrl+L), když:**

- ✅ Potřebujete poradit nebo se něco dozvědět

- ✅ Plánujete přístup k úkolu

- ✅ Chcete bezpečné prostředí bez automatických změn

- ✅ Začínáte a potřebujete vysvětlení

**Použijte Composer (Ctrl+I), když:**

- ✅ Chcete automaticky vytvářet nebo upravovat soubory

- ✅ Pracujete s více soubory najednou

- ✅ Potřebujete komplexní změny

- ✅ Automatizujete rutinní úkoly

**Použijte Edit Mode (Ctrl+K), když:**

- ✅ Děláte malé úpravy v jednom dokumentu

- ✅ Chcete rychlou změnu vybraného textu

- ✅ Nechcete spouštět celý agent

## 3. @ Symboly - Kontext je klíč

Základní princip: **Cursor je jen tak dobrý, jako kontext, který mu
poskytnete.**

Pomocí @ symbolů můžete explicitně určit, které soubory, složky nebo
zdroje má agent použít. To výrazně zlepšuje kvalitu výsledků.

### Typy @ zmínek

#### \@Files - Přidá konkrétní soubor

**Jak použít:**

- Zadejte @ a pak začněte psát název souboru

- Cursor vám nabídne auto-completion

- Nebo zadejte \@název_souboru.md

**Příklad:**

\@data.csv Analyzuj prodeje za Q4 a vytvoř souhrn

Agent použije obsah souboru data.csv jako kontext pro analýzu.

**Další příklady:**

\@poznámky_2024.md Vytvoř souhrn klíčových bodů z tohoto dokumentu

\@config.json Vytvoř dokumentaci z tohoto konfiguračního souboru

@template\.md Použij tento soubor jako šablonu pro vytvoření nového
dokumentu

\[Screenshot: Použití \@Files\]

#### \@Folders - Celá složka najednou

**Jak použít:**

- Zadejte @ a pak název složky

- Agent automaticky vidí všechny soubory ve složce

**Příklad:**

\@reports Shrň všechny měsíční reporty a vytvoř roční přehled

Agent projde všechny soubory ve složce reports a vytvoří souhrn.

**Vhodné pro:**

- Hromadné operace s více soubory

- Analýza celé složky

- Organizace dokumentů ve složce

**Další příklady:**

\@notes Organizuj všechny poznámky podle témat a vytvoř index

\@docs Zkontroluj konzistenci formátování ve všech dokumentech

\@archive Analyzuj všechny archivované soubory a vytvoř katalog

\[Screenshot: Použití \@Folders\]

#### \@Web - Live vyhledávání

**Jak použít:**

- Zadejte \@Web a pak váš dotaz

- Agent vyhledá aktuální informace na internetu

**Příklad:**

\@Web nejnovější postupy pro práci s Excel makry v roce 2024

Agent najde aktuální informace o Excel makrech a použije je pro odpověď.

**Kdy použít:**

- Potřebujete aktuální informace

- Hledáte best practices

- Chcete zkontrolovat nové postupy

- Potřebujete reference k externím zdrojům

**Další příklady:**

\@Web jak efektivně strukturovat Markdown dokumentaci

\@Web nejlepší nástroje pro konverzi CSV na Markdown

\[Screenshot: Použití \@Web\]

#### \@Docs - Dokumentace

**Jak použít:**

- Cursor automaticky má přístup k dokumentaci knihoven

- Můžete přidat vlastní dokumentaci přes URL

**Příklad:**

\@Docs Markdown Vytvoř dokumentaci podle oficiálních Markdown standardů

Agent použije dokumentaci Markdownu pro vytvoření správně formátovaného
dokumentu.

**Možnosti:**

- Přístup k dokumentaci knihoven (pokud pracujete s kódem)

- Přidání vlastní dokumentace přes URL

- Reference na oficiální standardy

**Další příklady:**

\@Docs Pandoc Jak převést dokument pomocí Pandoc

\[Screenshot: Použití \@Docs\]

#### \@Code - Konkrétní části obsahu

**Jak použít:**

- Reference specifických sekcí v souborech

- Funguje i pro strukturovaná data (JSON, YAML)

**Příklad:**

\@Code sekce_autentizace Uprav tuto sekci podle nejnovějších
bezpečnostních standardů

Agent použije konkrétní sekci kódu nebo textu jako kontext.

**Vhodné pro:**

- Práce s konkrétními částmi dokumentů

- Reference na strukturovaná data

- Přesné úpravy specifických sekcí

### Kombinace @ zmínek

Můžete kombinovat více @ zmínek pro komplexnější úkoly:

**Příklad 1:**

\@data.csv \@template.md Vytvoř nový report podle šablony s daty z CSV

**Příklad 2:**

\@notes \@reports Vytvoř souhrnný dokument z poznámek a reportů

**Příklad 3:**

\@Web \@docs Vytvoř dokumentaci podle aktuálních best practices

### Best practices pro @ symboly

1.  **Buďte konkrétní** - Použijte přesné názvy souborů a složek

2.  **Kombinujte** - Můžete použít více @ zmínek najednou

3.  **Využijte auto-completion** - Cursor vám pomůže najít správné
    soubory

4.  **Používejte \@Recommended** - Agent automaticky navrhne relevantní
    soubory

5.  **Zkontrolujte kontext** - Ujistěte se, že agent má přístup k
    správným souborům

## 4. Práce s více soubory současně

### Problém s klasickými nástroji

V běžných editorech nebo při práci s ChatGPT/Claude musíte:

- Kopírovat každý soubor zvlášť

- Vkládat do chatu postupně

- Ručně aplikovat změny zpět do souborů

- Trávit hodiny kopírováním a vkládáním

**Příklad:** Vytvoření souhrnu ze 20 poznámek = 30-60 minut ruční práce

### Řešení v Cursoru: Agent vidí celý projekt

**Jak to funguje:**

1.  Otevřete projekt se všemi dokumenty

2.  Agent automaticky vidí všechny soubory

3.  Můžete požádat o úkol s celým projektem

4.  Agent pracuje se všemi soubory současně

**Příklad: Vytvoření souhrnu ze všech poznámek**

1\. Otevřete projekt v Cursoru

2\. Stiskněte Ctrl+I (Composer)

3\. Zadejte: \"Vytvoř souhrn ze všech markdown souborů

v této složce a ulož ho jako souhrn.md\"

Agent automaticky:

\- Projde všechny .md soubory

\- Analyzuje obsah každého

\- Vytvoří strukturovaný souhrn

\- Vytvoří nový soubor souhrn.md

**Čas:** 2-5 minut (oproti 30-60 minutám ruční práce)

\[Screenshot: Práce s více soubory v Composeru\]

### Praktické příklady práce s více soubory

#### Příklad 1: Organizace dokumentů podle témat

Zadejte v Composer:

\"Organizuj všechny markdown soubory v této složce do podsložek

podle témat. Vytvoř složky: práce, osobní, projekty.\"

Agent:

- Analyzuje obsah všech souborů

- Identifikuje témata

- Vytvoří složky

- Přesune soubory do správných složek

#### Příklad 2: Vytvoření indexu pro všechny dokumenty

Zadejte v Composer:

\"Vytvoř index.md, který obsahuje seznam všech dokumentů

v projektu s jejich názvy, stručným popisem a kategoriemi.\"

Agent:

- Projde všechny soubory

- Analyzuje obsah

- Vytvoří strukturovaný index

- Uloží jako index.md

#### Příklad 3: Konzistentní formátování napříč projektem

Zadejte v Composer:

\"Uprav všechny markdown soubory tak, aby měly jednotný formát:

\- \## pro hlavní nadpisy

\- Metadata na začátku (datum, autor)

\- Konzistentní odsazení\"

Agent:

- Analyzuje formátování všech souborů

- Identifikuje nejčastější formát

- Aplikuje ho na všechny soubory

- Zobrazí změny v diff view

## 5. Vytváření a úpravy dokumentů

### Automatické vytváření souborů

**V klasických nástrojích:**

1.  Požádáte AI o vytvoření souboru

2.  AI vygeneruje obsah

3.  Musíte zkopírovat výsledek

4.  Musíte vytvořit nový soubor v editoru

5.  Musíte vložit obsah

6.  Musíte uložit soubor

**V Cursoru:**

1.  Požádáte agenta o vytvoření souboru

2.  Agent automaticky vytvoří soubor

3.  Soubor je uložen v projektu

4.  Můžete ho okamžitě použít

**Příklad: Vytvoření osnovy prezentace**

Zadejte v Composer:

\"Vytvoř strukturovaný dokument s osnovou pro prezentaci o AI

a ulož ho jako osnova_prezentace.md. Osnova by měla obsahovat:

\- Úvod

\- Klíčové body (5-7 bodů)

\- Závěr

\- FAQ sekci\"

Agent vytvoří:

- Soubor osnova_prezentace.md

- Strukturovanou osnovu

- Všechny požadované sekce

\[Screenshot: Vytvoření nového souboru agentem\]

### Vytváření více souborů najednou

**Příklad: Vytvoření souhrnů pro každý dokument**

Zadejte v Composer:

\"Vytvoř pro každý markdown soubor v této složce odpovídající

souhrn v samostatném souboru. Souhrny ulož jako

\[název_původního_souboru\]\_souhrn.md\"

Agent vytvoří:

- dokument1.md → dokument1_souhrn.md

- dokument2.md → dokument2_souhrn.md

- dokument3.md → dokument3_souhrn.md

- \... automaticky pro všechny soubory

### Úpravy dokumentů

**Kontrola změn před aplikací:**

1.  Agent navrhne změny

2.  Vidíte změny v diff view (co bylo odstraněno, co přidáno)

3.  Můžete změny upravit před přijetím

4.  Schválíte nebo odmítnete

**Příklad diff view:**

Původní text:

\# Úvod

Toto je úvodní text.

Navržená změna:

\- \# Úvod

\- Toto je úvodní text.

\+ \# Úvod

\+ Toto je úvodní text aktualizovaný pro rok 2024.

\[Screenshot: Diff view v Cursoru\]

## 6. Konverze formátů

### Konverze CSV na Markdown

**Úkol:** Převeď všechny CSV soubory na Markdown tabulky

Zadejte v Composer:

\"Převeď všechny CSV soubory v této složce na Markdown tabulky.

Každý CSV soubor převeď na odpovídající .md soubor s názvem

\[název_csv\].md\"

Agent:

1.  Najde všechny CSV soubory

2.  Pro každý soubor:

    - Přečte CSV

    - Převede na Markdown tabulku

    - Vytvoří nový .md soubor

3.  Uloží všechny výsledky

### Konverze TXT na Markdown

Zadejte v Composer:

\"Převeď všechny .txt soubory na .md a přidej metadata

(datum, autor) na začátek každého souboru\"

Agent:

1.  Najde všechny .txt soubory

2.  Převede je na Markdown

3.  Přidá metadata (datum, autor)

4.  Uloží jako .md soubory

### Konverze JSON na dokumentaci

Zadejte v Composer:

\"Vytvoř Markdown dokumentaci z tohoto JSON souboru.

Dokumentace by měla obsahovat popis všech polí a jejich význam.\"

Agent:

1.  Analyzuje JSON strukturu

2.  Vytvoří Markdown dokumentaci

3.  Popíše všechna pole

4.  Uloží jako dokumentace.md

## 7. Organizace a strukturování dokumentů

### Kategorizace dokumentů

**Úkol:** Organizuj dokumenty do složek podle témat

Zadejte v Composer:

\"Analyzuj všechny dokumenty v této složce a organizuj je

do podsložek podle témat. Vytvoř složky podle hlavních témat

a přesuň soubory do příslušných složek.\"

Agent:

1.  Analyzuje obsah všech dokumentů

2.  Identifikuje hlavní témata

3.  Vytvoří složky podle témat

4.  Přesune soubory do správných složek

### Vytvoření struktury projektu

Zadejte v Composer:

\"Vytvoř strukturu projektu pro dokumentaci:

\- docs/ (hlavní dokumentace)

\- notes/ (poznámky)

\- templates/ (šablony)

\- archive/ (staré dokumenty)

A přesuň existující soubory do příslušných složek.\"

Agent:

1.  Vytvoří požadovanou strukturu složek

2.  Analyzuje existující soubory

3.  Přesune je do správných složek

### Vytvoření indexu a navigace

Zadejte v Composer:

\"Vytvoř index.md pro tento projekt, který obsahuje:

\- Seznam všech dokumentů s odkazy

\- Stručné shrnutí každého dokumentu

\- Organizaci podle kategorií

\- Navigační strukturu\"

Agent:

1.  Projde všechny soubory v projektu

2.  Analyzuje jejich obsah

3.  Vytvoří strukturovaný index

4.  Přidá odkazy a popisy

5.  Organizuje podle kategorií

## 8. Analýza a extrakce informací

### Vytvoření souhrnu z více dokumentů

Zadejte v Composer:

\"Vytvoř souhrnný dokument ze všech poznámek v této složce.

Souhrn by měl obsahovat:

\- Klíčové body z každého dokumentu

\- Shrnutí hlavních témat

\- Společné body napříč dokumenty

\- Akční body (pokud jsou zmíněny)\"

Agent:

1.  Projde všechny soubory

2.  Analyzuje obsah

3.  Identifikuje klíčové body

4.  Vytvoří strukturovaný souhrn

5.  Uloží jako souhrn.md

### Extrakce dat z dokumentů

Zadejte v Composer:

\"Vytvoř CSV soubor s daty z těchto dokumentů. Pro každý dokument

extrahuj: název, datum (pokud je zmíněn), autor (pokud je zmíněn),

počet slov, hlavní témata.\"

Agent:

1.  Analyzuje všechny dokumenty

2.  Extrahuje požadované informace

3.  Vytvoří CSV soubor s daty

4.  Uloží jako data.csv

### Identifikace duplicitního obsahu

Zadejte v Composer:

\"Analyzuj všechny dokumenty a najdi duplicitní obsah.

Vytvoř seznam souborů s podobným obsahem a jejich míru podobnosti.\"

Agent:

1.  Analyzuje obsah všech dokumentů

2.  Identifikuje podobnosti

3.  Vytvoří seznam duplicit

4.  Uloží jako duplicity.md

## 9. Opravy a údržba dokumentů

### Oprava formátování

Zadejte v Composer:

\"Najdi všechny soubory s chybným formátováním a oprav je.

Zaměř se na:

\- Konzistentní formát nadpisů

\- Správné odsazení

\- Jednotné mezery

\- Správné Markdown syntax\"

Agent:

1.  Projde všechny soubory

2.  Identifikuje problémy s formátováním

3.  Opraví je automaticky

4.  Zobrazí vám seznam změn

### Oprava odkazů

Zadejte v Composer:

\"Oprav všechny odkazy v dokumentech, které odkazují na

přejmenované soubory. Aktualizuj odkazy tak, aby správně

odkazovaly na aktuální názvy souborů.\"

Agent:

1.  Analyzuje všechny odkazy v dokumentech

2.  Identifikuje přejmenované soubory

3.  Aktualizuje odkazy automaticky

4.  Zajistí, že všechny odkazy fungují

### Aktualizace metadata

Zadejte v Composer:

\"Uprav všechny markdown soubory tak, aby měly metadata

na začátku ve formátu:

\-\--

title: \[název souboru\]

date: \[datum poslední změny\]

author: \[autor, pokud je znám\]

\-\--\"

Agent:

1.  Projde všechny soubory

2.  Vytvoří nebo aktualizuje metadata

3.  Použije informace z názvů souborů a dat změn

4.  Aplikuje jednotný formát

## 10. Práce s různými formáty

### Markdown dokumenty

**Markdown je ideální formát pro dokumentaci v Cursoru.**

**Běžné úkoly:**

- Vytváření strukturovaných dokumentů

- Formátování nadpisů, seznamů, tabulek

- Přidávání odkazů a obrázků

- Vytváření obsahu

**Příklad: Vytvoření dokumentace s obsahem**

Zadejte v Composer:

\"Vytvoř dokumentaci z tohoto souboru. Přidej:

\- Obsah na začátek s odkazy na sekce

\- Formátuj nadpisy správně

\- Přidej odkazy mezi souvisejícími sekcemi\"

### CSV soubory

**Převod CSV na Markdown tabulky:**

Zadejte v Composer:

\"Převeď tento CSV soubor na Markdown tabulku s formátováním.

Přidej hlavičky a zajisti, že tabulka je čitelně formátovaná.\"

**Analýza CSV dat:**

Zadejte v Composer:

\"Analyzuj tento CSV soubor a vytvoř Markdown dokumentaci,

která popisuje strukturu dat, typy sloupců a příklady hodnot.\"

### JSON soubory

**Vytvoření dokumentace z JSON:**

Zadejte v Composer:

\"Vytvoř Markdown dokumentaci z tohoto JSON souboru.

Dokumentace by měla obsahovat:

\- Popis struktury

\- Vysvětlení každého pole

\- Příklady hodnot

\- Popis datových typů\"

**Validace JSON:**

Zadejte v Composer:

\"Zkontroluj všechny JSON soubory v projektu a najdi

soubory s chybnou strukturou. Vytvoř seznam chyb.\"

## 11. Praktické use cases

### Use Case 1: Organizace poznámek ze setkání

**Situace:** Máte 20 souborů s poznámkami ze setkání a chcete je
organizovat.

Krok 1: Otevřete složku s poznámkami v Cursoru

Krok 2: V Composer zadejte:

\"Organizuj všechny poznámky ze setkání:

1\. Vytvoř složky podle měsíců (2024-01, 2024-02, atd.)

2\. Přesuň soubory do příslušných složek podle data

3\. Vytvoř index.md s přehledem všech setkání

4\. Pro každé setkání extrahuj: datum, účastníky, klíčové body\"

**Výsledek:**

- Organizované soubory podle měsíců

- Index s přehledem

- Strukturované informace o každém setkání

### Use Case 2: Vytvoření dokumentace projektu

**Situace:** Máte projekt s různými soubory a chcete vytvořit
dokumentaci.

Krok 1: Otevřete projekt v Cursoru

Krok 2: V Composer zadejte:

\"Vytvoř kompletní dokumentaci pro tento projekt:

1\. README.md s popisem projektu

2\. docs/struktura.md - struktura projektu

3\. docs/pouziti.md - návod k použití

4\. docs/api.md - dokumentace API (pokud existuje JSON s API)

5\. Vytvoř index v hlavní složce s odkazy na všechny dokumenty\"

**Výsledek:**

- Kompletní dokumentační struktura

- Propojené dokumenty

- Profesionální dokumentace

### Use Case 3: Konverze starých dokumentů

**Situace:** Máte staré .txt soubory a chcete je převést na moderní
Markdown.

Krok 1: Otevřete složku s .txt soubory

Krok 2: V Composer zadejte:

\"Převeď všechny .txt soubory na Markdown:

1\. Převeď formátování na Markdown syntax

2\. Přidej metadata na začátek (název, datum)

3\. Formátuj nadpisy správně

4\. Ulož jako .md soubory

5\. Vytvoř archivní složku a přesuň původní .txt soubory\"

**Výsledek:**

- Všechny soubory převedené na Markdown

- Formátované a strukturované

- Původní soubory archivované

### Use Case 4: Vytvoření souhrnu z ročního projektu

**Situace:** Máte roční projekt s mnoha dokumenty a chcete vytvořit
roční souhrn.

Krok 1: Otevřete projekt v Cursoru

Krok 2: V Composer zadejte:

\"Vytvoř roční souhrn projektu:

1\. Analyzuj všechny dokumenty z posledního roku

2\. Vytvoř souhrn.md obsahující:

\- Přehled klíčových úspěchů

\- Hlavní projekty a jejich výsledky

\- Statistika (počet dokumentů, témat, atd.)

\- Trendy a změny v čase

\- Doporučení do budoucna

3\. Organizuj podle kategorií

4\. Přidej vizuální přehledy (tabulky, seznamy)\"

**Výsledek:**

- Komplexní roční souhrn

- Strukturované informace

- Přehledné statistiky a trendy

## 12. Tipy a triky

### Tip 1: Začněte s jednoduchými úkoly

Nejdřív zkuste jednoduché úkoly, abyste se seznámili s funkcionalitou:

- \"Vytvoř nový soubor s poznámkami\"

- \"Uprav formátování tohoto dokumentu\"

- \"Vytvoř souhrn z tohoto souboru\"

Pak postupně zkoušejte složitější úkoly.

### Tip 2: Používejte správný režim

- **Chat (Ctrl+L)** - když potřebujete poradit nebo se něco dozvědět

- **Composer (Ctrl+I)** - když chcete automaticky pracovat se soubory

- **Edit Mode (Ctrl+K)** - když děláte malé úpravy vybraného textu

Začátečníci by měli začít s Chat režimem, protože je bezpečný a
read-only.

### Tip 3: Používejte konkrétní pokyny

**Špatně:**

\"Uprav ty soubory\"

**Dobře:**

\"Uprav všechny markdown soubory v této složce tak, aby měly

jednotný formát nadpisů (## pro hlavní nadpisy) a metadata

na začátku ve formátu YAML front matter\"

### Tip 4: Používejte @ symboly pro lepší kontext

Vždy explicitně určete, které soubory nebo složky má agent použít:

- \@název_souboru.md - pro konkrétní soubor

- \@název_složky - pro celou složku

- \@Web - pro aktuální informace z internetu

- Kombinujte více @ zmínek pro komplexnější úkoly

**Příklad:**

\@data.csv \@template.md Vytvoř nový report podle šablony s daty z CSV

### Tip 5: Kombinujte úkoly

Můžete požádat o více úkolů najednou:

\"Vytvoř strukturu projektu pro dokumentaci, převeď všechny

.txt soubory na Markdown a vytvoř index všech dokumentů\"

### Tip 6: Využijte diff view

Vždy zkontrolujte změny v diff view před přijetím, abyste viděli, co se
změnilo.

### Tip 7: Používejte referenční soubory

Pokud chcete, aby agent použil konkrétní styl, můžete odkázat na
existující soubor:

\"Uprav tento dokument podle stylu souboru referencni_styl.md\"

### Tip 8: Iterujte

Pokud výsledek není ideální, upřesněte pokyn:

\"Uprav souhrn - přidej více detailů o každém projektu a

organizuj podle priority místo podle data\"

### Tip 9: Rychlé zkopírování cesty k souboru

**Pro Windows:**

- Klikněte pravým tlačítkem na soubor v Průzkumníku

- Při podržení klávesy Shift klikněte pravým tlačítkem

- Zobrazí se možnost \"Zkopírovat jako cestu\"

- Nebo vyberte soubor a stiskněte Shift + Ctrl + C

**Pro Mac:**

- Klikněte pravým tlačítkem (nebo Ctrl + klik) na soubor ve Finderu

- Při podržení klávesy Option (Alt) se zobrazí možnost \"Zkopírovat
  \[název souboru\] jako cestu\"

- Nebo vyberte soubor a stiskněte Option + Cmd + C

**Použití:** Po zkopírování cesty můžete přímo vložit do Cursoru nebo
použít v @ zmínce:

@/Users/uzivatel/dokumenty/poznamka.md Analyzuj tento soubor

### Tip 10: Nahraní celého linku webu/GitHub repozitáře do chatu

Můžete přímo vložit URL webové stránky nebo GitHub repozitáře do chatu a
agent ho automaticky analyzuje.

**Jak na to:**

1.  Zkopírujte URL (např. https://github.com/user/repo nebo
    https://example.com/article)

2.  Vložte do chatu v Cursoru (Ctrl+L nebo Ctrl+I)

3.  Agent automaticky načte obsah a může s ním pracovat

**Příklady použití:**

https://github.com/user/project Analyzuj tento repozitář a vytvoř souhrn
dokumentace

https://example.com/article Vytvoř souhrn tohoto článku v Markdown
formátu

**Výhody:**

- ✅ Nemusíte manuálně kopírovat obsah

- ✅ Agent vidí celou strukturu webu/repozitáře

- ✅ Můžete kombinovat s dalšími @ zmínkami

- ✅ Funguje pro dokumentaci, články, README soubory atd.

**Tip:** Můžete kombinovat URL s @ symboly:

\@Web https://github.com/user/project Vytvoř dokumentaci podle best
practices z tohoto repozitáře

## 13. Kde najít další informace

### Dokumentace Cursoru

- **Oficiální dokumentace:**
  [[https://cursor.com/en-US/docs]{.underline}](https://cursor.com/en-US/docs)

- **Funkce a možnosti:**
  [[https://cursor.com/features]{.underline}](https://cursor.com/features)

- **Changelog a novinky:**
  [[https://cursor.com/changelog]{.underline}](https://cursor.com/changelog)

### V Cursoru samotném

**Příkazová paleta:**

- Stiskněte Ctrl+Shift+P (Windows/Linux) nebo Cmd+Shift+P (Mac)

- Zadejte \"help\" nebo \"documentation\"

- Zobrazí se dostupné příkazy a nápověda

**Nastavení:**

- Ctrl+, (Windows/Linux) nebo Cmd+, (Mac)

- Sekce \"Cursor\" obsahuje dokumentaci k nastavení

### Komunita a podpora

- **Reddit:** r/cursor (pokud existuje)

- **Discord:** Oficiální Discord server Cursoru

- **GitHub:** Issues a diskuse (pokud existuje)

### Doprovodné materiály

- **Prezentace:** prezentace.md - základní přehled funkcí

- **Srovnání:** cursor_vs_klasicke_llm.md - rozdíly mezi Cursorem a
  klasickými LLM

## 14. Časté problémy a řešení

### Problém 1: Agent nevidí soubory

**Řešení:**

- Ujistěte se, že jste otevřeli složku (ne jen jednotlivý soubor)

- Zkontrolujte, že máte povolená systémová oprávnění (viz prezentace.md,
  slide 4)

### Problém 2: Agent neaplikuje změny

**Řešení:**

- Zkontrolujte nastavení oprávnění pro práci se soubory

- Ujistěte se, že máte povolený přístup k terminálu (pokud je potřeba)

- Zkontrolujte, zda schvalujete změny v diff view

### Problém 3: Výsledky nejsou přesné

**Řešení:**

- Upřesněte pokyn - buďte konkrétnější

- Poskytněte příklady nebo referenční soubory

- Rozdělte složitý úkol na více jednoduchých kroků

### Problém 4: Agent pracuje příliš pomalu

**Řešení:**

- Pro velké projekty rozdělte úkol na menší části

- Použijte konkrétnější pokyny, aby agent věděl, co přesně má dělat

- Zkontrolujte nastavení modelu (některé modely jsou rychlejší)

## 15. Shrnutí: Klíčové body

### Co si zapamatovat

1.  **Tři režimy práce** - Chat (Ctrl+L) pro konzultace, Composer
    (Ctrl+I) pro automatizaci, Edit Mode (Ctrl+K) pro rychlé úpravy

2.  **@ Symboly pro kontext** - vždy explicitně určete, které
    soubory/složky má agent použít

3.  **Cursor vidí celý projekt** - nemusíte kopírovat soubory

4.  **Agent automaticky pracuje** - vytváří, upravuje, organizuje
    soubory

5.  **Diff view** - vždy zkontrolujte změny před přijetím

6.  **Konkrétní pokyny** - čím konkrétnější, tím lepší výsledky

7.  **Začněte jednoduše** - postupně zkoušejte složitější úkoly

### Nejčastější použití

- ✅ Vytváření souhrnů z více dokumentů

- ✅ Organizace dokumentů do složek

- ✅ Konverze formátů (CSV → Markdown, TXT → Markdown)

- ✅ Oprava formátování napříč projektem

- ✅ Vytváření indexů a navigace

- ✅ Extrakce a analýza dat z dokumentů

### Kdy použít Cursor vs. ChatGPT/Claude

**Použijte Cursor, když:**

- Pracujete s více soubory najednou

- Potřebujete automatizovat úkoly s dokumenty

- Chcete, aby AI aktivně pracovalo s vašimi soubory

- Máte otevřený projekt v editoru

**Použijte ChatGPT/Claude, když:**

- Potřebujete obecnou konzultaci

- Chcete brainstorming nápadů

- Potřebujete vysvětlení konceptu

- Pracujete s jedním malým textem

## Závěr

Cursor je mocný nástroj pro práci s dokumenty. Klíčové je pochopit, že
agent **vidí celý projekt** a může **automaticky pracovat** s vašimi
soubory - nemusíte kopírovat, vkládat nebo ručně aplikovat změny.

**Začněte s jednoduchými úkoly a postupně zkoušejte složitější.** S
praxí zjistíte, jak efektivně využívat Cursor pro vaši práci s
dokumenty.

**Potřebujete pomoc?**

- Projděte si prezentace.md pro základní přehled

- Podívejte se na cursor_vs_klasicke_llm.md pro srovnání s jinými
  nástroji

- Navštivte oficiální dokumentaci:
  [[https://cursor.com/en-US/docs]{.underline}](https://cursor.com/en-US/docs)

**Hodně štěstí s prací s dokumenty v Cursoru!** 🚀
