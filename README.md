# 關西冬日海陸盛宴 · 家族旅行計劃書

Interactive 10-day / 9-night Kansai winter itinerary for a family of 6 (Dec 13–22, 2026).

Open the static site: https://logansolamanhermes.github.io/kansai-family-trip/

## Features
- 10 day cards, 42 timeline items with checkboxes and per-day notes
- 12-item booking tracker synced with per-day status dropdowns
- 5 / 6 person toggle (defaults to 6) that updates people-dependent copy
- Search, category filters, dark mode, print, JSON export/import, reset
- All state is stored in each visitor browser localStorage

## Notes
- State is per-browser/per-device, not shared between family members. Use the JSON export/import buttons to pass a filled-in plan around.
- `.nojekyll` is required so GitHub Pages does not run Liquid templating over the `{{N}}` placeholders inside the inline script.
- This is a public repository: anyone with the URL can view the page and its source.
