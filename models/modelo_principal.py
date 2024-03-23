from models.exhaustivo import roFB
from models.voraz import roV


class modelo_principal:
    def __init__(self):
        self.finca = None
        self.algoritmo = None

    def set_finca(self, finca):
        """
        Asigna la finca a la que se le va a aplicar el algoritmo

        Args:
            algoritmo (str): El tipo de algoritmo ('exhaustivo', 'dinamico', 'voraz')

        Returns:
            None
        """
        self.finca = finca
        print(
            f"modelo_principal.py: Finca se ha cambiado a {self.finca}")

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
            None
        """
        self.algoritmo = algoritmo
        print(
            f"modelo_principal.py: El algoritmo a usar se ha cambiado a {self.algoritmo}")

    def iniciar(self):
        if self.finca == None:
            print("modelo_principal.py: Error: No se ha cargado ninguna finca")
            return None

        if self.algoritmo == 'exhaustivo':
            return roFB(self.finca)
        elif self.algoritmo == 'dinamico':
            print("modelo_principal.py:  Este algoritmo esta en proceso de creacion")
            return None
        elif self.algoritmo == 'voraz':
            return roV(self.finca)
        else:
            print(
                f"modelo_principal.py:  Error: El algoritmo {str(self.algoritmo)} no es valido")
            return None
