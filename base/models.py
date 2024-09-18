from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PersonnageBase(models.Model):
    nom = models.CharField(max_length=100)
    chronique = models.CharField(max_length=100)
    
    # Attributs
    intelligence = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    astuce = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    resolution = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    force = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    dexterite = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    vigueur = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    presence = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    manipulation = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    calme = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # Compétences
    informatique = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    artisanat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    combat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    conduite = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    erudition = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    investigation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    medecine = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    occulte = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    politique = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    science = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    armes_a_feu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    armes_blanches = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    athletisme = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    discretion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    larcin = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    pilotage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    survie = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    animaux = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    empathie = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    expression = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    intimidation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    persuasion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    relationnel = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sagesse_de_la_rue = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    subterfuge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        abstract = True

    def __str__(self):
        return self.nom

class PersonnageHumain(PersonnageBase):
    vice = models.CharField(max_length=50)
    vertu = models.CharField(max_length=50)
    
    # Vous pouvez ajouter d'autres champs spécifiques aux humains ici
    
    class Meta:
        verbose_name = "Personnage Humain"
        verbose_name_plural = "Personnages Humains"

class PersonnageChangelin(PersonnageBase):
    aiguille = models.CharField(max_length=50)
    fil = models.CharField(max_length=50)
    
    # Vous pouvez ajouter d'autres champs spécifiques aux changelins ici
    
    class Meta:
        verbose_name = "Personnage Changelin"
        verbose_name_plural = "Personnages Changelins"