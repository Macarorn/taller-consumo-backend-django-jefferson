from rest_framework import serializers
from proyectos.models import Proyecto


class ProyectoSerializer(serializers.ModelSerializer):
    
    creado_por_username = serializers.CharField(
        source='creado_por.username',
        read_only=True
    )
    
    class Meta:
        model = Proyecto
        fields = [
            'id_proyecto',
            'nombre',
            'descripcion',
            'tipo',
            'estado',
            'fecha_inicio',
            'fecha_fin_est',
            'creado_por',
            'creado_por_username',
            'fecha_creacion',
        ]
        read_only_fields = ['id_proyecto', 'fecha_creacion', 'creado_por_username']
        
    def validate_nombre(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("El nombre del proyecto no puede estar vacío")
        return value
    
    def validate(self, data):
        if data.get('fecha_inicio') and data.get('fecha_fin_est'):
            if data['fecha_inicio'] > data['fecha_fin_est']:
                raise serializers.ValidationError(
                    "La fecha de inicio no puede ser posterior a la fecha de fin"
                )
        return data
