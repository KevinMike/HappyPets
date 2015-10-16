# -*- encoding: utf-8 -*-
from django.db import models
from apps.trabajador.models import Veterinario
from apps.mascota.models import Mascota
from django.utils import timezone
# Create your models here.
class Cita(models.Model):
    veterinario = models.ForeignKey(Veterinario)
    mascota = models.ForeignKey(Mascota)
    fecha = models.DateField()
    def __unicode__(self):
        return "%s - %s" %(self.fecha,self.mascota.nombre)

class AtencionClinica(models.Model):
    veterinario = models.ForeignKey(Veterinario)
    mascota = models.ForeignKey(Mascota)
    fecha = models.DateField(default=timezone.now())
    diagnostico = models.TextField()
    proxima_cita = models.ForeignKey(Cita,blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s - %s" %(self.fecha,self.mascota.nombre)
    class Meta:
        verbose_name = 'Atención Clínica'
        verbose_name_plural = 'Atenciones Clinicas'
