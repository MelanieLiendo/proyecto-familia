from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from vacaciones.models import Post, Mensaje
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from vacaciones.forms import UsuarioForm
from vacaciones.models import Avatar
from django.contrib.auth.admin import User


def index(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, "vacaciones/index.html", {"posts": posts})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post

class PostCrear(CreateView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy("vacaciones-listar")
    fields= '__all__'

class PostBorrar(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy("vacaciones-listar")

class PostActualizar(UpdateView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy("vacaciones-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('vacaciones-listar')

class UserLogin(LoginView):
    next_page= reverse_lazy('vacaciones-listar')

class UserLogout(LogoutView):
    next_page= reverse_lazy('vacaciones-listar')

class AvatarActualizar(UpdateView):
    model= Avatar
    fields= ['imagen']
    success_url= reverse_lazy('vacaciones-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('vacaciones-listar')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("vacaciones-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("vacaciones-mensajes-listar")