from django.shortcuts import render

from recipes.models import Recipe
from recipes.models import Author

# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe(request, recipe_id):
    data = Recipe.objects.filter(id=recipe_id)
    return render(request, 'recipe.html', {'data': data})


def author(request, author_id):
    data = Author.objects.filter(id=author_id)
    recipes_published = Recipe.objects.all()
    return render(request, 'author.html', {'data': data, 'recipes_published': recipes_published})
