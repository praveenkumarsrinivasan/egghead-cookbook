# BGE Cookbook

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_recipes_index.py
mkdocs serve
```

Run `python scripts/generate_recipes_index.py` after adding or renaming recipes to refresh the lists.
Open the local site at the URL shown in the `mkdocs serve` output.

## Deployment

GitHub Actions deploys the site to the `gh-pages` branch.
In your GitHub repo settings, set GitHub Pages to publish from the `gh-pages` branch.
