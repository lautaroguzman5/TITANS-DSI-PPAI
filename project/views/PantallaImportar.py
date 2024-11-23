import tkinter as tk
from tkinter import messagebox, ttk
from controllers.GestorImportarVinoDeBodega import GestorImportarVinoDeBodega

class PantallaImportar(tk.Tk):
    def __init__(self, gestor_importar_vino_de_bodega):
        super().__init__()
        self.gestor_importar_vino_de_bodega = gestor_importar_vino_de_bodega

        # Configuración inicial de la ventana
        self.title("Pantalla Importar")
        self.geometry("800x600")

        # Widgets
        self.comboBox1 = ttk.Combobox(self)
        self.comboBox1.bind("<<ComboboxSelected>>", self.comboBox1_selected)
        self.comboBox1.pack()

        self.lblBodegaSelec = tk.Label(self, text="Bodega seleccionada:")
        self.lblBodegaSelec.pack()

        self.dtgBodegaSeleccionada = ttk.Treeview(
            self, columns=("Vino", "Cantidad", "Precio", "Año", "Variedad"), show="headings"
        )
        for col in self.dtgBodegaSeleccionada["columns"]:
            self.dtgBodegaSeleccionada.heading(col, text=col)
        self.dtgBodegaSeleccionada.pack(fill="both", expand=True)

        self.btnImportarDatos = tk.Button(self, text="Importar Datos", command=self.btn_importar_datos_click)
        self.btnImportarDatos.pack()

        self.btnNotificar = tk.Button(self, text="Enviar Notificaciones", command=self.btn_enviar_notificaciones)
        self.btnNotificar.pack()
        self.btnNotificar.pack_forget()  # Ocultar inicialmente

        self.lblEnviarNotif = tk.Label(self, text="Notificaciones enviadas")
        self.lblEnviarNotif.pack()
        self.lblEnviarNotif.pack_forget()  # Ocultar inicialmente

        # Operación inicial
        self.op_actualizar_importacion_vino()

    def op_actualizar_importacion_vino(self):
        self.habilitar_pantalla()
        self.gestor_importar_vino_de_bodega.op_importar_actualizacion_vino_bodega(self)

    def mostrar_bodega_para_actualizar(self, bodegas_actualizaciones):
        self.comboBox1["values"] = bodegas_actualizaciones

    def no_existen_bodegas_con_actualizaciones(self):
        messagebox.showinfo("Información", "No hay actualizaciones disponibles")
        self.gestor_importar_vino_de_bodega.fin_cu()

    def api_no_disponible(self):
        messagebox.showinfo("Información", "La API no está disponible")
        self.gestor_importar_vino_de_bodega.fin_cu()

    def habilitar_pantalla(self):
        self.comboBox1.pack_forget()
        self.lblBodegaSelec.pack_forget()
        self.dtgBodegaSeleccionada.pack_forget()
        self.btnNotificar.pack_forget()
        self.lblEnviarNotif.pack_forget()

    def seleccionar_bodega(self):
        nombre_seleccionado = self.comboBox1.get()
        self.lblBodegaSelec.config(text=nombre_seleccionado)
        self.comboBox1.config(state="disabled")
        self.gestor_importar_vino_de_bodega.tomar_bodega_seleccionada(nombre_seleccionado)

    def mostrar_resumen_vinos_importados(self, actualizados, seleccionada):
        for row in self.dtgBodegaSeleccionada.get_children():
            self.dtgBodegaSeleccionada.delete(row)

        for vino in actualizados:
            self.dtgBodegaSeleccionada.insert("", "end", values=vino)

    def comboBox1_selected(self, event):
        self.seleccionar_bodega()
        self.btnNotificar.pack()
        self.lblEnviarNotif.pack()
        self.lblBodegaSelec.pack()

    def btn_importar_datos_click(self):
        self.comboBox1.set("")
        self.comboBox1.pack()
        self.lblBodegaSelec.pack()
        self.dtgBodegaSeleccionada.pack()
        self.op_actualizar_importacion_vino()

    def btn_enviar_notificaciones(self):
        self.gestor_importar_vino_de_bodega.enviar_notificaciones_novedad_a_suscriptores()


""" # Ejemplo de uso
if __name__ == "__main__":
    # Simular el gestor para pruebas
    class GestorImportarVinoDeBodega:
        def op_importar_actualizacion_vino_bodega(self, pantalla):
            bodegas = ["Bodega 1", "Bodega 2", "Bodega 3"]
            pantalla.mostrar_bodega_para_actualizar(bodegas)

        def tomar_bodega_seleccionada(self, nombre_bodega):
            print(f"Bodega seleccionada: {nombre_bodega}")

        def enviar_notificaciones_novedad_a_suscriptores(self):
            print("Notificaciones enviadas")

        def fin_cu(self):
            print("Fin del caso de uso")

    gestor = GestorImportarVinoDeBodega()
    app = PantallaImportar(gestor)
    app.mainloop() """
