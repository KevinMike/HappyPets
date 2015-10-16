# -*- encoding: utf-8 -*-
from django.db import models
from apps.mascota.models import Mascota
from django.utils import timezone
# Create your models here.
class Medicina(models.Model):
    nombre_cientifico = models.CharField(max_length=45)
    nombre_comercial = models.CharField(max_length=45)
    laboratorio = models.CharField(max_length=45, blank=True, null=True)
    forma_farmaceutica = models.CharField(max_length=35)
    lote = models.CharField(max_length=10, blank=True, null=True)
    def __unicode__(self):
        return "%s - %s" %(self.nombre_cientifico,self.forma_farmaceutica)

class Vacuna(models.Model):
    mascota = models.ForeignKey(Mascota)
    dosis_aplicacion = models.CharField(max_length=15)
    fecha = models.DateField(default=timezone.now())
    unidades = models.SmallIntegerField(default=1)
    proxima_vacuna = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s - %s - %s" %(self.fecha,self.mascota,self.dosis_aplicacion)
    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'vacunas'

class Composicion(models.Model):
    medicina = models.ForeignKey(Medicina,on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna,on_delete=models.CASCADE)
    dosis = models.CharField(max_length=15)
    class Meta:
        verbose_name = 'Composición'
        verbose_name_plural = 'Medicamentos'



