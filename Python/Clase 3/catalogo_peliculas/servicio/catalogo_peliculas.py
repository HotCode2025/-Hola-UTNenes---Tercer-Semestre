import os


class CatalogoPeliculas:
    ruta_archivo: str = "peliculas.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula) -> None:
        with open(cls.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def listar_peliculas(cls) -> None:
        with open(cls.ruta_archivo, "r", encoding="utf-8") as archivo:
            print("Catalogo de peliculas".center(50, "-"))
            print(archivo.read())

    @classmethod
    def eliminar(cls) -> None:
        try:
            os.remove(cls.ruta_archivo)
            print("Archivo de películas eliminado.")
        except FileNotFoundError:
            print("No existe el archivo de películas.")
