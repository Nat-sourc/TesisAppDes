import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore

class ButtonsDual:
    def __init__(self, master=None, patient_id=None, pageA=None,buttonsA=None,path=None,root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.buttonsA=buttonsA
        self.path = path
        self.setup_ui()
        print(self.pageA)

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.create_sidebar()
    
    def create_sidebar(self):
        global loadimage, homeimage, volverimage, volverATaskimage, botonSC, botonSM
        sidebar_color = "#77CCC1"
        sidebar_list_color = "#C4F1EB" 
        sidebar_blank_color = "#E5F5F3"

        db = firestore.client()

        sidebar = tk.Frame(self.root, bg=sidebar_color, width=150)
        sidebar.pack(fill="y", side="left")

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        homeimage = Image.open("./resources/img/home.png")
        homeimage = tk.PhotoImage(file="./resources/img/home.png")
        homeimage = homeimage.subsample(8, 8)

        canvashome = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvashome.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing
        

        rounded_buttonhome = tk.Button(canvashome, image=homeimage, bg=sidebar_color, bd=0, command=self.home)
        rounded_buttonhome.pack(side="top", pady=10)

        volverATaskimage = Image.open("./resources/img/volverATask.png")
        volverATaskimage = tk.PhotoImage(file="./resources/img/volverATask.png")
        volverATaskimage = volverATaskimage.subsample(8, 8)

        canvasvolverATask = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvasvolverATask.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_buttonVolverATask = tk.Button(canvasvolverATask, image=volverATaskimage, bg=sidebar_color, bd=0, command=self.vieTask)
        rounded_buttonVolverATask.pack(side="top", pady=10)

        volverimage = Image.open("./resources/img/atras.png")
        volverimage = tk.PhotoImage(file="./resources/img/atras.png")
        volverimage = volverimage.subsample(8, 8)

        canvasvolver = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvasvolver.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_buttonVolver = tk.Button(canvasvolver, image=volverimage, bg=sidebar_color, bd=0, command=self.atras)
        rounded_buttonVolver.pack(side="top", pady=10)

        loadimage = Image.open("./resources/img/logout.png")
        loadimage = tk.PhotoImage(file="./resources/img/logout.png")
        loadimage = loadimage.subsample(8, 8)

        canvas = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvas.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_button = tk.Button(canvas, image=loadimage, bg=sidebar_color, bd=0, command=self.logout)
        rounded_button.pack(side="top", pady=10)
        
        sidebar_blank = tk.Frame(self.root, bg=sidebar_blank_color, width=20)
        sidebar_blank.pack(fill="y", side="left")

        sidebar_list = tk.Frame(self.root, bg="#E5F5F3", width=700)
        sidebar_list.pack(fill="both", side="left", expand=True)

        sidebar_list_title = tk.Frame(sidebar_list, bg=sidebar_list_color)
        sidebar_list_title.pack(fill="x")

        print(self.buttonsA)

        if self.buttonsA=="BSimplesCog":
            title_label = tk.Label(
                sidebar_list_title,
                text="SIMPLES COGNITIVAS",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        if self.buttonsA=="BSimplesMotoras":
            title_label = tk.Label(
                sidebar_list_title,
                text="SIMPLES MOTORAS",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        if self.buttonsA=="BDual":
            title_label = tk.Label(
                sidebar_list_title,
                text="DUAL TASK JUNTAS",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        for _ in range(6):
            tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

        if self.buttonsA=="BSimplesCog":
            self.botonFV = tk.PhotoImage(file="./resources/img/btFluenciaVerbal.png")
            self.botonFV = self.botonFV.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasFV = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasFV.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonFV = tk.Button(self.botonFV, image=self.botonFV, bg="white", bd=0, command=self.fuenciaverbal)
            self.rounded_buttonFV.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonArit = tk.PhotoImage(file="./resources/img/btAritmetica.png")
            self.botonArit = self.botonArit.subsample(2, 2)
            # Create a Canvas widget
            self.canvasArit = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasArit.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonArit = tk.Button(self.canvasArit, image=self.botonArit, bg="white", bd=0, command=self.aritmetica)
            self.rounded_buttonArit.pack(side="top")

        if self.buttonsA=="BSimplesMotoras":
            self.botonbrazo = tk.PhotoImage(file="./resources/img/btBrazo.png")
            self.botonbrazo = self.botonbrazo.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasbrazo = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasbrazo.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonbrazo = tk.Button(self.canvasbrazo, image=self.botonbrazo, bg="white", bd=0, command=self.brazo)
            self.rounded_buttonbrazo.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonMarcha = tk.PhotoImage(file="./resources/img/btMarcha.png")
            self.botonMarcha = self.botonMarcha.subsample(2, 2)
            # Create a Canvas widget
            self.canvasMarcha = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasMarcha.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonMarcha = tk.Button(self.canvasMarcha, image=self.botonMarcha, bg="white", bd=0, command=self.marcha)
            self.rounded_buttonMarcha.pack(side="top")

        if self.buttonsA=="BDual":
            self.botonbrazoDual = tk.PhotoImage(file="./resources/img/btBrazoDual.png")
            self.botonbrazoDual = self.botonbrazoDual.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasbrazoDual = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasbrazoDual.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonbrazoDual = tk.Button(self.canvasbrazoDual, image=self.botonbrazoDual, bg="white", bd=0, command=self.brazoDual)
            self.rounded_buttonbrazoDual.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonMarchaDual = tk.PhotoImage(file="./resources/img/btMarchaDual.png")
            self.botonMarchaDual = self.botonMarchaDual.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasMarchaDual = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasMarchaDual.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonMarchaDual = tk.Button(self.canvasMarchaDual, image=self.botonMarchaDual, bg="white", bd=0, command=self.marchaDual)
            self.rounded_buttonMarchaDual.pack(side="top")



    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        self.master.mostrar_pagina("ViewPatients")

    def atras(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonsDualBrad",self.patient_id,"ButtonDual","BDual", self.path)

    def vieTask(self):
        self.master.mostrar_pagina("ViewTask")
    
    def fuenciaverbal(self):
        pass

    def aritmetica(self):
        pass

    def brazo(self):
        self.master.mostrar_paginaConIdAndButtons("MostrarVideosDual",self.patient_id,"ButtonsDualBrad","BBrazo", self.path)

    def marcha(self):
        self.master.mostrar_paginaConIdAndButtons("MostrarVideosDual",self.patient_id,"ButtonsDualBrad","BMarcha", self.path)

    def brazoDual(self):
        self.master.mostrar_paginaConIdAndButtons("MostrarVideosDual",self.patient_id,"ButtonsDualBrad","BBrazoDual", self.path)

    def marchaDual(self):
        self.master.mostrar_paginaConIdAndButtons("MostrarVideosDual",self.patient_id,"ButtonsDualBrad","BMarchaDual", self.path)

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    app.mainloop()