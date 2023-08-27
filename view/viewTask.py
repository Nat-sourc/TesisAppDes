import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore

class ViewTask:
    def __init__(self, master=None, patient_id=None, pageA=None,root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.setup_ui()
        print(pageA)

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.create_sidebar()
    

    def create_sidebar(self):
        global loadimage, homeimage, volverimage, volverATaskimage, botonBrad
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

        
        title_label = tk.Label(
            sidebar_list_title,
            text="BRAINFIT",
            font=("Arial", 20, "bold"),
            bg=sidebar_list_color,
            fg="#00BFA6"
        )
        title_label.pack(side="left",padx=10, pady=10)

        for _ in range(3):
            tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

        self.botonBrad = tk.PhotoImage(file="./resources/img/botonBrad.png")
        self.botonBrad = self.botonBrad.subsample(5, 5) 
        # Create a Canvas widget
        self.canvasBrad = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
        self.canvasBrad.pack(side="top")

        # Create a rounded button with the loaded image
        self.rounded_buttonBrad = tk.Button(self.canvasBrad, image=self.botonBrad, bg="white", bd=0, command=self.bradicinesia)
        self.rounded_buttonBrad.pack(side="top")

        for _ in range(3):
            tk.Label(sidebar_list, text="", bg=sidebar_blank_color).pack()  # Add spacing

        self.botonDual = tk.PhotoImage(file="./resources/img/botonDual.png")
        self.botonDual = self.botonDual.subsample(5, 5) 
        # Create a Canvas widget
        self.canvasDual = tk.Canvas(sidebar_list, bg=sidebar_blank_color, highlightthickness=0)
        self.canvasDual.pack(side="top")

        # Create a rounded button with the loaded image
        self.rounded_buttonDual = tk.Button(self.canvasDual, image=self.botonDual, bg="white", bd=0, command=self.dual)
        self.rounded_buttonDual.pack(side="top")

        patient_ref = db.collection("pacientes").document(self.patient_id)
        patient_data = patient_ref.get()
        
        if patient_data.exists:
            patient_data_dict = patient_data.to_dict()
            # Check if completeBradicinesis is true or false
            complete_bradicinesis = patient_data_dict.get("completeBradicinesis", False)
            complete_Dual = patient_data_dict.get("completetask", False)
            # Update button state
            if complete_bradicinesis:
                self.rounded_buttonBrad.config(state="normal")  # Enable the button
            else:
                self.rounded_buttonBrad.config(state="disabled")  # Disable the button

            if complete_Dual:
                self.rounded_buttonDual.config(state="normal")  # Enable the button
            else:
                self.rounded_buttonDual.config(state="disabled")  # Disable the button
        else:
            print("Patient data not found for ID:", patient_id)


    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        pass

    def atras(self):
        self.master.mostrar_pagina(self.pageA)

    def vieTask(self):
        pass
    
    def dual(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonsDualBrad",self.patient_id,"ViewTask","BDual")

    def bradicinesia(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonsDualBrad",self.patient_id,"ViewTask","BBrad")

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    patient_id = "12345"

    view_task = ViewTask(patient_id, root=app)
    app.mainloop()
