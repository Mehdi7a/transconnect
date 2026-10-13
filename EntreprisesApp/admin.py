from django.contrib import admin
from .models import Entreprise, Utilisateur
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Entreprise)
@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display=("user_id","role",'first_name','last_name')
    list_filter=('user_id','created_at')
    search_fields=('telephone','email')
    list_editable=('role','first_name','last_name')
    ordering=('-created_at')
    date_hierarchy='created_at'
    list_per_page=10
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=("raison_sociale","matricule_fiscale","type_entreprise")
    list_filter=('type_entreprise','created_at')
    search_fields=('raison_sociale','matricule_fiscale')
    list_editable=('type_entreprise',)
    ordering=('-created_at')
    date_hierarchy='created_at'
    list_per_page=10
    