from models.algorithms.voraz import *
from models.tools.txt_parser import leer_archivo_txt


class test_correctitud_voraz:
    def start():
        parsed = leer_archivo_txt()
        finca = parsed[0]
        print("Solucion voraz: ", roV(finca))
