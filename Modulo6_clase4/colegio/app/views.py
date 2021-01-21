from django.shortcuts import render
from .models import Departamento, Alumno, Transportista

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