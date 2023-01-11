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
from django.views.generic import TemplateView
from vacaciones.views import index, PostListar, PostCrear, PostBorrar, PostActualizar, PostDetalle, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacaciones/', index, name="vacaciones-index"),
    path('vacaciones/listar/', PostListar.as_view(), name="vacaciones-listar"),
    path('vacaciones/crear/', PostCrear.as_view(), name="vacaciones-crear"),
    path('vacaciones/<int:pk>/borrar/', PostBorrar.as_view(), name="vacaciones-borrar"),
    path('vacaciones/<int:pk>/actualizar/', PostActualizar.as_view(), name="vacaciones-actualizar"),
    path('vacaciones/<int:pk>/detalle/', PostDetalle.as_view(), name="vacaciones-detalle"),
    path('vacaciones/signup/', UserSignUp.as_view(), name= "vacaciones-signup"),
    path('vacaciones/login/', UserLogin.as_view(), name= "vacaciones-login"),
    path('vacaciones/logout/', UserLogout.as_view(), name= "vacaciones-logout"),
    path('vacaciones/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="vacaciones-avatars-actualizar"),
    path('vacaciones/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="vacaciones-users-actualizar"),
    path('vacaciones/mensajes/crear/', MensajeCrear.as_view(), name="vacaciones-mensajes-crear"),
    path('vacaciones/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="vacaciones-mensajes-detalle"),
    path('vacaciones/mensajes/listar/', MensajeListar.as_view(), name="vacaciones-mensajes-listar"),
    path('vacaciones/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="vacaciones-mensajes-borrar"),
    path('vacaciones/about/', TemplateView.as_view(template_name='vacaciones/about.html'), name="vacaciones-about"),    
    ]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 