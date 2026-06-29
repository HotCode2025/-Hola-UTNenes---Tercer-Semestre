from conexion import conectar
from psycopg2.extras import RealDictCursor


def crear_cliente(conn, nombre, apellido, dni, email=None, telefono=None, direccion=None):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            INSERT INTO clientes (nombre, apellido, dni, email, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING *;
        """, (nombre, apellido, dni, email, telefono, direccion))
        conn.commit()
        return dict(cur.fetchone())


def listar_clientes(conn):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM clientes ORDER BY apellido, nombre;")
        return [dict(row) for row in cur.fetchall()]


def obtener_cliente(conn, cliente_id):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM clientes WHERE id = %s;", (cliente_id,))
        resultado = cur.fetchone()
        return dict(resultado) if resultado else None


def buscar_por_dni(conn, dni):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM clientes WHERE dni = %s;", (dni,))
        resultado = cur.fetchone()
        return dict(resultado) if resultado else None


def actualizar_cliente(conn, cliente_id, nombre=None, apellido=None, dni=None,
                        email=None, telefono=None, direccion=None):
    campos = {
        "nombre": nombre, "apellido": apellido, "dni": dni,
        "email": email, "telefono": telefono, "direccion": direccion,
    }
    campos_a_actualizar = {k: v for k, v in campos.items() if v is not None}

    if not campos_a_actualizar:
        return obtener_cliente(conn, cliente_id)

    set_clause = ", ".join(f"{k} = %s" for k in campos_a_actualizar)
    valores = list(campos_a_actualizar.values()) + [cliente_id]

    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            f"UPDATE clientes SET {set_clause} WHERE id = %s RETURNING *;",
            valores
        )
        conn.commit()
        resultado = cur.fetchone()
        return dict(resultado) if resultado else None


def eliminar_cliente(conn, cliente_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM clientes WHERE id = %s;", (cliente_id,))
        conn.commit()
        return cur.rowcount > 0


def _mostrar_cliente(c):
    print(f"\n  ID: {c['id']} | {c['nombre']} {c['apellido']} | DNI: {c['dni']}")
    print(f"  Email: {c.get('email', '-')} | Tel: {c.get('telefono', '-')}")
    print(f"  Dirección: {c.get('direccion', '-')} | Registro: {c.get('fecha_registro', '-')}")


def menu_clientes():
    conn = conectar()

    while True:
        print("\n===== GESTIÓN DE CLIENTES =====")
        print("  1. Crear cliente")
        print("  2. Listar clientes")
        print("  3. Buscar cliente por ID")
        print("  4. Actualizar cliente")
        print("  5. Eliminar cliente")
        print("  6. Buscar cliente por DNI")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre    = input("Nombre: ").strip()
            apellido  = input("Apellido: ").strip()
            dni       = input("DNI: ").strip()
            email     = input("Email (opcional): ").strip() or None
            telefono  = input("Teléfono (opcional): ").strip() or None
            direccion = input("Dirección (opcional): ").strip() or None
            try:
                c = crear_cliente(conn, nombre, apellido, dni, email, telefono, direccion)
                print("Cliente creado:")
                _mostrar_cliente(c)
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "2":
            clientes = listar_clientes(conn)
            if not clientes:
                print("No hay clientes registrados.")
            for c in clientes:
                _mostrar_cliente(c)

        elif opcion == "3":
            cid = input("ID del cliente: ").strip()
            c = obtener_cliente(conn, int(cid))
            if c:
                _mostrar_cliente(c)
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            cid = input("ID del cliente a actualizar: ").strip()
            print("(Dejar vacío para no modificar)")
            nombre    = input("Nuevo nombre: ").strip() or None
            apellido  = input("Nuevo apellido: ").strip() or None
            dni       = input("Nuevo DNI: ").strip() or None
            email     = input("Nuevo email: ").strip() or None
            telefono  = input("Nuevo teléfono: ").strip() or None
            direccion = input("Nueva dirección: ").strip() or None
            try:
                c = actualizar_cliente(conn, int(cid), nombre, apellido, dni, email, telefono, direccion)
                if c:
                    print("Cliente actualizado:")
                    _mostrar_cliente(c)
                else:
                    print("Cliente no encontrado.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "5":
            cid = input("ID del cliente a eliminar: ").strip()
            try:
                cid_int = int(cid)
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(*) FROM turnos WHERE id_cliente = %s;", (cid_int,))
                    cantidad = cur.fetchone()[0]
                if cantidad > 0:
                    print(f"No se puede eliminar: el cliente tiene {cantidad} turno(s) asociado(s).")
                    print("Primero eliminá los turnos relacionados.")
                else:
                    confirmacion = input(f"¿Eliminar cliente {cid}? (s/n): ").strip().lower()
                    if confirmacion == "s":
                        ok = eliminar_cliente(conn, cid_int)
                        print("Cliente eliminado." if ok else "Cliente no encontrado.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "6":
            dni = input("DNI a buscar: ").strip()
            c = buscar_por_dni(conn, dni)
            if c:
                _mostrar_cliente(c)
            else:
                print("Cliente no encontrado.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    conn.close()