from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    
    ESTADO_CHOICES = [
        ('inicio', 'Inicio'),
        ('activo', 'Activo'),
        ('pausado', 'Pausado'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='inicio'
    )
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin_est = models.DateField(null=True, blank=True)
    creado_por = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'proyecto'
        ordering = ['-fecha_creacion']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return f"{self.nombre} ({self.estado})"