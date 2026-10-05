from django.db import models

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=20,unique=True)
    ville_depart=models.CharField(max_length=100)
    ville_arrivee=models.CharField(max_length=100)
    date_souhaitee=models.DateField()
    poids_kg=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    statut=models.CharField(choices=[('publiee','publiee'),('attribuee','attribuee'),('en_cours','en_cours'),('livree','livree'),('annulee','annulee')],default='publiee')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    entreprise=models.ForeignKey('EntreprisesApp.Entreprise',on_delete=models.CASCADE,related_name='expeditions')
    def __str__(self):
        return f"Expedition {self.reference} - De {self.ville_depart} à {self.ville_arrivee} - Entreprise {self.entreprise.raison_sociale}"