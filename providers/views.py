from rest_framework import generics

from providers.models import Provider
from providers.serializers import ProviderSerializer


class ProviderList(generics.ListCreateAPIView):
    """
    List all providers, or create a new provider.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update or delete provider.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
