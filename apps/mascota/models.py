from django.db import models
from apps.cliente.models import Cliente

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    id_cliente = models.ForeignKey(Cliente)
    tipo = models.CharField(max_length=35)
    raza = models.CharField(max_length=35)
    tipo_alimento = models.CharField(max_length=35, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)


