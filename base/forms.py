from django import forms
from .models import PersonnageHumain, PersonnageChangelin

class PersonnageBaseForm(forms.ModelForm):
    class Meta:
        fields = ['nom', 'chronique', 
                  'intelligence', 'force', 'presence',  # 3 attributs
                  'informatique', 'combat', 'empathie']  # 3 compétences

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False  # Rend tous les champs non obligatoires par défaut

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