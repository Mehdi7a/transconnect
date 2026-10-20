from django.contrib import admin
from .models import Vehicule
# Register your models here.

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display=("immatriculation","type_vehicule","capacite_kg","disponible","entreprise")
    fieldsets=(
        ("Informations du véhicule",{ 
            "fields":("immatriculation","type_vehicule","capacite_kg")
            }),
            ("Détails du véhicule", {
                "fields": ("disponible","entreprise")
            }),
            ("Dates système", {
                "fields": ("created_at", "updated_at")
            })  
    )
    readonly_fields=("created_at","updated_at")
    list_filter=('type_vehicule','disponible','entreprise')
    search_fields=('immatriculation','type_vehicule','entreprise__raison_sociale')
    list_editable=('type_vehicule','capacite_kg','disponible')
    ordering=('-created_at',)
    date_hierarchy='created_at'
    list_per_page=10

