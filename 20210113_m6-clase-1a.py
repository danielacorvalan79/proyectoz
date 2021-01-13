import psycopg2
print("Psycopg2 importado exitósamente!!!")

HOST = 'localhost'
USER = 'postgres'
PASSWORD = '1234'
DBNAME = 'mibase'
PORT = '5432'

conector = psycopg2.connect(
                        host = HOST,
                        user = USER,
                        password = PASSWORD,
                        dbname = DBNAME,
                        port = PORT
                        )

print("La base de datos ya fué abierta!!!!!")

with conector.cursor() as cursor:
    consulta = "SELECT * FROM profesor"
    #En DJANGO SERÍA: Profesor.objects.all()
    # consulta = "Select * from profesor where nombre ='Rocío'"
    #En DJANGO SERÍA: Profesor.objects.filter(nombre='Rocío')
    cursor.execute(consulta)
    profesores = cursor.fetchall()
    print("Memoria ocupada por cursor", cursor.__sizeof__())
    print("Memoria ocupada por profesores", profesores.__sizeof__())
    for profesor in profesores:
        print("Enviando Email a profesor:", profesor[1], profesor[2])
    
    cursor.scroll(8, mode='absolute')
    for i in range(0,5):
        print(cursor.fetchone())

