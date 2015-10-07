from django.db import models
from apps.mascota.models import Mascota

# Create your models here.
class Vacuna(models.Model):
    id_mascota = models.ForeignKey(Mascota, blank=True, null=True)
    dosis_aplicacion = models.CharField(max_length=15)
    fecha = models.DateField()
    unidades = models.SmallIntegerField()
    proxima_vacuna = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

class Medicina(models.Model):
    nombre_cientifico = models.CharField(max_length=45)
    nombre_comercial = models.CharField(max_length=45)
    laboratorio = models.CharField(max_length=45, blank=True, null=True)
    forma_farmaceutica = models.CharField(max_length=35)
    lote = models.CharField(max_length=10, blank=True, null=True)

class DetalleVacuna(models.Model):
    id_medicina = models.ForeignKey(Medicina)
    id_vacuna = models.ForeignKey(Vacuna)
    dosis = models.CharField(max_length=15)



