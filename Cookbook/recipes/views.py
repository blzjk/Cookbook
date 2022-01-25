import random, math

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Recipes, Categories, Rating
from users.form import RatingForm


def index(request):
    return index2(request, 1)


#wyświetlanie 3 ostatnio dodanych przepisów
def index2(request, page):
    maxId = Recipes.objects.latest('id').id
    recipes = Recipes.objects.filter(
        id__lte = maxId - ((page-1))*3,
        id__gt = maxId - 3 - ((page-1)*3)
    )
    #wyświetlanie przepisu ostatnio dodanego na samej górze
    recipes = recipes.order_by('-id')
    #pobranie ilości wszystkich przepisów aby obliczyć ilość stron potrzebnych do wyświetlenia 3 przepisów na stronie
    count = Recipes.objects.all().count()
    pagecount = math.ceil(count/3)
    dane = {
        'recipes': recipes,
        'pagecount': range(pagecount),
    }
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
        avg = Rating.objects.get(id=recipe_user)
        return render(request, 'recipe.html', {
            'recipe': recipe_user,
            'rating': avg,
        })
    except Recipes.DoesNotExist:
        return render(request, '404.html')
    except Rating.DoesNotExist:
        newRating = Rating(id=recipe_user, avg=0, count=0)
        newRating.save()
        return render(request, 'recipe.html', {
            'recipe': recipe_user,
            'rating': newRating,
        })


def search(request):
    if 'searched' in request.GET:
        searched = request.GET['searched']
    else:
        searched = False
    allRecipes = Recipes.objects.filter(content__icontains=searched)
    dane = {'recipes': allRecipes}
    return render(request, 'search.html', dane)

@login_required
def panel(request):
    recipes = Recipes.objects.all()
    dane = {'recipes': recipes}
    return render(request, 'panel.html', dane)

@login_required
def rateRecipe(request):
    if(request.method == 'POST'):
        form = RatingForm(request.POST)
        if(form.is_valid()):
            recipes = Recipes.objects.get(id = form.cleaned_data['recipeId'])
            rating = Rating.objects.get(id = recipes)
            rating.CalculateNewAverage(form.cleaned_data['rate'])
            rating.save()
            return redirect('przepis', id = recipes.id)
        return redirect('strona', strona=1)
