from django.db import models

# Create your models here.
class Comentario (models.Model):
    mombre = models.CharField(max_length=50)
    fecha = models.DateField()
    correo = models.EmailField(max_length=100)
    comentario = models.CharField(max_length=500)
