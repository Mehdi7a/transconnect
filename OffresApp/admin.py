from django.contrib import admin
from django.utils.html import format_html
from .models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ("id", "expedition", "entreprise", "vehicule", "statut_colore")
    list_filter = ("statut", "expedition", "entreprise", "vehicule")
    search_fields = ("id", "expedition__reference",
                     "entreprise__raison_sociale", "vehicule__immatriculation")

    @admin.display(description="Statut")
    def statut_colore(self, obj):
        couleurs = {
            "proposee": "#F0AD4E", "acceptee": "#5CB85C",
            "refusee": "#D9534F", "retirée": "#777777",
        }
        return format_html(
            '<span style="color:white; background:{}; padding:3px 8px; border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, "#999"),
            obj.get_statut_display(),
        )