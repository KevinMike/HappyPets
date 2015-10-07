from django.db import models
from apps.trabajador.models import Veterinario
from apps.mascota.models import Mascota
# Create your models here.
class AtencionClinica(models.Model):
    dni_veterinario = models.ForeignKey(Veterinario, blank=True, null=True)
    id_mascota = models.ForeignKey(Mascota, unique=True, blank=True, null=True)
    fecha = models.DateField()
    diagnostico = models.TextField()
    proxima_cita = models.ForeignKey(Cita,blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)



class Cita(models.Model):
    dni_veterinario = models.ForeignKey(Veterinario, blank=True, null=True)
    id_mascota = models.ForeignKey(Mascota, blank=True, null=True)
    fecha = models.DateField()

