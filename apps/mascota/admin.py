from django.contrib import admin
from .models import Mascota
# Register your models here.
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    model = Mascota
    list_display = ('nombre','cliente','tipo','raza','tipo_alimento','fecha_nacimiento',)
    list_filter = ('cliente__nombre',)

