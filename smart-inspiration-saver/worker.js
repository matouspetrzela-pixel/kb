const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, x-api-key",
  "Content-Type": "application/json"
};

export default {
  async fetch(request, env) {

    // ✅ CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    // ✅ Povolen jen POST
    if (request.method !== "POST") {
      return new Response(
        JSON.stringify({ error: "Method Not Allowed" }),
        { status: 405, headers: CORS_HEADERS }
      );
    }

    // ✅ Auth přes x-api-key
    const apiKey = request.headers.get("x-api-key");
    if (!apiKey || apiKey !== env.AUTH_TOKEN) {
      return new Response(
        JSON.stringify({ error: "x-api-key header is required" }),
        { status: 401, headers: CORS_HEADERS }
      );
    }

    // ✅ Parse body
    let data;
    try {
      data = await request.json();
    } catch {
      return new Response(
        JSON.stringify({ error: "Invalid JSON" }),
        { status: 400, headers: CORS_HEADERS }
      );
    }

    const text = `${data.title || ""} ${data.url || ""}`.toLowerCase();

    // ✅ Keyword-based mapování kategorií
    const rules = [
      { category: "AI v praxi", keywords: ["ai", "artificial intelligence", "llm", "machine learning"] },
      { category: "Workshopy", keywords: ["workshop", "seminar", "training", "školení"] },
      { category: "Copilot", keywords: ["copilot", "github copilot", "microsoft copilot"] },
      { category: "Coding", keywords: ["code", "programming", "javascript", "python", "github"] },
      { category: "Prezentace", keywords: ["presentation", "slides", "pitch", "deck"] },
      { category: "LinkedIn content", keywords: ["linkedin", "post", "personal brand"] },
      { category: "Automatizace", keywords: ["automation", "make.com", "zapier", "workflow"] },
      { category: "Inspirace", keywords: ["inspiration", "idea", "thought", "creativity"] }
    ];

    let category = "Nezařazeno";

    for (const rule of rules) {
      if (rule.keywords.some(k => text.includes(k))) {
        category = rule.category;
        break;
      }
    }

    return new Response(
      JSON.stringify({ category }),
      { headers: CORS_HEADERS }
    );
  }
};
