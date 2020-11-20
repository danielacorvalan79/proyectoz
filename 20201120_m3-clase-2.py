'''
class SerVivo(object): # Creamos una clase en base a una clase plantilla llamada object 
    ...

class SerVivo0(): # Implícitamente está object como clase base
    ...

class SerVivo0: # Implicitamente está object como clase base
    ...
'''

# reflexión / investigación sobre atributos de clase y atributos de instancia
# Usaremos en este caso la más breve

# función para observar objetos
def observar_objeto(objeto_a_analizar):
    print("\nClase de objeto: ", type(objeto_a_analizar))
    # cadena de herencia
    print("\nCadena de Herencia del objeto:")
    for elemento in reversed(objeto_a_analizar.__class__.__mro__):
        print(elemento)

    print("\nDetalle de objeto:")
    for elemento in dir(objeto_a_analizar):
        print(elemento)


class SerVivo0:
    pass

celula = SerVivo0()
microbio = SerVivo0() 
protozoo = SerVivo0()

# Observemos el objeto ser_vivo
observar_objeto(microbio)

# definimos un atributo de Clase
SerVivo0.altura = 20
observar_objeto(microbio)


print("Altura de los seres vivos creados:\n", 
    celula.altura, microbio.altura, protozoo.altura)

#cambio atributo de Clase
SerVivo0.altura = 80

print("Altura de los seres vivos creados:\n", 
    celula.altura, microbio.altura, protozoo.altura)

# cambio de atributo de objeto
microbio.altura = 20

print("Altura de los seres vivos creados:\n", 
    celula.altura, microbio.altura, protozoo.altura)

# cambiamos nuevamente el atributo de clase
SerVivo0.altura = 10
print("Altura de los seres vivos creados:\n", 
    celula.altura, microbio.altura, protozoo.altura) 

observar_objeto(microbio) # microbio mantuvo su altura definida en el objeto

# volvemos a nuestro última clase de SerVivo que habíamos creado

class SerVivo04:

    def __init__(self, tamano, peso, especie):
        self.tamano = tamano # atributo de la instancia
        self.peso = peso # atributo de la instancia
        self.especie = especie # atributo de la instancia

    def alimentarse(self, cantidad): # esto es un método (capacidad de actuar)
        print("Soy", id(self), "y estoy Alimentándome!")
        self.tamano = self.tamano + 0.1 * cantidad
        self.peso = self.peso + cantidad
    
    def ejercitar(self, tiempo):
        print("Haciendo Ejercicio!")
        self.peso = self.peso - 0.02 *tiempo

    def eleminar_desechos(self, cantidad):
        print("Estoy ocupado en este momento!")
        self.peso = self.peso - cantidad


luke = SerVivo04(170, 80, "Humana")
leiah = SerVivo04(160, 60, "Humana")
yoda = SerVivo04(60, 15, "MetaHumano")

print(luke.peso, leiah.peso, yoda.peso)


# recordatorio de funciones

# esta función acepta una cantidad indefinida de argumentos con el orden ingresado
def sumar(*args):
    print(args)
    suma=0
    for elemento in args:
        suma += elemento
    return suma

print("La suma es: ", sumar(1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2,
                        1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2,
                        1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2,
                        1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2,
                        1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2,4,
                        1,2,3,4,5,6,7,8,6,4,3,23,5,6,7,8,2))

# esta función acepta una cantidad indefinida de argumentos con nombre
def mostrar_datos(**kwargs):
    return kwargs

print(mostrar_datos(nombre="Rocío", apellido="Canibilo", edad = 18, direccion="Av. Python 245"))


# sobrecarga de métdos 
class Opciones:
    opciones_predeterminadas = { 'port': 21, 
                        'host': 'localhost',
                        'username': None,
                        'password': None,
                        'debug': False}


    def __init__(self, **kwargs):
        self.opciones = dict(Opciones.opciones_predeterminadas)
        self.opciones.update(kwargs)


opciones1 = Opciones(username="alexandra", 
                    password="1234", 
                    direccion="Av. Linux 465",
                    educacion="Media",
                    cuidad="Puchuncaví"
                    )

observar_objeto(opciones1)
print("opciones_predeterminadas: ", opciones1.opciones_predeterminadas)
print("opciones: ", opciones1.opciones)


#

class Pelota00:

    def __init__(self, radio):
        self.radio = radio
        self.volumen = (4/3)*(3.14*self.radio**3)

pelota_futbol_1 = Pelota00(11) # Pelota FIFA

print("\nRadio Pelota: ", pelota_futbol_1.radio)
print("\nVolmen Pelota: ", pelota_futbol_1.volumen)

# quiero redefinir el radio de la pelota
pelota_futbol_1.radio = 15

print("\nRadio Pelota: ", pelota_futbol_1.radio)
print("\nVolmen Pelota: ", pelota_futbol_1.volumen)


# encapsulamiento de atributos.
# atributos "privados"
# LOS ATRIBUTOS PRIVADOS EN PYTHON NO EXISTEN

class Pelota01:

    def __init__(self, radio):
        self.__radio = radio
        self.__volumen = (4/3)*(3.14*self.__radio**3)

pelota_futbol_B = Pelota01(11) # Pelota FIFA

try:
    print("\nRadio Pelota: ", pelota_futbol_B.__radio)
    print("\nVolmen Pelota: ", pelota_futbol_B.__volumen)

    # quiero redefinir el radio de la pelota
    pelota_futbol_B.__radio = 15

    print("\nRadio Pelota: ", pelota_futbol_B.__radio)
    print("\nVolmen Pelota: ", pelota_futbol_B.__volumen)
except Exception as e:
    print("Error: ", e)
    print("Error de acceso a los atributos porque están 'Mangelados' o escondidos")

#SECRETO: LA VARIABLE SI SE PUEDE ACCEDER.  sshhhhhhhhh!
# la variable está escondida bajo otro nombre (Técnica de Name-Mangling)
print("\nRadio Pelota: ", pelota_futbol_B._Pelota01__radio)
print("\nVolmen Pelota: ", pelota_futbol_B._Pelota01__volumen)

# cómo interactúo con esos atributos?? Soy un programador de otro lenguajes 
# y estoy usando mi conocimiento actual pero en python

class Pelota02:

    def __init__(self, radio):
        self.__radio = radio
        self.__volumen = (4/3)*(3.14*self.__radio**3)

    def set_radio(self, radio):
        self.__radio = radio
        self.__volumen = (4/3)*(3.14*self.__radio**3)

    def get_radio(self):
        return self.__radio

    def get_volumen(self):
        return self.__volumen

pelota_futbol_C = Pelota02(11) # Pelota FIFA

print("\nRadio Pelota:", pelota_futbol_C.get_radio())
print("\nVolumen Pelota:", pelota_futbol_C.get_volumen())

print("Redefinición del Radio")
pelota_futbol_C.set_radio(15)
print("\nVolumen Pelota:", pelota_futbol_C.get_volumen())


# acercamiento de Python a este problema

class Pelota03:

    def __init__(self, radio):
        self.__radio = radio
        self.__volumen = (4/3)*(3.14*self.__radio**3)

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        print("Seteando atributo encapsulado radio y recalculando volumen")
        self.__radio = radio
        self.__volumen = (4/3)*(3.14*self.__radio**3)

    @property
    def volumen(self):
        return self.__volumen

pelota_futbol_D = Pelota03(11)

print("\nRadio Pelota: ", pelota_futbol_D.radio)
print("\nVolumen Pelota: ", pelota_futbol_D.volumen)
pelota_futbol_D.radio = 15
print("\nRadio Pelota: ", pelota_futbol_D.radio)
print("\nVolumen Pelota: ", pelota_futbol_D.volumen)
try:
    pelota_futbol_D.volumen = 100
except Exception as e:
    print("Error: ", e)
    print("Error de acceso a volumen porque es 'privado'")
print("\nVolumen Pelota: ", pelota_futbol_D.volumen)

# haremos una maldad en Python
print("\nEstamos haciendo una maldad!! No debemos hacer esto. Esto NO se hace!!!")
pelota_futbol_D._Pelota03__volumen = 100
print("\nVolumen Pelota: ", pelota_futbol_D.volumen)