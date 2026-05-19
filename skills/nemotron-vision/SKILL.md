---
name: nemotron-vision
description: "Analyze images and screenshots using the Nemotron-Omni vision model. Use when the user sends an image and asks to describe, analyze, or extract information from it. Supports charts, diagrams, UI screenshots, photos, and documents. Triggers on: analyze image, describe screenshot, what's in this image, recognize photo, extract data from chart, OCR image."
---

# Nemotron Vision

Analyze images using the `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` model via OpenRouter.

## Model Info

- **Model ID:** `openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- **Context:** 256K tokens
- **Capabilities:** Text + image understanding
- **Cost:** Free on OpenRouter

## Quick Start

Use the `image` tool with the model override:

```
image tool:
  image: <path or media URL>
  prompt: <what to analyze>
  model: openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

## Input Formats

The model accepts:
- **Local file paths** — e.g. `/home/aiuser/.openclaw/workspace/screenshot.png`
- **Media URLs** — e.g. `media://inbound/image---<id>.png`
- **Base64 data URIs** — `data:image/png;base64,...`

## Prompting Tips

- Be specific: "Extract all text from this image" vs "What's in this image?"
- For charts: "Describe the chart. What are the exact values, labels, and trends?"
- For UI screenshots: "Describe the UI layout. List all visible elements and their positions."
- For documents: "Extract all text preserving the original structure."
- Request language: "Answer in Russian" / "Answer in English"

## Direct API (Advanced)

For batch processing or custom workflows, use `scripts/nemotron_vision.py`:

```bash
python3 scripts/nemotron_vision.py <image_path> "Describe this image" [--lang ru]
```

## Examples

**Chart analysis:**
```
image: chart.png
prompt: Describe this chart in detail. What data is shown? What are the exact values, labels, and trends? Answer in Russian.
model: openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

**Screenshot OCR:**
```
image: screenshot.png
prompt: Extract all text from this screenshot. Preserve the original structure and formatting.
model: openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

**Photo description:**
```
image: photo.jpg
prompt: Describe this photo in detail. What objects, people, and scenes are visible?
model: openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

## Notes

- Reasoning is auto-disabled for image analysis (prevents garbled output)
- For best results, use clear, high-resolution images
- The model supports both English and Russian
- If `image` tool returns garbled text, retry with a more specific prompt
