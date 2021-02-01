from django.urls import path 
from . import views

app_name='app'
urlpatterns = [
    path('', views.inicio, name='home'),
    path('alumnos', views.alumno, name='alumno'),
    path('transportista', views.transportista, name='transportista'),
    path('asignatura', views.asignatura, name='asignatura'),
    path('agregar_asignatura', views.AgregarAsignatura.as_view(), name='agregar_asignatura'),
    path('inicio/', views.Inicio.as_view(), name = 'inicio')

]