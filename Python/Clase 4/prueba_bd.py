import psycopg2 #Esto es para conectarse a postgre

conexion = psycopg2.connect(
    user = "postgres",
    password = "Abril060924",
    host= "127.0.0.1",
    port = "5433",
    database= "test_bd"

)

cursor = conexion.cursor()
sentencia= "SELECT * FROM persona"
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)


