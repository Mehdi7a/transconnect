import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models import Offre


@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="offres.csv"'
    writer = csv.writer(response)
    writer.writerow(['reference_expedition', 'transporteur', 'prix', 'statut'])
    for offre in queryset.select_related('expedition', 'entreprise'):
        writer.writerow([
            offre.expedition.reference,
            offre.entreprise.raison_sociale,
            offre.prix,
            offre.statut,
        ])
    return response


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ("id", "expedition", "entreprise", "vehicule", "statut_colore")
    list_filter = ("statut", "expedition", "entreprise", "vehicule")
    search_fields = ("id", "expedition__reference",
                     "entreprise__raison_sociale", "vehicule__immatriculation")
    actions = [exporter_offres_csv]

    @admin.display(description="Statut")
    def statut_colore(self, obj):
        couleurs = {
            "proposee": "#F0AD4E",
            "acceptee": "#5CB85C",
            "refusee": "#D9534F",
            "retiree": "#777777",
        }
        return format_html(
            '<span style="color:white; background:{}; padding:3px 8px; border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, "#999"),
            obj.get_statut_display(),
        )