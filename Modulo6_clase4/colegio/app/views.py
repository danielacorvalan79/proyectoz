from django.shortcuts import render, redirect
from .models import Departamento, Alumno, Transportista, Asignatura
from .forms import FormularioAsignatura
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
def inicio(request):
    tabla_departamento=list(Departamento.objects.all().values())
    context={"departamento":tabla_departamento}
    return render (request, 'app/index.html', context)

def alumno(request):
    tabla_alumno=list(Alumno.objects.all().values())
    context={"alumno":tabla_alumno}
    return render (request, 'app/alumnos.html', context)

def transportista(request):
    tabla_transportista=list(Transportista.objects.all().values())
    context={"transportista":tabla_transportista}
    return render (request, 'app/transportista.html', context)

def asignatura(request):
    tabla_asignatura=list(Asignatura.objects.all().values())
    context={"asignatura":tabla_asignatura}
    return render (request, 'app/asignatura.html', context)

def usuario_profesor(usuario):
    es_profesor=usuario.is_superuser
    return es_profesor


class AgregarAsignatura(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=Asignatura
    template_name='app/agregar_asignatura.html'
    fields='__all__'
    success_url=reverse_lazy('app:asignatura')
    #form_class=FormularioAsignatura

    def test_func(self):
        return usuario_profesor(self.request.user)

    """ def agregar_asignatura(request):
        formulario_asignatura=FormularioAsignatura(request.POST or None)
        context={'formulario':formulario_asignatura}
        if formulario_asignatura.is_valid():
            form_data = formulario_asignatura.cleaned_data
            Asignatura.objects.create(
                nombre= form_data['nombre'],
                descripcion= form_data['descripcion'],
                departamento_id= form_data['departamento_id'],
                )
            return redirect ('app:asignatura')               
        return render (request, 'app/agregar_asignatura.html', context)
  """

class Inicio(LoginRequiredMixin, View):
    def get (self, request):
        return render (request, 'app/inicio.html')    
