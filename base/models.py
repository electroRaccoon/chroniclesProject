from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class PersonnageBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)ss')
    nom = models.CharField(max_length=100)
    chronique = models.CharField(max_length=100)
    
    # Attributs avec valeur par défaut de 0
    intelligence = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    force = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    presence = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    astuce = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    # Compétences avec valeur par défaut de 1
    informatique = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    combat = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    empathie = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        abstract = True

    def __str__(self):
        return self.nom

    def get_type(self):
        return self.__class__.__name__.replace('Personnage', '')

class PersonnageHumain(PersonnageBase):
    vice = models.CharField(max_length=50)
    vertu = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Personnage Humain"
        verbose_name_plural = "Personnages Humains"

class PersonnageChangelin(PersonnageBase):
    aiguille = models.CharField(max_length=50)
    fil = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Personnage Changelin"
        verbose_name_plural = "Personnages Changelins"