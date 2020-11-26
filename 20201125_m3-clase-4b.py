#!/usr/bin/env python
# coding: utf-8

# ## Curso Full Stack Python 154-2
# ### Clase 20201126_m3-clas-4b  
# 
# **Clase Herencia y Polimorfismo**  
# 

# In[51]:


import this


# In[3]:


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


# In[42]:


def imprimir_datos_objeto(objeto):
    nombre_objeto = [ k for k,v in locals().items() if v == objeto][0]
    print("\n"+79*"#")
    print("#### MRO OBJETO")
    print("#### C3 Linearization")
    print("#### Clases hijas se chequean antes que las madres")
    print("#### Madres múltiples se chequean en el orden listado")
    for element in reversed(objeto.__class__.__mro__):
        print(element)
    print("\n#### dir del objeto\n")
    print(dir(objeto))
    print("\n#### Variables de Clase".upper()) 

    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"."+elemento)) != True and elemento[:2]!="__":
            print(elemento+":", eval(nombre_objeto+".__class__."+elemento))
    '''
    print("\n#### Métodos de Clase".upper()) 
    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]!="__":
            print(elemento)
    '''
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


# In[1]:


class SerVivo0(object):
    pass


# In[2]:


gusano = SerVivo0()


# In[4]:


observar_objeto(gusano)


# In[76]:


class SerVivo00:
    variable_prueba = "variable_prueba desde clase SerVivo00"
    variable_prueba_00 = "variable_prueba_00 desde clase SerVivo00"

    def __init__(self):
        self.variable_prueba = "variable_prueba desde init SerVivo00"
        self.peso = "40 desde SerVivo00"
        print("Ejecutado __init__() de SerVivo00")
    
    def metodo_prueba00(self):
        print("metodo_prueba00() desde SerVivo00")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00")


# In[77]:


class SerVivo01(SerVivo00):
    variable_prueba = "variable_prueba desde clase SerVivo01"
    variable_prueba_01 = "variable_prueba_01 desde clase SerVivo01"
    
    def __init__(self):
        super().__init__()
        #SerVivo00.__init__(self)
        self.variable_prueba = "variable_prueba desde init SerVivo01"
        self.variable_prueba_01 = "variable_prueba_01 desde init SerVivo01"
        print("Ejecutado __init__() de SerVivo01")

    def metodo_prueba01(self):
        print("metodo_prueba01() desde SerVivo01")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo01")


# In[78]:


ser_vivo = SerVivo01()
imprimir_datos_objeto(ser_vivo)


# In[79]:


class SerVivo01b(SerVivo00):
    variable_prueba = "variable_prueba desde clase SerVivo01b"
    variable_prueba_01b = "variable_prueba_01b desde clase SerVivo01b"
    
    def __init__(self):
        super().__init__()
        #SerVivo01.__init__(self)
        self.variable_prueba = "variable_prueba desde init SerVivo01b"
        self.variable_prueba_01b = "variable_prueba_01 desde init SerVivo01b"
        print("Ejecutado __init__() de SerVivo01b")

    def metodo_prueba01(self):
        print("metodo_prueba01b() desde SerVivo01b")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo01b")


# In[80]:


otro_ser_vivo = SerVivo01b()
imprimir_datos_objeto(otro_ser_vivo)


# In[81]:


class SerVivo00Mutacion01(SerVivo01):
    variable_prueba = "variable_prueba desde clase SerVivo00Mutacion01"
    variable_prueba_00Mutacion01 = "variable_prueba_00Mutacion01 desde clase SerVivo00Mutacion01"
    
    def __init__(self):
        super().__init__()
        #SerVivo01.__init__(self)
        self.variable_prueba = "variable_prueba desde init SerVivo00Mutacion01"
        self.variable_prueba_00Mutacion01 = "variable_prueba_01 desde init SerVivo00Mutacion01"
        print("Ejecutado __init__() de SerVivo00Mutacion01")
        
    def metodo_prueba00Mutacion01(self):
        print("metodo_prueba00Mutacion01() desde SerVivo00Mutacion01")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00Mutacion01")
        


# In[82]:


otro_ser_vivo_mas = SerVivo00Mutacion01()
imprimir_datos_objeto(otro_ser_vivo_mas)


# In[98]:


class SerVivo00Mutacion02(SerVivo01b):
    variable_prueba = "variable_prueba desde clase SerVivo00Mutacion02"
    variable_prueba_00Mutacion02 = "variable_prueba_00Mutacion02 desde clase SerVivo00Mutacion02"
    
    def __init__(self):
        super().__init__()
        #SerVivo01.__init__(self)
        #self.variable_prueba = "variable_prueba desde init SerVivo00Mutacion02"
        self.variable_prueba_00Mutacion02 = "variable_prueba_00Mutacion02 desde init SerVivo00Mutacion02"
        print("Ejecutado __init__() de SerVivo00Mutacion02")
        
    def metodo_prueba00Mutacion02(self):
        print("metodo_prueba00Mutacion02() desde SerVivo00Mutacion02")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00Mutacion02")


# In[103]:


class SerVivo02(SerVivo00Mutacion02, SerVivo00Mutacion01):
    #variable_prueba = "variable_prueba desde clase SerVivo02"
    variable_prueba_02 = "variable_prueba_02 desde clase SerVivo02"
    
    def __init__(self):
        super().__init__()
        #SerVivo00Mutacion02.__init__(self)
        #SerVivo00Mutacion01.__init__(self)
        print("Ejecutado __init__() de SerVivo02")
        
    def metodo_prueba02(self):
        print("metodo_prueba02() desde SerVivo02")
        
    #def metodo_prueba(self):
    #    print("metodo_prueba() desde SerVivo02")


# In[104]:


ser_vivo_2 = SerVivo02()


# In[105]:


imprimir_datos_objeto(ser_vivo_2)


# # Ejemplo de Animales

# In[146]:


class Animal():
    
    def __init__(self,nombre, peso, posicion):
        self.name = nombre
        self.peso = peso
        self.posicion = posicion
    
    def alimentarse(self, cantidad):
        self.peso += cantidad
        return self.peso
    
    def ejercitar(self, tiempo):
        self.peso -= 0.1 * tiempo # tiempo[s] ==> 0.1 [kg/s]
        return self.peso
    
    def moverse(self, distancia):
        self.peso -= 0.01*distancia
        self.posicion += distancia
        mensaje = "Me desplacé a la posición "
        return mensaje, self.posicion
        
    def hablar(self):
        raise NotImplementedError("Esta clase debe implementarse en clases hijas")
        


# In[147]:


animal01 = Animal("Lalo", 10, 0)
print(animal01.moverse(10))
print(animal01.moverse(-5))


# In[167]:


class AnimalDeCircoChino(Animal):

    tipo_id = "00034"
    certificacion = "axfe"
    propietario = "Wang Ke"
    
    def __init__(self, nombre, peso, posicion, grupo):
        import time
        self.time = time
        #super().__init__(nombre, peso, posicion)
        Animal.__init__(self, nombre, peso, posicion)
        self.grupo_acrobatico = grupo
    
    
    def moverse(self, energia):
        distancia = 0
        mensaje = ""
        for i in range(energia):
            print("Tomando impulso... ", end=" ")
            self.time.sleep(0.2)
            distancia += 3
        print()
        #resultado = Animal.moverse(self, distancia)
        mensaje, resultado = Animal.moverse(self, distancia)
        print(resultado, mensaje)
        return resultado, "Tomando mucho impulso, Salté y m" + mensaje[1:]

    def ir_a_jaula(self):
        return("Caminando hacia la jaula")
    
    def simular_muerte(self):
        return "Ohhh, qué dolor!!!! Estoy muriendo! Adiós"


# In[168]:


animalcirquero = AnimalDeCircoChino("mono1", 40, 0, "A")


# In[169]:


class Serpiente(Animal):
    
    def __init__(self, nombre, peso, posicion, propietario, grosor_piel, venenosa = True):
        #super().__init__(nombre, peso, posicion)
        Animal.__init__(self, nombre, peso, posicion)
        self.propietario = propietario
        self.grosor_piel = grosor_piel
        self.venenosa = venenosa
    
    def moverse(self, distancia):
        #mensaje, resultado = Animal.moverse(self, distancia)
        mensaje, resultado = super().moverse(distancia)
        return "Arrastrándome " + "m" + str(mensaje[1:]) + " " + str(resultado)


# In[170]:


serpiente01 = Serpiente("Snake", 10, 0, "juanito", "gruesa")
print(serpiente01.moverse(10))
print(serpiente01.moverse(-5))


# In[171]:


class SerpienteAcrobatica(AnimalDeCircoChino, Serpiente):
    
    def __init__(self, nombre, peso, posicion, propietario, grosor_piel):
        Serpiente.__init__(self, nombre, peso, posicion, propietario, grosor_piel)
        AnimalDeCircoChino.__init__(self, nombre, peso, posicion, "B")
        
    def moverse(self, energia):
        distancia, mensaje = AnimalDeCircoChino.moverse(self, energia)
        resultado = Serpiente.moverse(self, distancia)
        return mensaje, distancia

    def ir_a_jaula(self):
        resultado = AnimalDeCircoChino.ir_a_jaula(self)
        return self.saludar_al_publico() + " y voy c" + resultado[1:]
        
    def saludar_al_publico(self):
        return "Hola Público, soy la Serpiente Acrobática"
    


# In[172]:


serpent_ina = SerpienteAcrobatica("pipa", 10, 0, "circo 1", "gruesa")


# In[173]:


print(serpent_ina.moverse(20))


# In[174]:


serpent_ina.__class__.__mro__


# In[175]:


imprimir_datos_objeto(serpent_ina)

