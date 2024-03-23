import random
from typing import List, Tuple


# Definición de tipos
Tablon = Tuple[int, int, int]
Finca = List[Tablon]
ProgRiego = List[int]
TiempoInicioRiego = List[int]


# Propiedades de tablones
def tsup(f, i):
    return f[i][0]


def treg(f, i):
    return f[i][1]


def prio(f, i):
    return f[i][2]
