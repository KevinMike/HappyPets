from django.contrib import admin
from .models import *
# Register your models here.
class AtencionClinicaAdmin(admin.ModelAdmin):
    model = AtencionClinica
    list_display = ('fecha','mascota','veterinario','diagnostico','proxima_cita','observaciones')

class CitaAdmin(admin.ModelAdmin):
    model = Cita
    list_display = ('fecha','veterinario','mascota')

admin.site.register(AtencionClinica,AtencionClinicaAdmin)
admin.site.register(Cita,CitaAdmin)
