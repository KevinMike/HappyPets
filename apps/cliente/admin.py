from django.contrib import admin
from apps.cliente.models import Cliente
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    model=Cliente
    list_display = ('dni','nombre','apellido','telefono','email',)