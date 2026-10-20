from django.contrib import admin
from .models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):

    list_display = ("id", "prix", "date_proposition", "statut", "expedition")

    list_display_links = ("id", "prix")

    list_filter = ("statut", "date_proposition")

    search_fields = ("prix", "expedition__reference")

    # Seul statut est modifiable directement dans la liste
    list_editable = ("statut",)

    ordering = ("-created_at",)

    date_hierarchy = "date_proposition"

    list_per_page = 10