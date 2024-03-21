from models.types import *

debug = True


def roFB(f):

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

    tablones = list(range(len(f)))

    def generar(restantes):
        if len(restantes) == 1:
            return [[restantes[0]]]
        else:
            permutaciones = []
            for i in restantes:
                resto = [x for x in restantes if x != i]
                for permutacion in generar(resto):
                    permutaciones.append([i] + permutacion)
            return permutaciones

    programacionesRiego = generar(tablones)

    progCostos = [(pi, costoRiegoFinca(f, pi))
                  for pi in programacionesRiego]

    if debug:
        i = 0
        for prog in programacionesRiego:
            print(prog)

            programacionDefault = []
            for j in range(0, len(programacionesRiego[0]), 1):
                programacionDefault.append(j)

            costosTablones = [costoRiegoTablon(
                i, f, prog) for i in range(len(prog))]

            t = 0
            for costo in costosTablones:
                print("Tablon ", t, " cuesta: ", costo)
                t += 1

            print("Corresponde a la programacion: ", progCostos[i], "\n")
            i += 1

            print("")

    def encontrarMinimo(optimaActual, costosRestantes):
        if not costosRestantes:
            return optimaActual
        else:
            nuevoMin = costosRestantes[0] if costosRestantes[0][1] < optimaActual[1] else optimaActual
            return encontrarMinimo(nuevoMin, costosRestantes[1:])

    return encontrarMinimo(progCostos[0], progCostos[1:])