#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover - optional dependency
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
RECIPES_DIR = DOCS_DIR / "recipes"
MKDOCS_YML = ROOT / "mkdocs.yml"


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def extract_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # YAML front matter (legacy)
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                front = lines[1:i]
                for line in front:
                    if line.strip().startswith("title:"):
                        return _strip_quotes(line.split(":", 1)[1])
                break

    # First H1
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    # Fallback: slug
    return path.stem.replace("-", " ").title()


def load_category_order() -> list[tuple[str, Path]]:
    if not MKDOCS_YML.exists():
        return []

    if yaml is not None:
        data = yaml.safe_load(MKDOCS_YML.read_text(encoding="utf-8")) or {}
        nav = data.get("nav", [])
        for item in nav:
            if isinstance(item, dict) and "Recipes" in item:
                entries = item["Recipes"]
                if isinstance(entries, list):
                    ordered = []
                    for entry in entries:
                        if isinstance(entry, dict):
                            label, rel = next(iter(entry.items()))
                            ordered.append((label, DOCS_DIR / rel))
                    return ordered

    # Fallback: minimal parsing of mkdocs.yml to keep nav order
    lines = MKDOCS_YML.read_text(encoding="utf-8").splitlines()
    in_nav = False
    recipes_indent = None
    ordered: list[tuple[str, Path]] = []

    for line in lines:
        if not in_nav:
            if line.startswith("nav:"):
                in_nav = True
            continue

        if recipes_indent is None:
            stripped = line.lstrip()
            if stripped.startswith("- Recipes:"):
                recipes_indent = len(line) - len(stripped)
            elif line and not line.startswith(" "):
                break
            continue

        if line.strip() == "":
            continue

        indent = len(line) - len(line.lstrip())
        if indent <= recipes_indent:
            break

        stripped = line.strip()
        if stripped.startswith("- ") and ":" in stripped:
            item = stripped[2:]
            label, rel = item.split(":", 1)
            ordered.append((label.strip(), DOCS_DIR / rel.strip()))

    return ordered


def category_entries() -> list[tuple[str, Path]]:
    ordered = load_category_order()
    if ordered:
        return ordered

    # Fallback: alphabetical from folders containing index.md
    categories = []
    for path in sorted(RECIPES_DIR.iterdir()):
        if path.is_dir() and (path / "index.md").exists():
            label = path.name.replace("-", " ").title()
            categories.append((label, path / "index.md"))
    return categories


def list_recipes(category_dir: Path) -> list[tuple[str, Path]]:
    items = []
    for path in sorted(category_dir.glob("*.md")):
        if path.name == "index.md":
            continue
        title = extract_title(path)
        items.append((title, path))

    # Sort by title for stability
    items.sort(key=lambda item: item[0].lower())
    return items


def write_category_index(label: str, index_path: Path) -> None:
    category_dir = index_path.parent
    recipes = list_recipes(category_dir)

    lines = [f"# {label}", ""]
    if recipes:
        for title, path in recipes:
            slug = path.stem + "/"
            lines.append(f"- [{title}]({slug})")
    else:
        lines.append("No recipes yet.")

    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_all_recipes_page(categories: list[tuple[str, Path]]) -> None:
    lines = ["# Recipes", "", "Browse by category:", ""]

    for label, index_path in categories:
        rel_dir = index_path.parent.relative_to(DOCS_DIR)
        lines.append(f"- [{label}]({rel_dir.as_posix()}/)")

    lines += ["", "## All recipes", ""]

    for label, index_path in categories:
        category_dir = index_path.parent
        recipes = list_recipes(category_dir)
        lines.append(f"### {label}")
        lines.append("")
        if recipes:
            for title, path in recipes:
                rel = path.relative_to(DOCS_DIR).with_suffix("")
                lines.append(f"- [{title}]({rel.as_posix()}/)")
        else:
            lines.append("No recipes yet.")
        lines.append("")

    (DOCS_DIR / "recipes.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    categories = category_entries()
    for label, index_path in categories:
        write_category_index(label, index_path)
    write_all_recipes_page(categories)


if __name__ == "__main__":
    main()
