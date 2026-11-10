from django.urls import path
from .views import ListeViewExpeditions, ExpeditionDetailView

app_name = 'expeditions'

urlpatterns = [
    path('', ListeViewExpeditions.as_view(), name='liste'),
    path('<str:reference>/', ExpeditionDetailView.as_view(), name='details_expedition'),
]