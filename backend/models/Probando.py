from datetime import datetime
from typing import List

class Bodega:
    def __init__(self, nombre: str, id_bodega: int, descripcion: str, historia: str, coordenadas: List[float], fecha_fundacion: datetime):
        self.nombre = nombre
        self.id_bodega = id_bodega
        self.descripcion = descripcion
        self.historia = historia
        self.coordenadas = coordenadas
        self.fecha_fundacion = fecha_fundacion

    def get_nombre(self):
        return self.nombre


class TipoUva:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion


class Varietal:
    def __init__(self, nombre: str, cantidad: float, tipo_uva: TipoUva):
        self.nombre = nombre
        self.cantidad = cantidad
        self.tipo_uva = tipo_uva


class Maridaje:
    def __init__(self, tipo: str, descripcion: str):
        self.tipo = tipo
        self.descripcion = descripcion


class Vino:
    def __init__(self, bodega: Bodega, anio: int, nombre: str, nota_cata: str, stock: int, maridajes: List[Maridaje], varietales: List[Varietal], cantidad: int):
        self.bodega = bodega
        self.anio = anio
        self.nombre = nombre
        self.nota_cata = nota_cata
        self.stock = stock
        self.maridajes = maridajes
        self.varietales = varietales
        self.cantidad = cantidad


class Probando:
    @staticmethod
    def cargar_datos_iniciales():
        bodegas = []

        bodegas.append(Bodega("Bodega Cordoba", 1, "Descripcion Bodega Cordoba", "Historia Fernando", [40.7128, -74.0060], datetime.now().replace(month=datetime.now().month-1)))
        bodegas.append(Bodega("Bodega BSAS", 2, "Descripcion Bodega BSAS", "Historia Fernando", [40.7128, -74.0060], datetime.now().replace(month=datetime.now().month-2)))
        bodegas.append(Bodega("Bodega Mendoza", 4, "Descripcion Bodega Mendoza", "Historia Fernando", [40.7128, -74.0060], datetime.now().replace(month=datetime.now().month-3)))
        bodegas.append(Bodega("Bodega SanJuan", 1, "Descripcion Bodega SanJuan", "Historia Fernando", [40.7128, -74.0060], datetime.now().replace(month=datetime.now().month-2)))

        return bodegas

    @staticmethod
    def crear_lista_vinos():
        vinos = []

        maridajes_vino1 = [Probando.crear_lista_maridaje()[0], Probando.crear_lista_maridaje()[3], Probando.crear_lista_maridaje()[2]]
        maridajes_vino3 = [Probando.crear_lista_maridaje()[2], Probando.crear_lista_maridaje()[3]]
        maridajes_vino2 = [Probando.crear_lista_maridaje()[1], Probando.crear_lista_maridaje()[0], Probando.crear_lista_maridaje()[4]]

        varietales1 = [Probando.crear_lista_varietal()[2], Probando.crear_lista_varietal()[7]]
        varietales2 = [Probando.crear_lista_varietal()[1], Probando.crear_lista_varietal()[6]]
        varietales3 = [Probando.crear_lista_varietal()[0], Probando.crear_lista_varietal()[5]]

        for bodega in Probando.cargar_datos_iniciales():
            vinos.append(Vino(bodega, 2018, f"Vino 1 {bodega.get_nombre()}", "Nota De Cata", 300, maridajes_vino2, varietales1, 700))
            vinos.append(Vino(bodega, 2018, f"Vino 2 {bodega.get_nombre()}", "Nota De Cata", 300, maridajes_vino2, varietales1, 700))
            vinos.append(Vino(bodega, 2018, f"Vino 3 {bodega.get_nombre()}", "Nota De Cata", 300, maridajes_vino3, varietales2, 700))
            vinos.append(Vino(bodega, 2018, f"Vino 4 {bodega.get_nombre()}", "Nota De Cata", 300, maridajes_vino1, varietales3, 700))

        return vinos

    @staticmethod
    def crear_lista_tipo_uva():
        tipos_uva = []

        tipos_uva.append(TipoUva("Cabernet Sauvignon", "Uva con alta concentración de taninos"))
        tipos_uva.append(TipoUva("Merlot", "Uva con cuerpo medio y sabores afrutados"))
        tipos_uva.append(TipoUva("Malbec", "Uva con cuerpo completo y sabores especiados"))

        return tipos_uva

    @staticmethod
    def crear_lista_varietal():
        varietales = []

        varietales.append(Varietal("Varietal 1", 50.0, Probando.crear_lista_tipo_uva()[0]))
        varietales.append(Varietal("Varietal 2", 30.0, Probando.crear_lista_tipo_uva()[1]))
        varietales.append(Varietal("Varietal 3", 20.0, Probando.crear_lista_tipo_uva()[2]))
        varietales.append(Varietal("Varietal 4", 70.0, Probando.crear_lista_tipo_uva()[0]))
        varietales.append(Varietal("Varietal 5", 60.0, Probando.crear_lista_tipo_uva()[1]))
        varietales.append(Varietal("Varietal 1", 50.0, Probando.crear_lista_tipo_uva()[1]))
        varietales.append(Varietal("Varietal 2", 70.0, Probando.crear_lista_tipo_uva()[2]))
        varietales.append(Varietal("Varietal 3", 80.0, Probando.crear_lista_tipo_uva()[1]))
        varietales.append(Varietal("Varietal 4", 30.0, Probando.crear_lista_tipo_uva()[2]))
        varietales.append(Varietal("Varietal 5", 30.0, Probando.crear_lista_tipo_uva()[2]))

        return varietales

    @staticmethod
    def crear_lista_maridaje():
        maridajes = []

        maridajes.append(Maridaje("asado", "Unas buenas carnes asadas"))
        maridajes.append(Maridaje("picada", "embutidos"))
        maridajes.append(Maridaje("morcilla", "morcilla fria"))
        maridajes.append(Maridaje("empanada", "frita no arabe"))
        maridajes.append(Maridaje("Maridaje 5", "Postres de chocolate y frutos rojos"))

        return maridajes
