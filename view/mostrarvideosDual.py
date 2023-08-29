import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import firestore
from pathlib import Path
import os
import cv2

class MostrarVideosDual:
    def __init__(self, master=None, patient_id=None, pageA=None,buttonsA=None,path=None, root=None):
        self.master = master
        self.root = root
        self.patient_id=patient_id
        self.pageA=pageA
        self.buttonsA=buttonsA
        self.video_label=None
        self.pathAux=path
        self.path = path+"/"+self.patient_id+"/"+"dualTask"
        self.task_names = self.extract_task_names_from_videos()
        self.setup_ui()

        

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.video_cap = None
        self.video_pause = False
        self.btn_vidplay_img = tk.PhotoImage(file = "./resources/img/btn_play.png")
        self.btn_vidplay_img = self.btn_vidplay_img.subsample(3, 3)
        self.btn_vidpause_img = tk.PhotoImage(file = "./resources/img/btn_pause.png")
        self.btn_vidpause_img = self.btn_vidpause_img.subsample(3, 3)
        self.btn_vidfirst_img = tk.PhotoImage(file = "./resources/img/btn_first.png")
        self.btn_vidfirst_img = self.btn_vidfirst_img.subsample(3, 3)
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


        self.video_frame = tk.Frame(sidebar_list, bg="#E5F5F3")
        self.video_frame.pack(fill="both", side="top")

        self.video_label = tk.Label(self.video_frame, bg="#E5F5F3", width=640, height=560)
        self.video_label.pack(side="top", pady=10)

        # Crea un frame para los botones y usa grid para organizarlos
        button_frame = tk.Frame(self.video_frame, bg="#E5F5F3")
        button_frame.pack(side="top", pady=10)

        self.playvid_btn = tk.Button(button_frame, image=self.btn_vidplay_img, borderwidth=0, highlightthickness=0, command=self.vid_play, relief="flat")
        self.playvid_btn.grid(row=0, column=0, padx=10)

        pausevid_btn = tk.Button(button_frame, image=self.btn_vidpause_img, borderwidth=0, highlightthickness=0, command=self.vid_pause, relief="flat")
        pausevid_btn.grid(row=0, column=1, padx=10)

        firstvid_btn = tk.Button(button_frame, image=self.btn_vidfirst_img, borderwidth=0, highlightthickness=0, command=self.vid_first, relief="flat")
        firstvid_btn.grid(row=0, column=2, padx=10)


        if self.buttonsA=="BBrazo":
            title_label = tk.Label(
                sidebar_list_title,
                text="Brazo",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)

            if self.lastname is not None:
                self.path = self.path + "/" +"DUALBrazoREC"
                self.path = self.path + self.lastname + "REC"+ self.lastname
        elif self.buttonsA=="BMarcha":
            title_label = tk.Label(
                sidebar_list_title,
                text="Marcha",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)

            if self.lastname is not None:
                self.path = self.path + "/" +"DUALmarchaREC"
                self.path = self.path + self.lastname + "REC"+ self.lastname 
        elif self.buttonsA=="BBrazoDual":
            title_label = tk.Label(
                sidebar_list_title,
                text="Brazo con Dual",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)

            if self.lastname is not None:
                self.path = self.path + "/" +"DUALdualArmTaskREC"
                self.path = self.path + self.lastname + "REC"+ self.lastname

        elif self.buttonsA=="BMarchaDual":
            title_label = tk.Label(
                sidebar_list_title,
                text="Marcha con Dual",
                font=("Arial", 20, "bold"),
                bg=sidebar_list_color,
                fg="#00BFA6"
            )
            title_label.pack(side="left",padx=10, pady=10)

            if self.lastname is not None:
                self.path = self.path + "/" +"DUALdualMarchaTaskREC"
                self.path = self.path + self.lastname + "REC"+ self.lastname   
        print(self.path)
        self.video_cap = cv2.VideoCapture(self.path)
        self.vid_first_frame()
    

    def extract_task_names_from_videos(self):
        task_names = []
        video_files = os.listdir(self.path)
        for video_filename in video_files:
            if video_filename.endswith(".mp4"):
                print("soybrazo",self.buttonsA)
                task_name = video_filename.split("REC")[0].rstrip("_")  # Splitting by "REC" and removing trailing underscores
                if task_name=="DUALBrazo" and self.buttonsA=="BBrazo":
                    self.lastname = video_filename.split("REC")[1]
                if task_name=="DUALmarcha" and self.buttonsA=="BMarcha":
                    self.lastname = video_filename.split("REC")[1]
                if task_name=="DUALdualArmTask" and self.buttonsA=="BBrazoDual":
                    self.lastname = video_filename.split("REC")[1]
                    print(self.lastname)
                if task_name=="DUALdualMarchaTask" and self.buttonsA=="BMarchaDual":
                    self.lastname = video_filename.split("REC")[1]
                    print(self.lastname)
                print(task_name)
                task_names.append(task_name)
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

    def vid_play(self):
        # Play selected video
        self.video_pause = False
        self.playvid_btn['state'] = tk.DISABLED
        self.vid_reproduce()
    
    def vid_reproduce(self):
    # Reproduce selected video
        if not self.video_pause:
            ret, frame = self.video_cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = ImageTk.PhotoImage(image=Image.fromarray(frame))

                self.video_label.config(image=img)
                self.video_label.image = img
                self.video_label.after(30, self.vid_reproduce)  # Reproducir el siguiente cuadro después de 1 ms
            else:
                # Reiniciar la reproducción al final del video
                self.video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                self.vid_first_frame()
                self.playvid_btn['state'] = tk.NORMAL
        else:
            # Pausar la reproducción
            self.playvid_btn['state'] = tk.NORMAL

    
    def vid_pause(self):
        # Pause selected video
        self.video_pause = True
        self.playvid_btn['state'] = tk.NORMAL

    def vid_first(self):
        # Go back to video first frame
        self.video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def logout(self):
        self.master.mostrar_pagina("Start")

    def home(self):
        self.master.mostrar_pagina("ViewPatients")
        

    def atras(self):
        if self.buttonsA=="BMarcha" or self.buttonsA=="BBrazo":
            self.master.mostrar_paginaConIdAndButtons("ButtonDual",self.patient_id,"ButtonDual","BSimplesMotoras", self.pathAux)
        else:
            self.master.mostrar_paginaConIdAndButtons("ButtonDual",self.patient_id,"ButtonDual","BDual", self.pathAux)

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
        