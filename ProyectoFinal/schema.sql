-- ============================================================
-- SISTEMA DE GESTIÓN DE TURNOS — VETERINARIA
-- Esquema unificado de base de datos
-- ============================================================

-- Roles de usuario
CREATE TABLE IF NOT EXISTS roles (
    id_rol SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Datos iniciales de roles (Florencia — Módulo 1)
INSERT INTO roles (nombre) VALUES
    ('Administrador'),
    ('Recepcionista'),
    ('Veterinario')
ON CONFLICT (nombre) DO NOTHING;

-- Usuarios del sistema (Florencia — Módulo 1)
CREATE TABLE IF NOT EXISTS usuarios (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    email       VARCHAR(150),
    usuario     VARCHAR(50)  NOT NULL UNIQUE,
    contrasena  VARCHAR(255) NOT NULL,
    id_rol      INTEGER REFERENCES roles(id_rol),
    activo      BOOLEAN DEFAULT TRUE
);

-- Clientes / dueños de mascotas (Gabriel — Módulo 2)
CREATE TABLE IF NOT EXISTS clientes (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    apellido        VARCHAR(100) NOT NULL,
    dni             VARCHAR(20)  NOT NULL UNIQUE,
    email           VARCHAR(150),
    telefono        VARCHAR(30),
    direccion       TEXT,
    fecha_registro  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Mascotas (Serena — Módulo 3)
CREATE TABLE IF NOT EXISTS mascotas (
    id              SERIAL PRIMARY KEY,
    nombre_mascota  VARCHAR(100) NOT NULL,
    raza_mascota    VARCHAR(100),
    ingreso         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    salida          TIMESTAMP
);

-- Veterinarios (Fernando — Módulo 4)
CREATE TABLE IF NOT EXISTS veterinarios (
    id_veterinario  SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    matricula       VARCHAR(50)  NOT NULL UNIQUE,
    telefono        VARCHAR(30),
    email           VARCHAR(150)
);

-- Servicios ofrecidos (Joaquín — Módulo 5)
CREATE TABLE IF NOT EXISTS servicios (
    id_servicio         SERIAL PRIMARY KEY,
    nombre              VARCHAR(100) NOT NULL,
    descripcion         TEXT,
    precio              DECIMAL(10, 2) NOT NULL,
    duracion_minutos    INTEGER
);

-- Turnos (Emmanuel — Módulo 6)
CREATE TABLE IF NOT EXISTS turnos (
    id_turno        SERIAL PRIMARY KEY,
    id_cliente      INTEGER REFERENCES clientes(id),
    id_mascota      INTEGER REFERENCES mascotas(id),
    id_veterinario  INTEGER REFERENCES veterinarios(id_veterinario),
    fecha           DATE NOT NULL,
    hora            TIME NOT NULL,
    estado          VARCHAR(20) DEFAULT 'Pendiente'
        CHECK (estado IN ('Pendiente', 'Confirmado', 'Cancelado', 'Finalizado'))
);

-- Pagos (Matías — Módulo 7)
CREATE TABLE IF NOT EXISTS pagos (
    id_pago         SERIAL PRIMARY KEY,
    id_turno        INTEGER REFERENCES turnos(id_turno) ON DELETE CASCADE,
    monto           DECIMAL(10, 2) NOT NULL,
    metodo_pago     VARCHAR(20) NOT NULL
        CHECK (metodo_pago IN ('efectivo', 'tarjeta', 'transferencia')),
    estado          VARCHAR(20) NOT NULL DEFAULT 'pendiente'
        CHECK (estado IN ('pagado', 'pendiente')),
    fecha_pago      DATE,
    observaciones   TEXT,
    creado_en       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
