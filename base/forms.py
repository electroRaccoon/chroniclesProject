from django import forms
from .models import Human, Changeling

# Formulaire pour les humains
class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'age']

# Formulaire pour les changelins
class ChangelingForm(forms.ModelForm):
    class Meta:
        model = Changeling
        fields = ['name', 'age', 'seeming', 'kith']