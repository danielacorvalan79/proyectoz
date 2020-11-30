#!/usr/bin/env python
# coding: utf-8

# <span><p style="text-align:right; display: inline-block;">
#     <img style="display: inline-block;" src="https://www.solvetic.com/uploads/monthly_01_2016/tutorials-1415-0-60642300-1452279191.jpg">
# </p></span>
# 
# <p style="font-size: 170%;text-align: right; color:#555">Manejo de Archivos</p>
# 
# ---  
# <p style="text-align: right; color:blue;"> luis.jaraquemada@team.awakelab.cl  </p>

# # Accediendo a Archivos desde Python
# 
# - La función `open()` se utiliza para acceder a archivos desde Python.  
# 
# - Para archivos de texto, sólo se debe pasar el nombre del archivo a la función `open()`. El archivo se abre en modo lectura y los bytes se convierten a texto según la codificación de la plataforma.  
# 
# - Existen los parámetros `encoding` y `errors`, para especificar la codificación y para manejar bytes inválidos. 
# 
# - [Documentación Oficial Función Open en Python3](https://docs.python.org/3/library/functions.html#open)  
# - Encodings: Principalmente `utf-8` (8-bit Unicode), `utf-16` (16-bit Unicode), o `utf-32` (32-bit)
# https://docs.python.org/3/library/codecs.html#standard-encodings  

# # Modos para abrir un archivo en Python
# 
# - `r`: Sólo lectura, puntero al inicio del archivo.
# - `rb`: Sólo lectura en formato binario, puntero al inicio. 
# - `rb+`: Lectura y escritura en formato binario, puntero al inicio.
# - `w`: Sólo escritura, crea archivo, o sobreescribe si ya existe.
# - `wb`: Sólo escritura en formato binario, crea archivo, o sobreescribe si ya existe.
# - `w+`: Escritura y lectura. Sobreescribe archivo existente o crea nuevo.
# - `wb+`: Escritura y lectura en formato binario. Sobreescribe archivo existente o crea nuevo.
# - `a`: Agrega, puntero al final del archivo. Si no existe crea nuevo archivo.
# - `ab`: Agrega en formato binario. Puntero al final del archivo. Si no existe el archivo crea nuevo.
# - `a+`: Agrega o lee. Puntero al final del archivo. Si no existe crea el archivo.
# - `ab+`: Agrega o lee en formato binario. Puntero al final del archivo. Si no existe crea el archivo.

# # Escribiendo datos a un archivo desde Python
# 

# In[ ]:


contenidos = "Nuestro primeros datos valiosos a guardar en un archivo para uso futuro"
archivo_salida = open("data/datos.txt", "w")
archivo_salida.write(contenidos)
print("Hemos escrito en el archivo")
archivo_salida.close()


# In[ ]:


import random
import time
import datetime

# En este caso cada vez que el archivo se abre para escribir
# el Puntero queda posicionado al inicio del archivo
for i in range(0,10000):
    archivo_salida3 = open("data/datos_sensor_3.txt", "w")
    medicion3 = str(random.randint(28,40))
    archivo_salida3.write(medicion3)
    archivo_salida3.close()
    
# En este caso cada vez que el archivo se abre para escribir 
# el Puntero queda posicionado al final del archivo
for i in range(0,10000):
    tiempo_ahora = datetime.datetime.now()
    archivo_salida2 = open("data/datos_sensor.txt", "a")
    variable = random.randint(28,40)
    medicion = str(tiempo_ahora) + ", " + str(variable)
    archivo_salida2.write(medicion+ "\n")
    archivo_salida2.close()
    if variable > 38:
        print("PELIGRO!! Variable fuera de rango!!")
    time.sleep(1)


# # Recuperando datos desde un archivo desde Python

# In[ ]:


archivo_entrada = open('data/datos_sensor.txt', 'r')
print(archivo_entrada.read())
archivo_entrada.close()


# # Agregando datos a un archivo existente desde Python

# In[ ]:


contenidos = "\nEstos datos son agregados para esta clase"
archivo_salida = open("data/datos.txt", "a")
for i in range(0,100):
    archivo_salida.write(contenidos)
archivo_salida.close()


# # Accediendo a archivos con `with`

# In[ ]:


with open("data/quijote.txt") as archivo:
   quijote = archivo.read()
print(quijote)


# In[ ]:


with open("data/iris.csv") as archivo
   iris = archivo.read()
print(iris)


# In[ ]:


with open('data/output.txt', 'w') as archivo:
    archivo.write('Hola jovenes!')


# # Explorando datos de un archivo

# In[ ]:


with open("data/quijote.txt") as file:
    print(len(file.read()))
    file.seek(790000)
    print(file.read(100), "XXXXX")
    file.seek(0)
    #print(file.read())
    print(len(file.read()))
    file.seek(0)
    otro = file.read(200)
    file.seek(0)
    for i in range(0,8):
        print(file.readline())
    file.seek(0)
    # comenzar desde el comienzo
    for i in range(0,10):
        print(file.readline())
    file.seek(0)
    #busqueda de línea especifica
    for i, line in enumerate(file):
        if i == 5:
            print(line)


# # Archivos CSV

# In[72]:


import csv
with open('data/iris.csv', 'r') as file:
    reader = csv.reader(file)
    #for linea in reader:
    #    print(linea)
    datos = list(reader)

print("Forma Ineficiente")
acumulador_setosa = 0
contador_setosa = 0
acumulador_versicolor = 0
contador_versicolor = 0
acumulador_virginica = 0
contador_virginica = 0
for elemento in datos:
    print(elemento)
    if elemento[4]=="setosa":
        contador_setosa = contador_setosa + 1
        acumulador_setosa = acumulador_setosa + float(elemento[0])
    if elemento[4]=="versicolor":
        contador_versicolor = contador_versicolor + 1
        acumulador_versicolor = acumulador_versicolor + float(elemento[0])
    if elemento[4]=="virginica":
        contador_virginica = contador_virginica + 1
        acumulador_virginica = acumulador_virginica + float(elemento[0])

print("El promedio de Sepal_Length de las especies Setosa es: ", round(acumulador_setosa/contador_setosa,2))
print("El promedio de Sepal_Length de las especies Versicolor es: ", round(acumulador_versicolor/contador_versicolor,2))
print("El promedio de Sepal_Length de las especies Virginica es: ", round(acumulador_virginica/contador_virginica,2))
        
    
print("Forma más eficiente")
def promedio(especie, variable, datos):
    variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    indice_variable = variables.index(variable)
    acumulador= 0
    contador = 0
    for elemento in datos:
        if elemento[4] == especie:
            contador = contador + 1
            acumulador = acumulador + float(elemento[indice_variable])
    return round(acumulador/contador, 2)

variable = "sepal_length"
especie = "virginica"
print("El promedio de " 
      + variable 
      + " de las especies "
      + especie 
      + " es: ", 
          promedio(especie, variable, datos))

    


# In[ ]:


import csv
with open('salida.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Luis', 'Perez', '46'])
    writer.writerow(['Claudia', 'Reyes', '37'])


# In[74]:


import csv

with open('data/personas.csv', mode='w') as csv_file:
    fieldnames = ['nombre', 'apellido', 'edad']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'nombre': 'Luis', 'apellido': 'Perez', 'edad': 30})
    writer.writerow({'nombre': 'Claudia', 'apellido': 'Reyes', 'edad': 40})


# # Archivos con objetos de Python

# In[78]:


import pickle

data = ["elemento", "nombre", 5,
        "otro texto", ["lista0", "lista1"]]

class Arbol:
    def __init__(self, altura):
        self.componente_quimico=self.__calculo()
        self.altura=altura
        
    def crecer(self, cuanto):
        self.altura += cuanto
        
    def __calculo(self):
        #llamar a base de datos masiva y hace un calculo que demora 24 hora
        pass

arbol1=Arbol(10)

#with open("data/datos_pickle", 'wb') as file:
#    pickle.dump(arbol1, file)
with open("data/datos_pickle", 'rb') as file:
    data_cargada = pickle.load(file)
print(data_cargada)


# In[99]:


import json
with open('data/datos.json') as archivo:
    linea = archivo.readline()

data = json.loads(linea) # crea un diccionario
print(data['albums']['genero'])

data['albums']['genero'] = "jazz"

with open('data/datos.json', 'w') as archivo:
    string_json = json.dumps(data) # creo un string json desde el diccionario python
    archivo.write(string_json)


# In[129]:


class Inventario:
    def __init__(self):
        self.__nombre_archivo = "data/inventario"+self.__repr__()+".txt"
        self.__crear_archivo()
    
    def __crear_archivo(self):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("Inventario Iniciado")
    
    def agregar_elemento(self, elemento):
        with open(self.__nombre_archivo, 'a') as file:
            file.write("\n"+elemento)


# In[130]:


bodega_sillas = Inventario()


# In[134]:


bodega_sillas.agregar_elemento("Silla de Terraza 06")


# In[135]:


bodega_materiales = Inventario()


# In[140]:


bodega_materiales.agregar_elemento("Palo forma 6")


# <span><p style="text-align:right; display: inline-block;">
#     <img style="display: inline-block;" src="https://www.solvetic.com/uploads/monthly_01_2016/tutorials-1415-0-60642300-1452279191.jpg">
# </p></span>
# 
