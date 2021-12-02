from . import views
from django.urls import path

from .views import panel

urlpatterns = [
    path('rejestracja', views.register, name='rejestracja'),
    path('logowanie', views.user_login, name='logowanie'),
    path('panel', panel, name='panel')
]
