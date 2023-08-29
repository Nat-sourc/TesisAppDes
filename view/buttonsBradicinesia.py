import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore

class ButtonsBradicinesia:
    def __init__(self, master=None, patient_id=None, pageA=None,buttonsA=None,path=None, root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.buttonsA=buttonsA
        self.path = path
        self.setup_ui()
        print("soy pagina anterior " + self.pageA)

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

        if self.buttonsA=="BToqueD":
            title_label = tk.Label(
                sidebar_list_title,
                text="TOQUE DE DEDOS",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        if self.buttonsA=="BGiroM":
            title_label = tk.Label(
                sidebar_list_title,
                text="GIRO DE MANOS",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        if self.buttonsA=="BAyCMano":
            title_label = tk.Label(
                sidebar_list_title,
                text="ABRE Y CIERRA LA MANO",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
        for _ in range(4):
            tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

        if self.buttonsA=="BToqueD":
            self.botonTD = tk.PhotoImage(file="./resources/img/manoDerecha.png")
            self.botonTD = self.botonTD.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasTD = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasTD.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonTD = tk.Button(self.canvasTD, image=self.botonTD, bg="white", bd=0, command=self.toqueDedosMD)
            self.rounded_buttonTD.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonSM = tk.PhotoImage(file="./resources/img/manoIzquierda.png")
            self.botonSM = self.botonSM.subsample(2, 2)
            # Create a Canvas widget
            self.canvasSM = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasSM.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonSM = tk.Button(self.canvasSM, image=self.botonSM, bg="white", bd=0, command=self.simpleMotor)
            self.rounded_buttonSM.pack(side="top")

        if self.buttonsA=="BGiroM":
            self.botonSC = tk.PhotoImage(file="./resources/img/manoDerecha.png")
            self.botonSC = self.botonSC.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasSC = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasSC.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonSC = tk.Button(self.canvasSC, image=self.botonSC, bg="white", bd=0, command=self.simpleCog)
            self.rounded_buttonSC.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonSM = tk.PhotoImage(file="./resources/img/manoIzquierda.png")
            self.botonSM = self.botonSM.subsample(2, 2)
            # Create a Canvas widget
            self.canvasSM = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasSM.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonSM = tk.Button(self.canvasSM, image=self.botonSM, bg="white", bd=0, command=self.simpleMotor)
            self.rounded_buttonSM.pack(side="top")

        if self.buttonsA=="BAyCMano":
            self.botonTD = tk.PhotoImage(file="./resources/img/manoDerecha.png")
            self.botonTD = self.botonTD.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasTD = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasTD.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonTD = tk.Button(self.canvasTD, image=self.botonTD, bg="white", bd=0, command=self.toqueD)
            self.rounded_buttonTD.pack(side="top")

            for _ in range(3):
                tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

            self.botonGM = tk.PhotoImage(file="./resources/img/manoIzquierda.png")
            self.botonGM = self.botonGM.subsample(2, 2) 
            # Create a Canvas widget
            self.canvasGM = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
            self.canvasGM.pack(side="top")

            # Create a rounded button with the loaded image
            self.rounded_buttonGM = tk.Button(self.canvasGM, image=self.botonGM, bg="white", bd=0, command=self.giroM)
            self.rounded_buttonGM.pack(side="top")



    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        self.master.mostrar_pagina("ViewPatients")
        

    def atras(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonsDualBrad",self.patient_id,"ButtonsDualBrad","BBrad", self.path)

    def vieTask(self):
        self.master.mostrar_pagina("ViewTask")
        
    
    def toqueDedosMD(self):
        self.master.mostrar_paginaConIdAndButtons("MostrarVideos",self.patient_id,"ButtonsDualBrad","BToqueMD", self.path)

    def simpleCog(self):
        pass
    def simpleMotor(self):
        pass

    def toqueD(self):
        pass

    def dual(self):
        pass

    def giroM(self):
        pass

    def AyCMano(self):
        pass

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    app.mainloop()