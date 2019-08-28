from django.contrib.postgres.fields import JSONField
from django.db import models

from providers.models import Provider


class ServiceArea(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    geo_polygon = JSONField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
