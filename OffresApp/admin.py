from django.contrib import admin
from .models import Offre 
# Register your models here.
admin.site.register(Offre)
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display=("prix","date_souhaitee","statut","expedition")
    list_filter=('statut','date_souhaitee')
    search_fields=('prix','expedition__reference')
    list_editable=('prix','date_souhaitee','statut')
    ordering=('-created_at',)
    date_hierarchy='date_souhaitee'
    list_per_page=10