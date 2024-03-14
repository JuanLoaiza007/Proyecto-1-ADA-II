from exhaustivo import *

# Ejemplo 1
print("Pruebas con Ejemplo 1:")

finca1 = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]

d1 = [
    [0, 2, 2, 4, 4],
    [2, 0, 4, 2, 6],
    [2, 4, 0, 2, 2],
    [4, 2, 2, 0, 4],
    [4, 6, 2, 4, 0]
]

progRiego1 = [0, 1, 2, 3, 4]

print("Tiempo de inicio de riego (Esperado: [0, 3, 6, 8, 9]):", tIR(
    finca1, progRiego1))
print("Costo de riego de la finca (Esperado: 31):",
      costoRiegoFinca(finca1, progRiego1))
print("Costo de movilidad en la finca (Esperado: 12):",
      costoMovilidad(finca1, progRiego1, d1))
print("\n\n")

progRiego2 = [0, 1, 4, 2, 3]
print("Tiempo de inicio de riego (Esperado: [0, 3, 10, 12, 6]):", tIR(
    finca1, progRiego2))
print("Costo de riego de la finca (Esperado: 33):",
      costoRiegoFinca(finca1, progRiego2))
print("Costo de movilidad en la finca (Esperado: 12):",
      costoMovilidad(finca1, progRiego2, d1))
print("\n\n")

progRiego3 = [2, 1, 4, 3, 0]
print("Tiempo de inicio de riego (Esperado: [10, 2, 0, 9, 5]):", tIR(
    finca1, progRiego3))
print("Costo de riego de la finca (Esperado: 20):",
      costoRiegoFinca(finca1, progRiego3))
print("Costo de movilidad en la finca (Esperado: 18):",
      costoMovilidad(finca1, progRiego3, d1))
print("\n\n")


# Ejemplo 2
print("Pruebas con Ejemplo 2:")

finca2 = [(9, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]

d2 = [
    [0, 2, 2, 4, 4],
    [2, 0, 4, 2, 6],
    [2, 4, 0, 2, 2],
    [4, 2, 2, 0, 4],
    [4, 6, 2, 4, 0]
]

print("Tiempo de inicio de riego (Esperado: [0, 3, 6, 8, 9]):", tIR(
    finca2, progRiego1))
print("Costo de riego de la finca (Esperado: 30):",
      costoRiegoFinca(finca2, progRiego1))
print("Costo de movilidad en la finca (Esperado: 12):",
      costoMovilidad(finca2, progRiego1, d2))
print("\n\n")

progRiego4 = [2, 1, 4, 3, 0]
print("Tiempo de inicio de riego (Esperado: [10, 2, 0, 9, 5]):", tIR(
    finca2, progRiego4))
print("Costo de riego de la finca (Esperado: 24):",
      costoRiegoFinca(finca2, progRiego4))
print("Costo de movilidad en la finca (Esperado: 18):",
      costoMovilidad(finca2, progRiego4, d2))
print("\n\n")

progRiego5 = [2, 1, 4, 0, 3]
print("Tiempo de inicio de riego (Esperado: [9, 2, 0, 12, 5]):", tIR(
    finca2, progRiego5))
print("Costo de riego de la finca (Esperado: 23):",
      costoRiegoFinca(finca2, progRiego5))
print("Costo de movilidad en la finca (Esperado: 18):",
      costoMovilidad(finca2, progRiego5, d2))
print("\n\n")

print("Pruebas de todas las programaciones de riego posibles:")

# Pruebas de todas las programaciones de riego posibles


def calcular_permutaciones(n):
    if n <= 1:
        return 1
    else:
        return n * calcular_permutaciones(n - 1)


# Pruebas hasta de n-1 tablones
n = 11
for i in range(1, n):
    f = finca_al_azar(i)
    print(f"Para {i} tablones:")
    print("Número de permutaciones generadas:",
          len(generarProgramacionesRiego(f)))
    print("Número de permutaciones esperadas:", calcular_permutaciones(i))
    print("\n\n")
