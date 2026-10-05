from django.db import models

# Create your models here.
class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=10,unique=True)
    type_vehicule=models.CharField(max_length=15,choices=[('camionnette','camionnette'),('fourgon','fourgon'),('camion porteur','camion porteur'),('semi-remorque','semi-remorque')])
    capacite_kg=models.PositiveIntegerField()
    disponible=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    entreprise=models.ForeignKey('EntreprisesApp.Entreprise',on_delete=models.CASCADE,related_name='vehicules')
    def __str__(self):
        return f"Vehicule {self.immatriculation} - Type {self.type_vehicule} - Entreprise {self.entreprise.raison_sociale}"