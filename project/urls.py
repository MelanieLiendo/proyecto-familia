"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (index, saludar_a, sumar, buscar, mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, AltaMascota, mostrar_mascotas, BuscarMascota, mostrar_automovil, AltaAutomovil, BuscarAutomovil)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a ),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view(), name="mi-familia/buscar"),
    path('mi-familia/alta', AltaFamiliar.as_view(), name="mi-familia/alta"),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view(), name="mi-familia/actualizar"),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view(),name="mi-familia/borrar"),
    path('mi-mascota/alta', AltaMascota.as_view(),name="mi-mascota/alta"),
    path('mi-mascota', mostrar_mascotas),
    path('mi-mascota/buscar', BuscarMascota.as_view(), name="mi-mascota/buscar"),
    path('mi-automovil', mostrar_automovil),
    path('mi-automovil/alta', AltaAutomovil.as_view(), name= "mi-automovil/alta"),
    path('mi-automovil/buscar', BuscarAutomovil.as_view(), name= "mi-automovil/buscar")]

