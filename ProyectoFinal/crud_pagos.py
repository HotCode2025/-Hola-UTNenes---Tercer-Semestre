from conexion import conectar


def _listar_turnos(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT t.id_turno,
                   c.nombre || ' ' || c.apellido AS cliente,
                   m.nombre_mascota,
                   COALESCE(v.nombre, '-') AS veterinario,
                   t.fecha, t.hora, t.estado
            FROM turnos t
            JOIN clientes c ON t.id_cliente = c.id
            JOIN mascotas m ON t.id_mascota = m.id
            LEFT JOIN veterinarios v ON t.id_veterinario = v.id_veterinario
            ORDER BY t.fecha DESC, t.hora DESC;
        """)
        return cur.fetchall()


def registrar_pago(conn, id_turno, monto, metodo_pago, estado='pendiente',
                   fecha_pago=None, observaciones=None):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO pagos (id_turno, monto, metodo_pago, estado, fecha_pago, observaciones)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_pago;
        """, (id_turno, monto, metodo_pago, estado, fecha_pago, observaciones))
        conn.commit()
        return cur.fetchone()[0]


def listar_pagos(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT p.id_pago,
                   c.nombre || ' ' || c.apellido AS cliente,
                   m.nombre_mascota,
                   COALESCE(v.nombre, '-') AS veterinario,
                   p.monto, p.metodo_pago, p.estado, p.fecha_pago
            FROM pagos p
            JOIN turnos t ON p.id_turno = t.id_turno
            JOIN clientes c ON t.id_cliente = c.id
            JOIN mascotas m ON t.id_mascota = m.id
            LEFT JOIN veterinarios v ON t.id_veterinario = v.id_veterinario
            ORDER BY p.id_pago DESC;
        """)
        return cur.fetchall()


def actualizar_pago(conn, id_pago, estado=None, metodo_pago=None,
                    fecha_pago=None, observaciones=None):
    campos = {}
    if estado:
        campos['estado'] = estado
    if metodo_pago:
        campos['metodo_pago'] = metodo_pago
    if fecha_pago:
        campos['fecha_pago'] = fecha_pago
    if observaciones is not None:
        campos['observaciones'] = observaciones

    if not campos:
        return False

    set_clause = ", ".join(f"{k} = %s" for k in campos)
    valores = list(campos.values()) + [id_pago]

    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE pagos SET {set_clause} WHERE id_pago = %s;",
            valores
        )
        conn.commit()
        return cur.rowcount > 0


def mostrar_estadisticas(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT COALESCE(SUM(monto), 0) FROM pagos WHERE estado = 'pagado'")
        total_recaudado = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM pagos WHERE estado = 'pendiente'")
        pendientes = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM pagos")
        total_pagos = cur.fetchone()[0]

        cur.execute("""
            SELECT TO_CHAR(fecha_pago, 'MM/YYYY') AS mes, SUM(monto) AS total
            FROM pagos
            WHERE estado = 'pagado' AND fecha_pago IS NOT NULL
            GROUP BY mes, DATE_TRUNC('month', fecha_pago)
            ORDER BY DATE_TRUNC('month', fecha_pago) DESC;
        """)
        por_mes = cur.fetchall()

        cur.execute("""
            SELECT metodo_pago, COUNT(*) AS cantidad, SUM(monto) AS total
            FROM pagos
            WHERE estado = 'pagado'
            GROUP BY metodo_pago
            ORDER BY total DESC;
        """)
        por_metodo = cur.fetchall()

        cur.execute("""
            SELECT v.nombre, COUNT(*) AS turnos
            FROM turnos t
            JOIN veterinarios v ON t.id_veterinario = v.id_veterinario
            GROUP BY v.nombre
            ORDER BY turnos DESC;
        """)
        por_vet = cur.fetchall()

    print("\n===== ESTADÍSTICAS Y REPORTES =====")
    print(f"\n  Total recaudado:  ${total_recaudado:.2f}")
    print(f"  Pagos pendientes: {pendientes}")
    print(f"  Total de pagos:   {total_pagos}")

    if por_mes:
        print("\n  Recaudación por mes:")
        for mes, total in por_mes:
            print(f"    {mes}: ${total:.2f}")

    if por_metodo:
        print("\n  Por método de pago:")
        for metodo, cantidad, total in por_metodo:
            print(f"    {metodo}: {cantidad} pagos — ${total:.2f}")

    if por_vet:
        print("\n  Turnos por veterinario:")
        for vet, cantidad in por_vet:
            print(f"    {vet}: {cantidad} turnos")


def _mostrar_pago(p):
    fecha = p[7] if p[7] else '-'
    print(f"\n  ID Pago: {p[0]} | Cliente: {p[1]} | Mascota: {p[2]}")
    print(f"  Veterinario: {p[3]} | Monto: ${p[4]:.2f}")
    print(f"  Método: {p[5]} | Estado: {p[6]} | Fecha pago: {fecha}")


def menu_pagos():
    conn = conectar()

    while True:
        print("\n===== GESTIÓN DE PAGOS =====")
        print("  1. Registrar pago")
        print("  2. Listar pagos")
        print("  3. Actualizar pago")
        print("  4. Estadísticas y reportes")
        print("  0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            turnos = _listar_turnos(conn)
            if not turnos:
                print("No hay turnos registrados.")
                continue
            print("\n  Turnos disponibles:")
            for t in turnos:
                print(f"    ID: {t[0]} | {t[1]} - {t[2]} | Vet: {t[3]} | {t[4]} {t[5]} | {t[6]}")
            try:
                id_turno  = int(input("ID del turno: ").strip())
                monto     = float(input("Monto: ").strip())
                print("  Métodos: efectivo / tarjeta / transferencia")
                metodo    = input("Método de pago: ").strip()
                print("  Estado: pendiente / pagado")
                estado    = input("Estado: ").strip()
                fecha     = input("Fecha de pago (YYYY-MM-DD, opcional): ").strip() or None
                obs       = input("Observaciones (opcional): ").strip() or None
                id_pago   = registrar_pago(conn, id_turno, monto, metodo, estado, fecha, obs)
                print(f"Pago registrado. ID: {id_pago}")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "2":
            pagos = listar_pagos(conn)
            if not pagos:
                print("No hay pagos registrados.")
            for p in pagos:
                _mostrar_pago(p)

        elif opcion == "3":
            pid = input("ID del pago a actualizar: ").strip()
            print("(Dejar vacío para no modificar)")
            print("  Estado: pendiente / pagado")
            estado   = input("Nuevo estado: ").strip() or None
            print("  Métodos: efectivo / tarjeta / transferencia")
            metodo   = input("Nuevo método de pago: ").strip() or None
            fecha    = input("Nueva fecha de pago (YYYY-MM-DD): ").strip() or None
            obs      = input("Nuevas observaciones: ").strip() or None
            try:
                ok = actualizar_pago(conn, int(pid), estado, metodo, fecha, obs)
                print("Pago actualizado." if ok else "Pago no encontrado o sin cambios.")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                mostrar_estadisticas(conn)
            except Exception as e:
                print(f"Error al obtener estadísticas: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

    conn.close()
