from django import forms
from .models import Asignatura

class FormularioAsignatura(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    departamento_id = forms.CharField(max_length=50)
