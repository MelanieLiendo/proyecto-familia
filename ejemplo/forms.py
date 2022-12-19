from django import forms
from ejemplo.models import Familiar, Mascota, Automovil

#Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']


#Mascota

class BuscarMascota(forms.Form):
    nombre = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))
  

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['animal', 'nombre']

#Automovil


class BuscarAutomovil(forms.Form):
    color = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))


class AutomovilForm(forms.ModelForm):
  class Meta:
    model = Automovil
    fields = ['marca', 'color']


