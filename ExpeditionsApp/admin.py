from django.contrib import admin
from .models import Expedition
# Register your models here.
@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display=("reference","ville_depart","ville_arrivee","date_souhaitee","poids_kg","statut")
    list_filter=('statut','date_souhaitee')
    search_fields=('reference','ville_depart','ville_arrivee')
    list_editable=('ville_depart','ville_arrivee','date_souhaitee','poids_kg','statut')
    ordering=('-created_at',)
    date_hierarchy='date_souhaitee'
    list_per_page=10
