# [juan_aerodinamico.py]

from models.types import *

debug = False
memoization_active = True


def print_debug(message: str):
    new_message = "{}: {}".format(__file__.split("/")[-1], message)
    if debug:
        print(new_message)


class Ahorro():
    def __init__(self):
        self.ahorro = 0

    def aumentar_ahorro(self):
        self.ahorro += 1

    def get_ahorro(self):
        return self.ahorro


"""
=== Obtencion de valor optimo ===
progOptima(t0, t1, t2, t3) (0)
costo(progOptima(t0, t1, t2, t3))
= minCosto(
    // alguno de esos tablones estará al final como en la voraz y antes
    // estará la programación optima de la combinacion de anteriores
    progOptima(t1, t2, t3) :: t0,   // Sacar el costo de esta (i)
    progOptima(t0, t2, t3) :: t1,   // Sacar el costo de esta 
    progOptima(t0, t1, t3) :: t2,   // Sacar el costo de esta
    progOptima(t0, t1, t2) :: t3    // Sacar el costo de esta
)

progOptima(t1, t2, t3) (i)
costo(progOptima(t1, t2, t3))
= minCosto(
    progOptima(t2, t3) :: t1,       // Sacar el costo de esta (ii)
    progOptima(t1, t3) :: t2,       // Sacar el costo de esta 
    progOptima(t1, t2) :: t3        // Sacar el costo de esta
)

progOptima(t2, t3) (ii)
costo(progOptima(t2, t3))
= minCosto(
    progOptima(t3) :: t2,           // Sacar el costo de esta (iii)
    progOptima(t2) :: t3            // Sacar el costo de esta
)

progOptima(t3) (iii)
costo(progOptima(t3))
= minCosto(
    progOptima(t3)                  // Es trivial!!!
)

=== Obtencion de solucion optima ===
La chimbaaaaaa, si ya tenemos costos con memorizacion vamos guardando las programaciones y nos las robamos :D
"""


def roPD(f):
    ahorro = Ahorro()
    print_debug("Obtuve la finca: {}\n\n".format(str(f)))

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

    def costoOptimo(finca: Finca):
        if len(finca) == 1:
            return costoRiegoFinca(finca)
        else:
            # Comprueba si los resultados ya han sido calculados
            if memoization_active and tuple(finca) in dic_memoization:
                ahorro.aumentar_ahorro()
                return dic_memoization[tuple(finca)]

            tiempo_total = tiempoRiegoFinca(finca)
            costos = []

            for i in range(len(finca)):
                copia_finca = finca[:]
                copia_tablon = copia_finca.pop(i)
                t_ini_local = tiempo_total - treg_t(copia_tablon)

                # print_debug("La finca original es {}".format(str(f)))
                # print_debug("copia_finca recortada {} de len {}\ntablon extraido {}\nt_ini {}\n\n".format(
                #     str(copia_finca), str(len(copia_finca)), str(copia_tablon), str(t_ini_local)))

                costo_act = costoOptimo(copia_finca) + \
                    costoRiegoTablon(copia_tablon, t_ini_local)
                costos.append(costo_act)

            dic_memoization[tuple(finca)] = min(costos)
            print_debug("Tamaño del diccionario: {}".format(
                str(len(dic_memoization))))
            return min(costos)

    # Pondré los diccionarios aqui pa que no me estorben en los argumentos de la funcion Atte: Juan
    dic_memoization = {}
    costo_optimo = costoOptimo(f)

    print_debug("Memorizacion ha ahorrado {} calculos".format(
        str(ahorro.get_ahorro())))

    temp_return = ['Error', costo_optimo]

    return temp_return
