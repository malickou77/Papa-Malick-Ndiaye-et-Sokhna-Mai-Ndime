from django.db import models
from django.utils import timezone

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    promo = models.CharField(max_length=20)
    filiers = models.CharField(max_length=100, default='')
    annees = models.DateField(default='2022-05-21')
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return f"{self.nom} {self.prenom}  {self.promo} {self.filiers} {self.Annees} {self.id}"

class Annees(models.Model):
    nom_filieres = models.CharField(max_length=100)
    date_inscriptions= models.DateField()
    heure_inscriptions = models.TimeField()
    

    def __str__(self):
        return f" {self.nom_filieres} {self.date_inscriptions} {self.heure_inscriptions} "

class Inscrits(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    Annees = models.ForeignKey(Annees, on_delete=models.CASCADE)
    heure_inscriptions= models.DateField()
    
    def __str__(self):
        return f"{self.etudiant} - {self.Annees} - {self. heure_inscriptions} "