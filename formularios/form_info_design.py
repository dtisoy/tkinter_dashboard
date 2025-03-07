import tkinter as tk
from typing_extensions import Literal

class FormularioInfoDesign(tk.Toplevel):

    def __init__(self) -> None:
        super().__init__()
        self.title("Python GUI")
        self.geometry("400x100")
        self.construir_widget()

    def construir_widget(self):
        self.labelVersion = tk.Label(self, text="Version : 1.0")
        self.labelVersion.config(fg="#000000", font=(
            "Roboto", 15), pady=10, width=20)
        self.labelVersion.pack()

        self.labelAutor = tk.Label(self, text="Autor : dtisoy")
        self.labelAutor.config(fg="#000000", font=(
            "Roboto", 15), pady=10, width=20)
        self.labelAutor.pack()
