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



        
costoOptimo(finca: Finca):

    // Aqui empiezo a trabajar
    copia_finca = finca[:]

    if len(copia_finca) == 1:
        tablon = copia_finca.pop(0)
        return costoRiegoTablon(tablon, 0)
    else: 
        
            min(
                costo(
                    for tablon in copia_finca:
                        otra_copia_finca = finca[:]
                        otra_copia_finca.remove(tablon).append(tablon)
                )
            )

    
progOptima(finca):t

    tablones = finca[:] // Copiamos los tablones
    indice_original = {i: i for i in range(len(tablones))}

    if len(finca) == 1:
        return [(finca[0]), calcularCosto(finca[0])]
    else:
"""


def costoRiegoTablon(t: Tablon, t_ini: int):
    if tsup_t(t) - treg_t(t) >= t_ini:
        return tsup_t(t) - (t_ini + treg_t(t))
    else:
        return prio_t(t) * ((t_ini + treg_t(t)) - tsup_t(t))


def costoRiegoFinca(f: Finca):
    costo = 0
    t_ini = 0

    for t in f:
        costo += costoRiegoTablon(t, t_ini)
        t_ini += treg_t(t)
    return costo


def roPD(f):

    temp_return = ["¡TEMPORARY RETURN!", "¡TEMPORARY RETURN!"]

    return temp_return
