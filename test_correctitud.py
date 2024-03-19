from exhaustivo import *

# Ejemplo 1
finca1 = [(2, 2, 1), (3, 4, 1)]
finca2 = [(10, 5, 1), (8, 3, 1), (16, 8, 1), (32, 16, 1)]

# tsup - (t_ini + treg)             ,si tsup - treg >= t_ini
#   8  - (  5   +   3)              ,si  8   -  3   >=   5

# Cuando t_ini = tsup-treg costoRiegoTablon = 0

# Cuando

print("Optima es: ", roFB(finca2))
