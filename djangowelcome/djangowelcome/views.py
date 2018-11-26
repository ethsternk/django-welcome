from django.shortcuts import render
from django.http import HttpResponse
from djangowelcome.models import Recipe, Author


def all_recipes(request):
    results = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'data': results})


def recipe(request, recipe_id):
    results = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe.html', {'data': results})


def author(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {'data': {
        'author': author,
        'recipes': recipes,
    }})
