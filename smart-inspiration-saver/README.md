# 💡 Smart Inspiration Saver

**Bezpečné Edge extension pro ukládání webů s AI kategorizací**

## ✨ Funkce

- 🔖 **Uložení stránky jedním kliknutím**
- 🤖 **Automatická AI kategorizace** (Claude Sonnet 4)
- 📁 **8 předdefinovaných kategorií**
- 🔍 **Filtrování podle kategorií**
- 🔒 **Maximální bezpečnost** - API klíč NIKDY není v extension

## 🏗️ Architektura

```
Extension (čistý kód) → Cloudflare Worker → Anthropic API
                       (API key v secrets)
```

## 📂 Kategorie

- AI v praxi
- Workshopy
- Copilot
- Coding
- Prezentace
- Politika
- LinkedIn content
- Automatizace

## 🚀 Quick Start

1. **Deploy Cloudflare Worker:**
   ```bash
   npm install -g wrangler
   wrangler login
   wrangler secret put ANTHROPIC_API_KEY
   wrangler secret put AUTH_TOKEN
   wrangler deploy
   ```

2. **Konfigurace Extension:**
   - Uprav `background.js` - nastav WORKER_URL a AUTH_TOKEN
   - Načti do Edge: `edge://extensions/` → Load unpacked

3. **Použití:**
   - Otevři stránku → Klikni na ikonu → Uložit

📖 **Detailní návod:** `DEPLOY.md`

## 🔒 Bezpečnost

✅ API klíč pouze v Cloudflare secrets (šifrovaný)
✅ Rate limiting: 50 req/den/IP
✅ Auth token ochrana
✅ Žádné citlivé údaje v extension
✅ Open source kód

## 💰 Náklady

- Cloudflare Worker: **FREE** (100k req/den)
- Anthropic API: ~$0.003/request (~$5/měsíc při běžném používání)

## 📝 Licence

MIT
