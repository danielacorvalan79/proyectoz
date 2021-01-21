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
    asignatura = models.ManyToManyField(Asignatura)


class Transportista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_contratacion = models.DateField()
    sueldo = models.IntegerField()
    
class Curso(models.Model):
    nivel = models.CharField(max_length=50)
    cantidad_de_alumnos = models.IntegerField()
    profesor = models.ManyToManyField(Profesor)


class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Transportista = models.ForeignKey(Transportista, on_delete=models.SET_NULL, null=True)




