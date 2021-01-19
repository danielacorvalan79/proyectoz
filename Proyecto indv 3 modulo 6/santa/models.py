from django.db import models

# Create your models here.
class SantaClaus(models.Model):
    nombre= models.CharField(max_length=50)

class Padres(models.Model):
    apellido_familiar= models.CharField(max_length=50)

class Ninos(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    id_padres= models.ForeignKey(Padres, on_delete=models.CASCADE, default=None)
    