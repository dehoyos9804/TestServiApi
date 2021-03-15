from django.db import models

# Create your models here.
class Buyer(models.Model):
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    longitud = models.CharField(max_length=150)
    latitud = models.CharField(max_length=150)
    estado_geo = models.IntegerField(max_length=2)



