import tkinter as tk
from controllers.GestorImportarVinoDeBodega import GestorImportarVinoDeBodega
from models.Bodega import Bodega
from models.Maridaje import Maridaje
from models.TipoUva import TipoUva
from models.Varietal import Varietal
from models.Probando import Probando
from views.PantallaImportar import PantallaImportar

def main():
    bodegas = Probando.cargar_datos_iniciales()
    vinos = Probando.crear_lista_vinos()
    maridajes = Probando.crear_lista_maridaje()
    tipos_uva = Probando.crear_lista_tipo_uva()

    # Instanciamos el gestor con las listas creadas
    gestor_importar_vino_de_bodega = GestorImportarVinoDeBodega(bodegas, vinos, maridajes, tipos_uva)

    # Crear la ventana principal (en este caso, la PantallaImportar) en Tkinter
    #root = tk.Tk()
    app = PantallaImportar(gestor_importar_vino_de_bodega)
    gestor_importar_vino_de_bodega.set_pantalla(app)

    # Iniciar la interfaz gráfica
    pantalla_importar.mainloop()

if __name__ == "__main__":
    main()
