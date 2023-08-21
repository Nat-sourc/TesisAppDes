import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from start import Pagina1

class Aplicacion(tk.Tk):
    def __init__(self, *args, **kwargs):  # Corregir _init_ a __init__
        tk.Tk.__init__(self, *args, **kwargs)  # Corregir _init_ a __init__
        
        self.contenedor = ttk.Frame(self)
        self.contenedor.pack(side="top", fill="both", expand=True)
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        
        self.paginas = {}
        
        self.mostrar_pagina(Pagina1)
    
    def mostrar_pagina(self, clase_pagina):
        pagina = self.paginas.get(clase_pagina)
        if pagina is None:
            pagina = clase_pagina(self.contenedor, self)
            self.paginas[clase_pagina] = pagina
            pagina.grid(row=0, column=0, sticky="nsew")
        
        pagina.tkraise()


if __name__ == "__main__":  # Corregir _main_ a __main__
    app = Aplicacion()
    app.mainloop()
