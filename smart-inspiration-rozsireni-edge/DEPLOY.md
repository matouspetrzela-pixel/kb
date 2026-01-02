# 🚀 DEPLOYMENT GUIDE - Smart Inspiration Saver

## BEZPEČNOSTNÍ ARCHITEKTURA

```
Extension (žádný API key) → Cloudflare Worker → Anthropic API
                           (API key v secrets)
```

✅ API key NIKDY není v extension
✅ Rate limiting: 50 requestů/den/IP
✅ Auth token ochrana
✅ Cloudflare free tier

---

## 1. INSTALACE CLOUDFLARE WRANGLER

```bash
npm install -g wrangler
```

Nebo přes npx (bez instalace):
```bash
npx wrangler login
```

---

## 2. PŘIHLÁŠENÍ K CLOUDFLARE

```bash
wrangler login
```

Otevře se prohlížeč → přihlas se k Cloudflare účtu (zdarma)

---

## 3. NASTAVENÍ SECRETS

**a) Anthropic API klíč:**
```bash
wrangler secret put ANTHROPIC_API_KEY
```
Zadej: `sk-ant-api03-...`

**b) Auth token (vytvoř vlastní náhodný string):**
```bash
wrangler secret put AUTH_TOKEN
```
Zadej např: `muj-super-tajny-token-abc123xyz`

---

## 4. DEPLOY WORKER

```bash
wrangler deploy
```

**Výstup:**
```
Published smart-inspiration-saver (1.23s)
  https://smart-inspiration-saver.tvoje-subdomena.workers.dev
```

**Zkopíruj URL!**

---

## 5. KONFIGURACE EXTENSION

Uprav soubor `background.js`:

```javascript
// Řádek 2: Nahraď URL z předchozího kroku
const WORKER_URL = 'https://smart-inspiration-saver.tvoje-subdomena.workers.dev';

// Řádek 3: Nastav STEJNÝ token jako v kroku 3b
const AUTH_TOKEN = 'muj-super-tajny-token-abc123xyz';
```

---

## 6. NAČTENÍ EXTENSION DO EDGE

1. Otevři Edge: `edge://extensions/`
2. Zapni "Developer mode"
3. Klikni "Load unpacked"
4. Vyber složku: `C:\kb\smart-inspiration-saver`

---

## 7. TEST

1. Otevři libovolnou stránku
2. Klikni na ikonu extension
3. Klikni "Uložit aktuální stránku"
4. **Stránka se uloží a automaticky zařadí do kategorie!**

---

## 🔒 BEZPEČNOSTNÍ KONTROLA

✅ API klíč je POUZE v Cloudflare secrets (šifrovaný)
✅ Extension neobsahuje žádný API klíč
✅ Auth token chrání worker před zneužitím
✅ Rate limiting: max 50 requestů/den/IP
✅ CORS ochrana

---

## 💰 NÁKLADY

**Cloudflare Worker:**
- Free tier: 100,000 requestů/den
- Tvoje použití: ~10-50 requestů/den
- **= ZDARMA navždy**

**Anthropic API:**
- Claude Sonnet: ~$0.003/request (50 tokenů)
- 50 requestů/den = ~$0.15/den = $4.50/měsíc
- (Reálně méně, když neukládáš 50 stránek denně)

---

## 🛠️ TROUBLESHOOTING

**Worker vrací 401 Unauthorized:**
- Zkontroluj že AUTH_TOKEN v `background.js` odpovídá tokenu v Cloudflare secrets

**Worker vrací 500 error:**
- Zkontroluj že ANTHROPIC_API_KEY je správně nastavený: `wrangler secret put ANTHROPIC_API_KEY`

**Extension se nenačte:**
- Zkontroluj že ikony existují v `icons/` složce
- Restartuj Edge

**Kategorizace nefunguje:**
- Otevři DevTools (F12) v popup.html
- Podívej se na Console errors
- Zkontroluj že WORKER_URL je správně nastavená

---

## 🔄 ZMĚNA AUTH TOKENU

Kdykoliv můžeš změnit auth token:

```bash
wrangler secret put AUTH_TOKEN
# Zadej nový token

wrangler deploy
# Redeploy worker
```

Pak uprav `background.js` s novým tokenem a reload extension.

---

## 📊 MONITORING

Zobraz statistiky workeru:
```bash
wrangler tail
```

Sleduj requesty v reálném čase.

---

**Hotovo! Extension je plně zabezpečený a funkční.**
