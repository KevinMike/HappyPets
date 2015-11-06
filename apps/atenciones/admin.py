from django.contrib import admin
from .models import *
# Register your models here.

class AtencionClinica_DetalleProductosAdmin(admin.TabularInline):
    model = AtencionClinica_DetalleProductos
    list_display = ('atencion_clinica','codigo_producto','cantidad',)
    extra = 1

class AtencionClinica_DetalleMedicinaAdmin(admin.TabularInline):
    model = AtencionClinica_DetalleMedicina
    list_display = ('atencion_clinica','medicina','dosis',)
    extra = 1

class AtencionClinicaAdmin(admin.ModelAdmin):
    model = AtencionClinica
    list_display = ('fecha','mascota','veterinario','diagnostico','proxima_cita','observaciones')
    inlines =[AtencionClinica_DetalleProductosAdmin,AtencionClinica_DetalleMedicinaAdmin,]

class CitaAdmin(admin.ModelAdmin):
    model = Cita
    list_display = ('fecha','veterinario','mascota')

admin.site.register(AtencionClinica,AtencionClinicaAdmin)
admin.site.register(Cita,CitaAdmin)
#admin.site.register(AtencionClinica_DetalleMedicina)
#admin.site.register(AtencionClinica_DetalleProductos)
