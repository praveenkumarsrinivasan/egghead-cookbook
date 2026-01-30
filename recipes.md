---
layout: page
title: Recipes
permalink: /recipes/
nav: true
nav_order: 2
---

Browse by category:

- [Lamb](/recipes/lamb/)
- [Beef](/recipes/beef/)
- [Pork](/recipes/pork/)
- [Chicken](/recipes/chicken/)
- [Seafood](/recipes/seafood/)
- [Vegetarian](/recipes/vegetarian/)
- [Sides](/recipes/sides/)

## All recipes

{% assign recipe_pages = site.pages | where_exp: "p", "p.dir contains '/recipes/'" | where_exp: "p", "p.name != 'index.md'" | sort: "title" %}
{% if recipe_pages.size > 0 %}
<ul class="recipe-index">
  {% for recipe in recipe_pages %}
    {% assign parts = recipe.dir | split: "/" %}
    {% assign category = parts[2] | capitalize %}
    <li>
      <a href="{{ recipe.url }}">{{ recipe.title }}</a> ({{ category }})
    </li>
  {% endfor %}
</ul>
{% else %}
No recipes yet.
{% endif %}
