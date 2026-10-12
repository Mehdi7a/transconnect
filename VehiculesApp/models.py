from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=10,unique=True)
    type_vehicule=models.CharField(max_length=50,choices=[('camionnette','camionnette'),('fourgon','fourgon'),('camion porteur','camion porteur'),('semi-remorque','semi-remorque')])
    capacite_kg=models.PositiveIntegerField(validators=[MinValueValidator(1,"Une capacité nulle ne peut pas être acceptée")])
    disponible=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    entreprise=models.ForeignKey('EntreprisesApp.Entreprise',on_delete=models.CASCADE,related_name='vehicules')
    def __str__(self):
        return f"Vehicule {self.immatriculation} - Type {self.type_vehicule} - Entreprise {self.entreprise.raison_sociale}"
    
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError("doit etre de type transporteur")
        
    CAPACITE_MAX_TYPE = {'camionnette':1500,'fourgon':3500,'camion porteur':19000,'semi-remorque':26000}  # pour la règle 7

    def save(self, *args, **kwargs):          # sinon clean() n'est jamais appelé
        self.full_clean()
        super().save(*args, **kwargs)
            