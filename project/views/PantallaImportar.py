import tkinter as tk
from tkinter import ttk

class PantallaImportar(tk.Toplevel):
    def __init__(self, gestorImportarVinoDeBodega):
        super().__init__()
        self.gestorImportarVinoDeBodega = gestorImportarVinoDeBodega
        self.title("Importar Bodegas")
        self.geometry("600x400")

        self.comboBox = ttk.Combobox(self)
        self.comboBox.pack(pady=10)

        self.labelBodegaSelec = tk.Label(self, text="Bodega seleccionada:", font=("Arial", 10))
        self.labelBodegaSelec.pack()

        self.tree = ttk.Treeview(self, columns=("Vino", "Cantidad", "Precio", "Año", "Variedad"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=20, fill="both", expand=True)

        self.btnImportarDatos = tk.Button(self, text="Importar Datos", command=self.importarDatos)
        self.btnImportarDatos.pack()

        self.btnEnviarNotificaciones = tk.Button(self, text="Enviar Notificaciones", command=self.enviarNotificaciones)
        self.btnEnviarNotificaciones.pack()

    def mostrarBodegaParaActualizar(self, bodegasActualizaciones):
        self.comboBox["values"] = bodegasActualizaciones
        self.comboBox.set("")  # Reset

    def mostrarResumenVinosImportados(self, actualizados):
        for vino in actualizados:
            self.tree.insert("", "end", values=vino)

    def importarDatos(self):
        # Aquí llamarías al método que maneja la importación
        print("Importando datos...")
        bodegas = ["Bodega 1", "Bodega 2", "Bodega 3"]
        self.mostrarBodegaParaActualizar(bodegas)

    def enviarNotificaciones(self):
        print("Enviando notificaciones...")

# Ejemplo de uso:
# gestorImportarVinoDeBodega = ...
# ventana = PantallaImportar(gestorImportarVinoDeBodega)
# ventana.mainloop()
