#!/usr/bin/env python
# coding: utf-8

# In[22]:


class SerVivo0:
    pass

servivo=SerVivo0()
servivo.peso=10
servivo.peso


# Se creó un atributo de instancia en la ejecución, después de estar definida la clase y creado el objeto

# In[12]:


class Pieza:
    
    def __init__(self, color, activa):
        self.__color = color
        self.activa = activa


# In[13]:


pieza_1 = Pieza("blanca", True)


# In[19]:


pieza_1.color


# no exite atributo `color`

# In[24]:


pieza_1.color = "negra"
pieza_1.color


# creé el atributo color, pero no tiene nada que ver con mi clase ni objeto

# In[25]:


dir(pieza_1)


# el atributo que realmente es valido para nuewstro programa es `__color`pero que está encapsulado

# Ok, y a recordamos algunas cosas básicas

# In[27]:


class Pieza0: # esto es lo mismo que class Pieza0(object):
    
    def __init__(self, color, activa):
        self.__color = color
        self.activa = activa


# In[29]:


pieza_uno = Pieza0("negra", True)


# # Cómo sé cual es la cadena de herencia de un objeto?

# In[41]:


pieza_uno.__class__.__mro__


# In[48]:


class PiezaHija(Pieza0):
    categoria = "chica"


# In[49]:


pieza_hija_uno = PiezaHija("blanca", False)


# In[50]:


pieza_hija_uno.__class__.__mro__


# ------------------------------------> es más alta jerarquía

# # Qué pasa si mi clase hereda de dos clases superiores que definen mismo atributo pero con valor distinto?

# In[128]:


class SerVivo:
    raza = "Chilena"
    vivo = True

class Mamifero(SerVivo):
    raza = "Argentina"
    
class PersonajeDisfrazado(SerVivo):
    raza = "China"
    def __init__(self, color_disfraz, color_zapatos, tiene_gorro, tiene_guantes, tiene_barba):
        self.disfraz = color_disfraz
        self.zapatos = color_zapatos
        self.gorro = tiene_gorro
        self.guantes = tiene_guantes
        self.barba = tiene_barba
        
    
class Humano(Mamifero, PersonajeDisfrazado):
    #raza = "Ario"
    def __init__(self, edad, peso, altura, barba):
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.barba = barba
        self.pestanias = "largas"



class PersonajeDeTradicion(Humano):
    #raza = "Esquimal"
    def __init__(self, fiesta):
        self.fiesta = fiesta
    
class ViejoPascuero(PersonajeDeTradicion, Humano):
    #raza = "Mestizo"
    def __init__(self, trineo, lentes, carbon):
        Humano.__init__(self,45, 30, 180, True)
        self.trineo = trineo
        self.lentes = lentes
        self.carbon = carbon


# In[131]:


viejo_rojo = ViejoPascuero(True, True, True)


# In[132]:


viejo_rojo.raza


# In[133]:


viejo_rojo.__class__.__mro__


# # Qué pasa con las variables de instancia?

# In[137]:


viejo_rojo.pestanias


# In[138]:


viejo_rojo.carbon


# # Qué ocurre cuando las clases con herencia tienen distintos argumentos?

# Cómo se instancia la Clase hija?

# In[ ]:





# # Qué es la función `super()`?

# In[ ]:




