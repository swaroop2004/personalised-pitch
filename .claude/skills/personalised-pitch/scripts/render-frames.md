# Rendering Excalidraw scenes to PNG frames

Goal: `visuals/scene-NN.excalidraw.json` → `visuals/scene-NN.png` at 1920×1080.

## CRITICAL lesson (verified 2026-08-15)

The `label` sugar accepted by `create_view` is MCP-only. `export_to_excalidraw` and
excalidraw.com **silently drop label sugar AND minimal text elements** (ones missing
width/height/fontFamily/etc.) — you get share links containing only naked rectangles.

Working pipeline:
1. Draw scenes with `create_view` as usual (label sugar OK there) and save the lite
   JSON per scene.
2. Transform lite → full Excalidraw format: every `label` becomes a standalone text
   element, centered on its shape, word-wrapped manually (est. char width ≈
   fontSize × 0.55), with ALL fields populated (angle, seed, version, versionNonce,
   isDeleted, groupIds, boundElements, fontFamily: 1, textAlign, lineHeight: 1.25,
   originalText, baseline...). Standalone lite texts also get the full field set.
   A reference transformer lives at the scratchpad from the first run; rewrite it
   per-run if needed (it's ~80 lines of node).
3. Render WITHOUT share links: Playwright loads excalidraw.com once, then per scene
   injects elements via `localStorage.setItem('excalidraw', JSON.stringify(elements))`
   + `page.reload()`. Faster than share URLs, no upload, no "Loading scene" races.
4. Per scene after reload: `await document.fonts.ready`, wait ~2.5 s, inject CSS to
   hide `.App-menu, .App-toolbar, .layer-ui__wrapper, footer, .Island`, press
   `Shift+1` (zoom to fit), wait ~1.2 s, screenshot 1920×1080.
5. **Read every PNG** and eyeball: labels present, nothing clipped, no UI chrome.

One-time setup: `npm i playwright && npx playwright install chromium` (in scratchpad).

## Gotchas
- If navigating between share URLs instead: hash-only navigation does NOT reload the
  SPA — the old scene stays on canvas and you screenshot the wrong scene. Use the
  localStorage approach.
- Windows PowerShell 5.1 running .ps1 helpers: save scripts as UTF-8 **with BOM** or
  em-dashes/quotes mangle and the parse fails.
- Zoom-to-fit magnifies sparse scenes differently per scene; keep scene content
  footprints similar (~1150×620) for consistent apparent text size across frames.
