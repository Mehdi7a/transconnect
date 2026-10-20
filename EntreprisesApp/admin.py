from django.contrib import admin
from .models import Utilisateur, Entreprise
from django.contrib.auth.admin import UserAdmin


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'role', 'first_name', 'last_name')
    list_filter = ('user_id', 'created_at')
    search_fields = ('telephone',)
    list_editable = ('first_name', 'last_name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 1


class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'matricule_fiscale', 'type_entreprise')
    list_filter = ('type_entreprise', 'created_at')
    search_fields = ('raison_sociale', 'matricule_fiscale')
    list_editable = ('type_entreprise',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10


admin.site.register(Entreprise, EntrepriseAdmin)