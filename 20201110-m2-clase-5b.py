
nombre_completo1 = ["Albert", "Nabucodonosor", "Einstein", "Orrigorrieta"]

nombre_completo2 = "Albert Nabucodonosor Einstein Orrigorrieta"

for elemento in nombre_completo1:
    print(elemento)

for elemento in nombre_completo2:
    print(elemento)

# concatenar strings con el operador +

texto_de_prueba = " Soy un ser humane"

resultado = nombre_completo2 + texto_de_prueba
print(resultado)


# strings con números

texto_con_numero = "500"
texto_con_numero2 = "400"

resultado = texto_con_numero + texto_con_numero2
print("Suma de textos con numeros: ", resultado)

#para poder sumarlos se debe transformar el Tipo de las variables

resultado = int(texto_con_numero) + int(texto_con_numero2)
print("Suma de textos con numeros tansformados a int: ", resultado)

# funcion inputa para obtener datos desde el usuario
# siempre obtiene strings!

datos_del_usuario = input("Ingrese lo que usted estime: ")
print(type(datos_del_usuario), datos_del_usuario)

# calculadora con input

suma = 0
while True: # lo mismo que decir para siempre
    datos_del_usuario = input("ingrese un numero (q pasa salir): ")
    if datos_del_usuario == "q":
        break
    suma = suma + float(datos_del_usuario)
    print("La suma hasta el momento es: ", suma)


# mutabilidad de un string
un_string = "carmen nos cuenta sobre la mutabilidad de los strings"

otro_string = "456"
print(id(otro_string), type(otro_string), otro_string)

otro_string = int(otro_string)
print(id(otro_string), type(otro_string), otro_string)

### CÓMO VERIFICAR SI MUTAMOS UN OBJETO O ES UNO NUEVO
# para saber si aún es el mismo objeto se revisa su id
lista = [1,2,3,4,5]
print(id(lista), type(lista), lista)
lista.pop(0)
lista.pop(0)
print(id(lista), type(lista), lista)
lista[1] = "un texto"
print(id(lista), type(lista), lista)
lista = [3,4,5]
print(id(lista), type(lista), lista)

#los strings son INMUTABLES
try:
    un_string[3] = "e"
    print(id(un_string), type(un_string), un_string)
except Exception as e:
    print("Error: ", e)
    print("Este error se debe a que intentamos reasignar un elemento de un string, y")
    print("los strings son INMUTABLES")

# puedo tomar como base un string y crear otro que asemeje al primero mutado, pero es
# uno nuevo
texto_modificado = un_string[:10] + "INSERCIÓN" + un_string[10:]
print(id(un_string), id(texto_modificado), type(texto_modificado), texto_modificado)

# indexando y segmentando (slicing) strings
print(  un_string[:]  )
print(  un_string[:10]  )
print(  un_string[10:]  )
print(  un_string[3:15]  )
print(  un_string[2:35:2]  )

# largo de un string
print(   len(un_string)   )

# iterar sobre strings
for elemento in un_string:
    print(elemento)

# métodos de strings
print(  un_string.capitalize()  )
print(  un_string.upper()  )
print(  un_string.count("c")  )
print(  un_string.replace("carmen", "Ruth")  )
print(  un_string  )


# Diccionarios!

print("\nDiccionarios:")
diccionario1 = dict() # crea diccionario vacío
print(diccionario1)
diccionario2 = {} # también crea un diccionario vacío
print(diccionario2)

# agregando datos al diccionario
diccionario3 = {'nombre': 'Pater', 'Apellido': 'Escobar', 'telefono': '56000000000'}
print(diccionario3)
try: 
    print(   diccionario3[2]    )
except Exception as e:
    print("ERROR: ", e)
    print("Este es un error porque los diccionario no se indexan por posicion!!!\nLos diccionarios no tienen orden")

# indexacion de diccionarios
print( diccionario3['telefono'] )

# diccionarios con claves repetidas
diccionario4 = {'nombre': 'Pater', 'nombre': 'Manuel', 'Apellido': 'Escobar', 'telefono': '56000000000'}
print( diccionario4['nombre'] ) # si hay claves repetidas entonces se conserva la última

# diccionarios más complejos
diccionario4 = {
                "rut": ("12.000.000-0", "3.456.4444-4", "34.232.222-4"),
                "nombres": ["Walter", "Carla", "Sofía"], 
                "apellidos": ["Bastías", "Moreno", "Díaz"],
                "edades": [20, 30, 40],
                "datos": [{"direccion": "Av. Italia 453", "telefono": "5600000000", "rut": "00.000.000-0"},
                        {"direccion": "Av. eee 453", "telefono": "560033330", "rut": "00.000.033-0"},
                        {"direccion": "Av. rrrr 453", "telefono": "5604444000", "rut": "00.000.330-0"}
                        ] }

print(diccionario4)

# indexación de diccionarios
print(  diccionario4['apellidos']  )
print(  diccionario4['datos']  )

# obteniendo diversos datos de una persona
print(  diccionario4['nombres'][0]  )
print(  diccionario4['edades'][0]   )
print(  diccionario4['datos'][0]['direccion']  )
print(  diccionario4['datos'][0]['telefono']  )

# para iterar se recurre a el metodo items() que se puede aplicar en diccionarios

print("\nIterando sobre diccionarios")
print(diccionario3)
print(   diccionario3.items()    )
for elemento in diccionario3.items():
    print(elemento)

for clave, valor in diccionario3.items():
    print(clave)
    print(valor)
    print()


import time
# contador de palabras en base a iteración sobre diccionarios
conteo = dict()
texto = input('Ingrese un texto: ')
palabras = texto.split()
print('Palabras:', palabras)
print('Contando...')
time.sleep(4)
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra,0) + 1

for cuenta in conteo.items():
    print(cuenta)






