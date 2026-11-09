# 關西冬日海陸盛宴 · 家族旅行計劃書

Interactive 10-day / 9-night Kansai winter itinerary for a family of 6 (Dec 13–22, 2026).

**Live:** https://logansolamanhermes.github.io/kansai-family-trip/

## Pages
- `index.html` — main itinerary: 10 day cards, per-item checkboxes, notes, booking tracker, budget table, Day 7 weather Plan A/B switch, search and filters.
- `booking-templates.html` — Japanese / English copy-paste letters (car rental, four restaurants, three hotels, five Day 5 onsen inquiries) with one-click copy.
- `packing-list.html` — printable "3 hard cases / 3 duffels / 6 people" packing checklist with handwriting fields and per-item checkboxes.

## Features
- 6-person locked itinerary; Day 7 Plan A (coastal) / Plan B (inland / stay in Wakayama) switch.
- Budget panel with planned vs actual per-day spend, weather contingency and budget-freeze rules.
- Search, category filters, dark mode, print, JSON export/import, reset.
- All state is stored in each visitor's browser `localStorage`.

## Notes
- State is per-browser / per-device, not shared between family members. Use the JSON export/import buttons to pass a filled-in plan around; the packing list has its own separate state.
- `.nojekyll` disables Jekyll processing on GitHub Pages.
- Vehicle is specified as **Toyota Sienna** throughout.
- This is a public repository: anyone with the URL can view the pages and their source.
