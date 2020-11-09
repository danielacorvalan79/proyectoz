'''
Módulo 2
Contenido 3
Instrucciones Condicionales
'''

import time
import random

# un caso de aplicacion de If
a = float(input("Ingrese el número A: "))
b = float(input("Ingrese el número B: "))

if a > b:
    m = a
    nombre_numero = "A"
else:
    m = b
    nombre_numero = "B"

print("El número mayor es: " + nombre_numero + " y su valor es: " + str(m))

# ejemplo de categorización de edades

edad_adolescente = 14
edad_adulto = 18

for intento in range(0, 5):
    print("Este es tu intento número: ", intento + 1)
    edad = int(input("Por favor ingrese la edad de individuo en análisis de edad: "))
    '''
    if (edad < 14) {
        console.log("Es un niño!");
    }
    '''
    if edad >= 0 and edad < 14:
        print("Es un Niño!")
        categoria = "Niño"
    elif edad >= 14 and edad < 18:
        print("Es un Adolescente!")
        categoria = "Adolescente"
    elif edad >= 18 and edad <65:
        print("Es un adulto!")
        categoria = "Adulto"
    elif edad >=65 and edad < 120:
        print("Es un adulto mayor!")
        categoria = "Adulto Mayor"
    elif edad >=120:
        print("Eres alguien increible!")
        categoria = "Increible"
    else:
        print("Tú desafías las leyes de la física y el tiempo!")
        categoria = "Imposible"

    # si desafía la física entonces llamar a seguridad nacional
    if categoria == "Imposible":
        print("Llamando a seguridad")
    # si es niño entonces dar un regalo
    elif categoria == "Niño":
        print("Enviando regalo")
    # si es un adolescente entonces huir a toda velocidad
    elif categoria == "Adolescente":
        #print("Huyendo raudamente!")
        #citar a sesión psicológica
        print("Enviando cita psicológica por Whatsapp..")
        print("Esperando al citado")
        time.sleep(random.randint(1, 10))
        print("El citado ha llegado")
        lista_respuestas = []
        contador = 1
        while contador <= 5:
            respuesta = input("Cuéntame tu problema N°: " + str(contador))
            lista_respuestas.append(respuesta)
            contador = contador + 1
        contador_de_silencios = 0
        for resp in lista_respuestas:
            if resp == "":
                contador_de_silencios = contador_de_silencios + 1
        if contador_de_silencios == len(lista_respuestas):
            print("El diagnóstico es PREOCUPANTE! Llamar a Padres!")
        else:
            print("Usted es un adolescente normal, vaya y siga con su vida, pero cancele la consulta al salir!")
    # si es un adulto inscribirlo en awakelab
    elif categoria == "Adulto":
        print("Inscribiendo en Awakelab")
    # si es adulto mayor ayudarlo a cruzar la calle
    elif categoria == "Adulto Mayor":
        print("Ayudando a cruzar calle")
    # si es increible hacer una fiesta
    elif categoria == "Increible":
        print("Haciendo fiesta")