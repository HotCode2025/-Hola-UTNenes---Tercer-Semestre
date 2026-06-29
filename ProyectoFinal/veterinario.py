class Veterinario:

    def __init__(self, id_veterinario, nombre, matricula, telefono, email):

        self.id_veterinario = id_veterinario
        self.nombre = nombre
        self.matricula = matricula
        self.telefono = telefono
        self.email = email

    def __str__(self):
            return (f"""
    ID: {self.id_veterinario}
    Nombre: {self.nombre}
    Matrícula: {self.matricula}
    Teléfono: {self.telefono}
    Email: {self.email}
    """)

