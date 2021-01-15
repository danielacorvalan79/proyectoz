from django.db import models

# Create your models here.
class SensorTemperatura(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    temperatura = models.FloatField()
    registro = models.DateField(auto_now_add=True)

class SensorPuerta(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apertura = models.BooleanField()
    registro = models.DateField(auto_now_add=True)

class SensorEstanque(models.Model):
        marca = models.CharField(max_length=20)
        modelo = models.CharField(max_length=20)
        nombre = models.CharField(max_length=20)
        nivel = models.CharField(max_length=5)
        registro = models.DateField(auto_now_add=True)

class CodigoAcceso(models.Model):
    codigo = models.IntegerField()
    usuario = models.CharField(max_length=25, primary_key=True)
    registro = models.DateField(auto_now_add=True)


