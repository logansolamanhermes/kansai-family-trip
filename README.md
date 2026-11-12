# 10天9夜「日日有高潮」 · 關西家族自駕計劃書

Interactive 10-day / 9-night Kansai winter itinerary (Dec 13–22, 2026): two travellers aged 60+, a sixth family member joining on 12/18, two onsen ryokan with 一泊二食, and two 4-bedroom house bases (Kyoto 12/14–17, Osaka 12/19–21).

**Live:** https://logansolamanhermes.github.io/kansai-family-trip/

## Pages
- `index.html` — main itinerary plus embedded packing checklist: 10 day cards, a 10-row "日日有高潮" highlight table with star ratings, a 4-bedroom Airbnb area-selection panel (Kyoto/Osaka districts + 4 booking filters), per-item checkboxes, notes, booking tracker, budget table, search/filters, handwriting fields and 31 packing checkboxes.
- `booking-templates.html` — Japanese / English copy-paste letters with one-click copy (retained from the previous version).

## Features
- Route: KIX → Tajiri morning market → Amanohashidate onsen → Ine → Kyoto base (Nara / Uji day trips) → Arima onsen → Kobe → Osaka base (Wakayama day trip) → Rinku Outlets → KIX. "先遠後近", no backtracking, no daily luggage moves.
- Budget panel with planned vs actual per-day spend, weather contingency and budget-freeze rules (category totals unchanged).
- Search, category filters, dark mode, print, JSON export/import, reset.
- All state is stored in each visitor's browser `localStorage` under `kansai-2026-family-trip-v7`.

## Notes
- State is per-browser / per-device, not shared between family members. Use the JSON export/import buttons to pass a filled-in plan around. The packing checklist lives in the same page and shares its state; "只列印打包清單" prints only that section.
- `.nojekyll` disables Jekyll processing on GitHub Pages.
- Vehicle is specified as **Toyota Sienna** throughout. Airbnb parking clearance uses 5.3m × 1.97m as the minimum to also cover GranAce / Odyssey.
- The retained `booking-templates.html` and the legacy f1–f29 audit flags describe the earlier "海陸大縱走" route (Wakayama → Ise, Wadakin, Taiko-no-yu). They are kept as requested but no longer describe the current itinerary; the page's audit panel states which checks still apply.
- This is a public repository: anyone with the URL can view the pages and their source.
