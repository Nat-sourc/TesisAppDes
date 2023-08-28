import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore
from pathlib import Path
import os
import cv2

class MostrarVideos:
    def __init__(self, master=None, patient_id=None, pageA=None,buttonsA=None,path=None, root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.buttonsA=buttonsA
        self.video_label=None
        self.path = path+"/"+self.patient_id+"/"+"bradicinesia"
        self.task_names = self.extract_task_names_from_videos()
        self.setup_ui()
        print("soy path" , self.path)

        self.btn_vidplay_img = tk.PhotoImage(file = "../resources/img/btn_play.png")

        self.btn_vidpause_img = tk.PhotoImage(file = "../resources/img/btn_pause.png")

        self.btn_vidfirst_img = tk.PhotoImage(file = "../resources/img/btn_first.png")

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.video_cap = None
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

        homeimage = Image.open("../resources/img/home.png")
        homeimage = tk.PhotoImage(file="../resources/img/home.png")
        homeimage = homeimage.subsample(8, 8)

        canvashome = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvashome.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing
        

        rounded_buttonhome = tk.Button(canvashome, image=homeimage, bg=sidebar_color, bd=0, command=self.home)
        rounded_buttonhome.pack(side="top", pady=10)

        volverATaskimage = Image.open("../resources/img/volverATask.png")
        volverATaskimage = tk.PhotoImage(file="../resources/img/volverATask.png")
        volverATaskimage = volverATaskimage.subsample(8, 8)

        canvasvolverATask = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvasvolverATask.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_buttonVolverATask = tk.Button(canvasvolverATask, image=volverATaskimage, bg=sidebar_color, bd=0, command=self.vieTask)
        rounded_buttonVolverATask.pack(side="top", pady=10)

        volverimage = Image.open("../resources/img/atras.png")
        volverimage = tk.PhotoImage(file="../resources/img/atras.png")
        volverimage = volverimage.subsample(8, 8)

        canvasvolver = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvasvolver.pack(side="top", pady=(0, 10))

        for _ in range(3):
            tk.Label(sidebar, text="", bg=sidebar_color).pack()  # Add spacing

        rounded_buttonVolver = tk.Button(canvasvolver, image=volverimage, bg=sidebar_color, bd=0, command=self.atras)
        rounded_buttonVolver.pack(side="top", pady=10)

        loadimage = Image.open("../resources/img/logout.png")
        loadimage = tk.PhotoImage(file="../resources/img/logout.png")
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

        self.video_frame = tk.Frame(self.root, bg="#C4C4C4")
        self.video_frame.pack(fill="both", side="left", expand=True)

        self.video_label = tk.Label(self.video_frame, bg="#C4C4C4")
        self.video_label.pack(side="top", pady=10)


        if self.buttonsA=="BToqueMD":
            title_label = tk.Label(
                sidebar_list_title,
                text="TOQUE DE DEDOS MANO DERECHA",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)
            self.path = self.path + "/" + self.find_video("fingertapDerecha")
            video_path = self.path + '.mp4'
            self.video_cap = cv2.VideoCapture(video_path)
            self.vid_first_frame()
        

    def extract_task_names_from_videos(self):
        task_names = []
        video_files = os.listdir(self.path)
        for video_filename in video_files:
            if video_filename.endswith(".mp4"):
                task_name = video_filename.split("REC")[0].rstrip("_")  # Splitting by "REC" and removing trailing underscores
                task_names.append(task_name)
                print(task_name)
        return task_names
    
    def find_video(self, name):
        for task_name in self.task_names:
            if name in task_name:
                return task_name
        return task_name
    
    def vid_first_frame(self):
        # Show first frame of selected video
        ret, frame = self.video_cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.video_label.config(image=img)
            self.video_label.image = img
        else:
            print("Video capture failed.")

    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        self.master.mostrar_pagina("ViewPatients")
        

    def atras(self):
        self.master.mostrar_paginaConIdAndButtons("ButtonsDualBrad",self.patient_id,"ButtonsDualBrad","BBrad", self.path)

    def vieTask(self):
        self.master.mostrar_pagina("ViewTask")
    

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    app.mainloop()
        