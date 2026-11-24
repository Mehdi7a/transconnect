from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView ,DeleteView

from .forms import VehiculeForm
from .models import Vehicule
from django.contrib.auth.mixins import LoginRequiredMixin



class VehiculeListView(LoginRequiredMixin, ListView):
    model = Vehicule
    template_name = "vehicules/list.html"
    context_object_name = "vehicules"



class VehiculeCreateView(LoginRequiredMixin, CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicules/form.html"
    success_url = reverse_lazy("vehicules:list")



class VehiculeUpdateView(LoginRequiredMixin, UpdateView):   
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicules/form.html"
    success_url = reverse_lazy("vehicules:list")

class VehiculeDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicule
    template_name = "vehicules/confirm_delete.html"
    context_object_name = "vehicule"
    success_url = reverse_lazy("vehicules:list")