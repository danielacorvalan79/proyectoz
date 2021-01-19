from django import forms
from .models import SensorEstanque

class SensorEstanqueFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    nivel = forms.CharField(max_length=50)
