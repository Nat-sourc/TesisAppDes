import tkinter as tk
from tkinter import PhotoImage
from pathlib import Path

class Start(tk.Frame):
    def __init__(self, master=None, root=None):
        super().__init__(master)
        self.master = master
        self.pack()

        CREDS_PATH = Path(__file__).parent / Path("../resources/serviceAccountKey.json")
        self.master.configure(background="#D4ECE5")  # Agregar esta línea
        # Cargar la imagen
        self.image = PhotoImage(file="../resources/img/hospital.png")

        # Crear un Frame para contener la imagen y el título
        self.frame = tk.Frame(root, bg="#D4ECE5")  # Cambia el color de fondo del marco aquí
        self.frame.pack()

        # Agregar un espacio antes de la imagen
        self.space_label = tk.Label(self.frame, text="     ", bg="#D4ECE5")
        self.space_label.pack(side=tk.LEFT)

        # Ajustar el tamaño de la imagen al tamaño del título
        self.image = self.image.subsample(15, 15)  # Cambia los valores para ajustar el tamaño

        # Colocar la imagen en el Frame
        self.image_label = tk.Label(self.frame, image=self.image, bg="#D4ECE5")
        self.image_label.pack(side=tk.LEFT)

        # Crear un Label para el título en el mismo Frame
        self.title_label = tk.Label(
            self.frame,
            text="BRAINFIT",
            font=("RobotoMono-Bold", 20),
            fg="#00BFA6",
            bg="#D4ECE5"
        )
        self.title_label.pack(side=tk.LEFT, padx=10)  # Agregar espacio entre la imagen y el título

        # Agregar múltiples saltos de línea antes de la imagen de doctors
        for _ in range(3):
            tk.Label(root, text="", bg="#D4ECE5").pack()

        self.imageMedicos = PhotoImage(file="../resources/img/doctors.png")

        # Ajustar el tamaño de la imagen de doctors
        self.imageMedicos = self.imageMedicos.subsample(2, 2) # Cambia los valores para ajustar el tamaño

        # Crear un Label para la imagen y configurarla en el centro
        self.image_label = tk.Label(root, image=self.imageMedicos, bg="#D4ECE5")
        self.image_label.pack()

        # Agregar espacio entre la imagen de doctors y el botón
        tk.Label(root, text="", bg="#D4ECE5").pack()

        self.loadimage = tk.PhotoImage(file="../resources/img/button_comencemos.png")
        self.loadimage = self.loadimage.subsample(4, 4) 
        # Create a Canvas widget
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        # Create a rounded button with the loaded image
        self.rounded_button = tk.Button(self.canvas, image=self.loadimage, bg="#D4ECE5", bd=0, command=self.ir_a_view_patients)
        self.rounded_button.pack(side="top")


    def ir_a_view_patients(self):
        self.master.mostrar_pagina("ViewPatients")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("BrainFit")
    root.geometry("1340x768")
    root.configure(background="#D4ECE5")  # Cambia el color de fondo aquí
    start_page = Start(root=root)
    root.mainloop()