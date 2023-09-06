from django.db import models

# Create your models here.
class Clothe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)