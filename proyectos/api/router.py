from django.urls import path
from rest_framework.routers import DefaultRouter
from proyectos.api.views import ProyectoViewSet

router_proyectos = DefaultRouter()
router_proyectos.register(
    prefix='proyectos',
    viewset=ProyectoViewSet,
    basename='proyecto'
)

url_patterns = []