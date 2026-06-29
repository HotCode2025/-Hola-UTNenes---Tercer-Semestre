from conexion import conectar


def agregar_servicio(conn):
    nombre      = input("Nombre del servicio: ").strip()
    descripcion = input("Descripción: ").strip()
    precio      = float(input("Precio: "))
    duracion    = int(input("Duración en minutos: "))

    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO servicios (nombre, descripcion, precio, duracion_minutos)
            VALUES (%s, %s, %s, %s)
        """, (nombre, descripcion, precio, duracion))
        conn.commit()
    print("Servicio agregado correctamente.")


def mostrar_servicios(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM servicios ORDER BY id_servicio;")
        servicios = cur.fetchall()

    if not servicios:
        print("No hay servicios registrados.")
        return

    print("\n===== LISTA DE SERVICIOS =====")
    for s in servicios:
        print(f"\n  ID: {s[0]} | Nombre: {s[1]}")
        print(f"  Descripción: {s[2]}")
        print(f"  Precio: ${s[3]} | Duración: {s[4]} minutos")


def modificar_servicio(conn):
    mostrar_servicios(conn)
    id_servicio = int(input("ID del servicio a modificar: "))

    with conn.cursor() as cur:
        cur.execute("SELECT nombre, descripcion, precio, duracion_minutos FROM servicios WHERE id_servicio = %s;", (id_servicio,))
        actual = cur.fetchone()

    if not actual:
        print("Servicio no encontrado.")
        return

    print("(Dejar vacío para no modificar)")
    nombre      = input(f"Nombre [{actual[0]}]: ").strip() or actual[0]
    descripcion = input(f"Descripción [{actual[1]}]: ").strip() or actual[1]
    precio_str  = input(f"Precio [{actual[2]}]: ").strip()
    precio      = float(precio_str) if precio_str else actual[2]
    duracion_str = input(f"Duración en minutos [{actual[3]}]: ").strip()
    duracion    = int(duracion_str) if duracion_str else actual[3]

    with conn.cursor() as cur:
        cur.execute("""
            UPDATE servicios
            SET nombre = %s, descripcion = %s, precio = %s, duracion_minutos = %s
            WHERE id_servicio = %s
        """, (nombre, descripcion, precio, duracion, id_servicio))
        conn.commit()
    print("Servicio actualizado correctamente.")


def eliminar_servicio(conn):
    mostrar_servicios(conn)
    id_servicio = int(input("ID del servicio a eliminar: "))

    confirmacion = input(f"¿Eliminar servicio {id_servicio}? (s/n): ").strip().lower()
    if confirmacion == "s":
        with conn.cursor() as cur:
            cur.execute("DELETE FROM servicios WHERE id_servicio = %s", (id_servicio,))
            conn.commit()
            if cur.rowcount > 0:
                print("Servicio eliminado correctamente.")
            else:
                print("Servicio no encontrado.")


def menu_servicios():
    conn = conectar()

    while True:
        print("\n===== GESTIÓN DE SERVICIOS =====")
        print("  1. Agregar servicio")
        print("  2. Mostrar servicios")
        print("  3. Modificar servicio")
        print("  4. Eliminar servicio")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                agregar_servicio(conn)
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")
        elif opcion == "2":
            mostrar_servicios(conn)
        elif opcion == "3":
            try:
                modificar_servicio(conn)
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")
        elif opcion == "4":
            try:
                eliminar_servicio(conn)
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    conn.close()
