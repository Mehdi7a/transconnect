from django.urls import path
from .views import (
    ListeViewEntreprises, EntrepriseDetailView, EntrepriseCreateView,
    EntrepriseUpdateView, EntrepriseDeleteView,
)

app_name = 'entreprises'

urlpatterns = [
    path('', ListeViewEntreprises.as_view(), name='liste'),
    path('create/', EntrepriseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', EntrepriseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EntrepriseDeleteView.as_view(), name='delete'),
    path('<int:pk>/', EntrepriseDetailView.as_view(), name='detail'),
]