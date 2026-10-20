from django.contrib import admin
from .models import Utilisateur, Entreprise
from VehiculesApp.models import Vehicule

admin.site.site_header = "Transconnect-administration"
admin.site.site_title = "Transconnect"
admin.site.index_title = "Tableau de bord"

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'role', 'first_name', 'last_name')
    list_filter = ('created_at',)
    search_fields = ('telephone',)
    list_editable = ('first_name', 'last_name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10


class VehiculeInline(admin.TabularInline):
    model = Vehicule
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg')  # capacite_kg ajouté
    extra = 0  # évite un formulaire vide par défaut


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    inlines = [VehiculeInline]
    list_display = ('raison_sociale', 'type_entreprise')
    list_filter = ('type_entreprise', 'created_at')
    search_fields = ('raison_sociale', 'matricule_fiscale')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identité entreprise', {
            'fields': ('raison_sociale', 'matricule_fiscale', 'type_entreprise')  # type ajouté
        }),
        ('Contact', {
            'fields': ('adresse', 'gerant')
        }),
        ('Dates système', {
            'fields': ('created_at', 'updated_at')
        }),
    )