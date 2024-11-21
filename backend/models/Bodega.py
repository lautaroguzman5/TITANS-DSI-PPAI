from datetime import datetime
from typing import List

class Bodega:
    # Constructor con atributos inicializados
    def __init__(self, nombre: str = None, periodo_actualizacion: int = 0, descripcion: str = None,
                 historia: str = None, coordenadas: List[float] = None, ultima_actualizacion: datetime = None):
        self.id = None  # En Python, el ID debe ser manejado manualmente o por la base de datos.
        self.nombre = nombre
        self.historia = historia
        self.descripcion = descripcion
        self.coordenadas_ubicacion = coordenadas if coordenadas else []
        self.periodo_actualizacion = periodo_actualizacion
        self.ultima_actualizacion = ultima_actualizacion if ultima_actualizacion else datetime.now()
        self.vinos = []  # Lista vacía inicial para los vinos

    # Métodos getter y setter
    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion

    def get_descripcion(self) -> str:
        return self.descripcion

    def set_historia(self, historia: str):
        self.historia = historia

    def get_historia(self) -> str:
        return self.historia

    def set_periodo_actualizacion(self, periodo_actualizacion: int):
        self.periodo_actualizacion = periodo_actualizacion

    def get_periodo_actualizacion(self) -> int:
        return self.periodo_actualizacion

    def set_ultima_actualizacion(self, ultima_actualizacion: datetime):
        self.ultima_actualizacion = ultima_actualizacion

    def get_ultima_actualizacion(self) -> datetime:
        return self.ultima_actualizacion

    def set_coordenadas(self, coordenadas: List[float]):
        self.coordenadas_ubicacion = coordenadas

    def get_coordenadas(self) -> List[float]:
        return self.coordenadas_ubicacion

    def set_vinos(self, vinos: List):
        self.vinos = vinos

    def get_vinos(self) -> List:
        return self.vinos

    # Métodos adicionales
    def tiene_actualizaciones_disponibles(self) -> bool:
        # Calcula si las actualizaciones están disponibles
        cantidad_dias = (datetime.now() - self.ultima_actualizacion).days
        return cantidad_dias >= (self.periodo_actualizacion * 30)

    def actualizar_datos_vinos_existente(self, vinos_existente: List, vino_act: List[str]) -> List[str]:
        vino_lista = []
        for vino in vinos_existente:
            if vino.es_vino_para_actualizar(vino_act[1]):
                # Actualizar propiedades del vino
                vino.set_imagen_etiqueta(int(vino_act[6]))
                vino.set_anade(int(vino_act[0]))
                vino.set_nota_cata(vino_act[2])
                vino.set_precio_ars(float(vino_act[3]))

                # Añadir detalles a la lista
                vino_lista.extend([
                    str(vino.get_anade()),
                    vino.get_nombre(),
                    vino.get_nota_cata(),
                    str(vino.get_precio_ars()),
                    "actualizado"
                ])
                return vino_lista
        return None

    def set_fecha_de_actualizacion_vino_bodega(self, fecha_de_actualizacion: datetime):
        self.ultima_actualizacion = fecha_de_actualizacion
