from django.urls import path
from . import views

app_name = "app_sensores"

urlpatterns = [
    path('', views.crear_sensor_estanque),
    path('lista_sensores_estanque/', views.lista_sensores_estanque, name = 'lista_sensores_estanque'),
    path('agregar_sensor_estanque/', views.agregar_sensor_estanque, name = 'agregar_sensor_estanque')
]