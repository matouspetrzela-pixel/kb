// Konfigurace
const WORKER_URL = 'https://smart-inspiration-saver.matous-petrzela.workers.dev';
const AUTH_TOKEN = 'smart-saver-2025-7fA9dK';

// Listener pro zprávy z popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'categorize') {
    categorizePage(request.data).then(sendResponse);
    return true; // Async response
  }
});

// Kategorizace přes Cloudflare Worker
async function categorizePage(pageData) {
  try {
    const response = await fetch(WORKER_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': AUTH_TOKEN
      },
      body: JSON.stringify({
        title: pageData.title,
        url: pageData.url,
        text: pageData.text  // Už je sanitizovaný a limitovaný v popup.js
      })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Worker error');
    }

    const data = await response.json();
    const category = data.category;

    // Ulož stránku (bez plného textu - ušetří storage)
    const savedPage = {
      title: pageData.title,
      url: pageData.url,
      category,
      timestamp: pageData.timestamp,
      id: Date.now()
    };

    const { pages = [] } = await chrome.storage.local.get('pages');
    pages.unshift(savedPage);

    // Ulož max 100 stránek
    if (pages.length > 100) {
      pages.pop();
    }

    await chrome.storage.local.set({ pages });

    return { category, success: true };

  } catch (error) {
    console.error('Chyba při kategorizaci:', error);
    return { error: error.message };
  }
}
