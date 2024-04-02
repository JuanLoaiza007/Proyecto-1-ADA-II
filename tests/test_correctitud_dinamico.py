from models.dinamico import *
from models.tools.txt_parser import leer_archivo_txt


class test_correctitud_dinamico:
    def start():
        parsed = leer_archivo_txt()
        finca = parsed[0]
        print("Solucion dinamica", roPD(finca), "\n\n")
