# 🛠️ OpenClaw Toolkit

> Modular collection of skills, scripts, and configs for [OpenClaw](https://github.com/openclaw/openclaw) — an open-source AI agent platform.

**[Русский](README.ru.md)**

---

## 📦 What's Inside

### Skills

| Skill | Description | Install |
|-------|-------------|---------|
| **browser-cdp** | Headless browser via CDP (Chrome DevTools Protocol). Navigation, screenshots, JS execution, clicks, form filling. No GUI needed — perfect for servers. [Details ↓](#browser-cdp) | [SKILL.md](skills/browser-cdp/SKILL.md) |

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

---

## 📁 Structure

```
openclaw-toolkit/
├── README.md              ← You are here
├── README.ru.md           ← Russian version
├── LICENSE
├── skills/                ← OpenClaw skills
│   └── browser-cdp/
│       ├── SKILL.md
│       └── scripts/
│           └── browser_cdp.py
├── scripts/               ← Utility scripts
├── configs/               ← Config templates
└── docs/                  ← Documentation
```

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a PR. Skills, scripts, and configs are welcome.

## 📜 License

MIT — do whatever you want. See [LICENSE](LICENSE).
