import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from catalogo_peliculas.dominio.pelicula import Pelicula
from catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas


def menu():
    while True:
        print("\n--- Catálogo de Películas ---")
        print("1) Agregar película")
        print("2) Listar películas")
        print("3) Eliminar archivo de películas")
        print("4) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre)
            CatalogoPeliculas.agregar_pelicula(pelicula)
            print(f"Película '{nombre}' agregada.")
        elif opcion == "2":
            CatalogoPeliculas.listar_peliculas()
        elif opcion == "3":
            CatalogoPeliculas.eliminar()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
