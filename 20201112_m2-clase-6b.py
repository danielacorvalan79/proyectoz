import time
import random

# ejemplo de funciones, variables, globales y mutabilidad/inmmutabilidad de 
# listas, y otras variables

archivo_personal_historico = []

def progreso():
    for i in range(0, 40):
        print(".", end="", flush=True)
        time.sleep(0.01)
    print()

def pedir_pizza(dir, lista_ingr, p):
    print("\nGenerando Lista Ingredientes Totales:")
    progreso()
    print("ID antes de modificar lista_ingr: ", id(lista_ingr))
    lista_ingr.extend(["salsa de tomate", "queso", "masa", "oregano"])
    print("ID despues de modificar lista_ingr: ", id(lista_ingr))
    print("Los ingredientes finales son: ", lista_ingr)
    print("Generando Precio Final:")
    progreso()
    print("ID antes de modificar p: ", id(p))
    p = p + 500 * (len(lista_ingr)-7)
    print("ID despues de modificar p: ", id(p))
    print("El Precio Final es: ", p)
    print("Coordinando Despacho:")
    progreso()
    print("ID antes de modificar dir: ", id(dir))
    dir = dir + " ID: " + str(random.randint(1000, 9999))
    print("ID despues de modificar dir: ", id(dir))
    print("El identificador de despacho es: ", dir)
    return dir, p, lista_ingr

# programa principal
for veces in range(0,2):
    # Datos para encargar
    mi_direccion = "Calle # 13"
    precio = 10000
    ingredientes_a_pedir = ["aceituna", "pepperoni", "tocino", "doble queso", "piña", "huevo"]

    print("ID en programa princiap de mi_direccion: ", id(mi_direccion))
    print("ID en programa princiap de precio: ", id(precio))
    print("ID en programa princiap de ingredientes_a_pedir ", id(ingredientes_a_pedir))

    mi_direccion, precio, ingredientes_a_pedir = pedir_pizza(mi_direccion, ingredientes_a_pedir, precio)

    archivo_personal_historico.extend((mi_direccion, ingredientes_a_pedir, precio))

# revisión del histórico
print()
for elemento in archivo_personal_historico:
    print(elemento)


# cantidad indefinida de argumentos en una funcion
def sumar(*args):
    resultado = 0
    for elemento in args:
        resultado = resultado + elemento
    return resultado

suma_de_muchos_numeros = sumar(2,3,4,5,6,43,5,4,3,2,43,5,6,2,3,4,5,6,43,5,4,3,2,43,
                                5,6,2,3,4,5,6,43,5,4,3,2,43,5,6,2,3,4,5,6,43,5,4,3,
                                5,6,2,3,4,5,6,43,5,4,3,2,43,5,6,2,3,4,5,6,43,5,4,3,                                
                                5,6,2,3,4,5,6,43,5,4,3,2,43,5,6,2,3,4,5,6,43,5,4,3,
                                2,43,5,6)

print("La suma de muchos numeros es: ", suma_de_muchos_numeros)


# cantidad indefinida de argumentos nombrados
def listar(**kwargs):
    for clave, valor in kwargs.items():
        print("Clave: ", clave, " Valor: ", valor)
    return kwargs

resultado = listar(direccion="Calle lkajsd", edad="75", nombre="Donald", apellido="Trump", varios_datos={'flor': 'rosa', 'animal': 'perro'})
print(resultado)