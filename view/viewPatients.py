import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta, timezone
from connectToFirebase import connect

loadimage = None
def create_sidebar(app):
    global loadimage
    connect("./resources/serviceAccountKey.json")
    # Configurar el color de fondo de la barra lateral
    sidebar_color = "#77CCC1"
    sidebar_blank_color = "white"
    sidebar_calendar_color = "#C6F4EE"

    # Crear la barra lateral
    sidebar = tk.Frame(app, bg=sidebar_color, width=200)
    sidebar.pack(fill="y", side="left")

    # Crear la barra lateral en blanco
    sidebar_blank = tk.Frame(app, bg=sidebar_blank_color, width=20)
    sidebar_blank.pack(fill="y", side="left")

    # Crear la barra lateral con el calendario
    sidebar_calendar = tk.Frame(app, bg=sidebar_calendar_color, width=200)
    sidebar_calendar.pack(fill="both", side="left", expand=True)

    sidebar_blank2 = tk.Frame(app, bg=sidebar_blank_color, width=20)
    sidebar_blank2.pack(fill="y", side="left")

    sidebar_list = tk.Frame(app, bg=sidebar_calendar_color, width=800)
    sidebar_list.pack(fill="both", side="left", expand=True)

    loadimage = tk.PhotoImage(file="./resources/img/logout.png")
    loadimage = loadimage.subsample(5, 5) 
    # Create a Canvas widget
    canvas = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
    canvas.pack()

    # Create a rounded button with the loaded image
    rounded_button = tk.Button(canvas, image=loadimage, bg=sidebar_color, bd=0, command=logout)
    canvas.create_window(100, 30, window=rounded_button)

def logout():
    pass

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")
    create_sidebar(app)
    app.mainloop()
