from django.contrib.postgres.fields import JSONField
from django.db import models

from providers.models import Provider


class ServiceArea(models.Model):
    name = models.CharField(max_length=256, help_text='example: Test Area')
    price = models.FloatField(help_text='example: 15.05')
    geo_polygon = JSONField(help_text='[lng, lat] example: {"points": [[10,10],[20,10],[10,20],[20,20]]}')
    # TODO: validate geo_polygon
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, help_text='relation to Provider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
