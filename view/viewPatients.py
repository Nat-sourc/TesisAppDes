import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from connectToFirebase import connect
from firebase_admin import credentials, firestore
from tkinter import Scrollbar
import datetime
from tkinter import Radiobutton



class ViewPatients:
    def __init__(self,master=None, root=None):
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
        sidebar_blank_color = "white"
        sidebar_calendar_color = "#C6F4EE"
        sidebar_list_color = "#C4F1EB" 

        sidebar = tk.Frame(self.root, bg=sidebar_color, width=150)
        sidebar.pack(fill="y", side="left")

        sidebar_blank = tk.Frame(self.root, bg=sidebar_blank_color, width=20)
        sidebar_blank.pack(fill="y", side="left")

        sidebar_calendar = tk.Frame(self.root, bg=sidebar_calendar_color, width=200)
        sidebar_calendar.pack(fill="both", side="left", expand=True)

        sidebar_blank2 = tk.Frame(self.root, bg=sidebar_blank_color, width=20)
        sidebar_blank2.pack(fill="y", side="left")

        sidebar_list = tk.Frame(self.root, bg="white", width=500)
        sidebar_list.pack(fill="both", side="left", expand=True)

        sidebar_list_title = tk.Frame(sidebar_list, bg=sidebar_list_color)
        sidebar_list_title.pack(fill="x")

        # Crear el borde blanco ancho alrededor de sidebar_listb
        sidebar_listb = tk.Frame(sidebar_list, bg="white", highlightbackground="white", highlightthickness=10)
        sidebar_listb.pack(fill="both", side="left", expand=True)

        # Crear el segundo sidebar más pequeño dentro del sidebar_listb
        sidebar_list2 = tk.Frame(sidebar_listb, bg="#C4F1EB", width=150)  # Cambiar el color y el ancho según tu preferencia
        sidebar_list2.pack(fill="both", side="left", expand=True)

        loadimage = Image.open("./resources/img/logout.png")
        loadimage = tk.PhotoImage(file="./resources/img/logout.png")
        loadimage = loadimage.subsample(3, 3) 

        # Create a Canvas widget
        canvas = tk.Canvas(sidebar, bg=sidebar_color, highlightthickness=0)
        canvas.pack(side="bottom", pady=(0,10))

        rounded_button = tk.Button(canvas, image=loadimage, bg=sidebar_color, bd=0, command=self.logout)
        rounded_button.pack(side="bottom", pady=10)
        
        # Crear un estilo personalizado para el Frame redondeado
        style = ttk.Style()
        style.configure("Red.TFrame", background="white", relief="solid", borderwidth=2)
        style.layout("Red.TFrame", [('Frame.border', {'sticky': 'nsew',  'children':
            [('Frame.padding', {'expand': '1', 'sticky': 'nsew', 'children':
                [('Label', {'sticky': 'nswe'})],
            })]
        })])
    
        patient_id_label_frame = ttk.Frame(
            sidebar_calendar,
            style="Red.TFrame",
        )
        patient_id_label_frame.pack(anchor="w", padx=20, pady=20)
        
        lupa_img = Image.open("./resources/img/lupa.png")
        lupa_img = tk.PhotoImage(file="./resources/img/lupa.png")
        lupa_img = lupa_img .subsample(4, 4) 

        # Crear un Frame para contener la imagen y el texto
        lupa_and_id_frame = ttk.Frame(patient_id_label_frame, style="Red.TFrame")
        lupa_and_id_frame.pack(fill="x", padx=5, pady=5)

        # Colocar la imagen en el Frame
        lupa_label = tk.Label(lupa_and_id_frame, image=lupa_img, bg="white")
        lupa_label.pack(side="left", padx=5)

        # Crear el Label del ID del paciente dentro del Frame
        patient_id_label = tk.Label(
            lupa_and_id_frame,
            text="ID del paciente:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#00BFA6"
        )
        patient_id_label.pack(side="left", padx=10, pady=10)

        patient_id_entry = ttk.Entry(sidebar_calendar)
        patient_id_entry.pack(fill="x", padx=30, pady=(0, 20))


        ####
        patient_id_label_frame2 = ttk.Frame(
            sidebar_calendar,
            style="Red.TFrame",
        )
        patient_id_label_frame2.pack(anchor="w", padx=20, pady=20)

        date_img = Image.open("./resources/img/calender.png")
        date_img = tk.PhotoImage(file="./resources/img/calender.png")
        date_img = date_img .subsample(4, 4) 

        # Crear un Frame para contener la imagen y el texto
        date_and_frame = ttk.Frame(patient_id_label_frame2, style="Red.TFrame")
        date_and_frame.pack(fill="x", padx=5, pady=5)

        date_label = tk.Label(date_and_frame, image=date_img, bg="white")
        date_label.pack(side="left", padx=5)

        # Crear el Label del ID del paciente dentro del Frame
        patient_id_label_fecha = tk.Label(
            date_and_frame,
            text="Fecha:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#00BFA6"
        )
        patient_id_label_fecha.pack(side="left", padx=10, pady=10)



        cal = Calendar(sidebar_calendar,
                    background=sidebar_color,
                    foreground='#333333',  # Color de fuente de los días
                    headersbackground='#77CCC1',  # Color de fondo de los encabezados
                    headersforeground='white',  # Color de fuente de los encabezados
                    selectbackground='#77CCC1',  # Color de fondo de la selección
                    selectforeground='white',  # Color de fuente de la selección
                    weekendbackground='white',  # Color de fondo de los fines de semana
                    weekendforeground='#333333',  # Color de fuente de los fines de semana
                    othermonthbackground='#F0F0F0',  # Color de fondo de otros meses
                    othermonthforeground='#666666',  # Color de fuente de otros meses
                    )
        cal.pack(padx=20, pady=(0, 20))

        search_button = ttk.Button(sidebar_calendar,
                                text="Buscar",
                                command=lambda: self.perform_search(sidebar_list2, patient_id_entry,cal, sidebar_calendar),
                                style="Search.TButton",
                                width=20,  # Ajusta el ancho del botón
                                )
        search_button.pack(pady=(10, 20))

        patients_list_label = tk.Label(
            sidebar_list_title,
            text="LISTA DE PACIENTES",
            font=("Arial", 14, "bold"),
            bg=sidebar_list_color,
            fg="#00BFA6"
        )
        patients_list_label.pack(padx=10, pady=10)

        # Establecer el color de texto de los elementos en el sidebar_list
        style = ttk.Style()
        style.configure("TLabel", foreground="#333333")
        
        try:
            db = firestore.client()
            patients_ref = db.collection('pacientes')
            patients = patients_ref.stream()

            for idx, patient in enumerate(patients):
                patient_data = patient.to_dict()
                patient_frame = tk.Frame(sidebar_list2, bg="white")
                patient_frame.pack(fill="x", padx=10, pady=5)

                select_patient_radiobutton = Radiobutton(
                    patient_frame,
                    value=patient_data['id'],
                    bg="white",
                    command=lambda patient_id=patient_data['id']: self.select_patient(patient_id)
                )
                select_patient_radiobutton.pack(side="left", padx=5, pady=2)

                patient_id_label = tk.Label(
                    patient_frame,
                    text=f"{patient_data['id']}",
                    font=("Arial", 15),
                    bg="white",
                    fg="#00BFA6"
                )
                patient_id_label.pack(fill="x", padx=10, pady=2, anchor="w")

                patient_genero_label = tk.Label(
                    patient_frame,
                    text=f"Género: {patient_data['genero']}",
                    font=("Arial", 12),
                    bg="white",
                    fg="#333333"
                )
                patient_genero_label.pack(fill="x", padx=10, pady=2, anchor="w")

                patient_fecha_label = tk.Label(
                    patient_frame,
                    text=f"Fecha: {patient_data['fechaCreacion'].strftime('%d-%m-%Y')}",
                    font=("Arial", 12),
                    bg="white",
                    fg="#333333"
                )
                patient_fecha_label.pack(fill="x", padx=10, pady=2, anchor="w")




        except Exception as e:
            print("Firebase Error:", e)

        style = ttk.Style()
        style.configure("Search.TButton", background="#77CCC1")
        style.configure("Load.TButton",
                        background="#87E1D5")

        self.load_button = ttk.Button(sidebar_calendar,
                                      text="Cargar",
                                      command=self.load_patient_data,
                                      style="Load.TButton",
                                      state=tk.DISABLED)
        self.load_button.pack( pady=5)

    def select_patient(self, patient_id):
        self.selected_patient_id = patient_id  # Store the selected patient ID
        print("Selected patient:", patient_id)
        self.load_button.config(state=tk.NORMAL)  # Enable the Load button


    def load_patient_data(self):
        if self.selected_patient_id:
            # You can use self.selected_patient_id to fetch and display the selected patient's data
            print("Loading patient data for:", self.selected_patient_id)
        else:
            print("No patient selected")


    def logout(self):
        self.master.mostrar_pagina("Start")

    def perform_search(self,sidebar_list2,patient_id_entry,cal,sidebar_calendar):
        # Clear previous search results
        for widget in sidebar_list2.winfo_children():
            widget.destroy()

        search_id = patient_id_entry.get()
        selected_date_str = cal.get_date()  # Get the selected date as a string

        try:
            db = firestore.client()
            patients_ref = db.collection('pacientes')

            if search_id:
                query = patients_ref.where('id', '==', search_id)
            elif selected_date_str:
                selected_date = datetime.datetime.strptime(selected_date_str, '%m/%d/%y').date()
                selected_start = datetime.datetime.combine(selected_date, datetime.datetime.min.time())
                selected_end = selected_start + datetime.timedelta(days=1)
                query = patients_ref.where('fechaCreacion', '>=', selected_start).where('fechaCreacion', '<', selected_end)
            else:
                query = patients_ref

            patients = query.stream()

            for idx, patient in enumerate(patients):
                patient_data = patient.to_dict()
                patient_frame = tk.Frame(sidebar_list2, bg="white")
                patient_frame.pack(fill="x", padx=10, pady=5)

                select_patient_radiobutton = Radiobutton(
                    patient_frame,
                    bg="white",
                    value=patient_data['id'],
                    command=lambda patient_id=patient_data['id']: self.select_patient(patient_id)
                )
                select_patient_radiobutton.pack(side="left", padx=5, pady=2)
                patient_id_label = tk.Label(
                    patient_frame,
                    text=f"{patient_data['id']}",
                    font=("Arial", 15),
                    bg="white",
                    fg="#00BFA6"
                )
                patient_id_label.pack(fill="x", padx=10, pady=2, anchor="w")
                patient_genero_label = tk.Label(
                    patient_frame,
                    text=f"Género: {patient_data['genero']}",
                    font=("Arial", 12),  # Cambiar el tamaño de fuente según tu preferencia
                    bg="white",
                    fg="#333333"
                )
                patient_genero_label.pack(fill="x", padx=10, pady=2, anchor="w")  # Alinear a la izquierda
                patient_genero_label = tk.Label(
                    patient_frame,
                    text=f"Fecha: {patient_data['fechaCreacion'].strftime('%d-%m-%Y')}",
                    font=("Arial", 12),  # Cambiar el tamaño de fuente según tu preferencia
                    bg="white",
                    fg="#333333"
                )
                patient_genero_label.pack(fill="x", padx=10, pady=2, anchor="w")  # Alinear a la izquierda

        except Exception as e:
            print("Firebase Error:", e)

        
        


if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1340x768")
    app.configure(background="#D4ECE5")
    app.wm_title("BrainFit")

    style = ttk.Style()
    style.configure("Search.TButton", background="#77CCC1")

    # Configure the style for the Load button
    style.configure("Load.TButton", background="#87E1D5", foreground="white")

    
    my_app = ViewPatients(root=app)
    app.mainloop()
