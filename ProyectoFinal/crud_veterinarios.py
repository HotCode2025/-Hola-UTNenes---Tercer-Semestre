from conexion import conectar
from veterinario import Veterinario


def agregar_veterinario(veterinario):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO veterinarios
    (nombre, matricula, telefono, email)
    VALUES (%s,%s,%s,%s)
    """

    valores = (
        veterinario.nombre,
        veterinario.matricula,
        veterinario.telefono,
        veterinario.email
    )

    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

    print("\nVeterinario agregado correctamente.\n")


def listar_veterinarios():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM veterinarios ORDER BY id_veterinario;")
    registros = cursor.fetchall()

    if not registros:
        print("No hay veterinarios registrados.")
    else:
        for registro in registros:
            veterinario = Veterinario(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4]
            )
            print(veterinario)

    cursor.close()
    conexion.close()


def modificar_veterinario(veterinario):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    UPDATE veterinarios
    SET nombre=%s,
        matricula=%s,
        telefono=%s,
        email=%s
    WHERE id_veterinario=%s
    """

    valores = (
        veterinario.nombre,
        veterinario.matricula,
        veterinario.telefono,
        veterinario.email,
        veterinario.id_veterinario,
    )

    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

    print("\nVeterinario actualizado.\n")


def eliminar_veterinario(id_veterinario):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "DELETE FROM veterinarios WHERE id_veterinario=%s"
    cursor.execute(sql, (id_veterinario,))
    conexion.commit()
    cursor.close()
    conexion.close()

    print("\nVeterinario eliminado.\n")


def menu_veterinarios():
    while True:
        print("\n===== GESTIÓN DE VETERINARIOS =====")
        print("  1. Listar veterinarios")
        print("  2. Agregar veterinario")
        print("  3. Modificar veterinario")
        print("  4. Eliminar veterinario")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            listar_veterinarios()

        elif opcion == "2":
            nombre    = input("Nombre: ").strip()
            matricula = input("Matrícula: ").strip()
            telefono  = input("Teléfono: ").strip()
            email     = input("Email: ").strip()
            v = Veterinario(None, nombre, matricula, telefono, email)
            try:
                agregar_veterinario(v)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            listar_veterinarios()
            try:
                id_vet    = int(input("ID del veterinario a modificar: ").strip())
                print("(Completar todos los campos)")
                nombre    = input("Nombre: ").strip()
                matricula = input("Matrícula: ").strip()
                telefono  = input("Teléfono: ").strip()
                email     = input("Email: ").strip()
                v = Veterinario(id_vet, nombre, matricula, telefono, email)
                modificar_veterinario(v)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            listar_veterinarios()
            try:
                id_vet = int(input("ID del veterinario a eliminar: ").strip())
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM turnos WHERE id_veterinario = %s;", (id_vet,))
                cantidad = cursor.fetchone()[0]
                cursor.close()
                conexion.close()
                if cantidad > 0:
                    print(f"No se puede eliminar: el veterinario tiene {cantidad} turno(s) asociado(s).")
                    print("Primero reasigná o eliminá esos turnos.")
                else:
                    confirm = input(f"¿Eliminar veterinario {id_vet}? (s/n): ").strip().lower()
                    if confirm == "s":
                        eliminar_veterinario(id_vet)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
