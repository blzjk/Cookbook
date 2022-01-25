from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .form import MySignupForm, RecipyForm, LoginForm, IngredientsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from recipes.models import Ingredients


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = MySignupForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            # messages.success(request, 'Konto użytkownika: ' + str(user) + ' zostało utworzone.')
            return render(
                request, 'users/register_done.html', {'user' : user}
            )
    form = MySignupForm()
    return render(
        request=request,
        template_name='users/register.html',
        context={
            'form': form
        }
    )


# dekorator sprawdzający czy użytkownik jest zalogowany
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipyForm(request.POST, request.FILES)
        recipe = form.save(commit=False)
        recipe.author = request.user
        messages.success(request, 'Dodałeś nowy przepis.')

        recipe.save()
    form = RecipyForm()
    return render(
        request,
        'users/add.html',
        {
            'form': form
        }
    )


def user_login(request):
    # odebranie formularza
    if request.method == 'POST':
        messages.success(request, 'Przepis został poprawnie dodany.')
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            # sprawdzanie czy użytkownik został znaleziony
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nierawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

    form = AuthenticationForm()

    return render(
        request=request,
        template_name='users/login.html',
        context={
            'form': form
        }
    )


def user_logout(request):
    logout(request)
    return redirect("/uzytkownik/logowanie")


@login_required
def add_ingredient(request):
    if request.method == 'POST':
        messages.success(request, 'Dodałeś nowy składnik.')
        form = IngredientsForm(request.POST, request.FILES)
        ingredient = form.save(commit=False)
        ingredient.save()
    form = IngredientsForm()
    return render(
        request,
        'users/add_ingredient.html',
        {
            'form': form,
        }
    )




