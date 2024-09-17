from django.db import models
from django.contrib.auth.models import User

# Modèle de base pour tous les personnages
class Character(models.Model):
    HUMAN = 'HU'
    CHANGELING = 'CH'
    
    CHARACTER_TYPES = [
        (HUMAN, 'Humain'),
        (CHANGELING, 'Changelin'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien vers l'utilisateur créateur
    character_type = models.CharField(
        max_length=2,
        choices=CHARACTER_TYPES,
        default=HUMAN,
    )

    def __str__(self):
        return f"{self.name} ({self.get_character_type_display()})"

# Modèle spécifique pour les humains (actuellement vide, prêt à être étendu)
class Human(Character):
    pass

# Modèle spécifique pour les changelins
class Changeling(Character):
    SEEMING_CHOICES = [
        ('Fairest', 'Fairest'),
        ('Ogre', 'Ogre'),
        # Ajouter d'autres types de Seeming
    ]
    KITH_CHOICES = [
        ('Artist', 'Artist'),
        ('Soldier', 'Soldier'),
        # Ajouter d'autres types de Kith
    ]

    seeming = models.CharField(max_length=50, choices=SEEMING_CHOICES)
    kith = models.CharField(max_length=50, choices=KITH_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.seeming} ({self.kith})"

