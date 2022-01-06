from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipes, Categories


def index(request):
    # wszystkie = Recipes.objects.all()
    # jeden = Recipes.objects.get(pk=1)
    # cat_name = Categories.objects.get(id=1)
    # null = Recipes.objects.filter(category__isnull=True)
    # zawiera = Recipes.objects.filter(content__icontains='boczek')
    # return HttpResponse(zawiera)
    recipes = Recipes.objects.all()
    dane = {'recipes': recipes}
    return render(request, 'index.html', dane)
    # recipe = Recipes.objects.all()
    # return render(request, 'index.html', {
    #     'recipe': recipe
    # })


def category(request, id):
    category_user = Categories.objects.get(pk=id)
    cat_recipe = Recipes.objects.filter(category=category_user)
    return HttpResponse(cat_recipe)


# def kategories (request, id):
#     kategory_user = Kategories.objects.get(pk=id)
#     kategory_recipe = Recipes.objects.filter(kategory = kategory_user)
#     kategories = Kategories.objects.all()
#     dane = {'kategory_user' : kategory_user,
#             'kategory_recipe' : kategory_recipe,
#             'kategories' : kategories }
#     return render(request, 'kategorie.html', dane)


def categories(request):
    categories = Categories.objects.all()
    dane = {'categories': categories}
    return render(request, 'kategorie.html', dane)


def recipe(request, id):
    try:
        recipe_user = Recipes.objects.get(pk=id)
        return render(request, 'recipe.html', {
            'recipe': recipe_user
        })
    except Recipes.DoesNotExist:
        return render(request, '404.html')

def search(request):
    return render(request, 'szukaj.html')

