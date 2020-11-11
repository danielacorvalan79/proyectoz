# 1###########################################################################
# función range()

'''
for (let numero=0; numero<20; numero = numero +1) {
    console.log(numero);
}
'''
# funcion range()

#secuencia con paso 1
for numero in range(0,20):
    print(numero)

rango_numerico = range(0,20)
print("Resultado de función range: ", rango_numerico)
print("Tipo de datos: ", type(rango_numerico))
print("range transformado a lista", list(rango_numerico))

#secuencia con paso distinto de 1
rango_numerico = range(10, 100, 5)
print(list(rango_numerico))

# for recorre una secuencia de elementos data y ejecuta un codigo para cada iteración
#ejemplo 1
for elemento in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
    print(elemento)

#ejemplo 2
personas_formadas = [
    "Alvaro",
    "Boris", 
    "Cinthia",
    "Daniela",
    "Eduardo",
    "Diego",
    "Eduardo",
    "Eduardo2",
    "Germán",
    "Jean Carlos",
    "Jesús",
    "Joao",
    "José",
    "Manuel",
    "Martin",
    "Oscar",
    "Natalia",
    "Pedro",
    "Luis",
    "Rocío"]

import time
# peluquería
for persona_atendida in personas_formadas:
    print("\nAtendiendo a: ", persona_atendida)
    time.sleep(0.2)
    print("Al cliente: ", persona_atendida, " ya lo hemos hermoseado")
    print("Pase el siguiente")

#ejemplo iterando sobre tupla
comidas = ("ojo de pescado", "cerdo", "patas de gato", "cocodrilo", "patas de pollo", "cabeza de pollo")

for elemento in comidas: 
    print("Disfrutando de unos deliciosos: ", elemento)

#ejemplo iterando sobre diccionario
diccionario1 = {"pisco": "coca cola", "tequila": "limon", "wisky": "hielo", "cerveza": "limon"}
for elemento in diccionario1: # obtengo solo los keys
    print(elemento)

for elemento in diccionario1.keys(): # obtengo solo los keys
    print(elemento)

for elemento in diccionario1.values(): # obtengo solo los values
    print(elemento)

for elemento in diccionario1.items(): # obtengo keys y values
    print(elemento) 

for clave, valor in diccionario1.items(): # obtengo keys y values separados
    print("Key: ", clave, ", Value: ", valor)


# ejemplos varios

#encontrar el numero mayor: Forma 1
lista2 = [-9, -11, -100, -4, -3, -100 ,1000 , -20, 4, 6 ]
print("\nLista en análisis: ", lista2)
numero_mayor = lista2[0]
for indice_lista in range(0,len(lista2)):
    if lista2[indice_lista] > numero_mayor:
        numero_mayor = lista2[indice_lista]
print("El número mayor de la lista es: ", numero_mayor)

#encontrar el numero mayor: Forma 2
lista2 = [-9, -11, -100, -4, -3, -100 ,1000 , -20, 4, 6 ]
print("\nLista en análisis: ", lista2)
numero_mayor_anterior = 0
numero_mayor_actual = 0
for numero in lista2:
    if numero > numero_mayor_anterior:
        numero_mayor_anterior = numero
        numero_mayor_actual = numero
print("El número mayor es: ", numero_mayor_actual)

#encontrar el numero mayor: Forma 3
lista2 = [-9, -11, -100, -4, -3, -100 ,1000 , -20, 4, 6 ]
print("\nLista en análisis: ", lista2)
numero_mayor = lista2[0]
for numero in lista2:
    if numero > numero_mayor:
        numero_mayor = numero
print("El número mayor es: ", numero_mayor)

# interrupciones de loop for
print("\nInterrupción de loop for:")
for numero in range(0,100):
    if numero == 30:
        print("Estoy terminando el loop for con 'break'!!!")
        break
    elif numero == 20:
        print("Me estoy saltando con 'continue' el número: ", numero)
        continue
    print("El número actual: ", numero, " procesado es: ", 2*numero)
print("El último número al que llegué es: ", numero)


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\
# Forma rapida de imprimir la lista sacando los intrusos convirtiendo lista en conjuntos\*/*\*/*\*/*\

impostores=["niko","jose","kathe"]
alumnos=["qwerty","poiuy","lkjhgf","asdfg","zxcvb","niko"]

a= set(impostores)  # "set" El tipo set en Python es la clase utilizada por el lenguaje
# para representar los conjuntos. Un conjunto es una colección desordenada de elementos 
# únicos, es decir, que no se repiten. Este tutorial describe en detalle la clase set de 
# Python, sus principales usos y operaciones.


impostores=["niko","jose","kathe"]
alumnos=["qwerty","poiuy","lkjhgf","asdfg","zxcvb","niko"]

a= set(impostores)  # "set" El tipo set en Python es la clase utilizada por el lenguaje
# para representar los conjuntos. Un conjunto es una colección desordenada de elementos 
# únicos, es decir, que no se repiten. Este tutorial describe en detalle la clase set de 
# Python, sus principales usos y operaciones.
b= set(alumnos)

alumnos= list(b-a)
infiltrado= list(b&a)

print("Reportar por Infiltracion", infiltrado)
print("Alumnos Autorizados", alumnos)

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\