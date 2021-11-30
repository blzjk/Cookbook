from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .form import MySignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = MySignupForm(request.POST)
        print('NIE POSZŁO!!!')
        if form.is_valid():
            print('ZAREJESTROWANO HURRA')
            user = form.save()

    form = MySignupForm()
    return render(
        request=request,
        template_name='users/register.html',
        context={
            'form': form
        }
    )
#dekorator sprawdzający czy użytkownik jest zalogowany
@login_required
def panel(request):
    return render(
        request,
        'users/panel.html'
    )


def user_login(request):
    # odebranie formularza
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            print(user)
            # sprawdzanie czy użytkownik został znaleziony
            if user is not None:
                login(request, user)

    form = AuthenticationForm()
    return render(
        request=request,
        template_name='users/login.html',
        context={
            'form': form
        }
    )
