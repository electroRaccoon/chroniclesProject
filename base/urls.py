from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Page d'accueil
    path('signup/', views.signup_view, name='signup'),  # Page d'inscription
]