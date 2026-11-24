from rest_framework import serializers
from .models import Expedition

class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'
        read_only_fields = ('reference','created_at', 'updated_at')  # Assuming these fields are auto-generated and should not be modified