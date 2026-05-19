# Laguna Theme for OpenClaw

A beautiful theme from [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet).

## Preview

| Mode | Description |
|------|-------------|
| Light | Warm cream background (`#F5F0E8`), purple accent, Inter font |
| Dark | Deep black background, cyan-blue accent, brutalist shadows |

## How to Install 

### Method 1: Via Control UI

1. Open OpenClaw Control UI → Settings → Appearance → Theme
2. Find "Theme link or ID"
3. Paste URL: `https://tweakcn.com/themes/cmpc347ze000204l580xtaqet`
4. Choose mode: Light / Dark / System

### Method 2: Manual CSS injection (advanced)

Or, you can inject the CSS manually:

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
