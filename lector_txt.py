def leer_archivo_txt(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            # Leer la primera línea para obtener el valor de n
            n = int(archivo.readline().strip())
            
            # Leer las siguientes n líneas con los 3 enteros separados por comas
            datos = []
            for _ in range(n):
                linea = archivo.readline().strip()
                valores = [int(x) for x in linea.split(",")]
                datos.append(valores)
            return datos
        
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

# Ejemplo de uso
nombre_archivo = "test.txt"
datos_leidos = leer_archivo_txt(nombre_archivo)
if datos_leidos:
    print(f"Datos leídos del archivo '{nombre_archivo}':")
    #for linea in datos_leidos:
     #   print(linea)
    print(datos_leidos)