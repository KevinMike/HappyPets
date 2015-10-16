from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Medicina)
class MedicinaAdmin(admin.ModelAdmin):
    model=Medicina
    list_display=('nombre_cientifico','nombre_comercial','laboratorio','forma_farmaceutica','lote',)

class ComposicionAdmin(admin.TabularInline):
    model = Composicion
    list_display = ('medicina','vacuna','dosis',)
    extra = 1

@admin.register(Vacuna)
class Vacuna(admin.ModelAdmin):
    model = Vacuna
    list_display = ('mascota','dosis_aplicacion','fecha','unidades','proxima_vacuna','observaciones',)
    inlines =[ComposicionAdmin,]

