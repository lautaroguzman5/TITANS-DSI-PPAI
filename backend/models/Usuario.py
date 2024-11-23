class Usuario:
    def __init__(self, nombre, contraseña, premium=False):
        """
        Constructor de la clase Usuario.
        :param nombre: Nombre del usuario.
        :param contraseña: Contraseña del usuario.
        :param premium: Indica si el usuario es premium (por defecto, False).
        """
        self.id = None  # Este atributo se asignará automáticamente si se usa con una base de datos.
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium

    # Métodos para obtener y establecer el nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Métodos para obtener y establecer la contraseña
    def get_contraseña(self):
        return self.contraseña

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña

    # Método para establecer si el usuario es premium
    def es_premium(self, es_premium):
        self.premium = es_premium

    def __str__(self):
        """
        Representación en cadena del objeto Usuario.
        """
        tipo_usuario = "Premium" if self.premium else "Estándar"
        return f"Usuario(nombre={self.nombre}, tipo={tipo_usuario})"
