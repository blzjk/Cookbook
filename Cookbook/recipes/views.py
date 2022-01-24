import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipes, Categories

#wyświetlanych 10 ostatnio dodanych przepisów
def index(request):
    maxId = Recipes.objects.latest('id').id
    recipes = Recipes.objects.filter(
        id__lte = maxId, id__gte = maxId - 10
    )
    dane = {'recipes': recipes}
    return render(request, 'index.html', dane)


def category(request, id):
    category_user = Categories.objects.get(pk=id)
    cat_recipe = Recipes.objects.filter(category=category_user)
    dane = {'recipes': cat_recipe}
    return render(request, 'index.html', dane)


def categories(request):
    categories = Categories.objects.all()
    dane = {'categories': categories}
    return render(request, 'kategorie.html', dane)


def random_recipe(request):
    recipes_all = list(Recipes.objects.all())
    recipes = random.sample(recipes_all, 1)
    dane = {'recipes': recipes}
    return render(request, 'random_recipe.html', dane)


def recipe(request, id):
    try:
        recipe_user = Recipes.objects.get(pk=id)
        return render(request, 'recipe.html', {
            'recipe': recipe_user
        })
    except Recipes.DoesNotExist:
        return render(request, '404.html')


def search(request):
    if 'searched' in request.GET:
        searched = request.GET['searched']
    else:
        searched = False
    allRecipes = Recipes.objects.filter(title__icontains=searched)
    dane = {'recipes': allRecipes}
    return render(request, 'search.html', dane)

@login_required
def panel(request):
    recipes = Recipes.objects.all()
    dane = {'recipes': recipes}
    return render(request, 'panel.html', dane)

