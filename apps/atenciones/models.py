# -*- encoding: utf-8 -*-
from django.db import models
from apps.trabajador.models import Veterinario
from apps.mascota.models import Mascota
from django.utils import timezone
from apps.vacuna.models import Medicina
from apps.servicios.models import Producto
# Create your models here.
class Cita(models.Model):
    veterinario = models.ForeignKey(Veterinario)
    mascota = models.ForeignKey(Mascota)
    fecha = models.DateField()
    atendido = models.BooleanField(default=False)
    def __unicode__(self):
        return "%s - %s" %(self.fecha,self.mascota.nombre)

class AtencionClinica(models.Model):
    veterinario = models.ForeignKey(Veterinario)
    mascota = models.ForeignKey(Mascota)
    fecha = models.DateField(default=timezone.now())
    diagnostico = models.TextField()
    proxima_cita = models.ForeignKey(Cita,blank=True, null=True)
    #medicinas = models.ManyToManyField(Medicina,blank=True,null=True)
    #productos = models.ManyToManyField(Producto,blank=True,null=True)
    observaciones = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s - %s" %(self.fecha,self.mascota.nombre)
    class Meta:
        verbose_name = 'Atención Clínica'
        verbose_name_plural = 'Atenciones Clinicas'

class AtencionClinica_DetalleProductos(models.Model):
    atencion_clinica = models.ForeignKey(AtencionClinica)
    codigo_producto = models.ForeignKey(Producto)
    cantidad = models.SmallIntegerField()
    class Meta:
        verbose_name = 'Detalle - Producto'
        verbose_name_plural = 'Detalle - Productos'

class AtencionClinica_DetalleMedicina(models.Model):
    atencion_clinica = models.ForeignKey(AtencionClinica,on_delete=models.CASCADE)
    medicina = models.ForeignKey(Medicina,on_delete=models.CASCADE)
    dosis = models.CharField(max_length=15)

