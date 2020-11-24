#!/usr/bin/env python
# coding: utf-8

# # Auto de Carreras

# In[96]:


class AutoDeCarreras:
    
    def __init__(self, posicion):
        self.__velocidad = 0 
        self.__posicion = posicion
    
    def avanzar(self, tiempo):
        self.__posicion = self.__posicion + tiempo * self.__velocidad 
        return "La posicion ahora es: " + str(self.__posicion)
        
    def acelerar(self, cantidad):
        self.__velocidad = self.velocidad + cantidad
        return "La velocidad ahora es: " + str(self.__velocidad)
        
    @property
    def posicion(self):
        return self.__posicion
    
    @property
    def velocidad(self):
        return self.__velocidad
        


# 
# La interfaz de esta clase permite solamente:  
# 
#     1. Cambiar la velocidad con `acelerar()`.  
#     2. Avanzar una cantidad de tiempo con `avanzar()`.  
#     3. Consultar la velocidad actual con `objeto.velocidad`.  
#     4. Consultar la posicion actual con `objeto.posicion`.  

# In[97]:


rayo_mcqueen = AutoDeCarreras(0)


# In[98]:


rayo_mcqueen.posicion


# In[99]:


rayo_mcqueen.velocidad


# In[100]:


rayo_mcqueen.avanzar(10)


# In[101]:


rayo_mcqueen.acelerar(10)


# In[102]:


rayo_mcqueen.avanzar(1)


# In[103]:


rayo_mcqueen.avanzar(2)


# - Como usamos `@property` entonces la velocidad puede consultarse:

# In[104]:


rayo_mcqueen.velocidad


# - Pero la velocidad **NO** puede setearse:

# In[105]:


rayo_mcqueen.velocidad = 10


# In[106]:


rayo_mcqueen.acelerar(-20)


# In[107]:


rayo_mcqueen.avanzar(3)


# # Casa y Pasillo

# In[147]:


class Casa:
    def __init__(self, area, num_hab, num_pasillos, tamanio_patio, num_banios):
        self.area = area
        self.num_hab = num_hab
        self.num_pasillos = num_pasillos
        self.num_banios = num_banios
        self.tamanio_patio = tamanio_patio
        self.pasillos = []
        self.__construir_pasillos()

    def __construir_pasillos(self):
        for i in range(self.num_pasillos):
            self.pasillos.append(Pasillo(2, 1.5, 2.5, "alfombra"))
        
    def abrir_acceso(self):
        pass
    
    def cerrar_acceso(self):
        pass
    
    def activar_alarma(self):
        pass
    
    def desactivar_alarma(self):
        pass

    
class Pasillo:
    def __init__(self, largo, ancho, alto, tipo_piso):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.tipo_piso = tipo_piso
        self.__luz = False

    def interruptor_luz(self):
        self.__luz = not self.__luz
        if self.__luz == True:
            estado = "ENCENDIDA" 
        else:
            estado = "APAGADA"
        print("La luz está ", estado)
        
    @property
    def luz(self):
        if self.__luz == True:
            estado = "ENCENDIDA" 
        else:
            estado = "APAGADA"
        return estado
    


# In[148]:


casa_1 = Casa(139, 5, 3, 200, 2)


# In[151]:


casa_1.pasillos[0].interruptor_luz()

for pasillo in casa_1.pasillos:
    print("El ID del Pasillo es:", id(pasillo))
    print(pasillo.luz)


# In[152]:


del casa_1


# In[156]:


casa_1.pasillos


# # Equipo de Futbol y Jugador

# In[171]:


class EquipoFutbol:
    
    def __init__(self, nombre, division):
        self.__nombre = nombre
        self.__division = division
        self.__jugadores = []
        
    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)
    
    def sacar_jugador(self):
        pass
      
    @property
    def jugadores(self):
        return self.__jugadores

class Jugador:
    
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
    
    def correr(self):
        pass
    
    def patear_al_arco(self):
        pass
    
    def pegar_patada(self):
        pass


# In[173]:


equipo_1 = EquipoFutbol("coca cola", "por zero")

print(equipo_1.jugadores)

jugador_1 = Jugador("Cuchilla Morales", 34, "defensa central")
jugador_2 = Jugador("Siete Pulmones", 29, "delantero")
equipo_1.agregar_jugador(jugador_1)
equipo_1.agregar_jugador(jugador_2)
print(equipo_1.jugadores[0].nombre)
print(equipo_1.jugadores[1].nombre)


# In[174]:


del equipo_1


# In[175]:


equipo_1


# In[178]:


jugador_1.nombre


# In[179]:


jugador_2.nombre

