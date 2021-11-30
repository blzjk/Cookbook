from . import  views
from django.urls import path

urlpatterns = [
    path('rejestracja', views.register, name='rejestracja'),
    path('logowanie', views.user_login, name='logowanie'),
    path('panel', views.panel, name='panel')
]