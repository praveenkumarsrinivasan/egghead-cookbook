# CLAUDE.md

## Project Overview

EggHead Cookbook — a recipe site built with MkDocs Material theme.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build

```bash
.venv/bin/mkdocs build
```

## Serve (local dev)

```bash
.venv/bin/mkdocs serve
```

Opens at http://127.0.0.1:8000 by default.

## Image Generation (Nano Banana)

The project has a nano-image-generator skill at `.agents/skills/nano-image-generator/` that uses Google's Gemini 3 Pro Preview API to generate images.

Requires a `.env` file in the project root with a Gemini API key (`apikey` or `GEMINI_API_KEY`).

```bash
python3 .agents/skills/nano-image-generator/scripts/generate_image.py "<prompt>" --output <path> [--aspect 1:1] [--size 2K]
```

Aspect ratios: `1:1`, `3:2`, `16:9`, `9:16`, etc.
Sizes: `1K`, `2K`, `4K`.
