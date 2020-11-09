
# Este es nuestro primer comentario

'''
Este es un comentario
multilinea
en python
'''

# define variable string e imprime
nombre= "Daniela" # nombre principal
print(nombre) # imprimir el nombre


# pregunta nombre y saluda
nombre = input("¿Cuál es tu nombre?: ")


# alcance de variables
# en qué parte del código es visible la variable

precio = 10000
print(precio)

for numero in [1,2,3,4,5,6]:
    print(numero)

print(numero)

# funcion en javascript: 
# function suma(a,b) { 
#     resultado = a + b; 
#     return resultado; 
# }

# funcion en python
def suma(a, b):
    resultado = a + b
    return resultado

variable_resultado_suma = suma(3,4)
print(variable_resultado_suma)

# alcance de variables
print("")
print(precio)
print(numero)
print(variable_resultado_suma)
# print(resultado) # error de alcance de variable, resultado no es visible aqui

# tipos de datos

# numeros enteros
numero_entero = 3
numero_entero2 = -300
print(numero_entero + numero_entero2)

# numeros flotante
numero_real = 3.45
numero_real2 = 5.89
resultado_multiplicacion = numero_real * numero_real2
print(resultado_multiplicacion)
print(round(resultado_multiplicacion, 1))

# comparación de numeros
print(numero_real == numero_real2)
a = 1
b = 1
print(a == b)

# strings o cadena de caracteres
nombre_y_apellido = "Eduardo Tapia"
print(nombre_y_apellido)
nombre_y_apellido2 = "Joao Guzmán"
print(nombre_y_apellido2)

print(nombre_y_apellido + ", " + nombre_y_apellido2)


# operacion de dos variables de distinto tipo

# en javascript
# >> console.log("Numero: " + 5)
# >> Numero: 5

print("Numero: " + str(5))

# Otras operaciones con strings
print("José "*6)
print("José " + "José " + "José " + "José " + "José " + "José ")

# variables más sofisticadas

# listas
#lista1 = []
print("\nListas: ")
lista1 = [2, 4, 5, "Hola", "café", 500, 45.67]
print(lista1)
#acceder a elementos de lista
print(lista1[3])
lista1[3] = "Chao" # modifica el elemento 3 de la lista
print(lista1)
print(lista1[3])
# agregar elemento a lista
lista1.append("Soy nuevo")
print(lista1)
# insertar elemento a lista en posicion
lista1.insert(2, "Me agregaron aquí, yo no tengo la culpa")
print(lista1)
# inserto cualquier cosa dentro de lista
lista1.insert(1, [55, 66, 77, 88])
print(lista1)
# largo de la lista
print(len(lista1))


# tuplas INMUTABLES
# tupla1 = ()
print("\nTuplas: ")
tupla1 = (2,4,5, "Hola", "café", 500, 45.67)
print(tupla1)
print(tupla1[3])
# lo siguiente no funciona en tuplas
# tupla1[3] = "Chao"
# print(tupla1)
# print(tupla1[3])


# diccionarios
#diccionario1 = {}
print("\nDiccionarios: ")

diccionario1 = {'nombre': 'Eduardo', 'Apellido': 'Tapia', 'Edad': 25, 'Direccion': 'Av. G.'}
print(diccionario1)
# seleccionar elemento de diccionario
print(diccionario1['Apellido'])
# reasignar valor a nombre
diccionario1['nombre'] = 'Felix'
print(diccionario1)


# if





# iteraciones
print("\nIteraciones")

# for
for elemento in lista1:
    print(elemento)

print("")
for elemento in lista1:
    if isinstance(elemento, int):
        print(str(elemento), " El elemento es un Entero")
    else:
        print(str(elemento), " El elemento no es un Entero")

# cómo iterar sobre un diccionario? Pista: usar en for diccionario1.items()



# while

c = 0 
while c < 100:
    print(c) 
    c = c + 1



