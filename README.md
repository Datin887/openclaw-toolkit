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
| **fire_copywriting_engine** | High-converting sales copy using proven direct-response techniques. Rewrite marketing text, sales pages, emails, landing pages, ads. Based on Ogilvy, Sugarman, Settle, Kennedy, Carlton and others. [Details ↓](#fire_copywriting_engine) | [SKILL.md](skills/fire_copywriting_engine/SKILL.md) |
| **deep_audience_analysis_premium** | Deep psychological analysis of target audience. Customer personas, pains, fears, desires, JTBD, objections, transformation, marketing angles. 21-section framework. [Details ↓](#deep_audience_analysis_premium) | [SKILL.md](skills/deep_audience_analysis_premium/SKILL.md) |

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

### fire_copywriting_engine

**Fire sales copy using proven direct-response techniques.**

**Features:**
- 🔥 Rewrite dry text into persuasive, converting copy
- 🧠 Psychological profiling — identify pains, fears, desires of target audience
- 📐 AIDA structure — Attention, Interest, Desire, Action
- 💬 Conversational style — talk like a friend, not a corporation
- 🎬 Cinematographic storytelling — show, don't tell
- 📊 Fact-based persuasion — back claims with data and social proof
- ⚡ Killer CTA — uncompromising call to action

**Algorithms:** Sugarman/Bencivenga, Ogilvy, Ben Settle, Haddad/Godin, Kennedy/Bly, Carlton, Makepeace

**Quick start:**
```
Just send your source text and ask to rewrite it as fire copy.
Or trigger with: "огненный текст", "продающий текст", "копирайтинг"
```

**Full docs:** [skills/fire_copywriting_engine/SKILL.md](skills/fire_copywriting_engine/SKILL.md)

### deep_audience_analysis_premium

**Deep psychological analysis of target audience — 21-section framework.**

**Features:**
- 🧠 Deep customer psychology — pains, fears, desires, shame, guilt, envy
- 📐 21-section analysis framework — from persona to marketing conclusions
- 💬 Customer's own language — authentic quotes and internal monologues
- 🎯 JTBD analysis — functional, emotional, social, hidden jobs
- 🚧 Objection handling — what blocks the purchase and why
- ✨ Transformation mapping — before/after customer journey

**Output sections:** Summary, Persona, Psychographics, Core Problem, JTBD, Top-5 Emotions, Top-5 Fears, Relationship Impact, Painful Phrases, Past Solutions, Resistance Points, Ideal Transformation, Post-Transformation Quotes, Myths & Beliefs, Blame Patterns, Sticking Points, What to Let Go, Top-5 Objections, Purchase Triggers, Marketing Conclusions, Hypotheses.

**Quick start:**
```
Provide product info, market, audience segments, competitors, positioning, sales channels, and analysis goal.
Or just describe your product and ask: "Сделай глубокий анализ ЦА"
```

**Full docs:** [skills/deep_audience_analysis_premium/SKILL.md](skills/deep_audience_analysis_premium/SKILL.md)

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
├── README.md              ← You are here
├── README.ru.md           ← Russian version
├── LICENSE
├── skills/                ← OpenClaw skills
│   ├── browser-cdp/
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── browser_cdp.py
│   ├── nemotron-vision/
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── nemotron_vision.py
│   ├── fire_copywriting_engine/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── system_prompt.md
│   └── deep_audience_analysis_premium/
│       ├── SKILL.md
│       └── references/
│           └── system_prompt.md
├── themes/                ← Control UI themes
│   └── laguna/
│       ├── theme.json
│       ├── theme.css
│       └── INSTALL.md
├── scripts/               ← Utility scripts
├── configs/               ← Config templates
└── docs/                  ← Documentation
```

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a PR. Skills, scripts, and configs are welcome.

## 📜 License

MIT — do whatever you want. See [LICENSE](LICENSE).
