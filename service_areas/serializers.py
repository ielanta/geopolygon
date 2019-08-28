from rest_framework import serializers
from service_areas.models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'price', 'geo_polygon', 'provider']
