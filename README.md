# 🛠️ OpenClaw Toolkit

> Modular collection of skills, scripts, and configs for [OpenClaw](https://github.com/openclaw/openclaw) — an open-source AI agent platform.

**[Русский](README.ru.md)**

---

## 📦 What's Inside

### Skills

| Skill | Description | Install |
|-------|-------------|---------|
| **browser-cdp** | Headless browser via CDP (Chrome DevTools Protocol). Navigation, screenshots, JS execution, clicks, form filling. No GUI needed — perfect for servers. [Details ↓](#browser-cdp) | [SKILL.md](skills/browser-cdp/SKILL.md) |
| **nemotron-vision** | Multimodal image analysis via Nemotron-Omni. Analyze screenshots, charts, photos, documents. Extract text, describe visuals, read diagrams. [Details ↓](#nemotron-vision) | [SKILL.md](skills/nemotron-vision/SKILL.md) |

### Themes

| Theme | Description | Install |
|-------|-------------|---------|
| **Laguna** | Warm cream + purple (light) / deep black + cyan (dark). Inter font, brutalist shadows. From [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet). [Details ↓](#laguna-theme) | [INSTALL.md](themes/laguna/INSTALL.md) |

---

## 🚀 Quick Install

### Option 1: Via Agent (recommended)

Ask your OpenClaw agent:

> «Clone `https://github.com/Datin887/openclaw-toolkit.git`, list the available skills, and install the ones I need.»

The agent will figure it out.

### Option 2: Manual

```bash
# 1. Clone
git clone https://github.com/Datin887/openclaw-toolkit.git

# 2. Copy the skill to your plugin-skills directory
cp -r openclaw-toolkit/skills/browser-cdp ~/.openclaw/plugin-skills/

# 3. Register the skill in OpenClaw config
# Add to skills.entries and skills.load.extraDirs (see skill docs)

# 4. Restart gateway
openclaw gateway restart
```

---

## 📋 Skills

### browser-cdp

**Headless browser automation via Chrome DevTools Protocol.**

**Features:**
- 🌐 Navigate to URLs
- 📸 Take screenshots
- ⚡ Execute JavaScript
- 🖱️ Click elements
- ✏️ Fill forms
- 📄 Extract page content
- 🔄 Manage tabs

**Requirements:**
- Chromium headless as a systemd service (port 9222)
- Python package: `websocket-client`

**Quick start:**
```bash
# Start the browser
sudo systemctl start chromium-headless

# Navigate
python3 scripts/browser_cdp.py navigate "https://example.com"

# Screenshot
python3 scripts/browser_cdp.py screenshot /tmp/screenshot.png

# Execute JS
python3 scripts/browser_cdp.py evaluate "document.title"
```

**Full docs:** [skills/browser-cdp/SKILL.md](skills/browser-cdp/SKILL.md)

### nemotron-vision

**Multimodal image analysis via Nemotron-Omni (free on OpenRouter).**

**Features:**
- 📊 Chart & graph analysis — extract values, labels, trends
- 📸 Photo description — objects, scenes, people
- 📄 Document OCR — extract text preserving structure
- 🖥️ UI screenshot analysis — describe layouts and elements

**Model:** `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (256K context)

**Quick start:**
```bash
python3 scripts/nemotron_vision.py chart.png "Describe this chart" --lang ru
```

Or via `image` tool with model override.

**Full docs:** [skills/nemotron-vision/SKILL.md](skills/nemotron-vision/SKILL.md)

---

## 🎨 Themes

### Laguna Theme

A beautiful theme from [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet).

| Mode | Description |
|------|-------------|
| Light | Warm cream background, purple accent, Inter font |
| Dark | Deep black background, cyan-blue accent, brutalist shadows |

See [INSTALL.md](themes/laguna/INSTALL.md) for manual options.

**Files:**
- `themes/laguna/theme.json` — original tweakcn payload
- `themes/laguna/theme.css` — converted CSS custom properties

---

## 📁 Structure

```
openclaw-toolkit/
├── README.md              ← You are here (English)
├── README.ru.md           ← Russian version
├── LICENSE                ← MIT License
│
├── skills/                ← OpenClaw agent skills
│   ├── browser-cdp/       ← Headless browser automation via CDP
│   │   ├── SKILL.md       ← Skill documentation
│   │   └── scripts/
│   │       └── browser_cdp.py   ← CDP helper (navigate, screenshot, evaluate JS)
│   └── nemotron-vision/   ← Multimodal image analysis via Nemotron-Omni
│       ├── SKILL.md       ← Skill documentation
│       └── scripts/
│           └── nemotron_vision.py  ← CLI for image analysis (charts, photos, OCR)
│
├── themes/                ← Control UI themes
│   └── laguna/            ← Laguna theme from tweakcn.com
│       ├── theme.json     ← Original tweakcn payload (source of truth)
│       ├── theme.css      ← Converted CSS custom properties (light + dark)
│       └── INSTALL.md     ← Installation instructions
│
├── scripts/               ← Utility scripts (agent status, collectors, etc.)
├── configs/               ← Config templates and examples
└── docs/                  ← Additional documentation
```

### Directory Descriptions

| Directory | Purpose |
|-----------|---------|
| `skills/` | OpenClaw agent skills — each subfolder is a self-contained skill with `SKILL.md` and optional scripts |
| `themes/` | Control UI themes — JSON/CSS themes for OpenClaw webchat interface |
| `scripts/` | Standalone utility scripts (agent status, log collectors, helpers) |
| `configs/` | Configuration templates and examples for OpenClaw setup |
| `docs/` | Additional documentation, guides, and notes |

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a PR. Skills, scripts, and configs are welcome.

## 📜 License

MIT — do whatever you want. See [LICENSE](LICENSE).
