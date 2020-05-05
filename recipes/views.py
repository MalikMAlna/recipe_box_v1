from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from recipes.models import Recipe
from recipes.models import Author
from recipes.forms import RecipeAddForm


# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipeadd(request):
    html = 'recipeaddform.html'

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=data['author']
            )
            
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {'form': form})


def recipe(request, recipe_id):
    data = Recipe.objects.filter(id=recipe_id)
    return render(request, 'recipe.html', {'data': data})


def author(request, author_id):
    data = Author.objects.filter(id=author_id)
    recipes_published = Recipe.objects.all()
    return render(request, 'author.html', {'data': data, 'recipes_published': recipes_published})
