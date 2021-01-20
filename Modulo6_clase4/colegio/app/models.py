from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    escuela= models.CharField(max_length=100)
    fecha_de_contratacion= models.DateField()
    sueldo = models.IntegerField()