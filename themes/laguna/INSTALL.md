# Laguna Theme for OpenClaw

A beautiful theme from [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet).

## Current Status

⚠️ **Work in progress** — OpenClaw doesn't yet have a native "import from tweakcn" UI button.
The spec exists ([docs](https://docs.openclaw.ai/superpowers/specs/2026-04-22-tweakcn-custom-theme-import-design)),
but it's not implemented yet.

This repo preserves the theme data so it's ready when the feature ships.

## Preview

| Mode | Description |
|------|-------------|
| Light | Warm cream background (`#F5F0E8`), purple accent, Inter font |
| Dark | Deep black background, cyan-blue accent, brutalist shadows |

## How to Install (when OpenClaw supports it)

### Method 1: Via Control UI (future)

1. Open OpenClaw Control UI → Settings → Appearance → Theme
2. Find "Theme link or ID"
3. Paste URL: `https://tweakcn.com/themes/cmpc347ze000204l580xtaqet`
4. Choose mode: Light / Dark / System

### Method 2: Manual CSS injection (advanced)

If you want to apply it right now, you can inject the CSS manually:

1. Copy `theme.css` to your OpenClaw webchat host
2. Add to your page:

```html
<link rel="stylesheet" href="path/to/theme.css">
```

Or inject via browser console / extension.

### Method 3: Agent-driven

Ask your OpenClaw agent:

> «Apply the Laguna theme from the openclaw-toolkit repo»

The agent will read `theme.json` and apply the CSS variables.

## Included Files

| File | Purpose |
|------|---------|
| `theme.json` | Original tweakcn JSON payload (source of truth) |
| `theme.css` | Converted CSS custom properties (light + dark) |

## Theme Details

**Fonts:** Inter, JetBrains Mono, Georgia
**Radius:** 2rem
**Light Primary:** Purple (`oklch(0.6268 0.2325 303.9004)`)
**Dark Primary:** Cyan-blue (`oklch(0.5739 0.1347 241.4036)`)
**Shadows:** Brutalist hard shadows (4px offset)
