from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule
from .models import Offre


class ListeViewOffres(ListView):
    model = Offre
    template_name = 'offres/liste.html'
    context_object_name = 'offres'

    def get_queryset(self):
        return Offre.objects.select_related('expedition', 'entreprise', 'vehicule')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transporteurs'] = Entreprise.objects.filter(type_entreprise='transporteur')
        return context


class OffreDetailView(DetailView):
    model = Offre
    template_name = 'offres/detail.html'
    context_object_name = 'offre'


class OffreCreateView(CreateView):
    model = Offre
    fields = ['expedition', 'vehicule', 'prix', 'delai_jours']  # ni statut ni entreprise
    template_name = 'offres/form.html'

    def get_entreprise_courante(self):
        return get_object_or_404(
            Entreprise,
            pk=self.kwargs['entreprise_id'],
            type_entreprise='transporteur'
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['expedition'].queryset = Expedition.objects.filter(statut='publiee')
        form.fields['vehicule'].queryset = Vehicule.objects.filter(
            entreprise=self.get_entreprise_courante(), disponible=True
        )
        return form

    def form_valid(self, form):
        form.instance.entreprise = self.get_entreprise_courante()
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.messages)
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('expeditions:details_expedition',
                       kwargs={'reference': self.object.expedition.reference})


class OffreUpdateView(UpdateView):
    model = Offre
    fields = ['vehicule', 'prix', 'delai_jours']  # ni statut, ni entreprise, ni expedition
    template_name = 'offres/form.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['vehicule'].queryset = Vehicule.objects.filter(
            entreprise=self.object.entreprise, disponible=True
        )
        return form

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.messages)
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('offres:details_offre', kwargs={'pk': self.object.pk})


class OffreDeleteView(DeleteView):
    model = Offre
    template_name = 'offres/confirm_delete.html'
    success_url = reverse_lazy('offres:liste')