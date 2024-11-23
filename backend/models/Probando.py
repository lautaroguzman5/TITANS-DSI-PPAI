from datetime import datetime

from backend.models import Bodega, Maridaje, TipoUva, Varietal, Vino

class Probando:
    def __init__(self):
        """
        Constructor de la clase Probando. Carga los datos iniciales al instanciar la clase.
        """
        self.context = None  # Reemplaza con tu ORM si es necesario
        self.bodegas = self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """
        Carga datos iniciales de bodegas, varietales, y tipos de uva.
        Retorna una lista de bodegas.
        """
        # Simulación de contexto (reemplazar con ORM en proyectos reales)
        tipos_uva = self.crear_lista_tipo_uva()
        varietal = Varietal("descripcion", 12, tipos_uva[2])

        # Crear la lista de bodegas
        bodegas = [
            Bodega("Bodega Cordoba", 1, "Descripcion Bodega Cordoba", "Historia Fernando",
                   [40.7128, -74.0060], datetime.now().replace(microsecond=0)),
            Bodega("Bodega BSAS", 2, "Descripcion Bodega BSAS", "Historia Fernando",
                   [40.7128, -74.0060], datetime.now().replace(microsecond=0)),
            Bodega("Bodega Mendoza", 4, "Descripcion Bodega Mendoza", "Historia Fernando",
                   [40.7128, -74.0060], datetime.now().replace(microsecond=0)),
            Bodega("Bodega SanJuan", 1, "Descripcion Bodega SanJuan", "Historia Fernando",
                   [40.7128, -74.0060], datetime.now().replace(microsecond=0))
        ]

        return bodegas

    def crear_lista_vinos(self):
        """
        Crea una lista de vinos para cada bodega inicial.
        Retorna una lista de vinos.
        """
        vinos = []
        maridajes = self.crear_lista_maridaje()
        tipos_uva = self.crear_lista_tipo_uva()

        # Crear varietales
        varietal1 = Varietal("Varietal 1", 50.0, tipos_uva[0])
        varietal2 = Varietal("Varietal 2", 30.0, tipos_uva[1])
        varietal3 = Varietal("Varietal 3", 20.0, tipos_uva[2])

        for bodega in self.bodegas:
            vinos.append(Vino(bodega, 2018, f"Vino 1 {bodega.nombre}", "Nota De Cata", 300,
                              [maridajes[0], maridajes[1], maridajes[2]], varietal1, 700))
            vinos.append(Vino(bodega, 2018, f"Vino 2 {bodega.nombre}", "Nota De Cata", 300,
                              [maridajes[1], maridajes[2], maridajes[3]], varietal2, 700))
            vinos.append(Vino(bodega, 2018, f"Vino 3 {bodega.nombre}", "Nota De Cata", 300,
                              [maridajes[2], maridajes[3]], varietal3, 700))

        return vinos

    def crear_lista_tipo_uva(self):
        """
        Crea una lista de tipos de uva.
        Retorna una lista de objetos TipoUva.
        """
        return [
            TipoUva("Cabernet Sauvignon", "Uva con alta concentración de taninos"),
            TipoUva("Merlot", "Uva con cuerpo medio y sabores afrutados"),
            TipoUva("Malbec", "Uva con cuerpo completo y sabores especiados")
        ]

    def crear_lista_maridaje(self):
        """
        Crea una lista de maridajes.
        Retorna una lista de objetos Maridaje.
        """
        return [
            Maridaje("Asado", "Unas buenas carnes asadas"),
            Maridaje("Picada", "Embutidos"),
            Maridaje("Morcilla", "Morcilla fría"),
            Maridaje("Empanada", "Frita no árabe"),
            Maridaje("Postres", "Postres de chocolate y frutos rojos")
        ]
