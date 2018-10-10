from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
