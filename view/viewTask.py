import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from connectToFirebase import connect


class ViewTask:
    def __init__(self,master=None, patient_id=None,root=None):
        self.master = master
        self.root = root
        self.setup_ui()
        print(patient_id)

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.create_sidebar()

    def create_sidebar(self):
        global loadimage, lupa_img, date_img
        sidebar_color = "#77CCC1"

        sidebar = tk.Frame(self.root, bg=sidebar_color, width=150)
        sidebar.pack(fill="y", side="left")

        loadimage = Image.open("./resources/img/logout.png")
        loadimage = tk.PhotoImage(file="./resources/img/logout.png")
        loadimage = loadimage.subsample(3, 3) 

        # Create a Canvas widget
        canvas = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvas.pack(side="bottom", pady=(0,10))

        rounded_button = tk.Button(canvas, image=loadimage, bg=sidebar_color, bd=0, command=self.logout)
        rounded_button.pack(side="bottom", pady=10)

    def logout(self):
        self.master.mostrar_pagina("Start")

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