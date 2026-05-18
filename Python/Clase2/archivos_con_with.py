from ManejoArchivos import ManejoArchivos

# MENEJO DE CONTEXTO WITH: Sintaxis simplificada, abre y cierra el archivo
#vwith open('prueba.txt', encoding='utf8') as archivo:
   # print(archivo.read())
# No hace falta ni el try, ni el finally
# En el contexto with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos:  __enter__ este es el quee abre
# Ahora el siguiente metodo es el que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())