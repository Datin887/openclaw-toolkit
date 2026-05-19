#!/usr/bin/env python3
"""
nemotron_vision.py — Analyze images via Nemotron-Omni on OpenRouter.

Usage:
    python3 nemotron_vision.py <image_path> "<prompt>" [--lang ru] [--max-tokens 1000]

Examples:
    python3 nemotron_vision.py chart.png "Describe this chart" --lang ru
    python3 nemotron_vision.py screenshot.png "Extract all text"
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path


MODEL = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("Error: OPENROUTER_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    return key


def encode_image(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return base64.b64encode(p.read_bytes()).decode()


def analyze(image_path: str, prompt: str, lang: str = "en", max_tokens: int = 1000) -> str:
    api_key = get_api_key()
    img_b64 = encode_image(image_path)

    if lang.lower() in ("ru", "russian", "русский"):
        prompt = f"{prompt}\n\nAnswer in Russian."

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
                ],
            }
        ],
        "max_tokens": max_tokens,
        "reasoning": {"enabled": False},
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )

    try:
        resp = urllib.request.urlopen(req, timeout=120)
        result = json.loads(resp.read())
        content = result["choices"][0]["message"].get("content", "")
        usage = result.get("usage", {})
        print(f"[tokens: {usage.get('prompt_tokens', '?')} in / {usage.get('completion_tokens', '?')} out]\n")
        return content
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"API error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Analyze images via Nemotron-Omni")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("prompt", help="Analysis prompt")
    parser.add_argument("--lang", default="en", help="Response language (en/ru)")
    parser.add_argument("--max-tokens", type=int, default=1000, help="Max output tokens")
    args = parser.parse_args()

    result = analyze(args.image, args.prompt, args.lang, args.max_tokens)
    print(result)


if __name__ == "__main__":
    main()
