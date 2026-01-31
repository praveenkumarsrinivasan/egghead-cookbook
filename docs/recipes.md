---
layout: page
title: Recipes
permalink: /recipes/
nav: true
nav_order: 2
---

Browse by category:

- [Lamb](recipes/lamb/)
- [Beef](recipes/beef/)
- [Pork](recipes/pork/)
- [Chicken](recipes/chicken/)
- [Seafood](recipes/seafood/)
- [Sauces/Condiments](recipes/sauces-condiments/)
- [Vegetarian](recipes/vegetarian/)
- [Sides](recipes/sides/)
- [Desserts](recipes/desserts/)
- [Techniques](recipes/techniques/)

## All recipes

{% assign recipe_pages = site.pages | where_exp: "p", "p.dir contains '/recipes/'" | where_exp: "p", "p.name != 'index.md'" | sort: "title" %}
{% if recipe_pages.size > 0 %}
<ul class="recipe-index">
  {% for recipe in recipe_pages %}
    {% assign parts = recipe.dir | split: "/" %}
    {% assign raw_category = parts[2] %}
    {% if raw_category == "sauces-condiments" %}
      {% assign category = "Sauces/Condiments" %}
    {% else %}
      {% assign category = raw_category | capitalize %}
    {% endif %}
    <li>
      <a href="{{ recipe.url }}">{{ recipe.title }}</a> ({{ category }})
    </li>
  {% endfor %}
</ul>
{% else %}
No recipes yet.
{% endif %}
