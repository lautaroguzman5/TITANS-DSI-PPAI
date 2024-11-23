import tkinter as tk
from controllers import GestorImportarVinoDeBodega
from models import Bodega, Vino, Maridaje, TipoUva
from models import Probando
from views import PantallaImportar
from views import PantallaNotificacion

def crear_lista_bodegas():
    # Aquí llamarías a la función que carga las bodegas, similar a Probando.CargarDatosIniciales()
    return 

def crear_lista_vinos():
    # Aquí crearías la lista de vinos, similar a Probando.crear_lista_vinos()
    return Probando.crear_lista_vinos()

def crear_lista_maridajes():
    # Crear la lista de maridajes, similar a Probando.crear_lista_maridaje()
    return Probando.crear_lista_maridaje()

def crear_lista_tipo_uva():
    # Crear la lista de tipos de uva, similar a Probando.crear_lista_tipo_uva()
    return Probando.crear_lista_tipo_uva()

def main():
    bodegas = crear_lista_bodegas()
    vinos = crear_lista_vinos()
    maridajes = crear_lista_maridajes()
    tipos_uva = crear_lista_tipo_uva()

    # Instanciamos el gestor con las listas creadas
    gestor_importar_vino_de_bodega = GestorImportarVinoDeBodega(bodegas, vinos, maridajes, tipos_uva)

    # Crear la ventana principal (en este caso, la PantallaImportar) en Tkinter
    root = tk.Tk()
    pantalla_importar = PantallaImportar(root, gestor_importar_vino_de_bodega)

    # Iniciar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
