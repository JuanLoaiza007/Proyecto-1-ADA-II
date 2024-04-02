from models.algorithms.datatypes.types import *

debug = False


def print_debug(message: str):
    new_message = "{}: {}".format(__file__.split("/")[-1], message)
    if debug:
        print(new_message)


def roV(f):

    def calcularCostoComoUltimo(finca, ti):
        """
        Calcula el costo de un tablon considerandolo el ultimo

        Args:
            finca ([(),(),()]): La finca con sus tablones.
            ti (int): El indice del tablon en la finca.

        Returns:
            int: El costo de regar el tablon como si fuera el ultimo.
        """
        tablon = finca.pop(ti)
        t_ini = calcularTiempoFinalizacion(finca)
        return costoRiegoTablonTini(tablon, t_ini)

    def calcularTiempoFinalizacion(f):
        """
        Calcula el tiempo de finalizacion de regar una finca

        Args:
            finca ([(),(),()]): La finca con sus tablones.

        Returns:
            int: El tiempo en el que se termina de regar la finca.
        """
        tiempoFinalizacion = 0
        for i in range(0, len(f), 1):
            tiempoFinalizacion += treg(f, i)

        return tiempoFinalizacion

    def costoRiegoTablonTini(tablon, t_ini):
        """
        Calcula el costo de regar un tablon dado el tiempo de inicio

        Args:
            tablon ( (int, int, int) ): Un tablon.
            t_ini (int): El tiempo de inicio en el que se empieza a regar el tablon.

        Returns:
            int: El costo de regar el tablon.
        """
        if tsup_t(tablon) - treg_t(tablon) >= t_ini:
            return tsup_t(tablon) - (t_ini + treg_t(tablon))
        else:
            return prio_t(tablon) * (t_ini + treg_t(tablon) - tsup_t(tablon))

    def costoRiegoTablon(i, f, pi):

        def calcularTiempoInicio(tablon):
            if tablon == pi[0]:
                return 0
            else:
                return calcularTiempoInicio(pi[pi.index(tablon) - 1]) + treg(f, pi[pi.index(tablon) - 1])

        def costoRiego(ti):
            if tsup(f, i) - treg(f, i) >= ti:
                return tsup(f, i) - (ti + treg(f, i))
            else:
                return prio(f, i) * ((ti + treg(f, i)) - tsup(f, i))

        tiemposInicioRiego = [calcularTiempoInicio(ti) for ti in range(len(f))]

        return costoRiego(tiemposInicioRiego[i])

    def costoRiegoFinca(f, pi):

        costos = [costoRiegoTablon(i, f, pi) for i in range(len(f))]

        def sumarElementos(vector):
            if not vector:
                return 0
            else:
                return vector[0] + sumarElementos(vector[1:])

        return sumarElementos(costos)

    tablones = f[:]

    solucionVoraz = []
    last = len(tablones)
    indice_original = {i: i for i in range(len(tablones))}

    for j in range(0, len(tablones), 1):
        solucionVoraz.append(-1)

    for _ in range(len(tablones)-1, -1, -1):
        costos = []

        for j in range(0, len(tablones), 1):
            copia_tablones = tablones[:]
            costos.append(calcularCostoComoUltimo(copia_tablones, j))

        index = 0
        costo_menor = costos[0]

        for j in range(1, len(costos), 1):
            if costo_menor > costos[j]:
                costo_menor = costos[j]
                index = j

        clave_org = None

        for clave, valor in indice_original.items():
            if valor == index:
                solucionVoraz[last-1] = clave
                clave_org = clave

        del indice_original[clave_org]

        for clave, valor in indice_original.items():

            if valor >= index:
                indice_original[clave] -= 1

        last -= 1

        tablones.pop(index)

    return tuple([solucionVoraz, costoRiegoFinca(f, solucionVoraz)])
