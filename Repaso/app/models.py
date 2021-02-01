from django.db import models

# Create your models here.

class Paciente(models.Model):
    run = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

