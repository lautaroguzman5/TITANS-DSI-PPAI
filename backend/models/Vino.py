from typing import List, Optional
from datetime import datetime

from models import Varietal


class Vino:
    def __init__(self, 
                 bodega=None, 
                 aniade: int = 0, 
                 nombre: str = "", 
                 nota_de_cata: str = "", 
                 precio_ars: float = 0.0, 
                 maridajes: Optional[List] = None, 
                 varietal=None, 
                 imagen_etiqueta: int = 0):
        self.id = None  # Similar a [Key] en C#, lo manejarías con un ORM si usas uno como SQLAlchemy.
        self.aniada = aniade
        self.nombre = nombre
        self.nota_de_cata = nota_de_cata
        self.precio_ars = precio_ars
        self.imagen_etiqueta = imagen_etiqueta
        self.maridajes = maridajes if maridajes else []
        self.varietal = varietal
        self.varietal_id = varietal.id if varietal else 0
        self.bodega = bodega
        self.bodega_id = bodega.id if bodega else 0

    # Métodos setter y getter
    def set_aniade(self, aniade: int):
        self.aniada = aniade

    def get_aniade(self) -> int:
        return self.aniada

    def set_bodega(self, bodega):
        self.bodega = bodega

    def get_bodega(self):
        return self.bodega

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre

    def set_nota_cata(self, nota_de_cata: str):
        self.nota_de_cata = nota_de_cata

    def get_nota_cata(self) -> str:
        return self.nota_de_cata

    def set_precio_ars(self, precio_ars: float):
        self.precio_ars = precio_ars

    def get_precio_ars(self) -> float:
        return self.precio_ars

    def set_imagen_etiqueta(self, imagen_etiqueta: int):
        self.imagen_etiqueta = imagen_etiqueta

    def get_imagen_etiqueta(self) -> int:
        return self.imagen_etiqueta

    def set_maridaje(self, maridajes: List):
        self.maridajes = maridajes

    def get_maridaje(self) -> List:
        return self.maridajes

    def set_varietal(self, varietal):
        self.varietal = varietal

    def get_varietal(self):
        return self.varietal

    # Método para verificar si el vino necesita ser actualizado
    def es_vino_para_actualizar(self, nombre_vino: str) -> bool:
        return nombre_vino == self.get_nombre()

    # Método para crear los varietales del vino
    def crear_varietal(self, tipo_uva_actualizar, porcentaje_actualizar: float):
        # La clase `Varietal` necesita estar definida o importada.
        aux = Varietal("Dulce aroma de campo", porcentaje_actualizar, tipo_uva_actualizar)
        self.set_varietal(aux)
