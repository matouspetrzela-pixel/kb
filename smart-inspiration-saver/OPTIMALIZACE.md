# 🚀 TOKEN OPTIMALIZACE

## PŘED vs. PO

### Extrakce textu

**PŘED:**
```
- Surový body.innerText (3000 znaků)
- Všechny elementy (header, footer, nav, ads)
- Prostý substring(0, 2000)
```

**PO:**
```
- Priorita: <main>, <article>, [role="main"]
- Ignoruje navigaci, footer, sidebary
- Sémantické krácení:
  ✓ 1000 znaků intro (kontext)
  ✓ Nejdelší odstavec z dalších 2000 (hlavní obsah)
  ✓ Filtrování spam odstavců (cookies, newsletter)
  = Max 1500 znaků relevantního obsahu
```

---

## ÚSPORA TOKENŮ

### Text
- **PŘED:** 2000 znaků × 0.25 = ~500 tokenů
- **PO:** 1500 znaků × 0.25 = ~375 tokenů
- **Úspora:** 25%

### Prompt
- **PŘED:** Verbose prompt (~100 tokenů)
- **PO:** Kompaktní prompt (~30 tokenů)
- **Úspora:** 70%

### Output
- **PŘED:** max_tokens: 50
- **PO:** max_tokens: 20
- **Úspora:** 60%

---

## CELKOVÁ ÚSPORA NA REQUEST

**PŘED:**
```
Input:  500 + 100 = 600 tokenů
Output: 50 tokenů
Cost:   600 × $0.003 + 50 × $0.015 = $2.55 / 1000 req
```

**PO:**
```
Input:  375 + 30 = 405 tokenů  (-32%)
Output: 20 tokenů              (-60%)
Cost:   405 × $0.003 + 20 × $0.015 = $1.52 / 1000 req
```

**💰 Úspora: 40% nákladů na request**

---

## KVALITA KATEGORIZACE

**Lepší extrakce = lepší kategorizace:**

✅ Priorita hlavního obsahu (ne menu/footer)
✅ Nejdůležitější odstavec (nejdelší = obvykle hlavní)
✅ Filtrování spam textu (cookies, newsletter)
✅ Intro + hlavní obsah = kompletní kontext

**Výsledek:** Přesnější kategorie s nižšími náklady

---

## MĚSÍČNÍ NÁKLADY (odhad)

**Scénář: 50 stránek/den**

**PŘED:**
- 50 req/den × 30 dní = 1500 req/měsíc
- 1500 × $0.00255 = **$3.83/měsíc**

**PO:**
- 50 req/den × 30 dní = 1500 req/měsíc
- 1500 × $0.00152 = **$2.28/měsíc**

**💰 Měsíční úspora: $1.55 (40%)**

---

## TECHNICKÉ DETAILY

### Content Extraction Priority
```javascript
1. <main>               // Sémantický hlavní obsah
2. <article>            // Článek
3. [role="main"]        // ARIA role
4. .content             // Běžná třída
5. .post-content        // Blog post
6. .article-content     // Článek
7. #content             // ID content
8. body                 // Fallback
```

### Paragraph Filtering
```javascript
- Min délka: 100 znaků
- Exclude: /cookie|subscribe|newsletter|sign up/i
- Sort by: length DESC
- Pick: longest = main paragraph
```

### Final Assembly
```javascript
intro (1000) + separator (\n\n) + main (400-500) = 1500 max
```

---

## MONITORING

**Sleduj kvalitu:**
```bash
wrangler tail
```

**Pokud kategorizace selhává:**
1. Zkontroluj délku textu v DevTools
2. Zobraz extrahovaný text v console
3. Uprav content selectors pro daný web
