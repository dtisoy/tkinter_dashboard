import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL


class FormularioSitioConstruccionDesign():

    def __init__(self, panel_principal, logo):


        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.label_titulo = tk.Label(self.barra_superior, text="pagina en construccion")
        self.label_titulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)

        self.label_imagen = tk.Label(self.barra_inferior, image=logo)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_imagen.config(font=("Roboto", 10), bg=COLOR_CUERPO_PRINCIPAL)
