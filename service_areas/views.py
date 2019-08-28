import logging
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class ServiceAreaList(generics.ListCreateAPIView):
    """
    List all service areas, or create a new service area.
    """
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update or delete service area.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaPoint(APIView):
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        """
        API take a lat/lng pair as arguments and Return a list of data(service name, provider name and price)
        for all services that include the given lat/lng.
        Parameters
            lat: float
                point latitude
            lng: float
                point longitude
        Returns
            [(service name, provider name, service price)]
        """
        lng = request.query_params.get('lng')
        lat = request.query_params.get('lat')
        logging.info(f'Find service areas for point lng={lng} and lat={lat}')
        if not lng or not lat:
            logging.error('lng or lat missed')
            raise ValidationError('Please provide lng and lat params')
        # TODO: validate lng/lat float
        point = Point(float(lng), float(lat))  # create point
        result = []
        for service in ServiceArea.objects.all():
            polygon = Polygon(service.geo_polygon['points'])  # create polygon
            if polygon.contains(point):
                result.append((service.name, service.provider.name, service.price))
        return Response(result)
