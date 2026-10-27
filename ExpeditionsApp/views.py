from django.shortcuts import render
from .models import Expedition
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

def liste_expeditions(request):
    expeditions = (
    Expedition.objects
    .filter(statut='publiee')
    .select_related('entreprise')
    .order_by('-created_at')
    )
    return render(request, 'expeditions/liste.html', {'expeditions': expeditions})
class ListeViewExpeditions(ListView):
    model = Expedition
    template_name = 'expeditions/liste.html'
    context_object_name = 'expeditions'
    
"""def detail_expedition(request, reference):
    expedition = get_object_or_404(Expedition, reference=reference)
    offres = (expedition.offres.select_related('transporteur', 'vehicule')
    .order_by('-date_proposition')
    )
    return render(
        request, 'expeditions/detail.html',
    {'expedition': expedition, 'offres': offres},
    )"""