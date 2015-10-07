from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=35)
    marca = models.CharField(max_length=35, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)

