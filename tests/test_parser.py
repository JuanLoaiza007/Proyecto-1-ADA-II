from models.exhaustivo import *
from models.tools.lector_txt import leer_archivo_txt

finca = leer_archivo_txt()
print("Optima es: ", roFB(finca))
