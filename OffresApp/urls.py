from django.urls import path
from .views import (
    ListeViewOffres, OffreDetailView, OffreCreateView,
    OffreUpdateView, OffreDeleteView,
)

app_name = 'offres'

urlpatterns = [
    path('', ListeViewOffres.as_view(), name='liste'),
    path('ajouter/<int:entreprise_id>/', OffreCreateView.as_view(), name='ajouter'),
    path('update/<int:pk>/', OffreUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OffreDeleteView.as_view(), name='delete'),
    path('<int:pk>/', OffreDetailView.as_view(), name='details_offre'),
]