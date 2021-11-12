from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .form import MyForm

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user = form.save()

    form = MyForm()
    return render(request=request, template_name='users/register.html',
                  context={
                      'form': form
                  })
