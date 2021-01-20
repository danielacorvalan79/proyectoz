from django.shortcuts import render
from .models import Departamento

# Create your views here.
def inicio(request):
    tabla_departamento=list(Departamento.objects.all().values())
    context={"departamento":tabla_departamento}
    return render (request, 'app/index.html', context)