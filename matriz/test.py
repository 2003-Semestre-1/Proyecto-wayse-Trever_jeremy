import csv

# Constantes
LEER = "r"
A_NORTE_SUR = "S"
A_SUR_NORTE = "N"
C_LEFT = "L"
C_RIGTH = "R"
INTERSECCION = "C"
DOBLE_SENTIDO = "ND"
EDIFICIO = "0"


def sacar_matriz(nombre):
    CSV = ".csv"
    RUTAS = 'rutas/'
    RUTA_ENTERA = RUTAS + nombre + CSV
    matriz = []
    with open(RUTA_ENTERA, LEER) as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        for fila in lector_csv:
            matriz.append(fila)
    return matriz


def encontrar_ruta(matriz, salida):
    visitados = set()
    pila = [[salida[0], salida[1], [(salida[0], salida[1])]]]

    while pila:
        y, x, ruta = pila.pop()

        if (y, x) == (0, 0):
            return ruta[::-1]  # Invertir la ruta encontrada

        if (y, x) in visitados:
            continue

        visitados.add((y, x))

        # Mover hacia el norte
        if y - 1 >= 0 and matriz[y - 1][x] != EDIFICIO:
            pila.append([y - 1, x, ruta + [(y - 1, x)]])

        # Mover hacia el sur
        if y + 1 < len(matriz) and matriz[y + 1][x] != EDIFICIO:
            pila.append([y + 1, x, ruta + [(y + 1, x)]])

        # Mover hacia el este
        if x + 1 < len(matriz[y]) and matriz[y][x + 1] != EDIFICIO:
            pila.append([y, x + 1, ruta + [(y, x + 1)]])

        # Mover hacia el oeste
        if x - 1 >= 0 and matriz[y][x - 1] != EDIFICIO:
            pila.append([y, x - 1, ruta + [(y, x - 1)]])

    return None  # No se encontró una ruta


def buscar_ruta(inicio, salida, nombre_archivo):
    matriz = sacar_matriz(nombre_archivo)
    ruta = encontrar_ruta(matriz, salida)

    if ruta:
        print("Ruta encontrada:")
        for paso in ruta:
            print(paso)
    else:
        print("No se encontró una ruta válida.")


# Ejemplo de uso
inicio = (0, 0)
salida = (4, 4)
nombre_archivo = "base"

buscar_ruta(inicio, salida, nombre_archivo)
