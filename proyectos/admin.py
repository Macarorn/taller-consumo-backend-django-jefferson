from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'creado_por', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_creacion',)