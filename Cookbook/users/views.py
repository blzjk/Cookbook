from django.shortcuts import render
from .form import MyForm

def register(request):
    form = MyForm()
    return render(request=request, template_name='users/register.html',
                  context={
                      'form': form
                  })
