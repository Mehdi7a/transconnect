from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.core.validators import MinValueValidator
# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=20,unique=True,editable=False)
    ville_depart=models.CharField(max_length=100)
    ville_arrivee=models.CharField(max_length=100)
    date_souhaitee=models.DateField()
    poids_kg=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    statut=models.CharField(max_length=20,choices=[('publiee','publiee'),('attribuee','attribuee'),('en_cours','en_cours'),('livree','livree'),('annulee','annulee')],default='publiee')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    entreprise=models.ForeignKey('EntreprisesApp.Entreprise',on_delete=models.CASCADE,related_name='expeditions')

    def __str__(self):
        return f"Expedition {self.reference} - De {self.ville_depart} à {self.ville_arrivee} - Entreprise {self.entreprise.raison_sociale}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference=self._generate_ref()
        self.full_clean()
        super().save(*args, **kwargs)
    @classmethod
    def _generate_ref(cls):
        annee=timezone.now().strftime("%Y")
        prefixe= f"EXP-{annee}-"
        last_value=(
        cls.objects.filter(reference__startswith=prefixe)
        .order_by("reference")
        .first()

        )
        c=int(last_value.reference[-5:])+1 if last_value else 1
        if c>99999:
            raise ValidationError("Le nombre d'expeditions a atteint sa limite pour cette année {annee}")

        return f"{prefixe}{c:05d}"
    @admin.register(Expedition)
    class ExpeditionAdmin(admin.ModelAdmin):
        list_display=("reference","ville_depart","ville_arrivee","date_souhaitee","poids_kg","statut")
        list_filter=('statut','date_souhaitee')
        search_fields=('reference','ville_depart','ville_arrivee')
        list_editable=('ville_depart','ville_arrivee','date_souhaitee','poids_kg','statut')
        ordering=('-created_at',)
        date_hierarchy='date_souhaitee'
        list_per_page=10
    
