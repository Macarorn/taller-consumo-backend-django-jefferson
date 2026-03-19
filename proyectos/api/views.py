from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from proyectos.models import Proyecto
from proyectos.api.serializers import ProyectoSerializer


class ProyectoViewSet(ModelViewSet):
    
    permission_classes = [AllowAny]
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()
    
    def get_queryset(self):

        queryset = Proyecto.objects.all()
        estado = self.request.query_params.get('estado', None)
        
        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset