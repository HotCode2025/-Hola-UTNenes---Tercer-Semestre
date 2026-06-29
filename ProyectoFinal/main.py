from usuario import registrar_usuario
from CRUDdeClientes import menu_clientes
from crud_mascotas import menu_mascotas
from Crud_servicios import menu_servicios
from crud_turnos import menu_turnos
from crud_veterinarios import menu_veterinarios
from crud_pagos import menu_pagos


def menu_administrador():
    while True:
        print("\n===== MENÚ ADMINISTRADOR =====")
        print("  1. Gestión de clientes")
        print("  2. Gestión de mascotas")
        print("  3. Gestión de servicios")
        print("  4. Gestión de turnos")
        print("  5. Gestión de veterinarios")
        print("  6. Gestión de pagos")
        print("  0. Cerrar sesión")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_mascotas()
        elif opcion == "3":
            menu_servicios()
        elif opcion == "4":
            menu_turnos()
        elif opcion == "5":
            menu_veterinarios()
        elif opcion == "6":
            menu_pagos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_recepcionista():
    while True:
        print("\n===== MENÚ RECEPCIONISTA =====")
        print("  1. Gestión de clientes")
        print("  2. Gestión de turnos")
        print("  3. Gestión de pagos")
        print("  0. Cerrar sesión")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_turnos()
        elif opcion == "3":
            menu_pagos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_veterinario():
    while True:
        print("\n===== MENÚ VETERINARIO =====")
        print("  1. Gestión de mascotas")
        print("  2. Gestión de turnos")
        print("  0. Cerrar sesión")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_mascotas()
        elif opcion == "2":
            menu_turnos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def login():
    from conexion import conectar

    print("\n===== LOGIN =====")
    print("(Presioná Enter sin escribir nada para cancelar)\n")
    usuario_input = input("Usuario: ").strip()
    if not usuario_input:
        return None
    contrasena_input = input("Contraseña: ").strip()

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        SELECT u.nombre, u.apellido, r.nombre
        FROM usuarios u
        JOIN roles r ON u.id_rol = r.id_rol
        WHERE u.usuario = %s AND u.contrasena = %s AND u.activo = TRUE
    """
    cursor.execute(sql, (usuario_input, contrasena_input))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado:
        nombre, apellido, rol = resultado
        print(f"\nBienvenido, {nombre} {apellido} ({rol})")
        return rol
    else:
        print("\nUsuario o contraseña incorrectos.")
        return None


# ===== PROGRAMA PRINCIPAL =====

print("\n==============================")
print("     SISTEMA VETERINARIA      ")
print("==============================")

while True:
    print("\n  1. Iniciar sesión")
    print("  2. Registrar nuevo usuario")
    print("  0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        rol = login()
        if rol == "Administrador":
            menu_administrador()
        elif rol == "Recepcionista":
            menu_recepcionista()
        elif rol == "Veterinario":
            menu_veterinario()

    elif opcion == "2":
        registrar_usuario()

    elif opcion == "0":
        print("\nHasta luego.")
        break

    else:
        print("Opción inválida.")
