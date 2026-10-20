from django.db import models, transaction
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    date_proposition = models.DateField(auto_now_add=True)
    delai_jours = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    statut = models.CharField(
        max_length=20,
        choices=[('proposee', 'proposee'), ('acceptee', 'acceptee'), ('refusee', 'refusee'), ('retirée', 'retirée')],
        default='proposee'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expedition = models.ForeignKey('ExpeditionsApp.Expedition', on_delete=models.CASCADE, related_name='offres')
    entreprise = models.ForeignKey('EntreprisesApp.Entreprise', on_delete=models.CASCADE, related_name='offres')
    vehicule = models.ForeignKey('VehiculesApp.Vehicule', on_delete=models.CASCADE, related_name='offres')

    def __str__(self):
        return f"Offre {self.id} - Expédition : {self.expedition.reference} - Entreprise : {self.entreprise.raison_sociale} - Véhicule : {self.vehicule.immatriculation}"

    def clean(self):
        super().clean()
        creation = self._state.adding
        if self.entreprise_id and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError("Une offre ne peut être créée que par un transporteur")            # R1
        if self.vehicule_id and self.entreprise_id and self.vehicule.entreprise_id != self.entreprise_id:
            raise ValidationError("Le véhicule doit appartenir au transporteur de l'offre")           # R2
        if creation and self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError("Cette expédition n'accepte plus de nouvelles offres")             # R3
        if (self.statut == 'proposee' and self.expedition_id and self.entreprise_id
                and Offre.objects.filter(expedition=self.expedition, entreprise=self.entreprise,
                                         statut='proposee').exclude(pk=self.pk).exists()):
            raise ValidationError("Une offre proposée existe déjà pour cette expédition")            # R4
        if creation and self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError("Ce véhicule n'est pas disponible")                                # R6
        if self.vehicule_id and self.expedition_id:                                                  # R7
            v = self.vehicule
            if self.expedition.poids_kg > min(v.CAPACITE_MAX_TYPE[v.type_vehicule], v.capacite_kg):
                raise ValidationError("Véhicule incompatible avec le poids de l'expédition")

    def _appliquer_cascade_acceptation(self):                                                       # R5
        exp = self.expedition
        exp.statut = 'attribuee'
        exp.save()
        Offre.objects.filter(expedition=exp, statut='proposee').exclude(pk=self.pk).update(statut='refusee')

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.full_clean()
            super().save(*args, **kwargs)
            if self.statut == 'acceptee':
                self._appliquer_cascade_acceptation()