from datetime import datetime, timedelta
from typing import List

from models import Bodega, Enofilo, Maridaje, Siguiendo, TipoUva, Usuario, Varietal, Vino
from views import PantallaNotificacion

class GestorImportarVinoDeBodega:
    def __init__(self, bodegas: List['Bodega'], listado_vino: List['Vino'], maridajes: List['Maridaje'], tipo_uvas: List['TipoUva']): # type: ignore
        self.listado_bodega = bodegas
        self.listado_vino = listado_vino
        self.tipo_uvas = tipo_uvas
        self.maridajes = maridajes
        self.bodega_seleccionada = None
        self.vinos_actualizados = []
        self.fecha_actual = None
        self.vinos = []
        self.enofilos = []
        self.enofilo_notifiaciones = []

    def set_pantalla(self, pantalla_importar_vino):
        self.pantalla_importar_vino = pantalla_importar_vino

    def op_importar_actualizacion_vino_bodega(self, pantalla_importar_vino):
        self.set_pantalla(pantalla_importar_vino)
        bodegas_con_actualizaciones = self.buscar_bodegas_actualizar()
        if len(bodegas_con_actualizaciones) == 0:
            pantalla_importar_vino.no_existen_bodegas_con_actualizaciones()
        else:
            pantalla_importar_vino.mostrar_bodega_para_actualizar(bodegas_con_actualizaciones)

    def buscar_bodegas_actualizar(self) -> List[str]:
        bodega_con_actualizaciones = []
        siguiendo = [Siguiendo(self.listado_bodega[1], datetime.now() - timedelta(days=3)),
                     Siguiendo(self.listado_bodega[0], datetime.now() - timedelta(days=3))]
        siguiendo1 = [Siguiendo(self.listado_bodega[1], datetime.now() - timedelta(days=3)),
                      Siguiendo(self.listado_bodega[0], datetime.now() - timedelta(days=3))]

        usuario = Usuario("Jesus", "Merequetengue", True)
        usuario1 = Usuario("Emi", "contra123", True)

        self.enofilos = [Enofilo("Bordiga", "Bordiga", usuario, siguiendo),
                         Enofilo("Nico", "Ojea", usuario1, siguiendo)]

        for bodega in self.listado_bodega:
            if bodega.tiene_actualizaciones_disponibles():
                bodega_con_actualizaciones.append(bodega.get_nombre())

        return bodega_con_actualizaciones

    def tomar_bodega_seleccionada(self, nombre_bodega: str):
        for bodega in self.listado_bodega:
            if bodega.get_nombre() == nombre_bodega:
                self.bodega_seleccionada = bodega
        self.obtener_actualizacion_vinos_bodega()

    def obtener_actualizacion_vinos_bodega(self):
        self.obtener_actualizacion_vinos()

    def obtener_actualizacion_vinos(self):
        for vino in self.listado_vino:
            if vino.get_bodega().get_nombre() == self.bodega_seleccionada.get_nombre():
                print(vino)

        if self.bodega_seleccionada.get_nombre() == "Bodega Cordoba":
            self.vinos = [
                ["2020", "Vino 1 Bodega Cordoba", "1", "250", "asado queso pimiento", "malbec 50 rosada 50", "2"],
                ["2030", "Vino Esteban Quito", "3", "550", "picada morcilla lomito", "malbec 50 rosada 50", "3"],
                ["2030", "Vino Quito", "3", "550", "morcilla lomito", "malbec 50 rosada 50", "3"]
            ]
        elif self.bodega_seleccionada.get_nombre() == "Bodega BSAS":
            self.vinos = [
                ["2020", "Vino 1 Bodega BSAS", "4", "250", "asado queso pimiento", "malbec 50 rosada 50", "2"],
                ["2020", "Vino 2 Bodega BSAS", "3", "550", "asado queso pimiento", "malbec 50 rosada 50", "3"],
                ["2020", "Vino Findo", "2", "250", "picada morcilla lomito", "malbec 50 rosada 50", "2"]
            ]
        elif self.bodega_seleccionada.get_nombre() == "Bodega SanJuan":
            self.vinos = [
                ["2020", "Vino 1 Bodega SanJuan", "2", "250", "asado queso pimiento", "malbec 50 rosada 50", "2"],
                ["2020", "Vino 2 Bodega SanJuan", "5", "550", "asado queso pimiento", "malbec 50 rosada 50", "3"]
            ]
        if len(self.vinos) == 0:
            self.pantalla_importar_vino.api_no_disponible()

        self.get_fecha_actual()

    def get_fecha_actual(self):
        self.fecha_actual = datetime.now()
        self.actualizar_datos_de_vino_bodega()

    def actualizar_datos_de_vino_bodega(self):
        self.vinos_actualizados = []
        for vino in self.vinos:
            self.vinos_actualizados.append(self.bodega_seleccionada.actualizar_datos_vinos_existente(self.listado_vino, vino))
        self.actualizar_fecha_actualizacion_de_vino_bodega()
        print(len(self.listado_vino))

        for i in range(len(self.vinos_actualizados)):
            if self.vinos_actualizados[i] is None:
                self.buscar_maridaje(i)

        self.pantalla_importar_vino.mostrar_resumen_vinos_importados(self.vinos_actualizados, self.bodega_seleccionada)

    def buscar_maridaje(self, posicion: int):
        maridaje_vino = self.vinos[posicion][4].split(' ')
        maridajes_actualizar = []

        for maridaje_str in maridaje_vino:
            for maridaje in self.maridajes:
                if maridaje.es_maridaje(maridaje_str):
                    maridajes_actualizar.append(maridaje)

        print(maridajes_actualizar[0])
        self.buscar_tipo_uva(posicion, maridajes_actualizar)

    def buscar_tipo_uva(self, posicion: int, maridajes: List['Maridaje']): # type: ignore
        tipo_uva_actu = self.vinos[posicion][5].split(' ')
        porcentaje_vino = self.vinos[posicion][6].split(' ')
        tipo_uva_actualizar = []
        porcentaje_actualizar = []

        for i in range(len(tipo_uva_actu)):
            for tipo_uva in self.tipo_uvas:
                if tipo_uva.es_tipo_uva(tipo_uva_actu[i]):
                    tipo_uva_actualizar.append(tipo_uva)
                    porcentaje_actualizar.append(porcentaje_vino[i])

        self.crear_vinos(maridajes, tipo_uva_actualizar, posicion, porcentaje_actualizar)

    def crear_vinos(self, maridajes_actualizar: List['Maridaje'], tipo_uva_actualizar: List['TipoUva'], posicion: int, porcentaje_actualizar: List[str]): # type: ignore
        varietales = Varietal()
        contador = len(self.listado_vino)
        self.listado_vino.append(Vino(self.bodega_seleccionada, int(self.vinos[posicion][0]), self.vinos[posicion][1], self.vinos[posicion][2], float(self.vinos[posicion][3]), maridajes_actualizar, varietales, int(self.vinos[posicion][6])))
        vino = [self.vinos[posicion][0], self.vinos[posicion][1], self.vinos[posicion][2], self.vinos[posicion][3], "nuevo"]
        self.vinos_actualizados[posicion] = vino

    def actualizar_fecha_actualizacion_de_vino_bodega(self):
        self.bodega_seleccionada.set_fecha_de_actualizacion_vino_bodega(self.fecha_actual)

    def enviar_notificaciones_novedad_a_suscriptores(self):
        self.enofilo_notifiaciones = []
        for enofilo in self.enofilos:
            self.enofilo_notifiaciones.append(enofilo.seguir_bodega(self.bodega_seleccionada))

        for es_enofilo in self.enofilo_notifiaciones:
            self.notificacion = PantallaNotificacion(self.enofilo_notifiaciones)
            self.notificacion.show()
            self.notificacion.notificar_novedad_a_suscriptores(es_enofilo)

    def fin_cu(self):
        exit()

