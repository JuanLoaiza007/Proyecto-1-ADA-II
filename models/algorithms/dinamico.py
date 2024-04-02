# [dinamico.py]

from models.algorithms.datatypes.types import *

debug = True


def print_debug(message: str):
    new_message = "{}: {}".format(__file__.split("/")[-1], message)
    if debug:
        print(new_message)


class Ahorro():
    """
    Una clase opcional para contar el ahorro de calculos que se hace usando memorizacion.
    """

    def __init__(self):
        self.ahorro = 0

    def aumentar_ahorro(self):
        self.ahorro += 1

    def get_ahorro(self):
        return self.ahorro


def roPD(f, memoization_active=True):
    """

    Args:
        f (Finca): La finca a la que se le quiere encontrar la programacion óptima
        memoization_active (bool): Por defecto activa la memorización pero se puede establecer en false para debug.

    Returns: 
        list(ProgRiego, int): Una lista con la programacion de riego optima (ProgRiego) y su costo (int).
    """

    def tiempoRiegoFinca(f: Finca):
        """
        Calcula todo el tiempo que tarda regar una finca, este dato sirve también como el t_ini del proximo tablon que se agregue a la finca.

        Args:
            f (Finca): La finca que se desea comprobar

        Returns:
            tiempo (int): El tiempo que tarda en regar la finca.
        """

        tiempo = 0

        for t in f:
            tiempo += treg_t(t)

        return tiempo

    def costoRiegoTablon(t: Tablon, t_ini: int):
        """
        Calcula el costo de regar un tablon dado su tiempo de inicio, usa directamente la propiedad del enunciado.

        Args:
            t (Tablon): El tablón a calcular.
            t_ini (int): Un tiempo de inicio.

        Returns:
            (int): El costo de regar el tablon t.
        """
        costo = 0

        if tsup_t(t) - treg_t(t) >= t_ini:

            costo = tsup_t(t) - (t_ini + treg_t(t))
        else:
            costo = prio_t(t) * ((t_ini + treg_t(t)) - tsup_t(t))

        print_debug("costoRiegoTablon() -> El costo de {} con tini {} es {}".format(
            str(t), str(t_ini), str(costo)))
        return costo

    def costoRiegoFinca(f: Finca):
        """
        Calcula el costo de regar la finca CON EL MISMO ORDEN DE RIEGO EN QUE SE DA LA FINCA.

        Args:
            f (Finca): La finca que se desea calcular.

        Returns: 
            (int): El costo de regar la finca.
        """
        costo = 0
        t_ini = 0

        for t in f:
            costo += costoRiegoTablon(t, t_ini)
            t_ini += treg_t(t)
        return costo

    def minProgCostoT(l_prog_costo):
        """
        Saca la programacionCosto con el valor minimo de una lista de programacionCosto.
        programacionCosto es list(list(tablon), int)

        Args: 
            l_prog_costo (list(programacionCosto)): Una lista de programaciones y sus costos

        Returns:
            prog_opt (programacionCosto): La programacionCosto con el menor costo

        Example: 
        minProgCostoT([[[(1, 2, 3), (4, 5, 6)], 0], [[(4, 5, 6), (1, 2, 3)], 2], [[(1, 2, 3)], -1] ])
        -> [[(1, 2, 3)], -1]
        """
        prog_opt = l_prog_costo[0]
        if len(l_prog_costo) == 1:
            print("Lista tamaño 1")
            return prog_opt

        for prog in l_prog_costo:
            if prog[1] < prog_opt[1]:
                prog_opt = prog
        return prog_opt

    def combinarProgCostoT(pc1, pc2):
        """
        Combina dos programacionCosto, ATENCION: Lea los Args.
        programacionCosto es list(list(tablon), int)

        Args:
            CUIDADO: EL COSTO DE pc2 DEBE HABERSE CALCULADO TENIENDO EN MENTE QUE SE ANEXARIA AL FINAL DE pc1.

            pc1 (programacionCosto): Una programacion de varios tablones con su costo, esta se refiere a los primeros tablones en ser regados.
            pc2 (programacionCosto): Una programacion de un solo tablon con su costo. 

        Returns:
            [prog, costo] (programacionCosto): La programacionCosto resultante de regar el tablon de pc2 despues de los de pc1

        Ejemplo:
        pc1 = [[(1, 2, 3), (4, 5, 6)], 2]
        pc2 = [[(6, 7, 8)], 3]
        sumProgCostoT(pc1, pc2)
        -> [[(1, 2, 3), (4, 5, 6), (6, 7, 8)], 5]
        """
        prog = list(pc1[0])
        prog.append(pc2[0][0])
        costo = pc1[1] + pc2[1]
        return [prog, costo]

    def progCostoOptima(finca: Finca):
        if len(finca) == 1:
            return [finca, costoRiegoFinca(finca)]
        else:
            if tuple(finca) in dic_memoization_sol:
                ahorro.aumentar_ahorro()
                return dic_memoization_sol[tuple(finca)]
            tiempo_total = tiempoRiegoFinca(finca)
            programaciones = []

            for i in range(len(finca)):
                copia_finca = finca[:]
                copia_tablon = copia_finca.pop(i)
                t_ini_local = tiempo_total - treg_t(copia_tablon)

                pc1 = progCostoOptima(copia_finca)
                pc2 = list(([copia_tablon],
                           costoRiegoTablon(copia_tablon, t_ini_local)))

                prog_costo_act = combinarProgCostoT(pc1, pc2)

                programaciones.append(prog_costo_act)

            dic_memoization_sol[tuple(finca)] = minProgCostoT(programaciones)
            return minProgCostoT(programaciones)

    # === Estableciendo algunas variables === #
    dic_tablon_indice = {tupla: indice for indice,
                         tupla in enumerate(f)}  # Indices originales
    dic_memoization_sol = {}  # Para almacenar calculos de la solucion
    ahorro = Ahorro()  # Para comprobar si estamos ahorrando calculos (opcional)

    # === PROCESANDO FINCA === #
    # Aqui se trae directamente la solucion pero la programacion dada por los tablones, no sus indices
    prog_costo_optima = progCostoOptima(f)

    # Separo la programacion de tablones (tuplas) y su costo (int)
    programacion_t = prog_costo_optima[0]
    costo = prog_costo_optima[1]

    # Creo un arreglo de la programacion de tablones pero esta vez los indices
    programacion_i = []
    # Repaso cada tablon y pongo su indice original
    for tablon in programacion_t:
        programacion_i.append(dic_tablon_indice[tablon])

    # === DEBUG === #
    print_debug("\n\nFINCA ORIGINAL:\n\n{}\n".format(str(f)))
    print_debug("COPIA INDICES:\n\n{}\n".format(str(dic_tablon_indice)))
    print_debug("\n\nCALCULO DIRECTO INDEPENDIENTE:\n\nProgramacion: {}\nCosto: {}\n".format(
        str(programacion_t), str(costoRiegoFinca(programacion_t))))
    print_debug("Calculos ahorrados: {}\n".format(str(ahorro.get_ahorro())))

    return [programacion_i, costo]
