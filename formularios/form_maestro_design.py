import tkinter as tk
from tkinter import font, ttk
from config import *
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficaDesign

class FormularioMaestroDesign(tk.Tk):
    """app root"""
    def __init__(self):
        super().__init__()
        # app root
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560, 136))
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))
        self.img_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (100, 100))
        self.config_window()

        # button styles
        # It's not possible to use tk.Buttons in my linux.
        self.style = ttk.Style()

        self.style.configure("lat.TButton", font=("roboto", 15),
                foreground="white", width=20,
                border=0, relief=tk.FLAT, background=COLOR_MENU_LATERAL, anchor=tk.W)

        self.style.configure("TButton", font=("roboto", 15),
                width=5,
                foreground="white", border=0, relief=tk.FLAT,
                background=COLOR_BARRA_SUPERIOR)

        self.style.map("TButton",
                foreground=[('active', "white")],
                background=[('active', COLOR_MENU_CURSOR_ENCIMA)])

        # show the three main frames
        self.paneles()


    def config_window(self):
        self.title("tkinter GUI")
        # self.iconbitmap("./imagenes/logo.ico")
        self.geometry("1024x600")

    def paneles(self):
        # crea paneles: barra superior, menú lateral, cuerpo principal
        self.panel_superior = PanelSuperior(self)

        self.menu_lateral = PanelLateral(self)

        self.panel_principal = PanelPrincipal(self)


class PanelSuperior(tk.Frame):
    """this is something like the navbar"""
    def __init__(self, master):
        super().__init__(master, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.pack(side=tk.TOP, fill="both")

        # show buttons and text
        self.controles()

    def controles(self):
        # Button to toggle the side menu
        self.botton_menu_lateral = ttk.Button(self,
                text="\uf0c9", style="TButton", command=self.toggle_panel)
        self.botton_menu_lateral.pack(side=tk.LEFT)

        # titulo
        label_titulo = tk.Label(self, text="dtisoy")
        label_titulo.config(fg="#fff", font=("roboto", 15), bg=COLOR_BARRA_SUPERIOR, padx=10)
        label_titulo.pack(side=tk.LEFT)

    def toggle_panel(self):
        if self.master.menu_lateral.winfo_ismapped():
            self.master.menu_lateral.forget()
        else:
            self.master.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)


class PanelLateral(tk.Frame):
    """Side frame with the menu"""
    def __init__(self, master):
        super().__init__(master, bg=COLOR_MENU_LATERAL)
        self.master = master

        self.pack(side=tk.LEFT, fill="both", expand=False)

        # lateral buttons and profile picture
        self.controles()

    def controles(self):

        # profile picture
        labelPerfil= tk.Label(
                self, image=self.master.perfil, bg=COLOR_MENU_LATERAL)

        labelPerfil.pack(side=tk.TOP, pady=10, padx=10)

        # Menu options
        botonDashboard = BotonMenuLateral(self, "Dashboard", "\uf109", command=self.abrir_panel_graficas)
        botonProfile = BotonMenuLateral(self, "Profile", "\uf0c0")
        botonPicture = BotonMenuLateral(self, "Picture", "\uf03e")
        botonInfo = BotonMenuLateral(self, "Info", "\uf129", command=self.abrir_panel_info)
        botonSettings = BotonMenuLateral(self, "Settings", "\uf1de")

    def abrir_panel_info(self):
        self.master.panel_principal.limpiar()
        FormularioInfoDesign()

    def abrir_sitio_en_construccion(self):
        self.master.panel_principal.limpiar()
        FormularioSitioConstruccionDesign(self.master.panel_principal, self.master.img_construccion)

    def abrir_panel_graficas(self):
        self.master.panel_principal.limpiar()
        FormularioGraficaDesign(self.master.panel_principal)

# pylint: disable=too-many-ancestors
class BotonMenuLateral(ttk.Button):

    """Menu options configuration """
    def __init__(self, master, titulo, icono, command=None):
        super().__init__(master, style="lat.TButton")
        self.titulo = titulo
        self.icono = icono
        self["text"] = f"   {self.icono}       {self.titulo}"
        if not command:
            self["command"] = master.abrir_sitio_en_construccion
        self["command"] = command


        self.pack(side=tk.TOP)

class PanelPrincipal(tk.Frame):
    """Main Frame"""
    def __init__(self, master):
        super().__init__(master, bg=COLOR_CUERPO_PRINCIPAL)

        self.pack(side=tk.RIGHT, fill="both", expand=True)
        self.logo = tk.Label(self, image=self.master.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()
