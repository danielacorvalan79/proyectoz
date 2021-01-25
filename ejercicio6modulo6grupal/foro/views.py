from django.shortcuts import render
from .models import Comentario

# Create your views here.
def inicio(request):
    lista_comentarios = list(Comentario.objects.all().values())
    context={"comentarios": lista_comentarios}
    return render (request, 'foro/inicio.html', context)