# [modelo_principal.py]

from models.tools.txt_parser import exportar_programacion_txt
from models.exhaustivo import roFB
from models.voraz import roV

debug = True


def print_debug(message):
    new_message = "modelo_principal.py: " + message
    if debug:
        print(new_message)


class modelo_principal:
    def __init__(self):
        self.finca = None
        self.algoritmo = None
        self.resultado = None

    def set_finca(self, finca):
        """
        Asigna la finca a la que se le va a aplicar el algoritmo

        Args:
            algoritmo (str): El tipo de algoritmo ('exhaustivo', 'dinamico', 'voraz')

        Returns:
            None
        """
        self.finca = finca
        self.resultado = None

        print_debug(
            "Finca se ha cambiado a {}".format(str(self.finca)))

    def get_finca(self):
        """
        Retorna la finca

        Args:
            None

        Returns:
            finca ([(), (), ()]): La finca cargada en el modelo
        """
        return self.finca

    def set_algoritmo(self, algoritmo):
        """
        Asigna el tipo de algoritmo que se va a usar

        Args:
            algoritmo (str): El tipo de algoritmo ('exhaustivo', 'dinamico', 'voraz')

        Returns:
            self.resultado [(int, int,... int), int]: La programación  de riego con su costo.
            None si hay alguna inconsistencia
        """
        self.algoritmo = algoritmo
        self.resultado = None

        print_debug("El algoritmo a usar se ha cambiado a {}".format(
            str(self.algoritmo)))

    def iniciar(self):
        if self.finca == None:
            print_debug("Error: No se ha cargado ninguna finca")
            return None

        if self.algoritmo == 'exhaustivo':
            self.resultado = roFB(self.finca)
        elif self.algoritmo == 'dinamico':
            print_debug("Este algoritmo esta en proceso de creacion")
            self.resultado = None
        elif self.algoritmo == 'voraz':
            self.resultado = roV(self.finca)
        else:
            print_debug("Error: El algoritmo {} no es valido".format(
                str(self.algoritmo)))
            return None

        return self.resultado

    def exportar(self):
        if self.resultado != None:
            return exportar_programacion_txt(self.resultado)
