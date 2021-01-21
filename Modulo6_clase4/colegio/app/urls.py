from django.urls import path 
from . import views

app_name='app'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos', views.alumno, name='alumno'),
    path('transportista', views.transportista, name='transportista')
]