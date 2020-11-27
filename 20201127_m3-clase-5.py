#!/usr/bin/env python
# coding: utf-8

# In[112]:


def imprimir_datos_objeto(objeto):
    nombre_objeto = [ k for k,v in locals().items() if v == objeto][0]
    print("\n"+79*"#")
    print("#### MRO OBJETO")
    print("#### C3 Linearization")
    print("#### Clases hijas se chequean antes que las madres")
    print("#### Madres múltiples se chequean en el orden listado")
    for element in reversed(objeto.__class__.__mro__):
        print(element)
    print("\n#### Variables de Clase".upper()) 

    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"."+elemento)) != True and elemento[:2]!="__":
            print(elemento+":", eval(nombre_objeto+".__class__."+elemento))

    print("\n#### Métodos de Clase".upper()) 
    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]!="__":
            print(elemento)

    print("\n#### Variables de Instancia".upper())
    for clave, valor in vars(objeto).items():
        print(clave+": "+str(valor))

    print("\n#### Métodos de Instancia".upper())
    index=1
    for elemento in dir(objeto):
        if callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]=="__":
            if (index)%7==0:
                end_char = "\n"
                index = 0
            else:
                end_char = ","
            print(elemento, end=end_char)
            index +=1
        elif callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]!="__":
            try:
                print("\n",elemento, sep="")
                eval(nombre_objeto+"." + elemento+"()")
                index +=1
            except Exception as e:
                print("No se puede evaluar el método " + elemento+"() pues no se ingresaron argumentos")

    print("\n"+79*"#"+"\n")


# <span><p style="text-align:right; display: inline-block;">
#     <img style="display: inline-block;" src="https://www.solvetic.com/uploads/monthly_01_2016/tutorials-1415-0-60642300-1452279191.jpg">
# </p><img width="30%" style="display: inline-block;" src="https://ungerboeckdotcomassets.blob.core.windows.net/volumes/content/_wide/when-good-info-goes-bad.jpg"></span>
# 
# <p style="font-size: 250%;text-align: right; color:#555"> Errores y Excepciones </p>
# 
# ---  
# <p style="text-align: right; color:blue;"> luis.jaraquemada@team.awakelab.cl  </p>

# ## Errores de Sintaxis
# --- 
# 1. Errores entregados por el interprete antes de comenzar la ejecución del programa.
# 2. Son los errores más comunes en las etapas de aprendizaje de Python.
# 3. Se indica el error y número de línea dónde éste ocurre. 
# 
# 
# <p style="margin: 20px 30% 20px 40px; background:#eeeeee; padding:0px 18px 18px;">
#     <code class="language-html" style="font-family: Courier New; font-size: 80%;background:#eeeeee;color:black;">  
#     File "<ipython-input-28-5729801846ee>", line 1
#         while True
#                   ^
#     SyntaxError: invalid syntax
#     </code>
# </p>
# 
# 
# 
# 
# 

# # Ejemplos de Errores de Sintaxis
# <center><img width="50%" src="https://ungerboeckdotcomassets.blob.core.windows.net/volumes/content/_wide/when-good-info-goes-bad.jpg"></center> 

# # SyntaxError: invalid syntax

# In[6]:


while True:
    print("Hola Curso!!")


# # Otro Error de Sintaxis

# In[16]:


edades = {
    'pamela': 24,
    'jaime': 24
    'miguel': 43
}

print("Miguel tiene", edades['miguel'], "Años")


# # Otro Ejemplo - IndentationError

# In[33]:


def contador():
    for i in range(10):
        print(i)
  print('Listo!')

contador()


# # ¡Otro Ejemplo Más!

# In[44]:


if i in [1,2,3,4,5,6,8,9,0,10]:
    print(i)
    continue
    


# # Excepciones  
# 
# - Una excepción es un error que ocurre durante la ejecución de un programa. 
# - El nombre "Excepción" --> No ocurre con frecuencia, es la Excepción a la Regla.  
# - El manejo de excepciones es una construcción para manejar o tratar los errores automáticamente.
# 
# 

# # Tipos de Excepciones
# 
# <img width="100%" src="https://w3.cs.jmu.edu/lam2mo/cs240_2014_08/images/exception_hierarchy.png">  
# 
# [Mapa de Excepciones](https://julien.danjou.info/content/images/2018/03/python3-exceptions-graph.png)

# # Ejemplos  de Excepciones
# <center><img width="50%" src="https://www.elpublicista.es/adjuntos/fichero_22884_20200413.jpg"></center> 

# # ValueError  
# 

# In[47]:


n = int(input("Ingrese un número: "))
print("El numero ingresado fué:", n)


# # ZeroDivisionError

# In[54]:


a = 1
b = 0
print(a/b)


# # OverflowError

# In[59]:


import math
print("The exponential value is")
print(math.exp(1000))


# # Manejando una Excepción
# 
# Si sospechamos que en un código puede generarse una excepción, podemos incluir un código que la maneje.

# 
# <p style="margin: 20px 20% 20px 0px; background:#eeeeee; padding:0px 18px 18px;">
# <code class="language-html" style="font-family: Courier New; font-size: 90%;background:#eeeeee;color:black;">
# <b>try:</b>
#   Nuestro código sospechoso;
#   ......................
# <b>except Exception_A:</b>
#   Si ocurre Exception_A,se ejecuta este bloque de código
# <b>except Exception_B:</b>
#   Si ocurre Exception_B,se ejecuta este bloque de código
#   .......................
# :
# <b>else:</b>
#   Se ejecuta si no hubo excepción (Ej: print("No hubo excepción!"))
# <b>finally:</b>
#   Se ejecuta pase lo que pase
# </code>
# </p>
# 

# # Ejemplo 1

# In[72]:


try:
    print(1/0)
except:
    print("ERROR")
print("Puedo seguir adelante")
try:
    print(1/0)
except Exception as e:
    print("ERROR", e)
print("ocurrió un error pero puedo seguir")


# # Ejemplo 2

# In[93]:


try:
    print(1/0)
except ZeroDivisionError as mi_excepcion:
    print(type(mi_excepcion), "\n", dir(mi_excepcion), "\n", mi_excepcion.__class__.__mro__)
    print(type(mi_excepcion))
    print("enviar email de emergencia para advertir de lo ocurrido")
print("Sigo ejecutando")


# # Ejemplo 3

# In[95]:


try:
    print(1/0)
except IOError as exception:
    print("Error de IO", exception)
except Exception as exception:
    print("El tipo de excepción es:", exception)
print("Sigo ejecutando")


# # Ejemplo 4

# In[99]:


import traceback

try:
    int("lkwjerlkjer")
except:
    print("Error", traceback.format_exc())
    #guardar en un archivo de texto .log este error para ser estudiado

print("Sigo ejecutando")


# # Ejemplo 5

# In[100]:


def f(denominador):
    try:
        print(1/denominador)
    except IOError:
        print("Exception")
        return 0
    except Exception:
        print("Error, pero No IOError")
        return -1
    else:
        print("Else") # código a ejecutar (Por ejemplo que confirma que excepción no ocurrió)
        return 1
    finally: 
        print("Ejecuto esto pase lo que pase, incluso returns")



print(f(0))
print("Sigo ejecutandome")


# # Ejemplo 6

# In[102]:


import traceback

try:
    float("lkjdas")
except (ZeroDivisionError, ValueError, TypeError) as e:
    print(e)
    print(traceback.format_exc())
print("Sigo adelante")


# # Ejemplo 6: Acorralando Excepciones

# In[103]:


def captura_fallida():
    try:
        raise ValueError('Otro bug que no estamos buscando capturar')
        raise Exception('Excepción que deseamos capturar')
    except Exception as error:
        print('Error Capturado: ' + repr(error))

captura_fallida()


# In[104]:


def error_no_capturado():
    try:
        raise Exception('Excepción general')
        raise ValueError('Este es un error buscado')
    except ValueError as e:
        print('No capturamos la excepción')

error_no_capturado()


# # Ejemplo 7

# In[108]:


try:
    f = open("welcome.txt", "r")
except FileNotFoundError as e:
    print()
    print(e)
    print()
    print(traceback.format_exc())
print("Sigo adelante")


# # Creando Excepciones Personalizadas

# In[110]:


class ListaSoloEnterosYPares(list):
    def append(self, entero):
        if not isinstance(entero, int):
            raise TypeError("ERROR: Solo Enteros Pueden Ser Agregados y {} No Lo Es".format(entero))
        if int(entero) % 2 !=0:
            raise ValueError("Solo numeros pares pueden ser agregados y el número {} no lo es".format(entero))
        super().append(entero)

numeros = ListaSoloEnterosYPares()
print("Lista inicial:", numeros)

for i in range(2):
    try:
        numero = input("Ingrese un número a almacenar: ")
        numero = int(numero)
    except:
        numero = numero
        
    try:
        numeros.append(numero)
    except Exception as e:
        print(e)
    print(numeros, "\n")
print("Gracias!!!")


# In[114]:


class SueldoFueraDeRango(Exception):
    """Excepción para sueldo fuera de rango.

    Atributos:
        sueldo -- sueldo de entrada que causa el error
        mensaje -- explicación del error
    """

    def __init__(self, sueldo, mensaje="El sueldo no está en el rango esperado (5000, 15000)"):
        self.sueldo = sueldo
        self.mensaje = mensaje
        super().__init__(mensaje)
        
print(SueldoFueraDeRango.__mro__)

imprimir_datos_objeto(Exception())



sueldo = int(input("Ingreso Monto del Sueldo: "))
imprimir_datos_objeto(SueldoFueraDeRango(sueldo))
if not 5000 < sueldo < 15000:
    raise SueldoFueraDeRango(sueldo)


# # Levantando Excepciones Manualmente

# In[120]:


lista = []
def divide(dividend, divisor):
    if divisor == 0:
        print('División por Cero Indefinida!')
        return # Qué retorno es sensato?
    return dividend / divisor


# In[121]:


for numero in [1,4,3,2,0,2,3,4]:
    lista.append( divide(1,numero) )


# In[122]:


print(lista)
suma_total = sum(lista)
print(suma_total)


# In[125]:


lista2 = []
def divide2(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('División por Cero Ocurrida, investigue la causa')
    return dividend / divisor


# In[126]:


for numero in [1,4,3,2,0,2,3,4]:
    lista2.append( divide2(1,numero) )


# In[127]:


print(lista2)
suma_total2 = sum(lista2)
print(suma_total2)


# <center>    <img style="display: inline-block;" src="https://www.solvetic.com/uploads/monthly_01_2016/tutorials-1415-0-60642300-1452279191.jpg"></center>
