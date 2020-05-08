from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from recipes.models import Recipe
from recipes.models import Author
from recipes.forms import AddRecipeForm
from recipes.forms import AddAuthorForm
from recipes.forms import LoginForm


# Create your views here.

def loginview(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutview(request):
    if request.method == 'GET':
        logout(request)

    return HttpResponseRedirect(reverse('homepage'))


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required
def add_recipe(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
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

    form = AddRecipeForm()

    return render(request, html, {'form': form})


@staff_member_required
def add_author(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})


def recipe(request, recipe_id):
    data = Recipe.objects.filter(id=recipe_id)
    return render(request, 'recipe.html', {'data': data})


def author(request, author_id):
    data = Author.objects.filter(id=author_id)
    recipes_published = Recipe.objects.all()
    return render(request, 'author.html', {'data': data, 'recipes_published': recipes_published})
