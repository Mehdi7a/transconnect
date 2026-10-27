from django.urls import path
from .views import liste_expeditions, detail_expedition  # Import direct

app_name = 'expeditions'

urlpatterns = [
    path('', ListeViewExpeditions.as_view(), name='liste'),
    path('<str:reference>/', detail_expedition, name='details_expedition'),
]