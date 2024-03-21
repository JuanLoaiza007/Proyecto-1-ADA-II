from models.exhaustivo import *
from models.voraz import *


class test_correctitud_voraz:
    def start():
        # Ejemplo 1
        finca1 = [(2, 2, 1), (3, 4, 1), (4, 2, 1), (7, 6, 1)]
        finca2 = [(10, 5, 1), (8, 3, 1), (16, 8, 1), (32, 16, 1)]
        finca3 = [(4, 4, 1), (8, 4, 1), (16, 8, 1), (33, 16, 1)]
        finca4 = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (6, 4, 2)]

        # tsup - (t_ini + treg)             ,si tsup - treg >= t_ini
        #   8  - (  5   +   3)              ,si  8   -  3   >=   5

        # Cuando t_ini = tsup-treg costoRiegoTablon = 0clea

        # Cuando

        finca = finca4
        print(roV(finca1))

        # print("Optima es: ", roFB(finca))
        # print("Optima según voraz es: ", roV(finca))
        # print("Finca tiene elementos: ", len(finca))
