from . import  views
from django.urls import path

urlpatterns = [
    path('rejestracja', views.register, name='rejestracja')
]