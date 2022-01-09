from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .form import MySignupForm, RecipyForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = MySignupForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Konto użytkownika: ' + str(user) + ' zostało utworzone.')
            return redirect("/uzytkownik/logowanie")
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
def panel(request):
    if request.method == 'POST':
        form = RecipyForm(request.POST, request.FILES)
        recipe = form.save(commit=False)
        recipe.author = request.user
        print(request.user)

        recipe.save()
        # if form.is_valid():
        #     print("HELLO!!!!!!!!!!!")
        #     form.save()
        #     return redirect('/')
    form = RecipyForm()
    return render(
        request,
        'users/panel.html',
        {
            'form': form
        }
    )


def user_login(request):
    # odebranie formularza
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            # sprawdzanie czy użytkownik został znaleziony
            if user is not None:
                login(request, user)
                return redirect("/uzytkownik/panel")


    form = AuthenticationForm()

    return render(
        request=request,
        template_name='users/login.html',
        context={
            'form': form
        }
    )


def logout_view(request):
    logout(request)
    return redirect("/uzytkownik/logowanie")


