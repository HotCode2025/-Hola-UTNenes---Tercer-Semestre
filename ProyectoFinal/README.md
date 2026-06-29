# Sistema de Gestión de Turnos — Veterinaria

Proyecto integrador UTN · Python + PostgreSQL

---

## Equipo

| Integrante | Módulo | Archivo principal |
|---|---|---|
| Florencia | Login, registro y control de roles | `usuario.py` |
| Gabriel | CRUD de clientes | `CRUDdeClientes.py` |
| Serena | CRUD de mascotas | `crud_mascotas.py` |
| Fernando | CRUD de veterinarios | `crud_veterinarios.py`, `veterinario.py` |
| Joaquín | CRUD de servicios | `Crud_servicios.py` |
| Emmanuel | Módulo de turnos | `crud_turnos.py` |
| Matías | Pagos y estadísticas | `crud_pagos.py` |
| Otar | Base de datos, integración y documentación | `schema.sql`, `conexion.py`, `main.py` |

---

## Tecnologías

- Python 3.x
- PostgreSQL
- psycopg2

---

## Instalación y configuración

### 1. Instalar dependencias

```bash
pip install psycopg2-binary
```

### 2. Crear la base de datos

Abrir psql o pgAdmin y ejecutar:

```sql
CREATE DATABASE veterinaria;
```

### 3. Crear las tablas

Desde la carpeta del proyecto:

```bash
psql -U postgres -d veterinaria -f schema.sql
```

O desde pgAdmin: abrir `schema.sql` y ejecutarlo sobre la base `veterinaria`.

### 4. Configurar la conexión

Editar `conexion.py` con las credenciales de tu instalación de PostgreSQL:

```python
conexion = psycopg2.connect(
    host="localhost",
    database="veterinaria",
    user="postgres",
    password="admin",   # <-- cambiar por tu contraseña
    port=5432
)
```

### 5. Ejecutar el sistema

```bash
python main.py
```

---

## Estructura del proyecto

```
ProyectoFinal/
├── main.py              # Punto de entrada y menús por rol
├── conexion.py          # Conexión centralizada a PostgreSQL
├── schema.sql           # Esquema unificado de la base de datos
│
├── usuario.py           # Login y registro (Florencia)
├── CRUDdeClientes.py    # CRUD de clientes (Gabriel)
├── crud_mascotas.py     # CRUD de mascotas (Serena)
├── crud_veterinarios.py # CRUD de veterinarios (Fernando)
├── veterinario.py       # Clase Veterinario (Fernando)
├── Crud_servicios.py    # CRUD de servicios (Joaquín)
├── crud_turnos.py       # Módulo de turnos (Emmanuel)
├── crud_pagos.py        # Pagos y estadísticas (Matías — versión consola)
│
└── modulo_pagos/        # Versión Flask original de Matías (no integrada)
```

---

## Menú por roles

### Administrador — acceso completo
| Opción | Módulo |
|---|---|
| 1 | Gestión de clientes |
| 2 | Gestión de mascotas |
| 3 | Gestión de servicios |
| 4 | Gestión de turnos |
| 5 | Gestión de veterinarios |
| 6 | Gestión de pagos |

### Recepcionista
| Opción | Módulo |
|---|---|
| 1 | Gestión de clientes |
| 2 | Gestión de turnos |
| 3 | Gestión de pagos |

### Veterinario
| Opción | Módulo |
|---|---|
| 1 | Gestión de mascotas |
| 2 | Gestión de turnos |

---

## Cómo se conectan los módulos

Todos los módulos importan la misma función `conectar()` de `conexion.py`.
No hay conexiones duplicadas ni credenciales hardcodeadas en cada archivo.

```
main.py
  └─ login() ──────────────────────────► conexion.py ──► PostgreSQL
  └─ menu_clientes() ──► CRUDdeClientes ► conexion.py
  └─ menu_mascotas() ──► crud_mascotas  ► conexion.py
  └─ menu_servicios() ─► Crud_servicios ► conexion.py
  └─ menu_turnos() ────► crud_turnos    ► conexion.py
  └─ menu_veterinarios() crud_veterinarios conexion.py
  └─ menu_pagos() ─────► crud_pagos     ► conexion.py
```

### Relaciones entre tablas

```
roles ◄──────── usuarios
                    │
clientes ◄──────── turnos ──────► mascotas
                    │
veterinarios ◄─────┘
                    │
                   pagos
```

---

## Cambios de integración

### Módulo de Pagos (Matías) — migración a consola

El módulo original fue desarrollado con **Flask + HTML templates** (`modulo_pagos/`).
Se creó `crud_pagos.py` como reemplazo por consola para unificar la experiencia con el resto del sistema.

Cambios realizados:
- Eliminada la dependencia de Flask
- Las queries de pagos y estadísticas se adaptaron al esquema real de tablas (`id_turno`, `id_cliente`, `id_mascota`, `id_veterinario`)
- La versión Flask original se conserva en `modulo_pagos/` y puede ejecutarse de forma independiente (ver sección al final)

### Módulo de Veterinarios (Fernando) — correcciones de bugs

`crud_veterinarios.py` tenía dos errores que impedían su ejecución:

| Bug | Línea original | Corrección |
|---|---|---|
| Función de conexión inexistente | `from conexion import obtener_conexion` | `from conexion import conectar` |
| Atributo incorrecto en `modificar_veterinario` | `veterinario.id` | `veterinario.id_veterinario` |

Además se agregó la función `menu_veterinarios()` que faltaba para poder integrarlo al menú principal.

### `main.py` — nuevas integraciones

- Agregados imports de `menu_veterinarios` y `menu_pagos`
- Opción 5 (Veterinarios) y opción 6 (Pagos) en el menú de Administrador
- Opción 3 (Pagos) en el menú de Recepcionista

### `schema.sql` — esquema unificado

Se creó un único archivo `schema.sql` en la raíz que define todas las tablas del sistema en el orden correcto (respetando las claves foráneas) e inserta los roles por defecto.

El archivo `modulo_pagos/schema.sql` define tablas propias simplificadas y **no es compatible** con el sistema integrado; pertenece a la versión Flask independiente.

---

## Módulo de pagos Flask (versión original de Matías)

El subdirectorio `modulo_pagos/` contiene la versión web original. Se puede ejecutar de forma independiente:

```bash
cd modulo_pagos
pip install flask psycopg2-binary
python app.py
```

Luego abrir `http://localhost:5000` en el navegador.

> **Nota:** usa su propio esquema simplificado (`modulo_pagos/schema.sql`) con tablas distintas a las del sistema integrado. La contraseña en `modulo_pagos/config.py` y `modulo_pagos/db.py` es `postgres`; asegurarse de que coincida con la instalación local.
