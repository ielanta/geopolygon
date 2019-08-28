from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=256, help_text='example: GeoLab')
    email = models.EmailField(unique=True, help_text='example: test@mail.ru')
    phone = models.CharField(max_length=64, blank=True, help_text='example: +7 (123) 456 789')  # TODO: add validation
    language = models.CharField(max_length=64, blank=True, help_text='example: English')
    currency = models.CharField(max_length=3, blank=True, help_text='example: USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name