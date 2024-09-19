from django import forms
from .models import PersonnageHumain, PersonnageChangelin

class PersonnageBaseForm(forms.ModelForm):
    class Meta:
        fields = ['nom', 'chronique', 'intelligence', 'astuce', 'resolution', 'force', 'dexterite', 'vigueur', 'presence', 'manipulation', 'calme', 'informatique', 'artisanat', 'combat', 'conduite', 'erudition', 'investigation', 'medecine', 'occulte', 'politique', 'science', 'armes_a_feu', 'armes_blanches', 'athletisme', 'discretion', 'larcin', 'pilotage', 'survie', 'animaux', 'empathie', 'expression', 'intimidation', 'persuasion', 'relationnel', 'sagesse_de_la_rue', 'subterfuge']

class PersonnageHumainForm(PersonnageBaseForm):
    class Meta(PersonnageBaseForm.Meta):
        model = PersonnageHumain
        fields = PersonnageBaseForm.Meta.fields + ['vice', 'vertu']

class PersonnageChangelinForm(PersonnageBaseForm):
    class Meta(PersonnageBaseForm.Meta):
        model = PersonnageChangelin
        fields = PersonnageBaseForm.Meta.fields + ['aiguille', 'fil']

class ChoixPersonnageForm(forms.Form):
    TYPE_CHOICES = [
        ('humain', 'Humain'),
        ('changelin', 'Changelin'),
    ]
    type_personnage = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)