from django.contrib import admin, messages
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Expedition


class EnRetard(admin.SimpleListFilter):
    title = 'En retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return [('oui', 'Oui'), ('non', 'Non')]

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'oui':
            return queryset.filter(statut='publiee', date_souhaitee__lt=today)
        if self.value() == 'non':
            return queryset.filter(statut='publiee', date_souhaitee__gte=today)
        return queryset


@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ("reference", "entreprise", "ville_depart", "ville_arrivee",
                    "date_souhaitee", "poids_kg", "statut")
    fieldsets = (
        ("Informations de l'expédition", {
            "fields": ("reference", "entreprise", "ville_depart", "ville_arrivee",
                       "date_souhaitee", "poids_kg", "description")
        }),
        ("Détails de l'expédition", {
            "fields": ("statut",)
        }),
        ("Dates système", {
            "fields": ("created_at", "updated_at")
        }),
    )
    readonly_fields = ("reference", "created_at", "updated_at")
    list_filter = ('statut', 'date_souhaitee', EnRetard)
    search_fields = ('reference', 'ville_depart', 'ville_arrivee')
    list_editable = ('ville_depart', 'ville_arrivee', 'date_souhaitee', 'poids_kg', 'statut')
    ordering = ('-created_at',)
    date_hierarchy = 'date_souhaitee'
    list_per_page = 10
    actions = ['make_it_livree']          # au niveau de la classe

    @admin.action(description='Clôturer les expéditions sélectionnées')
    def make_it_livree(self, request, queryset):
        a_traiter = queryset.filter(statut='en cours')     # vérifie cette valeur
        ignorees = queryset.exclude(statut='en cours').count()
        compteur = 0
        erreurs = []

        for exp in a_traiter:
            exp.statut = 'livree'
            try:
                exp.save()
                compteur += 1
            except ValidationError as error:
                erreurs.append(f"{exp.reference} : erreur lors du changement de statut : {error}")

        if compteur:
            self.message_user(request, f"{compteur} expédition(s) clôturée(s).", messages.SUCCESS)
        if ignorees:
            self.message_user(request, f"{ignorees} expédition(s) ignorée(s) (pas en cours).", messages.WARNING)
        for e in erreurs:
            self.message_user(request, e, messages.ERROR)