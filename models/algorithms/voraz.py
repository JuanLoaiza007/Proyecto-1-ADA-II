from models.algorithms.datatypes.types import *

debug = False


def print_debug(message: str):
    new_message = "{}: {}".format(__file__.split("/")[-1], message)
    if debug:
        print(new_message)


def roV(f):

    def calcularCostoComoUltimo(finca, ti):  # O(n)
        """
        Calcula el costo de un tablon considerandolo el ultimo

        Args:
            finca ([(),(),()]): La finca con sus tablones.
            ti (int): El indice del tablon en la finca.

        Returns:
            int: El costo de regar el tablon como si fuera el ultimo.
        """
        tablon = finca.pop(ti)  # O(1)
        t_ini = calcularTiempoFinalizacion(finca)  # O(n)
        return costoRiegoTablonTini(tablon, t_ini)  # O(1)

    def calcularTiempoFinalizacion(f):  # O(n)
        """
        Calcula el tiempo de finalizacion de regar una finca

        Args:
            finca ([(),(),()]): La finca con sus tablones.

        Returns:
            int: El tiempo en el que se termina de regar la finca.
        """
        tiempoFinalizacion = 0
        for i in range(0, len(f), 1):  # O(n)
            tiempoFinalizacion += treg(f, i)

        return tiempoFinalizacion

    def costoRiegoTablonTini(tablon, t_ini):  # O(1)
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

    def costoRiegoTablon(i, f, pi):  # O (n²)

        def calcularTiempoInicio(tablon):  # O(n)
            if tablon == pi[0]:
                return 0
            else:
                # O (n)
                return calcularTiempoInicio(pi[pi.index(tablon) - 1]) + treg(f, pi[pi.index(tablon) - 1])

        def costoRiego(ti):  # O(1)
            if tsup(f, i) - treg(f, i) >= ti:
                return tsup(f, i) - (ti + treg(f, i))
            else:
                return prio(f, i) * ((ti + treg(f, i)) - tsup(f, i))

        tiemposInicioRiego = [calcularTiempoInicio(ti) for ti in range(len(f))]

        return costoRiego(tiemposInicioRiego[i])

    def costoRiegoFinca(f, pi):  # O (n³)

        costos = [costoRiegoTablon(i, f, pi)
                  for i in range(len(f))]  # O(n* O(n²)) = O(n³)

        def sumarElementos(vector):  # O(n)
            if not vector:
                return 0
            else:
                return vector[0] + sumarElementos(vector[1:])

        return sumarElementos(costos)

    tablones = f[:]  # O(n)

    solucionVoraz = []
    last = len(tablones)
    indice_original = {i: i for i in range(len(tablones))}  # O(n)

    for j in range(0, len(tablones), 1):  # O(n)
        solucionVoraz.append(-1)

    for _ in range(len(tablones)-1, -1, -1):  # O(n²)
        costos = []

        for j in range(0, len(tablones), 1):  # O(n * O(n)) = O(n²)
            copia_tablones = tablones[:]
            costos.append(calcularCostoComoUltimo(
                copia_tablones, j))  # O(n * O(n)) = O(n²)

        index = 0
        costo_menor = costos[0]

        for j in range(1, len(costos), 1):  # O(n * O(n))
            if costo_menor > costos[j]:
                costo_menor = costos[j]
                index = j

        clave_org = None

        for clave, valor in indice_original.items():  # O(n * O(n))
            if valor == index:
                solucionVoraz[last-1] = clave
                clave_org = clave

        del indice_original[clave_org]

        for clave, valor in indice_original.items():  # O(n * O(n))

            if valor >= index:
                indice_original[clave] -= 1

        last -= 1

        tablones.pop(index)

    # O(n³ * n²) = O(n⁵)
    return tuple([solucionVoraz, costoRiegoFinca(f, solucionVoraz)])
