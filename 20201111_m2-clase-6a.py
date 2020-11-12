# argumentos y parametros en una funcion
def sumar_dos_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def multiplicar_dos_numero(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


# variables que viven en el mundo exterior a función.
nombres = ["Pedro", "Álvaro", "Daniela", "Rocío", "Cinthia", "José", "Eduardo"]
num = 4000000

edad_pedro = 30
edad_manuel = 40
suma_de_edades = sumar_dos_numeros(edad_pedro, edad_manuel)
print("Suma de edades: ", suma_de_edades)

insectos = 500
ameba = 600
suma_de_insectos = sumar_dos_numeros(insectos, ameba)
print("Suma de insectos: ", suma_de_insectos)

# experimentar instentando acceder a variables de función
try:
    print("Variable resultado que fué creada en función sumar_dos_numeros(): ", resultado)
except Exception as e:
    print("Error: ", e)
    print("Se genera error porque variable resultado es interna (Local) en la función!!!")

# lectura de variable del programa principal dentro de una función 
def sumar_dos_numeros_version2(numero1, numero2):
    resultado = numero1 + numero2 + num # mala práctica!!! leer variables globales desde función
    return resultado

suma_de_edades_version2 = sumar_dos_numeros_version2(edad_pedro, edad_manuel)
print("Suma de edades versión 2: ", suma_de_edades_version2)

# forzar a que variable definida dentro de una función sea visible en el exterior (Definirla como Global)
def sumar_dos_numeros_version3(numero1, numero2):
    mensaje_de_auxilio = "ayúdenme por favor, sufro de violencia laboral"
    resultado = numero1 + numero2 + num # mala práctica!!! leer variables globales desde función
    return resultado

suma_de_edades_version3 = sumar_dos_numeros_version3(edad_pedro, edad_manuel)
print("Suma de edades versión 3: ", suma_de_edades_version3)

try: 
    print("Mensaje misterioso: ", mensaje_de_auxilio)
except Exception as e:
    print("Error: ", e)
    print("La variable no se puede leer en el exterior pues es local en la función")

def sumar_dos_numeros_version4(numero1, numero2):
    global mensaje_de_auxilio
    mensaje_de_auxilio = "ayúdenme por favor, sufro de violencia laboral"
    resultado = numero1 + numero2 + num # mala práctica!!! leer variables globales desde función
    return resultado

suma_de_edades_version4 = sumar_dos_numeros_version4(edad_pedro, edad_manuel)
print("Suma de edades versión 4: ", suma_de_edades_version4)
print("Mensaje misterioso: ", mensaje_de_auxilio) # MALA PRÁCTICA!!! ahora se puede acceder variable creada desntro de función

# Nota: Los dos casos anteriores son malas prácticas y llevan al Código Spaghetti


# ejemplo de función existente en python con parámetros por defecto
# print()
'''
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
print("Hola", "Mundo")
print("Hola", "Mundo", sep="$$$", end="XXXXXXX")



# función creada por nosotros con parámetros por defecto
def sumar_dos_numeros_version5(numero1, numero2, num_adicional=0, mensaje_especial=""):
    resultado = numero1 + numero2 + num_adicional
    return resultado, mensaje_especial

print()
print("Uso de función version5 sin pasar argumentos para parametros por defecto", 
            sumar_dos_numeros_version5(4,5))
print("Uso de función version5 pasando argumentos para parametros por defecto", 
            sumar_dos_numeros_version5(4,5, num_adicional=100, mensaje_especial = "Atención Atención"))