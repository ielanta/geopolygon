from rest_framework import serializers
from providers.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone', 'language', 'currency']