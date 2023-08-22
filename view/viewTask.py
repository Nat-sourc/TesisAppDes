import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from connectToFirebase import connect


class ViewTask:
    def __init__(self,patient_id,master=None, root=None):
        self.master = master
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.lupa_img = None
        self.date_img = None
        self.loadimage = None
        self.connect_firebase()
        self.create_sidebar()

    def connect_firebase(self):
        connect("./resources/serviceAccountKey.json")

    def create_sidebar(self):
        global loadimage, lupa_img, date_img
        sidebar_color = "#77CCC1"

        sidebar = tk.Frame(self.root, bg=sidebar_color, width=150)
        sidebar.pack(fill="y", side="left")

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