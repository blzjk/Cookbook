from . import views
from django.urls import path

from .views import add_recipe


urlpatterns = [
    path('rejestracja', views.register, name='rejestracja'),
    path('logowanie', views.user_login, name='logowanie'),
    path('wylogowanie', views.user_logout, name='wylogowanie'),
    path('przepis', add_recipe, name='przepis')
]
