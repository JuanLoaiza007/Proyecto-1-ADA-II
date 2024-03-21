# [lector_txt.py]
from file_selector import File_selector


def leer_archivo_txt():
    nombre_archivo = File_selector.select("data")
    if nombre_archivo:
        try:
            with open(nombre_archivo, "r") as archivo:
                n = int(archivo.readline().strip())

                datos = []
                for _ in range(n):
                    linea = archivo.readline().strip()
                    valores = tuple([int(x) for x in linea.split(",")])
                    datos.append(valores)
                return datos

        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encontró.")
            return None
    else:
        print("No se seleccionó ningún archivo.")
        return None


if __name__ == '__main__':
    # Ejemplo de uso
    datos_leidos = leer_archivo_txt()
    if datos_leidos:
        print("Datos leídos del archivo:")
        print(datos_leidos)
