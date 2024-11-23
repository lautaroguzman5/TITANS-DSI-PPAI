import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Clases simuladas para la lógica
class Bodega:
    def __init__(self, nombre, capacidad, descripcion, historia, ubicacion, fecha_creacion):
        self.nombre = nombre
        self.capacidad = capacidad
        self.descripcion = descripcion
        self.historia = historia
        self.ubicacion = ubicacion
        self.fecha_creacion = fecha_creacion

class Probando:
    def cargar_datos_iniciales(self):
        return [
            Bodega("Bodega Cordoba", 1, "Descripcion Bodega Cordoba", "Historia Fernando", 
                   [40.7128, -74.0060], datetime.now()),
            Bodega("Bodega BSAS", 2, "Descripcion Bodega BSAS", "Historia Fernando", 
                   [40.7128, -74.0060], datetime.now()),
            Bodega("Bodega Mendoza", 4, "Descripcion Bodega Mendoza", "Historia Fernando", 
                   [40.7128, -74.0060], datetime.now()),
            Bodega("Bodega SanJuan", 1, "Descripcion Bodega SanJuan", "Historia Fernando", 
                   [40.7128, -74.0060], datetime.now())
        ]

# Clase principal de la aplicación
class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Bodegas")
        self.geometry("600x400")

        # Botón para cargar datos
        self.btn_load = tk.Button(self, text="Cargar Datos", command=self.cargar_datos)
        self.btn_load.pack(pady=10)

        # Treeview para mostrar los datos
        self.tree = ttk.Treeview(self, columns=("Nombre", "Capacidad", "Descripción", "Fecha"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Capacidad", text="Capacidad")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Fecha", text="Fecha de Creación")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def cargar_datos(self):
        # Instancia de la lógica
        probando = Probando()
        bodegas = probando.cargar_datos_iniciales()

        # Limpiar datos previos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar datos en el Treeview
        for bodega in bodegas:
            self.tree.insert("", "end", values=(bodega.nombre, bodega.capacidad, 
                                                bodega.descripcion, bodega.fecha_creacion.strftime("%Y-%m-%d")))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
