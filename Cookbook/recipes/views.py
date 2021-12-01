from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes, Kategories


def index(request):
    # wszystkie = Recipes.objects.all()
    # jeden = Recipes.objects.get(pk=1)
    # kat_name = Kategories.objects.get(id=1)
    # null = Recipes.objects.filter(kategory__isnull=True)
    # zawiera = Recipes.objects.filter(content__icontains='boczek')
    # return HttpResponse(zawiera)
    recipes = Recipes.objects.all()
    dane = {'recipes': recipes}
    return render(request, 'index.html', dane)
    # recipe = Recipes.objects.all()
    # return render(request, 'index.html', {
    #     'recipe': recipe
    # })


def kategory(request, id):
    kategory_user = Kategories.objects.get(pk=id)
    kat_recipe = Recipes.objects.filter(kategory=kategory_user)
    return HttpResponse(kat_recipe)


# def kategories (request, id):
#     kategory_user = Kategories.objects.get(pk=id)
#     kategory_recipe = Recipes.objects.filter(kategory = kategory_user)
#     kategories = Kategories.objects.all()
#     dane = {'kategory_user' : kategory_user,
#             'kategory_recipe' : kategory_recipe,
#             'kategories' : kategories }
#     return render(request, 'kategorie.html', dane)


def kategories(request):
    kategories = Kategories.objects.all()
    dane = {'kategories': kategories}
    return render(request, 'kategorie.html', dane)


def recipe(request, id):
    try:
        recipe_user = Recipes.objects.get(pk=id)
        return render(request, 'recipe.html', {
            'recipe': recipe_user
        })
    except Recipes.DoesNotExist:
        return render(request, '404.html')




