from django.urls import path
from . import views
from .views import CreerPersonnageView

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Page d'accueil
    path('signup/', views.signup_view, name='signup'),  # Page d'inscription
    path('creer/', CreerPersonnageView.as_view(), name='creer_personnage'),
    path('personnage/<int:pk>/', views.detail_personnage, name='detail_personnage'),
    path('mes-personnages/', views.liste_personnages, name='liste_personnages'),
]