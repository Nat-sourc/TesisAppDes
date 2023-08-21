import tkinter as tk
from tkinter import PhotoImage

from pathlib import Path

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from viewPatients import create_sidebar

def navegabilidad():
    root = tk.Tk()
    root.title("Inicio")
    root.geometry("1340x768")

    # Llamar a la función para crear la barra lateral
    create_sidebar(root)



CREDS_PATH = Path(__file__).parent / Path("../resources/serviceAccountKey.json")


app = tk.Tk()
app.geometry("1340x768")
app.configure(background="#D4ECE5")  # Cambia el color de fondo aquí
app.wm_title("BrainFit")


# Cargar la imagen
image = PhotoImage(file="./resources/img/hospital.png")

# Crear un Frame para contener la imagen y el título
frame = tk.Frame(app, bg="#D4ECE5")  # Cambia el color de fondo del marco aquí
frame.pack()

# Agregar un espacio antes de la imagen
space_label = tk.Label(frame, text="     ", bg="#D4ECE5")
space_label.pack(side=tk.LEFT)

# Ajustar el tamaño de la imagen al tamaño del título
image = image.subsample(15, 15)  # Cambia los valores para ajustar el tamaño

# Colocar la imagen en el Frame
image_label = tk.Label(frame, image=image, bg="#D4ECE5")
image_label.pack(side=tk.LEFT)

# Crear un Label para el título en el mismo Frame
title_label = tk.Label(
    frame,
    text="BRAINFIT",
    font=("RobotoMono-Bold", 20),
    fg="#00BFA6",
    bg="#D4ECE5"
)
title_label.pack(side=tk.LEFT, padx=10)  # Agregar espacio entre la imagen y el título

# Agregar múltiples saltos de línea antes de la imagen de doctors
for _ in range(3):
    tk.Label(app, text="", bg="#D4ECE5").pack()

imageMedicos = PhotoImage(file="./resources/img/doctors.png")

# Ajustar el tamaño de la imagen de doctors
imageMedicos = imageMedicos.subsample(2, 2) # Cambia los valores para ajustar el tamaño

# Crear un Label para la imagen y configurarla en el centro
image_label = tk.Label(app, image=imageMedicos, bg="#D4ECE5")
image_label.pack()

# Agregar espacio entre la imagen de doctors y el botón
tk.Label(app, text="", bg="#D4ECE5").pack()

loadimage = tk.PhotoImage(file="./resources/img/button_comencemos.png")
loadimage = loadimage.subsample(4, 4) 
# Create a Canvas widget
canvas = tk.Canvas(app)
canvas.pack()

# Create a rounded button with the loaded image
rounded_button = tk.Button(canvas, image=loadimage, bg="#D4ECE5", bd=0, command=navegabilidad)

rounded_button.pack(side="top")

app.mainloop()
