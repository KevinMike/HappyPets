from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    model = Trabajador
    list_display = ('dni','nombre','apellido','telefono','fecha_nacimiento','fecha_contrato',)

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    model = Veterinario
    list_display = ('dni','nombre','apellido','telefono','fecha_nacimiento','fecha_contrato','especialidad',)