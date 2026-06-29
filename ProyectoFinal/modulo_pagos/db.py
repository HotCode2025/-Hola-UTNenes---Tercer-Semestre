import psycopg2

DB = {
    "host": "localhost",
    "database": "veterinaria",
    "user": "postgres",
    "password": "postgres"
}

def get_connection():
    return psycopg2.connect(**DB)

def init_db():
    conexion = get_connection()
    cursor = conexion.cursor()
    with open("schema.sql", "r", encoding="utf-8") as archivo:
        cursor.execute(archivo.read())
    conexion.commit()
    cursor.close()
    conexion.close()
