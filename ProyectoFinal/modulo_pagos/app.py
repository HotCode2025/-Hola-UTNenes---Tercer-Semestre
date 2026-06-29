from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "veterinaria2025"

# Datos de conexión a la base de datos
DB = {
    "host": "localhost",
    "database": "veterinaria",
    "user": "postgres",
    "password": "postgres"
}

# Función para conectarse a la base de datos
def conectar():
    conexion = psycopg2.connect(**DB)
    conexion.set_client_encoding('UTF8')
    return conexion


# -------------------------------------------------------
# PÁGINA DE INICIO
# -------------------------------------------------------

@app.route("/")
def inicio():
    conexion = conectar()
    cursor = conexion.cursor()

    # Cuánto dinero se recaudó en total
    cursor.execute("SELECT SUM(monto) FROM pagos WHERE estado = 'pagado'")
    resultado = cursor.fetchone()[0]
    total_recaudado = resultado if resultado else 0

    # Cuántos pagos están pendientes
    cursor.execute("SELECT COUNT(*) FROM pagos WHERE estado = 'pendiente'")
    pendientes = cursor.fetchone()[0]

    # Total de pagos registrados
    cursor.execute("SELECT COUNT(*) FROM pagos")
    total_pagos = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return render_template("index.html",
                           total_recaudado=total_recaudado,
                           pendientes=pendientes,
                           total_pagos=total_pagos)


# -------------------------------------------------------
# VER TODOS LOS PAGOS
# -------------------------------------------------------

@app.route("/pagos")
def ver_pagos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT p.id, t.cliente_nombre, t.mascota_nombre,
               s.nombre, v.nombre,
               p.monto, p.metodo_pago, p.estado, p.fecha_pago
        FROM pagos p
        JOIN turnos t ON p.turno_id = t.id
        JOIN servicios s ON t.servicio_id = s.id
        JOIN veterinarios v ON t.veterinario_id = v.id
        ORDER BY p.id DESC
    """)
    lista_pagos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("pagos/lista.html", pagos=lista_pagos)


# -------------------------------------------------------
# REGISTRAR UN NUEVO PAGO
# -------------------------------------------------------

@app.route("/pagos/nuevo", methods=["GET", "POST"])
def nuevo_pago():
    conexion = conectar()
    cursor = conexion.cursor()

    if request.method == "POST":
        turno_id    = request.form["turno_id"]
        monto       = request.form["monto"]
        metodo_pago = request.form["metodo_pago"]
        estado      = request.form["estado"]
        fecha_pago  = request.form["fecha_pago"] or None
        observaciones = request.form["observaciones"] or None

        cursor.execute("""
            INSERT INTO pagos (turno_id, monto, metodo_pago, estado, fecha_pago, observaciones)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (turno_id, monto, metodo_pago, estado, fecha_pago, observaciones))

        conexion.commit()
        cursor.close()
        conexion.close()

        flash("Pago registrado correctamente.", "success")
        return redirect(url_for("ver_pagos"))

    # Traemos los turnos para mostrar en el formulario
    cursor.execute("""
        SELECT t.id, t.cliente_nombre, t.mascota_nombre, s.nombre, t.fecha
        FROM turnos t
        JOIN servicios s ON t.servicio_id = s.id
        ORDER BY t.fecha DESC
    """)
    turnos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("pagos/nuevo.html", turnos=turnos)


# -------------------------------------------------------
# EDITAR UN PAGO EXISTENTE
# -------------------------------------------------------

@app.route("/pagos/editar/<int:id>", methods=["GET", "POST"])
def editar_pago(id):
    conexion = conectar()
    cursor = conexion.cursor()

    if request.method == "POST":
        estado      = request.form["estado"]
        metodo_pago = request.form["metodo_pago"]
        fecha_pago  = request.form["fecha_pago"] or None
        observaciones = request.form["observaciones"] or None

        cursor.execute("""
            UPDATE pagos
            SET estado = %s, metodo_pago = %s, fecha_pago = %s, observaciones = %s
            WHERE id = %s
        """, (estado, metodo_pago, fecha_pago, observaciones, id))

        conexion.commit()
        cursor.close()
        conexion.close()

        flash("Pago actualizado correctamente.", "success")
        return redirect(url_for("ver_pagos"))

    # Traemos el pago que queremos editar
    cursor.execute("""
        SELECT p.id, t.cliente_nombre, t.mascota_nombre, s.nombre,
               p.monto, p.metodo_pago, p.estado, p.fecha_pago, p.observaciones
        FROM pagos p
        JOIN turnos t ON p.turno_id = t.id
        JOIN servicios s ON t.servicio_id = s.id
        WHERE p.id = %s
    """, (id,))
    pago = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template("pagos/editar.html", pago=pago)


# -------------------------------------------------------
# ESTADÍSTICAS Y REPORTES
# -------------------------------------------------------

@app.route("/estadisticas")
def estadisticas():
    conexion = conectar()
    cursor = conexion.cursor()

    # 1. Cuánto se recaudó por mes
    cursor.execute("""
        SELECT TO_CHAR(fecha_pago, 'MM/YYYY') AS mes, SUM(monto) AS total
        FROM pagos
        WHERE estado = 'pagado' AND fecha_pago IS NOT NULL
        GROUP BY mes, DATE_TRUNC('month', fecha_pago)
        ORDER BY DATE_TRUNC('month', fecha_pago) DESC
    """)
    recaudacion = cursor.fetchall()

    # 2. Servicios más solicitados
    cursor.execute("""
        SELECT s.nombre, COUNT(*) AS cantidad
        FROM turnos t
        JOIN servicios s ON t.servicio_id = s.id
        GROUP BY s.nombre
        ORDER BY cantidad DESC
    """)
    servicios = cursor.fetchall()

    # 3. Turnos atendidos por cada veterinario
    cursor.execute("""
        SELECT v.nombre, COUNT(*) AS turnos
        FROM turnos t
        JOIN veterinarios v ON t.veterinario_id = v.id
        GROUP BY v.nombre
        ORDER BY turnos DESC
    """)
    veterinarios = cursor.fetchall()

    # 4. Totales por método de pago
    cursor.execute("""
        SELECT metodo_pago, COUNT(*) AS cantidad, SUM(monto) AS total
        FROM pagos
        WHERE estado = 'pagado'
        GROUP BY metodo_pago
    """)
    por_metodo = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("estadisticas/reportes.html",
                           recaudacion=recaudacion,
                           servicios=servicios,
                           veterinarios=veterinarios,
                           por_metodo=por_metodo)


# -------------------------------------------------------
# INICIAR LA APLICACIÓN
# -------------------------------------------------------

if __name__ == "__main__":
    # Crear las tablas si no existen (solo estructura, sin datos)
    conexion = conectar()
    cursor = conexion.cursor()
    with open("schema.sql", "r", encoding="utf-8") as archivo:
        cursor.execute(archivo.read())
    conexion.commit()
    cursor.close()
    conexion.close()

    app.run(debug=True)
