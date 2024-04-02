import random
from typing import List, Tuple


# Definición de tipos
Tablon = Tuple[int, int, int]
Finca = List[Tablon]
ProgRiego = List[int]
TiempoInicioRiego = List[int]


# Propiedades de tablones en una finca
def tsup(f: Finca, i: int):
    """
    Obtiene el tiempo de supervivencia de un tablon en una finca.

    Args:
        f: La finca con los tablones.
        i: El indice del tablon del que se desea esta propiedad.

    Returns:
        (int): El tiempo de supervivencia del tablon.
    """
    return f[i][0]


def treg(f: Finca, i: int):
    """
    Obtiene el tiempo de riego de un tablon en una finca.

    Args:
        f: La finca con los tablones.
        i: El indice del tablon del que se desea esta propiedad.

    Returns:
        (int): El tiempo de riego del tablon.
    """
    return f[i][1]


def prio(f: Finca, i: int):
    """
    Obtiene la prioridad de un tablon en una finca.

    Args:
        f: La finca con los tablones.
        i: El indice del tablon del que se desea esta propiedad.

    Returns:
        (int): La prioridad del tablon.
    """
    return f[i][2]


# Propiedades de un tablon directamente
def tsup_t(t: Tablon):
    """
    Obtiene el tiempo de supervivencia de un tablon.

    Args:
        t: El tablon.

    Returns:
        (int): El tiempo de supervivencia del tablon.
    """
    return t[0]


def treg_t(t: Tablon):
    """
    Obtiene el tiempo de riego de un tablon.

    Args:
        t: El tablon.

    Returns:
        (int): El tiempo de riego del tablon.
    """
    return t[1]


def prio_t(t: Tablon):
    """
    Obtiene la prioridad de un tablon.

    Args:
        t: El tablon.

    Returns:
        (int): La prioridad del tablon.
    """
    return t[2]
