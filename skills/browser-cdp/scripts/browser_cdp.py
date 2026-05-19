#!/usr/bin/env python3
"""
Browser CDP helper - interact with headless Chromium via Chrome DevTools Protocol.

Usage:
    python3 browser_cdp.py navigate <url>     - Navigate to URL
    python3 browser_cdp.py screenshot <path>   - Take screenshot
    python3 browser_cdp.py evaluate <js>       - Execute JavaScript
    python3 browser_cdp.py content             - Get page HTML
    python3 browser_cdp.py click <selector>    - Click element by CSS selector
    python3 browser_cdp.py fill <selector> <text> - Fill input
    python3 browser_cdp.py tabs                - List all tabs
    python3 browser_cdp.py newtab <url>        - Open new tab
    python3 browser_cdp.py close <tabId>       - Close tab
    python3 browser_cdp.py reload              - Reload current tab
    python3 browser_cdp.py wait <seconds>      - Wait N seconds
"""

import sys, json, time, base64, urllib.request, websocket

CDP_PORT = 9222
CDP_BASE = f"http://127.0.0.1:{CDP_PORT}"


def get_tabs():
    return json.loads(urllib.request.urlopen(f"{CDP_BASE}/json/list").read())


def get_default_tab():
    tabs = get_tabs()
    if not tabs:
        print("No tabs found", file=sys.stderr)
        sys.exit(1)
    # Prefer page type, skip about:blank
    for t in tabs:
        if t.get("type") == "page" and t.get("url", "") != "about:blank":
            return t
    return tabs[0]


def cdp_connect(tab=None):
    tab = tab or get_default_tab()
    ws_url = tab["webSocketDebuggerUrl"]
    return websocket.create_connection(ws_url, timeout=15), tab


def cdp_send(ws, method, params=None, msg_id=1):
    msg = {"id": msg_id, "method": method}
    if params:
        msg["params"] = params
    ws.send(json.dumps(msg))
    return json.loads(ws.recv())


def navigate(url, tab=None):
    ws, tab = cdp_connect(tab)
    resp = cdp_send(ws, "Page.navigate", {"url": url})
    ws.close()
    print(f"Navigating to {url}")
    return tab


def screenshot(path="/tmp/screenshot.png", tab=None):
    ws, tab = cdp_connect(tab)
    resp = cdp_send(ws, "Page.captureScreenshot", {"format": "png", "quality": 80})
    data = resp.get("result", {}).get("data", "")
    if data:
        with open(path, "wb") as f:
            f.write(base64.b64decode(data))
        print(f"Screenshot saved: {path}")
    else:
        print("No screenshot data", file=sys.stderr)
    ws.close()


def evaluate(js, tab=None, await_promise=False):
    ws, tab = cdp_connect(tab)
    params = {"expression": js, "returnByValue": True}
    if await_promise:
        params["awaitPromise"] = True
    resp = cdp_send(ws, "Runtime.evaluate", params)
    val = resp.get("result", {}).get("result", {})
    print(val.get("value", val.get("description", str(val))))
    ws.close()


def get_content(tab=None):
    ws, tab = cdp_connect(tab)
    resp = cdp_send(ws, "Runtime.evaluate", {"expression": "document.documentElement.outerHTML", "returnByValue": True})
    val = resp.get("result", {}).get("result", {}).get("value", "")
    print(val[:50000])  # Limit output
    ws.close()


def click(selector, tab=None):
    js = f"""
    (function() {{
        var el = document.querySelector('{selector}');
        if (el) {{ el.click(); return 'clicked'; }}
        return 'not found';
    }})()
    """
    evaluate(js, tab)


def fill(selector, text, tab=None):
    js = f"""
    (function() {{
        var el = document.querySelector('{selector}');
        if (el) {{
            el.value = '{text}';
            el.dispatchEvent(new Event('change', {{bubbles: true}}));
            return 'filled';
        }}
        return 'not found';
    }})()
    """
    evaluate(js, tab)


def new_tab(url="about:blank"):
    data = urllib.request.urlopen(f"{CDP_BASE}/json/new?{url}").read()
    tab = json.loads(data)
    print(f"New tab: {tab.get('id')} - {tab.get('url')}")
    return tab


def close_tab(tab_id):
    data = urllib.request.urlopen(f"{CDP_BASE}/json/close/{tab_id}").read()
    print(f"Closed tab: {tab_id}")


def reload(tab=None):
    ws, tab = cdp_connect(tab)
    cdp_send(ws, "Page.reload", {"ignoreCache": True})
    ws.close()
    print("Page reloaded")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "navigate" and len(sys.argv) >= 3:
        navigate(sys.argv[2])
    elif cmd == "screenshot" and len(sys.argv) >= 3:
        screenshot(sys.argv[2])
    elif cmd == "screenshot":
        screenshot()
    elif cmd == "evaluate" and len(sys.argv) >= 3:
        evaluate(" ".join(sys.argv[2:]))
    elif cmd == "content":
        get_content()
    elif cmd == "click" and len(sys.argv) >= 3:
        click(sys.argv[2])
    elif cmd == "fill" and len(sys.argv) >= 4:
        fill(sys.argv[2], sys.argv[3])
    elif cmd == "tabs":
        tabs = get_tabs()
        for t in tabs:
            print(f"  {t.get('id')} | {t.get('url', '')[:80]} | {t.get('title', '')[:40]}")
    elif cmd == "newtab" and len(sys.argv) >= 3:
        new_tab(sys.argv[2])
    elif cmd == "newtab":
        new_tab()
    elif cmd == "close" and len(sys.argv) >= 3:
        close_tab(sys.argv[2])
    elif cmd == "reload":
        reload()
    elif cmd == "wait" and len(sys.argv) >= 3:
        time.sleep(float(sys.argv[2]))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
