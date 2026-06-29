import psycopg2

def conectar():
    conexion = psycopg2.connect(
        host="localhost",
        database="veterinaria",
        user="postgres",
        password="admin",
        port=5432
    )
    return conexion