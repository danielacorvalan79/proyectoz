import time
import random

c = 100
while c != 5:
    print("c no es 5")
    c = random.randint(0,20)
    print("c es: ", c)
    time.sleep(0.01)

n = 5
while n > 0 :
    print('Lavar')
    print('Enjuagar')
    n = n - 1
print('Secar!')


print("\nSegunda lavadorea")
n = int(input("Cuéntas veces quiere lavar"))
while n > 0 :
    n = n - 1
    print('Lavar')
    print('Enjuagar')
print('Secar!')


# 4 ##########################################################################
# ejemplo de while con interrupciones a través de break y continue
print("\nLoop interrumpido")
impostores = ["Diego", "Oscar", "Luis"]

presentes = [
    "Alvaro",
    "Boris", 
    "Cinthia",
    "Daniela",
    "Eduardo",
    "Diego",
    "Eduardo",
    "Eduardo2",
    "Germán",
    "Jean Carlos",
    "Jesús",
    "Joao",
    "José",
    "Manuel",
    "Martin",
    "Oscar",
    "Natalia",
    "Pedro",
    "Luis",
    "Rocío"]

num_presentes = len(presentes)
contador = 0

print("Número de presentes: ", num_presentes)
contador_impostores_encontrados = 0

while contador <= num_presentes:
    time.sleep(0.1)
    print("")
    print("Contador: ", contador)
    contador_de_impostores = 0
    while contador_de_impostores <= len(impostores)-1:
        mensaje_de_continue = False
        print("Estoy dentro de loop de chequeo de impostores")
        #print(impostores[contador_de_impostores], presentes[contador])
        if impostores[contador_de_impostores] == presentes[contador]:
            contador_impostores_encontrados += 1
            print("EMERGENCIA!!: Llamando a Superman!!! Hay un impostor en la sala y se llama:", presentes[contador])
            mensaje_de_continue = True
            break
        contador_de_impostores += 1
    contador = contador + 1
    if contador_impostores_encontrados == len(impostores):
        print("ATENCIÓN MISIÓN CUMPLIDA: Hemos limpiado este curso!!! I'LL BE BACK!")
        break
    if mensaje_de_continue == True:
        continue
    print("El Alumno: " +  str(presentes[contador-1]) + " Está validado!")
    if contador > num_presentes-1:
        break
if contador_impostores_encontrados < len(impostores):
    print("ATENCIÓN: No se encontraron todos los impostores informados.")
print("Tarea Terminada. Los cuerpos de los impostores han sido arrojados a un pozo negro!!!")


# versión más eficiente del código 4, aún usando "while", "break", "continue" y sin utilizar "in"


# versión ultra eficiente del código 4, con cualquier método
