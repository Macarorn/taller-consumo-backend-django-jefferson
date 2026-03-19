from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from proyectos.api.router import router_proyectos

# Configuración de Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="SCRUM API",
      default_version='v1',
      description="API REST para Sistema de Gestión de Proyectos con Scrum",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contacto@scrum.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Swagger & ReDoc
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API Routes
    path('api/', include(router_proyectos.urls)),
]