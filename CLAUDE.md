# CLAUDE.md

## Project Overview

EggHead Cookbook — a recipe site for Big Green Egg and kamado-style cooking, built with MkDocs Material theme.

## Site Structure

- `docs/index.md` — Homepage
- `docs/history.md` — History of kamado & Big Green Egg
- `docs/recipes.md` — All recipes index
- `docs/recipes/<category>/` — Recipe categories: beef, chicken, lamb, pork, seafood, sauces-condiments, sides, vegetarian, desserts, techniques
- `docs/assets/images/` — Images used across the site
- `docs/stylesheets/extra.css` — Custom CSS (green theme, logo styling)
- `mkdocs.yml` — Site config, navigation, theme, and extensions

When adding a new page, update `mkdocs.yml` under `nav`.

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

## Deploy

```bash
.venv/bin/mkdocs gh-deploy
```

## Image Generation (Nano Banana)

The project has a nano-image-generator skill at `.agents/skills/nano-image-generator/` that uses Google's Gemini 3 Pro Preview API to generate images.

Requires a `.env` file in the project root with a Gemini API key (`apikey` or `GEMINI_API_KEY`).

```bash
python3 .agents/skills/nano-image-generator/scripts/generate_image.py "<prompt>" --output <path> [--aspect 1:1] [--size 2K]
```

Aspect ratios: `1:1`, `3:2`, `16:9`, `9:16`, etc.
Sizes: `1K`, `2K`, `4K`.
