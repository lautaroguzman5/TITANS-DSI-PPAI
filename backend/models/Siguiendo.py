from datetime import datetime

class Siguiendo:
    def __init__(self, bodega, fecha_inicio):
        """
        Constructor de la clase Siguiendo.
        :param bodega: Objeto de la clase Bodega que representa la bodega seguida.
        :param fecha_inicio: Fecha de inicio del seguimiento.
        """
        self.bodega = bodega
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = None  # Fecha de fin no se inicializa por defecto.

    # Métodos para establecer y obtener la bodega
    def set_bodega(self, bodega):
        self.bodega = bodega

    def get_bodega(self):
        return self.bodega

    # Métodos para establecer y obtener la fecha de inicio
    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def get_fecha_inicio(self):
        return self.fecha_inicio

    # Métodos para establecer y obtener la fecha de fin
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def get_fecha_fin(self):
        return self.fecha_fin

    # Método para verificar si el seguimiento pertenece a una bodega específica
    def sos_de_bodega(self, bodega_seleccionada):
        return self.get_bodega().get_nombre() == bodega_seleccionada.get_nombre()

    def __str__(self):
        """
        Representación en cadena del objeto Siguiendo.
        """
        return (
            f"Bodega: {self.bodega.get_nombre()}, "
            f"Inicio: {self.fecha_inicio}, "
            f"Fin: {self.fecha_fin or 'Seguimiento activo'}"
        )
