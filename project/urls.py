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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, saludar_a, sumar, buscar, mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, AltaMascota, mostrar_mascotas, BuscarMascota, mostrar_automovil, AltaAutomovil, BuscarAutomovil, ActualizarMascota, BorrarMascota, ActualizarAutomovil, BorrarAutomovil, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from ejemplo_dos.views import index, PostListar, PostCrear, PostBorrar, PostActualizar, PostDetalle, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle
from django.contrib.admin.views.decorators import staff_member_required

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
    path('mi-mascota', mostrar_mascotas),
    path('mi-mascota/buscar', BuscarMascota.as_view(), name="mi-mascota/buscar"),
    path('mi-mascota/alta', AltaMascota.as_view(),name="mi-mascota/alta"),
    path('mi-mascota/actualizar/<int:pk>', ActualizarMascota.as_view(), name="mi-mascota/actualizar"),
    path('mi-mascota/borrar/<int:pk>', BorrarMascota.as_view(),name="mi-mascota/borrar"),
    path('mi-automovil', mostrar_automovil),
    path('mi-automovil/buscar', BuscarAutomovil.as_view(), name= "mi-automovil/buscar"),
    path('mi-automovil/alta', AltaAutomovil.as_view(), name= "mi-automovil/alta"),
    path('mi-automovil/actualizar/<int:pk>', ActualizarAutomovil.as_view(), name="mi-automovil/actualizar"),
    path('mi-automovil/borrar/<int:pk>', BorrarAutomovil.as_view(),name="mi-automovil/borrar"),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view(), name="panel-familia-borrar"),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view(), name="panel-familia-actualizar"),
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', PostBorrar.as_view(), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', PostActualizar.as_view(), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/signup', UserSignUp.as_view(), name= "ejemplo-dos-signup"),
    path('ejemplo-dos/login', UserLogin.as_view(), name= "ejemplo-dos-login"),
    path('ejemplo-dos/logout', UserLogout.as_view(), name= "ejemplo-dos-logout"),
    path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    path('ejemplo-dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    path('ejemplo-dos/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    path('ejemplo-dos/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    path('ejemplo-dos/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 