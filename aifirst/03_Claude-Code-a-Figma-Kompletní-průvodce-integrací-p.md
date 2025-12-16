---
title: Claude Code a Figma: Kompletní průvodce integrací přes MCP
source: https://www.aifirst.cz/claude-code-a-figma-kompletni-pruvodce-integraci-pres-mcp-model-context-protocol/
scraped: 2025-12-15T22:32:13.743379
---

# Claude Code a Figma: Kompletní průvodce integrací přes MCP

Claude Code dokáže skutečně pracovat s Figma soubory a automaticky generovat kód z designů. Tato integrace funguje díky Model Context Protocol (MCP) – otevřenému standardu, který umožňuje AI nástrojům chápat designový kontext přímo z Figmy. Vzdálený MCP server je od září 2025 plně dostupný i bez nutnosti desktop aplikace, což otevírá tuto technologii širšímu okruhu vývojářů. V tomto komplexním průvodci se dozvíte, jak MCP funguje, jak ho nastavit v Claude Code, a jaké jsou praktické možnosti i současná omezení této technologie.

Obsah článku

Klíčové poznatky

Co je Model Context Protocol (MCP)?

Jak konkrétně funguje integrace Figma + Claude Code?

Co konkrétně můžete dělat?

Praktický návod k nastavení

Jak pracovat s designem

Co musíte vědět: Požadavky a omezení

Tipy pro nejlepší výsledky

Současný stav a budoucnost

Závěr

Klíčové poznatky

MCP je otevřený standardvyvinutý společností Anthropic, který funguje jako „USB-C port pro AI aplikace“

Figma MCP server je nyní Generally Available (GA)– oficiálně spuštěn v listopadu 2025 mimo beta verzi

Vzdálený server je dostupný od září 2025bez nutnosti desktop aplikace, i pro Starter plány (s limitem 6 calls/měsíc)

Lokální server vyžadujeFigma desktop aplikaci a Dev/Full seat na Professional+ plánu

Podporované nástrojezahrnují Claude Code, VS Code, Cursor, Windsurf, Android Studio a další

Není to automatický převod– MCP poskytuje kontext, ale kvalita závisí na promptech a lidském dohledu

Code Connect a Make souborybyly přidány v září 2025 pro lepší integraci s existujícím kódem

Co je Model Context Protocol (MCP)?

MCP je otevřený standard vyvinutý společností Anthropic, který funguje jako „USB-C port pro AI aplikace“. Umožňuje AI nástrojům připojit se k různým datovým zdrojům a aplikacím standardizovaným způsobem.

Figma včervnu 2025(konkrétně 4. června 2025) spustila svůj oficiální MCP server v otevřené beta verzi, který propojuje designová data přímo s AI vývojovými nástroji.

Jak konkrétně funguje integrace Figma + Claude Code?

Podporované způsoby připojení

Figma nabízí dva způsoby připojení k MCP serveru:

Běží přes Figma desktop aplikaci

Adresa: http://127.0.0.1:3845/mcp

Vyžaduje spuštěnou Figma aplikaci

Nižší latence, data zůstávají lokálně

Spuštěn23. září 2025a plně dostupný

Přímé připojení k https://mcp.figma.com/mcp

Nevyžaduje desktop aplikaci

Vhodné pro cloudové pracovní postupy

Dostupný pro všechny plány včetně Starter (s limity)

Podporované nástroje

MCP server od Figmy oficiálně podporuje:

Claude Code (terminál i VS Code rozšíření)

VS Code (s GitHub Copilot)

Cursor

Windsurf

Android Studio

Warp

Amazon Q

Replit

A další…

Co konkrétně můžete dělat?

Generování kódu z designu

Můžete vybrat frame nebo komponentu ve Figmě a nechat AI vygenerovat odpovídající kód pro React, HTML/CSS, Tailwind a další frameworky.

Extrakce designového kontextu

MCP server umožňuje vytáhnout proměnné, komponenty a layoutová data přímo do vašeho IDE, což je užitečné zejména pro design systémy a komponentové workflow.

Integrace s Code Connect

Systém Code Connect zajišťuje, že generovaný kód zůstává konzistentní s vaší existující code base a používá vaše skutečné komponenty.

Práce s Make soubory

Tato funkce byla přidána23. září 2025jako součást aktualizace vzdáleného serveru. Server dokáže získat kódové zdroje z Make souborů a poskytnout je jako kontext pro přechod z prototypu do produkční aplikace.

Praktický návod k nastavení

Krok 1: Aktivace Figma MCP serveru

Otevřete Figma desktop aplikaci (nejnovější verze)

Menu Figma → Preferences →Enable Desktop MCP server

Potvrzení se zobrazí ve spodní části okna

Není potřeba žádné speciální nastavení ve Figmě

Pouze připojení přes vaše IDE s následnou OAuth autentizací

Krok 2: Připojení Claude Code

Krok 3: Ověření připojení

V Claude Code zadejte příkaz/mcppro zobrazení všech připojených MCP serverů a jejich stavu.

Krok 4: Autentizace

Při prvním použití vzdáleného serveru budete vyzváni k autentizaci přes Figma OAuth flow. Postupujte podle pokynů v terminálu.

Jak pracovat s designem

Existují dva způsoby poskytnutí designového kontextu:

1. Výběr ve Figmě (selection-based) – pouze pro lokální server

Vyberte frame nebo vrstvu v Figma desktop aplikaci

V Claude Code zadejte prompt typu: „Vygeneruj React komponentu pro moji aktuální výběr s Tailwind CSS“

2. Odkaz na design (link-based) – funguje pro oba servery

Zkopírujte odkaz na frame nebo vrstvu ve Figmě

Do Claude Code vložte prompt: „Implementuj design z tohoto odkazu: [URL]“

Co musíte vědět: Požadavky a omezení

Požadavky na účet

Dostupný pro všechny plány včetněStarter

Starter a View/Collab seats:6 tool calls měsíčně

Dev/Full seats na Professional+: minutové rate limity dle Tier 1 REST API

Vyžaduje Dev nebo Full seat na Professional, Organization nebo Enterprise plánu

Aktuální omezení

MCP poskytuje kontext, ale AI nástroj stále vyžaduje interakci a správné prompty. Výsledná kvalita závisí na tom, jak dobře formulujete požadavky.

Claude Code skvěle generuje nové komponenty, ale když se design vyvíjí, je obtížné provádět chirurgické aktualizace existujícího kódu bez hlubokého porozumění vašemu design systému.

Konverze vícestránkového flow (např. carousel nebo onboarding) vyžaduje převod každého frame individuálně a následné propojení do interaktivní komponenty.

Vizuální feedback loop končí jakmile Claude Code vygeneruje komponentu – další úpravy se dělají v kódu nebo musíte znovu generovat.

Tipy pro nejlepší výsledky

Používejte sémantické názvy

Pojmenujte vrstvy a komponenty ve Figmě výstižně – AI pak lépe rozumí designovému záměru.

Organizujte design do komponent

Strukturovaný design s komponentami vede k čistšímu generovanému kódu.

Využívejte design tokeny a proměnné

MCP server extrahuje proměnné a tokeny, které pomáhají udržet konzistenci.

Rozdělujte velké výběry

Pro složité layouty je lepší generovat menší části a pak je složit dohromady.

Buďte konkrétní v promptech

Místo „udělej to hezké“ zkuste: „Vytvoř React komponentu s Tailwind CSS, použij naše designové tokeny pro barvy a spacing“

Současný stav a budoucnost

Aktuální stav (listopad 2025):

Figma MCP server je nynígenerally available (GA)– oficiálně spuštěn mimo beta verzi

Vzdálený server byl spuštěn23. září 2025a je plně dostupný bez nutnosti desktop aplikace

Code Connect UI bylo představeno23. září 2025s jednodušším mapováním komponent

Podpora Make souborů v MCP serveru byla přidána23. září 2025

Co Figma nadále vyvíjí:

Hlubší integraci s code base

Podporu pro anotace a Grid

Rozšíření funkcionality a partnerství

Další vylepšení výkonu a stability

Závěr

Ano, Claude Code dokáže pracovat s Figma soubory a převádět je do kódu – ale nikoli magickým přímým importem. Funguje to přes Model Context Protocol, který poskytuje AI nástrojům bohatý designový kontext.

Tato technologie je nynígenerally available(GA) a rychle se vyvíjí. Vzdálený server je již dostupný a funkční od září 2025, oficiální GA launch proběhl v listopadu 2025. Pro produkční workflow je stále potřeba lidský dohled a úpravy, ale proces design-to-code se dramaticky urychluje z hodin na minuty.

Doporučení:

Pokud pracujete s Claude Code, MCP server určitě vyzkoušejte. Vzdálený server je nyní dostupný i bez Professional+ plánu (s omezením 6 calls měsíčně pro Starter), což umožňuje širší testování. Je to výkonný nástroj pro prototypování, vytváření nových komponent a rychlé iterace designu.

Monika Šlajsová

Od roku 2022 vytváří projekty, které spojují kreativitu s podnikáním. Založila Minimo clay, projekt ručně vyráběných šperků ze Šumavy, se kterým je od roku 2025 součástí podnikatelského inkubátoru PointOne. Část svého studia strávila ve Finsku na Xamk - South-Eastern Finland University of Applied Sciences. V roce 2023 absolvovala Digisemestr a od stejného roku působila jako marketingový konzultant na PEF ČZU. V roce 2025 se stala Marketing Manager pro AI First a Project Operations Manager pro Mokabu. Zajímá se o startupy a projekty s dopadem, je idea maker a aktivně se věnuje seberozvoji - letos absolvovala výběrové akce jako Ogilvy Nulťák, Dentsu Bootcamp nebo Validation Camp od StartIt ČSOB. Jako freelancer působí jako fotografka pro agenturu Buzzoons a content creatorka pro Filmagix a DeeperSleeper. V minulosti dlouho doučovala matematiku. Poznávací znamení jsou barevné boty a špatný humor.

Cursor 2.0 a Composer: Revoluce v AI programování přichází rychleji, než jsme čekali4. 11. 2025

Listopadové přednášky Jindry Fáborského1. 11. 2025

Claude Code a Figma: Kompletní průvodce integrací přes MCP1. 11. 2025

Update kurzu AI First: ChatGPT Atlas a AI agenti mění pravidla hry23. 10. 2025

ChatGPT Atlas od OpenAI: Když se váš prohlížeč stane AI asistentem22. 10. 2025

---

**Zdroj:** [Claude Code a Figma: Kompletní průvodce integrací přes MCP](https://www.aifirst.cz/claude-code-a-figma-kompletni-pruvodce-integraci-pres-mcp-model-context-protocol/)
