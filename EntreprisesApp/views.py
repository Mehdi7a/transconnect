from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entreprise
from .forms import EntrepriseForm, RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ListeViewEntreprises(ListView):
    model = Entreprise
    template_name = 'entreprises/liste.html'
    context_object_name = 'entreprises'


class EntrepriseDetailView(DetailView):
    model = Entreprise
    template_name = 'entreprises/detail.html'
    context_object_name = 'entreprise'


class EntrepriseCreateView(CreateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprises/form.html'
    success_url = reverse_lazy('entreprises:liste')


class EntrepriseUpdateView(UpdateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprises/form.html'
    success_url = reverse_lazy('entreprises:liste')


class EntrepriseDeleteView(DeleteView):
    model = Entreprise
    template_name = 'entreprises/confirm_delete.html'
    success_url = reverse_lazy('entreprises:liste')