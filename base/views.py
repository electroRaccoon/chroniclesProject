from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Vue pour la page d'accueil
def welcome_view(request):
    return render(request, 'base/home.html')

# Vue d'inscription
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Création de l'utilisateur
            login(request, user)  # Connexion automatique après inscription
            return redirect('welcome')  # Redirection vers la page d'accueil
    else:
        form = UserCreationForm()  # Afficher un formulaire vide
    
    return render(request, 'base/signup.html', {'form': form})