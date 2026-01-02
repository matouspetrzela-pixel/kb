// Category mapping
const CATEGORY_MAP = {
  "Politika": "Inspirace"
};

function normalizeCategory(category) {
  return CATEGORY_MAP[category] || category || "Inspirace";
}

// UI elementy
const savePageBtn = document.getElementById('savePageBtn');
const mainStatus = document.getElementById('mainStatus');
const savedList = document.getElementById('savedList');
const categoriesFilter = document.getElementById('categoriesFilter');

// Kategorie
const CATEGORIES = [
  'Vše',
  'AI v praxi',
  'Workshopy',
  'Copilot',
  'Coding',
  'Prezentace',
  'Politika',
  'LinkedIn content',
  'Automatizace'
];

let activeFilter = 'Vše';

// Inicializace
initCategoriesFilter();
loadSavedPages();

// Filter kategorie
function initCategoriesFilter() {
  categoriesFilter.innerHTML = CATEGORIES.map(cat => `
    <div class="category-chip ${cat === 'Vše' ? 'active' : ''}" data-category="${cat}">
      ${cat}
    </div>
  `).join('');

  categoriesFilter.addEventListener('click', (e) => {
    if (e.target.classList.contains('category-chip')) {
      document.querySelectorAll('.category-chip').forEach(chip => {
        chip.classList.remove('active');
      });
      e.target.classList.add('active');
      activeFilter = e.target.dataset.category;
      loadSavedPages();
    }
  });
}

// Uložení aktuální stránky
savePageBtn.addEventListener('click', async () => {
  savePageBtn.disabled = true;
  showStatus(mainStatus, 'Ukládám a kategorizuji...', 'success');

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Získej obsah stránky
    const [result] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        // Priorita: hlavní obsahové elementy (ne header/footer/nav)
        const contentSelectors = [
          'main',
          'article',
          '[role="main"]',
          '.content',
          '.post-content',
          '.article-content',
          '#content'
        ];

        let contentElement = null;
        for (const selector of contentSelectors) {
          contentElement = document.querySelector(selector);
          if (contentElement) break;
        }

        // Fallback na body pokud nenajdeme hlavní obsah
        let rawText = (contentElement || document.body).innerText || '';

        // Sanitizace
        rawText = rawText
          .replace(/\s+/g, ' ')
          .replace(/\n\s*\n/g, '\n')
          .trim();

        // SÉMANTICKÉ KRÁCENÍ:
        // 1. Prvních 1000 znaků (úvod, kontext)
        const intro = rawText.substring(0, 1000);

        // 2. Najdi nejdůležitější odstavec z dalších 2000 znaků
        const restText = rawText.substring(1000, 3000);
        const paragraphs = restText
          .split(/\n+/)
          .filter(p => p.length > 100)  // Ignoruj krátké řádky
          .filter(p => !p.match(/cookie|subscribe|newsletter|sign up/i)); // Ignoruj spam

        // Vyber nejdelší odstavec (obvykle hlavní obsah)
        const mainParagraph = paragraphs.sort((a, b) => b.length - a.length)[0] || '';

        // Kombinuj: intro + hlavní odstavec (max ~1500 znaků)
        const finalText = (intro + '\n\n' + mainParagraph).substring(0, 1500);

        return {
          title: document.title.trim(),
          text: finalText
        };
      }
    });

    const pageData = {
      title: result.result.title,
      url: tab.url,
      text: result.result.text,
      timestamp: new Date().toISOString()
    };

    // Pošli na background pro kategorizaci
    chrome.runtime.sendMessage(
      { action: 'categorize', data: pageData },
      (response) => {
        if (response.error) {
          showStatus(mainStatus, 'Chyba: ' + response.error, 'error');
        } else {
          showStatus(mainStatus, `Uloženo do: ${response.category}`, 'success');
          loadSavedPages();
        }
        savePageBtn.disabled = false;
      }
    );
  } catch (error) {
    showStatus(mainStatus, 'Chyba: ' + error.message, 'error');
    savePageBtn.disabled = false;
  }
});

// Načtení uložených stránek
async function loadSavedPages() {
  const { pages = [] } = await chrome.storage.local.get('pages');

  if (pages.length === 0) {
    savedList.innerHTML = '<p style="text-align:center;color:#999;font-size:13px;">Zatím žádné uložené stránky</p>';
    return;
  }

  // Filtr podle kategorie
  let filtered = pages;
  if (activeFilter !== 'Vše') {
    filtered = pages.filter(p => p.category === activeFilter);
  }

  // Seřaď podle data (nejnovější první)
  filtered.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  if (filtered.length === 0) {
    savedList.innerHTML = '<p style="text-align:center;color:#999;font-size:13px;">Žádné stránky v této kategorii</p>';
    return;
  }

  savedList.innerHTML = filtered.map(page => {
    const finalCategory = normalizeCategory(page.category);
    return `
      <div class="saved-item" data-url="${escapeHtml(page.url)}">
        <button class="delete-btn" data-id="${page.id}" title="Smazat">🗑️</button>
        <div class="title">${escapeHtml(page.title)}</div>
        <div class="category">${escapeHtml(finalCategory)}</div>
        <div class="url">${escapeHtml(page.url)}</div>
      </div>
    `;
  }).join('');

  // Kliknutí otevře URL
  savedList.querySelectorAll('.saved-item').forEach(item => {
    item.addEventListener('click', (e) => {
      if (!e.target.classList.contains('delete-btn')) {
        chrome.tabs.create({ url: item.dataset.url });
      }
    });
  });
}

// Delete handler (event delegation)
document.addEventListener("click", async (e) => {
  if (e.target.classList.contains("delete-btn")) {
    const id = Number(e.target.dataset.id);

    const { pages = [] } = await chrome.storage.local.get("pages");
    const updated = pages.filter(p => p.id !== id);

    await chrome.storage.local.set({ pages: updated });
    loadSavedPages();
  }
});

// Helper funkce
function showStatus(element, message, type) {
  element.textContent = message;
  element.className = `status show ${type}`;

  setTimeout(() => {
    element.classList.remove('show');
  }, 3000);
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}
