from django.shortcuts import render
from ejemplo.models import Familiar

from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request, 
    "ejemplo/saludar_a.html",
    {"nombre": nombre})

def sumar(request, a, b ):
    return render(request,
    "ejemplo/sumar.html",
    {"a": a,
    "b": b,
    "resultado": a + b
    })

def buscar(request):
    lista_de_nombres= ["Melanie","Ingrid","Ronnie"]
    query= request.GET['q']
    if query in lista_de_nombres:
        indice_del_resultado = lista_de_nombres.index(query)
        resultado= lista_de_nombres[indice_del_resultado]
    else:
        resultado= "No hay match"
    return render(request,
    "ejemplo/buscar.html",
    {"resultado": resultado})

def mostrar_familiares(request):
    lista_familiares= Familiar.objects.all()
    return render(request,
    "ejemplo/familiares.html", 
    {"lista_familiares": lista_familiares})