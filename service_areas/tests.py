from __future__ import unicode_literals

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from providers.models import Provider
from service_areas.models import ServiceArea

POLYGON = {'points': [[10,10],[20,10],[10,20],[20,20]]}


class ServiceAreaListTests(APITestCase):
    def setUp(self):
        self.url = reverse('service-area-list')
        self.provider, _ = Provider.objects.get_or_create({'name': 'Test Provider', 'email': 'test@mail.ru'})
        self.data = {'name': 'S1', 'price': '10', 'geo_polygon': POLYGON}

    def test_get_list(self):
        service, _ = ServiceArea.objects.get_or_create(**self.data, provider=self.provider)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.data['name'])

    def test_create(self):
        self.data['provider'] = self.provider.pk
        self.assertEqual(ServiceArea.objects.count(), 0)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, self.data['name'])


class ServiceAreaDetailTests(APITestCase):
    def setUp(self):
        provider, _ = Provider.objects.get_or_create()
        self.data = {'name': 'S2', 'price': '15', "geo_polygon": POLYGON, 'provider': provider}
        self.service, _ = ServiceArea.objects.get_or_create(**self.data)
        self.url = reverse('service-area-detail', kwargs={'pk': self.service.pk})
        self.data['provider'] = provider.pk

    def test_update(self):
        self.data['name'] = 'Updated Provider Name'
        self.assertNotEqual(ServiceArea.objects.get(pk=self.service.pk).name, self.data['name'])
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ServiceArea.objects.get(pk=self.service.pk).name, self.data['name'])

    def test_delete(self):
        self.assertEqual(ServiceArea.objects.filter(pk=self.service.pk).count(), 1)
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ServiceArea.objects.filter(pk=self.service.pk).count(), 0)


class ServiceAreaPointTests(APITestCase):
    def setUp(self):
        provider, _ = Provider.objects.get_or_create()
        self.data = {'name': 'S2', 'price': '15', "geo_polygon": POLYGON, 'provider': provider}
        self.service, _ = ServiceArea.objects.get_or_create(**self.data)
        self.url = reverse('service-area-point')

    def test_point_inside(self):
        response = self.client.get(self.url+'?lat=11&lng=12', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_point_outside(self):
        response = self.client.get(self.url+'?lat=11&lng=11', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

