"""Cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from recipes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('strona/<int:page>', index2, name='strona'),
    path('przepis/ocena', rateRecipe, name='ocena'),
    path('szukaj/', search, name='szukaj'),
    path('kategorie/', categories, name='kategorie'),
    path('kategoria/<id>/', category, name='kategoria'),
    path('przepis/<id>/', recipe, name='przepis'),
    path('przepis/', random_recipe, name='losowanie'),
    path('panel', panel, name='panel'),
    path('uzytkownik/', include('users.urls')),
    path('social-auth/', include('social_django.urls', namespace='social'))
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
