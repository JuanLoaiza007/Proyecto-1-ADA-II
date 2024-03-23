from models.exhaustivo import *
from models.voraz import *
from models.tools.txt_parser import leer_archivo_txt


class test_correctitud_voraz:
    def start():
        # Ejemplo 1
        finca1 = [(2, 2, 1), (3, 4, 1), (4, 2, 1), (7, 6, 1)]
        finca2 = [(10, 5, 1), (8, 3, 1), (16, 8, 1), (32, 16, 1)]
        finca3 = [(4, 4, 1), (8, 4, 1), (16, 8, 1), (33, 16, 1)]
        finca4 = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (6, 4, 2)]

        finca = leer_archivo_txt()
        # finca = finca4
        print("Solucion voraz", roV(finca), "\n\n")
        # print("Solucion exhaustiva", roFB(finca))
