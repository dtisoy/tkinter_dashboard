import tkinter as tk
from tkinter import font, ttk
from config import *
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560, 136))
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))
        self.config_window()

        # button styles
        # It's not possible to use tk.Buttons in my linux.
        self.style = ttk.Style()
        self.style.configure("lat.TButton", font=("roboto", 15),
                foreground="white",
                border=0, relief=tk.FLAT, background=COLOR_MENU_LATERAL, anchor=tk.W)

        self.style.configure("TButton", foreground="white", border=0, relief=tk.FLAT, background=COLOR_BARRA_SUPERIOR)
        self.style.map("TButton",
                foreground=[('active', "white")],
        background=[('active', COLOR_MENU_CURSOR_ENCIMA)])


        self.paneles()


    def config_window(self):
        self.title("tkinter GUI")
        # self.iconbitmap("./imagenes/logo.ico")
        self.geometry("1024x600")

    def paneles(self):
        # crea paneles: barra superior, menú lateral, cuerpo principal
        # self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.panel_superior = PanelSuperior(self)

        self.menu_lateral = PanelLateral(self)

        self.panel_principal = PanelPrincipal(self)


class PanelSuperior(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.pack(side=tk.TOP, fill="both")


        self.controles()

    def controles(self):

        font_awesome = font.Font(family="FontAwesome", size=12
        )
        # titulo
        label_titulo = tk.Label(self, text="dtisoy")
        label_titulo.config(fg="#fff", font=("roboto", 15), bg=COLOR_BARRA_SUPERIOR, padx=10)
        label_titulo.pack(side=tk.LEFT)

        # Botón del menú lateral

        self.botton_menu_lateral = ttk.Button(self,
                text="\uf0c9", style="TButton", command=self.toggle_panel)
        self.botton_menu_lateral.pack(side=tk.LEFT)

    def toggle_panel(self):
        if self.master.menu_lateral.winfo_ismapped():
            self.master.menu_lateral.forget()
        else:
            self.master.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)


class PanelLateral(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_MENU_LATERAL)
        self.master = master
        self.font_awesome = font.Font(family="FontAwesome", size=15)

        self.pack(side=tk.LEFT, fill="both", expand=False)

        # lateral button styles

        self.controles()

    def controles(self):

        # Etiqueta de perfil
        labelPerfil= tk.Label(
                self, image=self.master.perfil, bg=COLOR_MENU_LATERAL)

        labelPerfil.pack(side=tk.TOP, pady=10, padx=10)

        # Botones
        botonDashboard = BotonMenuLateral(self, "Dashboard", "\uf109")
        botonProfile = BotonMenuLateral(self, "Profile", "\uf0c0")
        botonPicture = BotonMenuLateral(self, "Picture", "\uf03e")
        botonInfo = BotonMenuLateral(self, "Info", "\uf129")
        botonSettings = BotonMenuLateral(self, "Settings", "\uf1de")

class BotonMenuLateral(ttk.Button):
    def __init__(self, master, titulo, icono):
        super().__init__(master)
        self.titulo = titulo
        self.icono = icono
        self["text"] = f"   {self.icono}       {self.titulo}"
        self["width"] = 20
        self["style"] = "lat.TButton"


        self.pack(side=tk.TOP)

class PanelPrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_CUERPO_PRINCIPAL)

        self.pack(side=tk.RIGHT, fill="both", expand=True)
        self.logo = tk.Label(self, image=self.master.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)
