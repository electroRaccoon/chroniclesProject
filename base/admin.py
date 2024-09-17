from django.contrib import admin
from .models import Character, Human, Changeling

# Ajout des modèles dans l'admin
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_type', 'player')
    list_filter = ('character_type', 'player')

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'player')

@admin.register(Changeling)
class ChangelingAdmin(admin.ModelAdmin):
    list_display = ('name', 'seeming', 'kith', 'player')
    list_filter = ('seeming', 'kith', 'player')