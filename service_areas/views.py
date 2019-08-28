from rest_framework import generics
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
    def get(self, request):
        """
        Return a list of all users.
        """
        point = Point(float(request.query_params['lng']), float(request.query_params['lat']))  # create point
        result = []
        for service in ServiceArea.objects.all():
            polygon = Polygon(service.geo_polygon['points'])  # create polygon
            if polygon.contains(point):
                result.append((service.name, service.provider.name, service.price))
        return Response(result)
