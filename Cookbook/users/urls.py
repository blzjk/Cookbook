from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, reverse_lazy

from .views import add_recipe


urlpatterns = [
    path('rejestracja', views.register, name='rejestracja'),
    path('logowanie', views.user_login, name='logowanie'),
    path('wylogowanie', views.user_logout, name='wylogowanie'),
    path('przepis', add_recipe, name='przepis'),
    path('haslo/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='haslo'),
    path('zmiana-hasla/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
