class Maridaje:
    def __init__(self, nombre="", descripcion=""):
        """
        Constructor de la clase Maridaje.
        :param nombre: Nombre del maridaje.
        :param descripcion: Descripción del maridaje.
        """
        self.id = None  # Será gestionado por la base de datos como clave primaria autoincremental.
        self.nombre = nombre
        self.descripcion = descripcion

    # Métodos getters y setters para el nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Métodos getters y setters para la descripción
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    # Método para verificar si el maridaje coincide con un nombre dado
    def es_maridaje(self, maridaje):
        return self.get_nombre() == maridaje

    def __str__(self):
        """
        Representación en cadena del objeto Maridaje.
        """
        return f"Maridaje(nombre={self.nombre}, descripcion={self.descripcion})"
