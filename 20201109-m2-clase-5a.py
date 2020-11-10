import requests

def sumar_dos_numeros(a, b):
    resultado = a + b
    return resultado

# esta lista incluye strings, enteros y flotantes
lista1 = ["hola", 2, 50, -20, 4.0, "Nombre", 2, "Nombre"]
print("\nLista 1:")
print(lista1)
for elemento in lista1:
    print(elemento, type(elemento))

# esta lista incluye strings, enteros, flotantes y otra lista
lista2 = [1, 2, 3, lista1, "otro elemento", "texto", 4.0]
print("\nLista 2:")
print(lista2)
for elemento in lista2:
    print(elemento, type(elemento))

# esta lista incluye strings, enteros, una función e incluso un módulo
lista3 = [1,2,3, "a", "texto", sumar_dos_numeros, requests]
print("\nLista 3:")
print(lista3)
for elemento in lista3:
    print(elemento, type(elemento))

resultado =  sumar_dos_numeros(1, 5)
print("sumar 1 y 5: ", resultado)

resultado = lista3[5](1,5)
print("sumar 1 y 5: ", resultado)

# una lista puede estar vacía
lista4 = []

# indexando listas:
#leer el elemento de la cuarta posición en lista3
print(lista3[3])

# lista son mutables --> puedo cambiar sus elementos
#lista3 antes del reemplazo
print("lista3 antes del reemplazo")
print(lista3)
lista3[1] = "reemplazo"
lista3[5] = 3.0
lista3[6] = "reeamplazando al modulo"
#lista3 después del reemplazo
print("lista3 después del reemplazo")
print(lista3)

# largo de una lista
largo_lista3 = len(lista3)
print("Largo lista3:", largo_lista3)

# operador + sobre listas (concatenando)
resultado = lista1 + lista2
print("lista1:", lista1)
print("lista2", lista2)
print("resultado de aplicar operador +", resultado)

# segmentando listas 
# IMPORTANTE: Los intervalos en python son cerrados por la izq y abiertos por la derecha
# En matemáticas la notación es [1, 5[
print("lista1:", lista1)
print("lista2", lista2)

print("todo",  lista1[:]    ) # lo mismo que poner lista1 sin indexación
print("[:5]",  lista1[:5]    ) 
print("[4:]",  lista1[4:]    )
print("[2:5]", lista1[2:5]    ) 
print("[-1]",  lista1[-1]    )
print("[-2]",  lista1[-2]    )
print("[-3]",  lista1[-3]    )

print(dir(lista1))
print(dir(lista2))

# métodos de listas 
#append: agrega un elemento al final de la lista

lista1.append("soy un agregado")
print(lista1)

#pop: saca un elemento de la lista de la posicion indicada
print(lista1[3]) # muestra el elemento de indice 3
print(lista1.pop(3)) # elimina de la lista el elemento de indice 3
print(lista1)
lista1.pop()
print("pop sin argumento:", lista1)

#remove: elimina la primera ocurrencia del elemento de valor indicado
lista1.remove("Nombre")
print(lista1)

#reverse: invierte una lista
lista1.reverse()
print(lista1)

# buscar elemento en una lista
lista5 = [23, 4, 345, 1234, 435, "José", 3, 1, 2, "José", 43, 5, 4]
print("345 está en lista 5",   345 in lista5         ) # 345 está en lista 5
print("José está en la lista5",  "José" in lista5      ) # José está en la lista5
print("Índice del elemento José en la lista",   lista5.index("José")  ) # Índice del elemento José en la lista
