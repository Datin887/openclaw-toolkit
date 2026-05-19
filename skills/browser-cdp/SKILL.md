---
name: browser-cdp
description: Headless browser automation via CDP (Chrome DevTools Protocol). Use when you need to interact with web pages, take screenshots, execute JavaScript in a browser context, or test web UIs. The browser runs as a systemd service (chromium-headless) on port 9222. Works without GUI — perfect for server environments. Triggers include browser automation, headless browser, CDP, screenshot, navigate, evaluate JS.
---

# Browser CDP

Headless Chromium browser automation via Chrome DevTools Protocol.

## Setup

The browser runs as a systemd service:

```bash
# Check status
sudo systemctl status chromium-headless

# Start/stop/restart
sudo systemctl start chromium-headless
sudo systemctl stop chromium-headless
sudo systemctl restart chromium-headless

# View logs
journalctl -u chromium-headless -f
```

If the service is not running, start it:
```bash
sudo systemctl daemon-reload
sudo systemctl enable chromium-headless
sudo systemctl start chromium-headless
```

## Connection

- **CDP Port**: 9222
- **Endpoint**: `http://127.0.0.1:9222`
- **WebSocket**: `ws://127.0.0.1:9222/devtools/page/<tabId>`

## Quick Operations

### List tabs
```bash
curl -s http://127.0.0.1:9222/json/list | python3 -m json.tool
```

### Navigate to URL
Use the `scripts/browser_cdp.py` helper:
```bash
python3 scripts/browser_cdp.py navigate "https://example.com"
```

### Take screenshot
```bash
python3 scripts/browser_cdp.py screenshot /tmp/screenshot.png
```

### Execute JavaScript
```bash
python3 scripts/browser_cdp.py evaluate "document.title"
```

### Get page content
```bash
python3 scripts/browser_cdp.py content
```

### Click element
```bash
python3 scripts/browser_cdp.py click "#button-id"
```

### Fill input
```bash
python3 scripts/browser_cdp.py fill "#input-id" "text"
```

## Screenshots

Screenshots are saved to `/tmp/` by default. To view them:
1. Copy to workspace: `cp /tmp/screenshot.png ~/.openclaw/workspace/`
2. Use the `image` tool to analyze

## Notes

- The browser runs with `--ignore-certificate-errors` for testing with self-signed certs
- Origin header must be allowed: `--remote-allow-origins=*`
- If CDP returns 403, restart the service
- The `websocket-client` Python package is required (`pip3 install websocket-client --break-system-packages`)
