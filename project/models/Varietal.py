class Varietal:
    def __init__(self, descripcion="", porcentaje=0.0, tipo_uva=None):
        """
        Constructor de la clase Varietal.
        :param descripcion: Descripción del varietal.
        :param porcentaje: Porcentaje del varietal.
        :param tipo_uva: Objeto TipoUva asociado al varietal.
        """
        self.id = None  # Se manejará como autoincremental desde la base de datos
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.tipo_uva = tipo_uva
        self.tipo_uva_id = tipo_uva.id if tipo_uva else None

    # Métodos getters y setters para la descripción
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    # Métodos getters y setters para el porcentaje
    def set_porcentaje(self, porcentaje):
        self.porcentaje = porcentaje

    def get_porcentaje(self):
        return self.porcentaje

    # Métodos getters y setters para el tipo de uva
    def set_tipo_uva(self, tipo_uva):
        self.tipo_uva = tipo_uva
        self.tipo_uva_id = tipo_uva.id if tipo_uva else None

    def get_tipo_uva(self):
        return self.tipo_uva

    def __str__(self):
        """
        Representación en cadena del objeto Varietal.
        """
        return f"Varietal(descripcion={self.descripcion}, porcentaje={self.porcentaje}, tipo_uva_id={self.tipo_uva_id})"
