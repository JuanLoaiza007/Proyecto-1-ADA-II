from models.exhaustivo import *
from models.tools.txt_parser import leer_archivo_txt


class test_correctitud:
    def start():
        parsed = leer_archivo_txt()
        finca = parsed[0]
        print("Optima es: ", roFB(finca))
