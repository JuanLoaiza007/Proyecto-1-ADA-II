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

# Funciones del proyecto por si las moscas
# Generacion aleatoria


def finca_al_azar(long):
    return [(random.randint(1, long * 2),
             random.randint(1, long),
             random.randint(1, 4))
            for _ in range(long)]


def distancia_al_azar(long):
    v = [[random.randint(1, long * 3) for _ in range(long)]
         for _ in range(long)]
    return [[v[i][j] if i < j else (0 if i == j else v[j][i]) for j in range(long)] for i in range(long)]
