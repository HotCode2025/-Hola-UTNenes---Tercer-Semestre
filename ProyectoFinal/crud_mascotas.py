from conexion import conectar


def crear_mascota(conn, nombre_mascota, raza_mascota):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO mascotas (nombre_mascota, raza_mascota)
            VALUES (%s, %s)
            RETURNING *;
        """, (nombre_mascota, raza_mascota))
        conn.commit()
        return cur.fetchone()


def listar_mascotas(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM mascotas ORDER BY id;")
        return cur.fetchall()


def obtener_mascota(conn, id_mascota):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM mascotas WHERE id = %s;", (id_mascota,))
        return cur.fetchone()


def actualizar_mascota(conn, id_mascota, nombre_mascota=None, raza_mascota=None):
    campos = {"nombre_mascota": nombre_mascota, "raza_mascota": raza_mascota}
    campos_a_actualizar = {k: v for k, v in campos.items() if v is not None}

    if not campos_a_actualizar:
        return obtener_mascota(conn, id_mascota)

    set_clause = ", ".join(f"{k} = %s" for k in campos_a_actualizar)
    valores = list(campos_a_actualizar.values()) + [id_mascota]

    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE mascotas SET {set_clause} WHERE id = %s RETURNING *;",
            valores
        )
        conn.commit()
        return cur.fetchone()


def eliminar_mascota(conn, id_mascota):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM mascotas WHERE id = %s;", (id_mascota,))
        conn.commit()
        return cur.rowcount > 0


def _mostrar_mascota(m):
    print(f"\n  ID: {m[0]} | Nombre: {m[1]} | Raza: {m[2]}")
    print(f"  Ingreso: {m[3]} | Salida: {m[4] if m[4] else '-'}")


def menu_mascotas():
    conn = conectar()

    while True:
        print("\n===== GESTIÓN DE MASCOTAS =====")
        print("  1. Agregar mascota")
        print("  2. Listar mascotas")
        print("  3. Buscar mascota por ID")
        print("  4. Actualizar mascota")
        print("  5. Eliminar mascota")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la mascota: ").strip()
            raza   = input("Raza: ").strip()
            try:
                m = crear_mascota(conn, nombre, raza)
                print("Mascota agregada:")
                _mostrar_mascota(m)
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "2":
            mascotas = listar_mascotas(conn)
            if not mascotas:
                print("No hay mascotas registradas.")
            for m in mascotas:
                _mostrar_mascota(m)

        elif opcion == "3":
            mid = input("ID de la mascota: ").strip()
            m = obtener_mascota(conn, int(mid))
            if m:
                _mostrar_mascota(m)
            else:
                print("Mascota no encontrada.")

        elif opcion == "4":
            mid    = input("ID de la mascota a actualizar: ").strip()
            print("(Dejar vacío para no modificar)")
            nombre = input("Nuevo nombre: ").strip() or None
            raza   = input("Nueva raza: ").strip() or None
            try:
                m = actualizar_mascota(conn, int(mid), nombre, raza)
                if m:
                    print("Mascota actualizada:")
                    _mostrar_mascota(m)
                else:
                    print("Mascota no encontrada.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "5":
            mid = input("ID de la mascota a eliminar: ").strip()
            try:
                mid_int = int(mid)
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(*) FROM turnos WHERE id_mascota = %s;", (mid_int,))
                    cantidad = cur.fetchone()[0]
                if cantidad > 0:
                    print(f"No se puede eliminar: la mascota tiene {cantidad} turno(s) asociado(s).")
                    print("Primero eliminá los turnos relacionados.")
                else:
                    confirmacion = input(f"¿Eliminar mascota {mid}? (s/n): ").strip().lower()
                    if confirmacion == "s":
                        ok = eliminar_mascota(conn, mid_int)
                        print("Mascota eliminada." if ok else "Mascota no encontrada.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    conn.close()