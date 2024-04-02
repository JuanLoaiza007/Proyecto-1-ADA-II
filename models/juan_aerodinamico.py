from models.types import *

debug = True


def print_debug(message: str):
    new_message = "{}: {}".format(__file__.split("/")[-1], message)
    if debug:
        print(new_message)


"""
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

=== pseudocodigo ===
...
"""


def roPD(f):

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

    temp_return = ["¡TEMPORARY RETURN!", "¡TEMPORARY RETURN!"]

    return temp_return
