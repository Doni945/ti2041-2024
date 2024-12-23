"""
URL configuration for gestion_productos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos.views import (
    lista_productos, 
    registro_producto, 
    resultado_producto, 
    consulta_productos, 
    inicio_sesion, 
    despliegue_productos,
    cerrar_sesion,
    acceso_denegado
)
from productos.api import api  # Importamos la instancia de NinjaAPI desde el archivo api.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_sesion, name='login'),  # Página de inicio de sesión
    path('lista/', lista_productos, name='lista_productos'),  # Ruta para la lista de productos
    path('registro/', registro_producto, name='registro_producto'),
    path('resultado/', resultado_producto, name='resultado_producto'),
    path('consulta/', consulta_productos, name='consulta_productos'),
    path('despliegue/', despliegue_productos, name='despliegue_productos'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),  # Ruta para cerrar sesión
    path('acceso_denegado/', acceso_denegado, name='acceso_denegado'),  # Ruta para acceso denegado
    path('api/', api.urls),  # Punto de entrada para la API
    # Rutas para JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener tokens de acceso y actualización
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar el token de acceso
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verificar validez de un token
]


