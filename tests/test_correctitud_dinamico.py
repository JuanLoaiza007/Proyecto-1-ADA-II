from models.algorithms.datatypes.types import *
from models.tools.txt_parser import leer_archivo_txt
from models.algorithms.dinamico import roPD


class test_correctitud_dinamico:
    def start():
        parsed = leer_archivo_txt()
        finca = parsed[0]
        print("Solucion dinamica: ", roPD(finca))
