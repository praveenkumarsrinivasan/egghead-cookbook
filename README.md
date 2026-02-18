# EggHead Cookbook

A collection of tried-and-tested recipes for the Big Green Egg and kamado-style cooking — from low-and-slow smokes to high-heat sears.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## What's Inside

- **50+ recipes** across beef, chicken, lamb, pork, seafood, sides, desserts, sauces & rubs
- **Techniques** — temperature guides, roasting charts, Big Green Egg process
- **History** — the story of kamado cooking from ancient clay pots to modern ceramics

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 in your browser.

## Build

```bash
mkdocs build
```

## Adding Content

1. Add or edit markdown files under `docs/`.
2. Update `mkdocs.yml` under `nav` if adding a new page.
3. Preview with `mkdocs serve`.

## Deploy

To deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```
