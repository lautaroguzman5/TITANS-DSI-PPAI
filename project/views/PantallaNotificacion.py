import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para cargar imágenes

class PantallaNotificacion(tk.Toplevel):
    def __init__(self, enofilos):
        super().__init__()
        self.enofilos = enofilos
        self.title("Notificación")
        self.geometry("300x150")
        self.configure(bg="#404040")

        self.label1 = tk.Label(self, text="", font=("Arial", 10, "bold"), fg="white", bg="#404040")
        self.label1.pack(pady=20)

        self.label2 = tk.Label(self, text="Se envió la notificación al usuario:", font=("Arial", 8, "bold"), fg="white", bg="#404040")
        self.label2.pack()

        # Cargar una imagen
        self.image = Image.open("icono.png")  # Asegúrate de tener esta imagen en tu carpeta
        self.image = self.image.resize((64, 50))  # Redimensionar la imagen
        self.photo = ImageTk.PhotoImage(self.image)
        self.picture_label = tk.Label(self, image=self.photo, bg="#404040")
        self.picture_label.pack(side="right", padx=10)

    def notificarNovedadASuscriptores(self, enofiloNoti):
        self.label1.config(text=enofiloNoti)
        self.deiconify()  # Mostrar la ventana

    def cerrar(self):
        self.destroy()

# Ejemplo de uso:
# enofilos = ["Enófilo 1", "Enófilo 2"]
# ventana = PantallaNotificacion(enofilos)
# ventana.notificarNovedadASuscriptores("¡Notificación enviada al enófilo!")
# ventana.mainloop()
