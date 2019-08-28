from __future__ import unicode_literals

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from providers.models import Provider


class ProviderListTests(APITestCase):
    url = reverse('provider-list')
    data = {'name': 'Test Provider', 'email': 'test@mail.ru'}

    def test_get_list(self):
        self.client.post(self.url, self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.data['name'])

    def test_create(self):
        self.assertEqual(Provider.objects.count(), 0)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, self.data['name'])


class ProviderDetailTests(APITestCase):
    data = {'name': 'Test Provider Detail', 'email': 'test@mail.ru'}

    def setUp(self):
        self.provider, _ = Provider.objects.get_or_create(**self.data)
        self.url = reverse('provider-detail', kwargs={'pk': self.provider.pk})

    def test_update(self):
        self.data['name'] = 'Updated Provider Name'
        self.assertNotEqual(Provider.objects.get(pk=self.provider.pk).name, self.data['name'])
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.get(pk=self.provider.pk).name, self.data['name'])

    def test_delete(self):
        self.assertEqual(Provider.objects.filter(pk=self.provider.pk).count(), 1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Provider.objects.filter(pk=self.provider.pk).count(), 0)
