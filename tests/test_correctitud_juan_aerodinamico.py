from models.types import *
from models.tools.txt_parser import leer_archivo_txt
from models.juan_aerodinamico import roPD


class test_correctitud_juan_aerodinamico:
    def start():
        parsed = leer_archivo_txt()
        finca = parsed[0]
        print("Solucion dinamica", roPD(finca), "\n\n")
