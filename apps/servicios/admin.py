from django.contrib import admin
from .models import *
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    model = Servicios
    list_display = ('nombre','descripcion','precio',)

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','nombre','marca','descripcion','precio_venta',)

class DetalleServicioInline(admin.TabularInline):
    model = DetalleServicios
    extra = 1
class DetalleProductosInline(admin.TabularInline):
    model = DetalleProductos
    extra = 1

class AtencionServicioAdmin(admin.ModelAdmin):
    model = AtencionServicio
    fieldsets = (
        ('Atencion',{'fields': ('mascota','fecha','observaciones',)}),
    )
    list_display = ('mascota','fecha','observaciones',)
    inlines = [DetalleServicioInline,DetalleProductosInline]


admin.site.register(Servicios,ServicioAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(AtencionServicio,AtencionServicioAdmin)
