import os
from tkinter import messagebox
from zipfile import ZipFile
import tkinter as tk


def download_test(selected_folder, selected_patient_id, bucket):
    # Obtener la carpeta de descarga seleccionada
    folder_var = tk.StringVar(value="Carpeta no seleccionada")
    folder_var.set(selected_folder)
    download_folder = folder_var.get()
    pID = selected_patient_id
    
    # Verificar si se ha seleccionado una carpeta válida
    if download_folder == "Carpeta no seleccionada" or download_folder == "":
        messagebox.showinfo(message="Debe seleccionar una carpeta de descarga.", title="Seleccionar Carpeta")
        return
    
    # Construir la ruta completa de la carpeta de destino para el archivo ZIP
    folder_pathD = pID
    
    # Verificar si la carpeta del paciente ya existe, si no, crearla
    if not os.path.isdir(os.path.join(download_folder, pID)):
        os.mkdir(os.path.join(download_folder, pID))

    # Ruta en Firebase Storage
    firebase_path = pID
    
    # Descargar y procesar el archivo ZIP de dualTask
    dual_task_blob = bucket.blob(firebase_path + '/dualTask.zip')
    dual_task_zip_file_path = os.path.join(download_folder, folder_pathD, "dualTask.zip")
    dual_task_blob.download_to_filename(dual_task_zip_file_path)

    with ZipFile(dual_task_zip_file_path, 'r') as f:
        f.extractall(os.path.join(download_folder, folder_pathD, "dualTask"))

    os.remove(dual_task_zip_file_path)

    # Descargar y procesar el archivo ZIP de bradicinesia
    bradicinesia_blob = bucket.blob(firebase_path + '/bradicinesia.zip')
    bradicinesia_zip_file_path = os.path.join(download_folder, folder_pathD, "bradicinesia.zip")
    bradicinesia_blob.download_to_filename(bradicinesia_zip_file_path)

    with ZipFile(bradicinesia_zip_file_path, 'r') as f:
        f.extractall(os.path.join(download_folder, folder_pathD, "bradicinesia"))

    os.remove(bradicinesia_zip_file_path)
