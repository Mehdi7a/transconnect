from django.db import models

# Create your models here.
class Offre(models.Model):                                                        
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    date_proposition=models.DateField(auto_now_add=True)
    delai_jours=models.DecimalField(max_digits=5, decimal_places=1)
    statut=models.CharField(max_length=20,choices=[('proposee','proposee'),('acceptee','acceptee'),('refusee','refusee'),('retirée','retirée')],default='proposee')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    expedition=models.ForeignKey('ExpeditionsApp.Expedition',on_delete=models.CASCADE,related_name='offres')
    entreprise=models.ForeignKey('EntreprisesApp.Entreprise',on_delete=models.CASCADE,related_name='offres')
    vehicule=models.ForeignKey('VehiculesApp.Vehicule',on_delete=models.CASCADE,related_name='offres')
    def __str__(self):
        return f"Offre {self.id} - Expedition {self.expedition.reference} - Entreprise {self.entreprise.raison_sociale} - Vehicule {self.vehicule.immatriculation}"
 

