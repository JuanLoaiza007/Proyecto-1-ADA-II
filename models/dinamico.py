from models.types import *
import itertools

debug = True

def roPD(f):

    memo = {}  # Diccionario para memoization

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

        # Comprobar si ya calculamos el costo de riego para este tablón
        if (i, tuple(pi)) in memo:
            return memo[(i, tuple(pi))]

        tiemposInicioRiego = [calcularTiempoInicio(ti) for ti in range(len(f))]

        costo = costoRiego(tiemposInicioRiego[i])
        memo[(i, tuple(pi))] = costo  # Guardar el costo calculado en el diccionario de memoization
        return costo

    def costoRiegoFinca(f, pi):

        costos = [costoRiegoTablon(i, f, pi) for i in range(len(f))]
        return sum(costos)

    tablones = list(range(len(f)))

    def generar(restantes):
        return list(itertools.permutations(restantes))

    programacionesRiego = generar(tablones)

    progCostos = [(pi, costoRiegoFinca(f, pi))
                  for pi in programacionesRiego]

    if debug:
        i = 0
        for prog in programacionesRiego:
            # print(prog)

            programacionDefault = []
            for j in range(0, len(programacionesRiego[0]), 1):
                programacionDefault.append(j)

            costosTablones = [costoRiegoTablon(
                i, f, prog) for i in range(len(prog))]

            t = 0
            '''
            for costo in costosTablones:
                print("Tablon ", t, " cuesta: ", costo)
                t += 1

            print("Corresponde a la programacion: ", progCostos[i], "\n")
            i += 1

            print("")'''

    def encontrarMinimo(optimaActual, costosRestantes):
        minimo = optimaActual
        for costo in costosRestantes:
            if costo[1] < minimo[1]:
                minimo = costo
        return minimo
    print(memo)
    return encontrarMinimo(progCostos[0], progCostos[1:])