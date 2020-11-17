# revisando clases y objetos en Python
# preguntando a qué clase pertenece un objeto con type()
numero_1 = 1
print("A qué clase pertenece el objeto " + str(numero_1)+"?", type(numero_1))

numero_2 = 3.5
print("A qué clase pertenece el objeto " + str(numero_2)+"?", type(numero_2))

lista_1 = [1,2,3,4,5,6,7]
print("A qué clase pertenece el objeto " + str(lista_1)+"?", type(lista_1))

def sumar_dos_numeros(a, b):
    return a + b
print("A qué clase pertenece el objeto " + str(sumar_dos_numeros)+"?", type(sumar_dos_numeros))

# preguntando qué características tiene el objeto dir()
# obteniendo una radiografía del objeto

print("Cómo está compuesto el objeto " + str(numero_1)+"?", dir(numero_1))
print("Cómo está compuesto el objeto  " + str(lista_1)+"?", dir(lista_1))

##############################################################################
# creamos por nosotros mismos una clase y objeto en Python
##############################################################################

# definir una clase con atributos
class SerVivo00:
    tamano = 10
    peso = 30
    especie = "Animal"

print(SerVivo00)

# crear objetos o instancias
neo = SerVivo00()
trinity = SerVivo00()
morfeo = SerVivo00()

print("Cómo está compuesto el objeto " + str(neo)+"?", dir(neo))
print("Cómo está compuesto el objeto " + str(trinity)+"?", dir(trinity))
print("Cómo está compuesto el objeto " + str(morfeo)+"?", dir(morfeo))

# definir una clase con atributos y metodos
class SerVivo01:
    tamano = 10 # atributo de la clase
    peso = 30 # atributo de la clase
    especie = "Animal" # atributo de la clase

    def alimentarse(self, cantidad): # esto es un método (capacidad de actuar)
        SerVivo01.tamano = SerVivo01.tamano + 0.1 * cantidad
        SerVivo01.peso = SerVivo01.peso + cantidad

neo2 = SerVivo01()
trinity2 = SerVivo01()
morfeo2 = SerVivo01()

# como accedemos a atributos y metodos de un objeto
print("Peso de neo: ", neo2.peso  )
print("Peso de trinity: ", trinity2.peso)
neo2.alimentarse(20)
print("Peso de neo: ", neo2.peso  )
print("Peso de trinity: ", trinity2.peso)

print("WOW!! Alimentamos a Trinity a través de Neo.... Algo no está bien!!!!!")


# Tratemos de resolver esta falla de la Matrix

class SerVivo02:

    def __init__(self):
        self.tamano = 10 # atributo de la clase
        self.peso = 30 # atributo de la clase
        self.especie = "Animal" # atributo de la clase

    def alimentarse(self, cantidad): # esto es un método (capacidad de actuar)
        self.tamano = self.tamano + 0.1 * cantidad
        self.peso = self.peso + cantidad

neo3 = SerVivo02()
trinity3 = SerVivo02()
morfeo3 = SerVivo02()

# como accedemos a atributos y metodos de un objeto
print("Peso de neo: ", neo3.peso  )
print("Peso de trinity: ", trinity3.peso)
print("Peso de morfeo: ", morfeo3.peso)
neo3.alimentarse(20)
print("Peso de neo: ", neo3.peso  )
print("Peso de trinity: ", trinity3.peso)
print("Peso de morfeo: ", morfeo3.peso)


# agregaremos capacidad de crear seres vivos con distitos valores iniciales
# de sus atributos

class SerVivo03:

    def __init__(self, tamano, peso, especie):
        self.tamano = tamano # atributo de la instancia
        self.peso = peso # atributo de la instancia
        self.especie = especie # atributo de la instancia

    def alimentarse(self, cantidad): # esto es un método (capacidad de actuar)
        self.tamano = self.tamano + 0.1 * cantidad
        self.peso = self.peso + cantidad

neo4 = SerVivo03(20, 30, "Animal")
trinity4 = SerVivo03(15, 20, "Animal")
morfeo4 = SerVivo03(30, 40, "Animal")

print("Peso de neo: ", neo4.peso  )
print("Peso de trinity: ", trinity4.peso)
print("Peso de morfeo: ", morfeo4.peso)
trinity4.alimentarse(30)
print("Peso de neo: ", neo4.peso  )
print("Peso de trinity: ", trinity4.peso)
print("Peso de morfeo: ", morfeo4.peso)

for dia in range(0,100):
    neo4.alimentarse(40)
    trinity4.alimentarse(40)
    morfeo4.alimentarse(40)

print("Peso de neo: ", neo4.peso  )
print("Peso de trinity: ", trinity4.peso)
print("Peso de morfeo: ", morfeo4.peso)

# ser vivo que pueda no explotar por alimento

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


neo5 = SerVivo04(20, 30, "Animal")
trinity5 = SerVivo04(15, 20, "Animal")
morfeo5 = SerVivo04(30, 40, "Animal")

print("Peso de neo: ", neo5.peso  )
print("Peso de trinity: ", trinity5.peso)
print("Peso de morfeo: ", morfeo5.peso)
trinity5.alimentarse(30)
print("Peso de neo: ", neo5.peso  )
print("Peso de trinity: ", trinity5.peso)
print("Peso de morfeo: ", morfeo5.peso)
trinity5.eleminar_desechos(50)
print("Peso de neo: ", neo5.peso  )
print("Peso de trinity: ", trinity5.peso)
print("Peso de morfeo: ", morfeo5.peso)
neo5.ejercitar(30)
print("Peso de neo: ", neo5.peso  )
print("Peso de trinity: ", trinity5.peso)
print("Peso de morfeo: ", morfeo5.peso)