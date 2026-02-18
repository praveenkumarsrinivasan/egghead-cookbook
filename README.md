# EggHead Cookbook

This repo is set up for MkDocs (Material theme).

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open the local dev server printed by MkDocs (usually http://127.0.0.1:8000).

## Build the site

```bash
mkdocs build
```

## Update the index

1. Edit `docs/index.md`.
2. Save and preview with `mkdocs serve`.
3. If you add a new top-level page, update `mkdocs.yml` under `nav`.

## Deploy

If you use GitHub Pages via MkDocs, run:

```bash
mkdocs gh-deploy
```
