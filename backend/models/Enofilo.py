from backend.models import Siguiendo


class Enofilo:
    def __init__(self, apellido, nombre, usuario, siguiendo_bodegas=None):
        """
        Constructor de la clase Enofilo.
        :param apellido: Apellido del enófilo.
        :param nombre: Nombre del enófilo.
        :param usuario: Instancia de la clase Usuario asociada al enófilo.
        :param siguiendo_bodegas: Lista de bodegas que el enófilo está siguiendo.
        """
        self.apellido = apellido
        self.nombre = nombre
        self.usuario = usuario
        self.siguiendo_bodegas = siguiendo_bodegas if siguiendo_bodegas is not None else []
        self.vinos = []  # Lista de vinos asociada al enófilo.

    # Métodos getters y setters para Apellido
    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    # Métodos getters y setters para Nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Métodos getters y setters para Usuario
    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    # Métodos getters y setters para SiguiendoBodegas
    def get_siguiendo_bodegas(self):
        return self.siguiendo_bodegas

    def set_siguiendo_bodegas(self, siguiendo_bodegas):
        self.siguiendo_bodegas = siguiendo_bodegas

    # Método para agregar una nueva bodega a la lista de bodegas seguidas
    def seguir_bodega(self, bodega_seleccionada):
        """
        Agrega una bodega a la lista de bodegas seguidas si no está ya presente.
        :param bodega_seleccionada: Instancia de la clase Bodega a seguir.
        :return: El nombre del usuario si ya sigue la bodega, None si la agrega.
        """
        for siguiendo in self.siguiendo_bodegas:
            if siguiendo.sos_de_bodega(bodega_seleccionada):
                return self.usuario.get_nombre()

        # Si no está siguiendo la bodega, agregarla a la lista
        nuevo_siguiendo = Siguiendo(bodega=bodega_seleccionada)
        self.siguiendo_bodegas.append(nuevo_siguiendo)
        return None

    def __str__(self):
        """
        Representación en cadena del objeto Enofilo.
        """
        return f"Enofilo(apellido={self.apellido}, nombre={self.nombre}, usuario={self.usuario})"
