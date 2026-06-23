```mermaid
classDiagram
    class conexion {
        -DATABASE: String
        -USERNAME: String
        -PASSWORD: String
        -DB_PORT: String
        -HOST: String
        -conexion: connection
        -cursor: Cursor
        +obtenerConexion(cls): Connection
        +obtenerCursor(cls): Cursor
        +cerrar(cls)
    }

    class Persona {
        -id_persona: int
        -nombre: String
        -apellido: String
        -email: String
        +_str_(): String
        +metodo Get/Set de cada atributo()
    }

    class PersonaDao {
        -SELECCIONAR: String
        -INSERTAR: String
        -ACTUALIZAR: String
        -ELIMINAR: String
        +seleccionar(cls)
        +insertar(cls, persona)
        +actualizar(cls, persona)
        +eliminar(cls, persona)
    }

    PersonaDao o-- conexion : Usa
    PersonaDao o-- Persona : Administra