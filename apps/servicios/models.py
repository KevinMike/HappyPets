from django.db import models
from apps.producto.models import Producto
from apps.mascota.models import Mascota

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

class DetalleProductos(models.Model):
    id_atencion_servicio = models.ForeignKey(AtencionServicio)
    codigo_producto = models.ForeignKey(Producto)
    cantidad = models.SmallIntegerField()

class DetalleServicios(models.Model):
    id_atencion_servicio = models.ForeignKey(AtencionServicio)
    id_servicios = models.ForeignKey(Servicios)
    cantidad = models.SmallIntegerField()

class AtencionServicio(models.Model):
    id_mascota = models.ForeignKey(Mascota, blank=True, null=True)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)