from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import ChoixPersonnageForm, PersonnageHumainForm, PersonnageChangelinForm
from .models import PersonnageHumain, PersonnageChangelin
from django.http import Http404

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

@method_decorator(login_required, name='dispatch')
class CreerPersonnageView(View):
    def get(self, request):
        form = ChoixPersonnageForm()
        return render(request, 'base/creer_personnage.html', {'form': form})

    def post(self, request):
        type_personnage = request.POST.get('type_personnage')
        
        if not type_personnage:
            choix_form = ChoixPersonnageForm(request.POST)
            if choix_form.is_valid():
                type_personnage = choix_form.cleaned_data['type_personnage']
                if type_personnage == 'humain':
                    form = PersonnageHumainForm()
                else:
                    form = PersonnageChangelinForm()
                return render(request, 'base/creer_personnage.html', {'form': form, 'type': type_personnage})
            else:
                return render(request, 'base/creer_personnage.html', {'form': choix_form})
        else:
            if type_personnage == 'humain':
                form = PersonnageHumainForm(request.POST)
            else:
                form = PersonnageChangelinForm(request.POST)
            
            if form.is_valid():
                personnage = form.save(commit=False)
                personnage.user = request.user

                # Vérifier uniquement les champs spécifiques à chaque type de personnage
                required_fields = ['nom', 'chronique']
                if type_personnage == 'humain':
                    required_fields.extend(['vice', 'vertu'])
                else:
                    required_fields.extend(['aiguille', 'fil'])
                
                errors = {}
                for field in required_fields:
                    if not getattr(personnage, field):
                        errors[field] = 'Ce champ est obligatoire.'
                
                if errors:
                    for field, error in errors.items():
                        form.add_error(field, error)
                    return render(request, 'base/creer_personnage.html', {'form': form, 'type': type_personnage})
                
                personnage.save()
                return redirect('detail_personnage', pk=personnage.pk)
            
            return render(request, 'base/creer_personnage.html', {'form': form, 'type': type_personnage})
@login_required
def detail_personnage(request, pk):
    try:
        personnage = PersonnageHumain.objects.get(pk=pk, user=request.user)
    except PersonnageHumain.DoesNotExist:
        try:
            personnage = PersonnageChangelin.objects.get(pk=pk, user=request.user)
        except PersonnageChangelin.DoesNotExist:
            raise Http404("Personnage non trouvé")
    
    return render(request, 'base/detail_personnage.html', {'personnage': personnage})

@login_required
def liste_personnages(request):
    personnages_humains = PersonnageHumain.objects.filter(user=request.user)
    personnages_changelins = PersonnageChangelin.objects.filter(user=request.user)
    personnages = list(personnages_humains) + list(personnages_changelins)
    return render(request, 'base/liste_personnages.html', {'personnages': personnages})