import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficaDesign():
    def __init__(self, panel_principal):
        # crea dos subgraficos usando matplotlib
        self.figura = Figure(figsize=(8, 6), dpi=100)
        self.ax1 = self.figura.add_subplot(211)
        self.ax2 = self.figura.add_subplot(212)

        # agregar espacio entre las figuras
        self.figura.subplots_adjust(hspace=0.4)

        self.grafico1()
        self.grafico2()

        # Agregar los gráficos a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(self.figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def grafico1(self):
        # Función para graficar el primer conjunto de datos como un gráfico de barras
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        # grafico de barras
        self.ax1.bar(x, y, label='Gráfico 1', color='blue', alpha=0.7)

        # personalizar el aspecto del gráfico
        self.ax1.set_title("Gráfico 1 - Gráfico de barras")
        self.ax1.set_xlabel("Eje X")
        self.ax1.set_ylabel("Eje Y")
        self.ax1.legend()

        # Añadir etiquetas a cada barra
        for i, v in enumerate(y):
            self.ax1.text(x[i] - 0.1, v + 0.1, str(v), color='black')

        # Añadir cuadrícula
        self.ax1.grid(axis='y', linestyle='--', alpha=0.7)


    def grafico2(self):
        # Función para graficar el segundo conjunto de datos
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 1, 2, 1]
        self.ax2.plot(x, y, label='Gráfico 2', color='red')
        self.ax2.set_title('Gráfico 2',)
        self.ax2.set_xlabel('Eje X', fontsize=12)
        self.ax2.set_ylabel('Eje Y', fontsize=12)
        self.ax2.plot(x, y, label='Gráfico 2', color='red', linestyle='--', marker='o')
        self.ax2.annotate('Punto importante', xy=(3, 1), xytext=(3.5, 1.5),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        self.ax2.set_xlim(0, 6)  # Establece los límites del eje x
        self.ax2.set_ylim(0, 3)  # Establece los límites del eje y
        self.ax2.grid(True, linestyle='--', alpha=0.6)
        self.ax2.legend()
