from datetime import datetime
from typing import List

from models.Bodega import Bodega
from models.Maridaje import Maridaje
from models.TipoUva import TipoUva
from models.Varietal import Varietal
from models.Vino import Vino

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
