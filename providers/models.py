from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=64, blank=True)  # no validation here, because phone format not specified
    language = models.CharField(max_length=64, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name