from conexion import conectar


def registrar_usuario():
    print("\n===== REGISTRAR USUARIO =====")

    nombre     = input("Nombre: ").strip()
    apellido   = input("Apellido: ").strip()
    email      = input("Email: ").strip()
    usuario    = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    print("\nSeleccione un rol:")
    print("1 - Administrador")
    print("2 - Recepcionista")
    print("3 - Veterinario")
    try:
        id_rol = int(input("Rol: ").strip())
        if id_rol not in (1, 2, 3):
            print("Rol inválido. Debe ser 1, 2 o 3.")
            return
    except ValueError:
        print("Ingresá un número válido.")
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO usuarios (nombre, apellido, email, usuario, contrasena, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nombre, apellido, email, usuario, contrasena, id_rol))
        conexion.commit()
        cursor.close()
        conexion.close()

        print("\nUsuario registrado correctamente.")

    except Exception as e:
        if "unique" in str(e).lower() or "duplicate" in str(e).lower():
            print(f"\nError: el nombre de usuario '{usuario}' ya existe. Elegí otro.")
        else:
            print(f"\nError al registrar usuario: {e}")
