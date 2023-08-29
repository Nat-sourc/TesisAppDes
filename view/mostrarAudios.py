import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore
from pathlib import Path
import pygame


class MostrarAudios:
    def __init__(self, master=None, patient_id=None, pageA=None,buttonsA=None,path=None, root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.buttonsA=buttonsA
        self.video_label=None
        self.pathAux=path
        self.path = path+"/"+self.patient_id+"/"+"dualTask"
        self.setup_ui()

        

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.is_playing = False
        self.btn_vidplay_img = tk.PhotoImage(file = "./resources/img/btn_play.png")
        self.btn_vidplay_img = self.btn_vidplay_img.subsample(3, 3)
        self.btn_vidpause_img = tk.PhotoImage(file = "./resources/img/btn_pause.png")
        self.btn_vidpause_img = self.btn_vidpause_img.subsample(3, 3)
        self.create_sidebar()

    def create_sidebar(self):
        global loadimage, homeimage, volverimage, volverATaskimage, botonSC, botonSM, imageAudio
        sidebar_color = "#77CCC1"
        sidebar_list_color = "#C4F1EB" 
        sidebar_blank_color = "#E5F5F3"


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

        for _ in range(7):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_button = tk.Button(canvas, image=loadimage, bg=sidebar_color, bd=0, command=self.logout)
        rounded_button.pack(side="top", pady=10)
        
        sidebar_blank = tk.Frame(self.root, bg=sidebar_blank_color, width=20)
        sidebar_blank.pack(fill="y", side="left")

        sidebar_list = tk.Frame(self.root, bg="#E5F5F3", width=700)
        sidebar_list.pack(fill="both", side="left", expand=True)

        sidebar_list_title = tk.Frame(sidebar_list, bg=sidebar_list_color)
        sidebar_list_title.pack(fill="x")


        self.audio_frame = tk.Frame(sidebar_list, bg="#E5F5F3")
        self.audio_frame.pack(fill="both", side="top")


        button_frame = tk.Frame(self.audio_frame, bg="#E5F5F3")
        button_frame.pack(side="top", pady=10)

        imageAudio = Image.open("./resources/img/audio.png")
        imageAudio = ImageTk.PhotoImage(imageAudio)
        image_label = tk.Label(button_frame, image=imageAudio, bg="#E5F5F3")
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.playvid_btn = tk.Button(button_frame, image=self.btn_vidplay_img, bg="#E5F5F3", borderwidth=0, highlightthickness=0, command=self.play_audio, relief="flat")
        self.playvid_btn.grid(row=1, column=0, padx=10, pady=5)  # Add pady here

        pausevid_btn = tk.Button(button_frame, image=self.btn_vidpause_img, borderwidth=0, bg="#E5F5F3", highlightthickness=0, command=self.stop_audio, relief="flat")
        pausevid_btn.grid(row=1, column=1, padx=10, pady=5)  # Add pady here

        self.status_label = tk.Label(button_frame, text="Audio detenido",  bg="#E5F5F3",  font=("Helvetica", 14, "bold"))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

        if self.buttonsA=="BFluenciaV":
            title_label = tk.Label(
                sidebar_list_title,
                text="Fluencia Verbal",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
            self.path = self.path + "/" +"Cogni_DUAL.mp3"

        elif self.buttonsA=="BAritmetica":
            title_label = tk.Label(
                sidebar_list_title,
                text="Aritmetica",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)

            self.path = self.path + "/" +"DUAL.mp3" 
        
        

 

    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        self.master.mostrar_pagina("ViewPatients")
        

    def atras(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonDual",self.patient_id,"ButtonDual","BSimplesCog", self.pathAux)

    def vieTask(self):
        self.master.mostrar_pagina("ViewTask")
    

    def play_audio(self):
        
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        self.is_playing = True
        self.update_label()

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.update_label()

    def update_label(self):
        if self.is_playing:
            self.status_label.config(text="Reproduciendo audio...")
        else:
            self.status_label.config(text="Audio detenido")

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    app.mainloop()
        