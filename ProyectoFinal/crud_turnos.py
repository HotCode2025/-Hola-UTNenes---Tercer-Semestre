from conexion import conectar


def registrar_turno(conn, id_cliente, id_mascota, fecha, hora, id_veterinario=None):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO turnos (id_cliente, id_mascota, id_veterinario, fecha, hora, estado)
            VALUES (%s, %s, %s, %s, %s, 'Pendiente')
            RETURNING id_turno;
        """, (id_cliente, id_mascota, id_veterinario, fecha, hora))
        conn.commit()
        return cur.fetchone()[0]


def listar_turnos(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT t.id_turno,
                   c.nombre || ' ' || c.apellido AS cliente,
                   m.nombre_mascota,
                   COALESCE(v.nombre, 'Sin asignar') AS veterinario,
                   t.fecha, t.hora, t.estado
            FROM turnos t
            JOIN clientes c ON t.id_cliente = c.id
            JOIN mascotas m ON t.id_mascota = m.id
            LEFT JOIN veterinarios v ON t.id_veterinario = v.id_veterinario
            ORDER BY t.fecha, t.hora;
        """)
        return cur.fetchall()


def obtener_turno(conn, id_turno):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT t.id_turno,
                   c.nombre || ' ' || c.apellido AS cliente,
                   m.nombre_mascota,
                   COALESCE(v.nombre, 'Sin asignar') AS veterinario,
                   t.fecha, t.hora, t.estado
            FROM turnos t
            JOIN clientes c ON t.id_cliente = c.id
            JOIN mascotas m ON t.id_mascota = m.id
            LEFT JOIN veterinarios v ON t.id_veterinario = v.id_veterinario
            WHERE t.id_turno = %s;
        """, (id_turno,))
        return cur.fetchone()


def actualizar_estado(conn, id_turno, estado):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE turnos SET estado = %s WHERE id_turno = %s;
        """, (estado, id_turno))
        conn.commit()
        return cur.rowcount > 0


def eliminar_turno(conn, id_turno):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM turnos WHERE id_turno = %s;", (id_turno,))
        conn.commit()
        return cur.rowcount > 0


def _mostrar_turno(t):
    print(f"\n  ID: {t[0]} | Fecha: {t[4]} | Hora: {t[5]} | Estado: {t[6]}")
    print(f"  Cliente: {t[1]} | Mascota: {t[2]} | Veterinario: {t[3]}")


def _mostrar_disponibles(conn):
    print("\n  --- Clientes ---")
    with conn.cursor() as cur:
        cur.execute("SELECT id, nombre || ' ' || apellido FROM clientes ORDER BY apellido;")
        for row in cur.fetchall():
            print(f"    ID {row[0]}: {row[1]}")

    print("\n  --- Mascotas ---")
    with conn.cursor() as cur:
        cur.execute("SELECT id, nombre_mascota, raza_mascota FROM mascotas ORDER BY id;")
        for row in cur.fetchall():
            print(f"    ID {row[0]}: {row[1]} ({row[2]})")

    print("\n  --- Veterinarios ---")
    with conn.cursor() as cur:
        cur.execute("SELECT id_veterinario, nombre FROM veterinarios ORDER BY id_veterinario;")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(f"    ID {row[0]}: {row[1]}")
        else:
            print("    No hay veterinarios registrados.")


def menu_turnos():
    conn = conectar()

    while True:
        print("\n===== GESTIÓN DE TURNOS =====")
        print("  1. Registrar turno")
        print("  2. Listar turnos")
        print("  3. Buscar turno por ID")
        print("  4. Cambiar estado del turno")
        print("  5. Eliminar turno")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                _mostrar_disponibles(conn)
            except Exception as e:
                print(f"Error al cargar datos: {e}")
                continue

            try:
                id_cliente = int(input("\nID del cliente: ").strip())
                id_mascota = int(input("ID de la mascota: ").strip())

                fecha = input("Fecha (YYYY-MM-DD): ").strip()
                if not fecha:
                    print("La fecha es obligatoria.")
                    continue

                hora = input("Hora (HH:MM): ").strip()
                if not hora:
                    print("La hora es obligatoria.")
                    continue

                id_veterinario = input("ID del veterinario (Enter para dejar sin asignar): ").strip() or None
                if id_veterinario:
                    id_veterinario = int(id_veterinario)

                id_turno = registrar_turno(conn, id_cliente, id_mascota, fecha, hora, id_veterinario)
                t = obtener_turno(conn, id_turno)
                print("Turno registrado:")
                _mostrar_turno(t)
            except ValueError:
                print("Error: ingresá un número válido para los IDs.")
            except Exception as e:
                conn.rollback()
                error = str(e)
                if "id_cliente" in error:
                    print("Error: el cliente ingresado no existe. Creá el cliente primero.")
                elif "id_mascota" in error:
                    print("Error: la mascota ingresada no existe. Creá la mascota primero.")
                elif "id_veterinario" in error:
                    print("Error: el veterinario ingresado no existe.")
                elif "date" in error or "time" in error:
                    print("Error: formato de fecha u hora inválido. Usá YYYY-MM-DD y HH:MM.")
                else:
                    print(f"Error: {e}")

        elif opcion == "2":
            turnos = listar_turnos(conn)
            if not turnos:
                print("No hay turnos registrados.")
            for t in turnos:
                _mostrar_turno(t)

        elif opcion == "3":
            tid = input("ID del turno: ").strip()
            try:
                t = obtener_turno(conn, int(tid))
                if t:
                    _mostrar_turno(t)
                else:
                    print("Turno no encontrado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            tid = input("ID del turno: ").strip()
            print("Estados: Pendiente / Confirmado / Cancelado / Finalizado")
            estado = input("Nuevo estado: ").strip()
            try:
                ok = actualizar_estado(conn, int(tid), estado)
                if ok:
                    t = obtener_turno(conn, int(tid))
                    print("Estado actualizado:")
                    _mostrar_turno(t)
                else:
                    print("Turno no encontrado.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "5":
            tid = input("ID del turno a eliminar: ").strip()
            confirmacion = input(f"¿Eliminar turno {tid}? (s/n): ").strip().lower()
            if confirmacion == "s":
                try:
                    ok = eliminar_turno(conn, int(tid))
                    print("Turno eliminado." if ok else "Turno no encontrado.")
                except Exception as e:
                    conn.rollback()
                    print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    conn.close()
