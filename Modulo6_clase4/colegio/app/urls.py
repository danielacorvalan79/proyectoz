from django.urls import path 
from . import views

app_name='app'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos', views.alumno, name='alumno'),
    path('transportista', views.transportista, name='transportista'),
    path('asignatura', views.asignatura, name='asignatura'),
    path('agregar_asignatura', views.agregar_asignatura, name='agregar_asignatura')

]