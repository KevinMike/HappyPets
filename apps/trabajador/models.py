from django.db import models

# Create your models here.
class Trabajador(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_contrato = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido
    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'

class Veterinario(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_contrato = models.DateField(blank=True, null=True)
    especialidad = models.CharField(max_length=45)
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'