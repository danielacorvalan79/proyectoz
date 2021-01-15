from django.shortcuts import render
from .models import SensorEstanque, SensorTemperatura, SensorPuerta, CodigoAcceso
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
