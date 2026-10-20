from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils import timezone

def email_validate(value):
    if not value:
        raise ValidationError
    if not value.endswith('@gmail.com'):
        raise ValidationError("Seuls les emails appartenant au domaine gmail.com sont acceptés ")

matricule_fiscal_validator=RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$')

# Create your models here.
class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8,editable=False,primary_key=True)
    email=models.EmailField(unique=True, validators=[email_validate])
    role=models.CharField(max_length=20,choices=[('chargeur','chargeur'),('transporteur','transporteur'),('admin','admin')],default='chargeur')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return f"{self.username} {self.role}"
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()
        super().save(*args, **kwargs)

    @classmethod
    def _generate_user_id(cls):
        aa = timezone.now().strftime("%y")
        prefixe = f"{aa}user"
        last = cls.objects.filter(user_id__startswith=prefixe).order_by("-user_id").first()
        n = int(last.user_id[-2:]) + 1 if last else 0
        if n > 99:
            raise ValidationError(f"Limite atteinte pour l'année 20{aa}")
        return f"{prefixe}{n:02d}"

class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=100)

    matricule_fiscale = models.CharField(
        max_length=17,
        unique=True,
        validators=[matricule_fiscal_validator]
    )

    type_entreprise = models.CharField(
        max_length=15,
        choices=[
            ('chargeur', 'chargeur'),
            ('transporteur', 'transporteur')
        ]
    )

    adresse = models.TextField(
        validators=[MinLengthValidator(20, "error")]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gerant = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='entreprise',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Entreprise {self.raison_sociale} - Matricule Fiscale {self.matricule_fiscale} - Type {self.type_entreprise}"