from django.shortcuts import render, redirect
from .models import SensorEstanque, SensorTemperatura, SensorPuerta, CodigoAcceso
from .forms import SensorEstanqueFormulario
import random
# Create your views here.
""" def crear_sensor_estanque(request):
    
    sensor = SensorEstanque.objects.create(
                        marca = 'Copec',
                        modelo = 'Temporin A1',
                        nombre = 'Sensor Sensible v1',
                        nivel = 'Medio'
                        
                        )
    sensor = SensorEstanque.objects.create(
                        marca = 'Proto',
                        modelo = 'Temporin A2',
                        nombre = 'Sensor Sensible v2',
                        nivel = 'Bajo'
                        
                        )
    sensor = SensorEstanque.objects.create(
                        marca = 'Shell',
                        modelo = 'Temporin A1',
                        nombre = 'Sensor Sensible v3',
                        nivel = 'Medio'
                        
                        )
    sensor = SensorEstanque.objects.create(
                        marca = 'Petrobras',
                        modelo = 'Temporin A1',
                        nombre = 'Sensor Sensible v4',
                        nivel = 'Alto'
                        
                        )                
    sensor.save()

    context = {'key1': SensorEstanque.objects.values()}
    return render(request, 'app_sensores/sensor_estanque.html', context) """


def crear_sensor_estanque(request):
    lista = ['Copec', 'Shell', 'Petrobras', 'Perpent']
    for i in range(0,4):

        sensor = SensorEstanque.objects.create(
                        marca = random.choice(lista),
                        modelo = 'Temporin A1',
                        nombre = 'Sensor Sensible v1',
                        nivel = 'Medio'
                        
                        )
    
                        
                                        
        sensor.save()

    context = {'key1': SensorEstanque.objects.values()}
    return render(request, 'app_sensores/sensor_estanque.html', context)

def lista_sensores_estanque(request):
    lista_sensores_estanque = list(SensorEstanque.objects.all().values())
    sensores_estanque = {'sensores_estanque': lista_sensores_estanque}
    return render(request, 'app_sensores/sensor_estanque.html', context=sensores_estanque)

def agregar_sensor_estanque(request):
    formulario = SensorEstanqueFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        SensorEstanque.objects.create(
                    marca=form_data['marca'], 
					modelo=form_data['modelo'], 
					nombre=form_data['nombre'], 
					nivel=form_data['nivel'],
                    )
        return redirect('app_sensores:lista_sensores_estanque')
    return render(request, 'app_sensores/agregar_sensor_estanque.html', context)