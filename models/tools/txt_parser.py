# [lector_txt.py]
import tkinter as tk
from tkinter import filedialog
import os
import datetime
from models.tools.file_selector import File_selector


def leer_archivo_txt():
    nombre_archivo = File_selector.select("data/tests")
    if nombre_archivo:
        try:
            with open(nombre_archivo, "r") as archivo:
                n = int(archivo.readline().strip())

                datos = []
                for _ in range(n):
                    linea = archivo.readline().strip()
                    valores = tuple([int(x) for x in linea.split(",")])
                    datos.append(valores)
                return datos

        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encontró.")
            return None
    else:
        print("No se seleccionó ningún archivo.")
        return None


def exportar_programacion_txt(programacion):
    """
    Genera un archivo .txt formateado con una programacion dada

    Args:
        programacion [(int, int,... int), int]: La programación  de riego con su costo

    Returns:
        ruta_archivo (str): La ruta al archivo si todo funcionó
        None si la ruta del archivo no es válida
    """
    root = tk.Tk()
    root.withdraw()

    ruta_archivo = filedialog.asksaveasfilename(
        parent=root,
        initialdir="./data/results/",
        title="Guardar archivo como",
        defaultextension=".txt",
        filetypes=(("Archivos de texto", "*.txt"),
                   ("Todos los archivos", "*.*"))
    )

    if not (ruta_archivo):
        return None

    with open(ruta_archivo, 'w') as archivo:
        valor = programacion[1]
        archivo.write(str(valor) + '\n')
        for elemento in programacion[0]:
            archivo.write(str(elemento) + '\n')

    root.destroy()
    return ruta_archivo


if __name__ == '__main__':
    # Ejemplo de uso
    datos_leidos = leer_archivo_txt()
    if datos_leidos:
        print("Datos leídos del archivo:")
        print(datos_leidos)
