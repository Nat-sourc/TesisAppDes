import tkinter as tk
from start import Start
from buttonsDual import ButtonsDual
from buttonsBradicinesia import ButtonsBradicinesia
from viewPatients import ViewPatients
from viewTask import ViewTask
from buttonsDualBrad import ButtonsDualBrad
from tkinter import PhotoImage
from PIL import Image, ImageTk  

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BrainFit")
        self.geometry("1340x768")
        
        self.paginas = {
            "Start": Start,
            "ViewPatients": ViewPatients,
            "ViewTask": ViewTask,
            "ButtonsDualBrad": ButtonsDualBrad,
            "ButtonDual": ButtonsDual,
            "ButtonBradicinesia": ButtonsBradicinesia
        }

        self.mostrar_pagina("Start")
        #self.image_hospital = Image.open("../resources/img/hospital.png")

    def mostrar_pagina(self, nombre_pagina):
        for widget in self.winfo_children():
            widget.destroy()  # Destruir todos los widgets en la ventana actual

        for pagina_nombre, pagina_clase in self.paginas.items():
            if pagina_nombre == nombre_pagina:
                self.pagina_actual = pagina_clase(self)
                break
    def mostrar_paginaConId(self, nombre_pagina,id,pageA):
        for widget in self.winfo_children():
            widget.destroy()  # Destruir todos los widgets en la ventana actual

        for pagina_nombre, pagina_clase in self.paginas.items():
            if pagina_nombre == nombre_pagina:
                self.pagina_actual = pagina_clase(self,id,pageA)
                break
    def mostrar_paginaConIdAndButtons(self, nombre_pagina,id,pageA,buttonsA):
        for widget in self.winfo_children():
            widget.destroy()  # Destruir todos los widgets en la ventana actual

        for pagina_nombre, pagina_clase in self.paginas.items():
            if pagina_nombre == nombre_pagina:
                self.pagina_actual = pagina_clase(self,id,pageA,buttonsA)
                break

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
