from django.db import models
from apps.mascota.models import Mascota

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=35)
    marca = models.CharField(max_length=35, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class AtencionServicio(models.Model):
    mascota = models.ForeignKey(Mascota, blank=True, null=True)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s - %s" %(self.fecha,self.mascota)
    class Meta:
        verbose_name = 'Registro de Servicios'
        verbose_name_plural = 'Historial de Servicios'

class DetalleProductos(models.Model):
    atencion_servicio = models.ForeignKey(AtencionServicio)
    codigo_producto = models.ForeignKey(Producto)
    cantidad = models.SmallIntegerField()
    class Meta:
        verbose_name = 'Detalle - Producto'
        verbose_name_plural = 'Detalle - Productos'

class DetalleServicios(models.Model):
    atencion_servicio = models.ForeignKey(AtencionServicio)
    servicios = models.ForeignKey(Servicios)
    cantidad = models.SmallIntegerField()
    class Meta:
        verbose_name = 'Detalle - Servicio'
        verbose_name_plural = 'Detalle - Servicios'

