from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(primary_key=True,max_length=8)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)