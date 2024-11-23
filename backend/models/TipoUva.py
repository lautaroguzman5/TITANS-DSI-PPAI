class TipoUva:
    def __init__(self, nombre="", descripcion=""):
        """
        Constructor de la clase TipoUva.
        :param nombre: Nombre del tipo de uva.
        :param descripcion: Descripción del tipo de uva.
        """
        self.id = None  # Será manejada por la base de datos como autoincremental.
        self.nombre = nombre
        self.descripcion = descripcion

    # Métodos getters y setters para el nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    # Métodos getters y setters para la descripción
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    # Método para verificar si el tipo de uva coincide con un nombre dado
    def es_tipo_uva(self, tipo_uva):
        return self.get_nombre() == tipo_uva

    def __str__(self):
        """
        Representación en cadena del objeto TipoUva.
        """
        return f"TipoUva(nombre={self.nombre}, descripcion={self.descripcion})"
