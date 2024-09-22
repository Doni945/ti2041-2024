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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
]

from django.contrib import admin
from django.urls import path
from productos.views import registro_producto, resultado_producto, consulta_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registro_producto, name='registro_producto'),  # Redirige a la vista de registro
    path('registro/', registro_producto, name='registro_producto'),  # Nombre correcto
    path('resultado/', resultado_producto, name='resultado_producto'),
    path('consulta/', consulta_productos, name='consulta_productos'),
]
