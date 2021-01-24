from django.urls import reverse

from django.db import models

class Car(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.FloatField()
    body_style = models.CharField(max_length=200)

    def __str__(self):
        return self.make