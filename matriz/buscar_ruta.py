import csv

# Constantes
LEER = "r"
C_LEFT = "L"
C_RIGHT = "R"
INTERSECCION = "C"
DOBLE_SENTIDO_VERTICAL = "DN"
DOBLE_SENTIDO_HORIZONTAL = "DH"
NORTE = "N"
SUR = "S"
EDIFICIO = "0"

# Código
def sacarmatriz(nombre):
    CSV = ".csv"
    RUTAS = 'rutas\ '
    RUTAENTERA = RUTAS[:-1] + nombre + CSV
    matriz = []

    with open(RUTAENTERA, LEER) as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')

        for fila in lector_csv:
            matriz.append(fila)

    return matriz


def guardar_matriz(nombre, matriz):
    CSV = ".csv"
    RUTAS = 'rutas\ '
    RUTAENTERA = RUTAS[:-1] + nombre + CSV

    with open(RUTAENTERA, "w", newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=',')
        for fila in matriz:
            escritor_csv.writerow(fila)


def listaconcoords(nombre):
    print("a")


def analizaralrededor(inicio, salida, nombre):
    Y = inicio[0]
    Z = inicio[1]
    matriz = sacarmatriz(nombre)
    ruta_temporal = [[matriz[Y][Z], Y, Z]]
    ruta = alrededores(matriz, salida, ruta_temporal)

    # Reemplazar ruta con asteriscos en la matriz
    for paso in ruta:
        matriz[paso[1]][paso[2]] = "*"

    # Guardar la matriz modificada en un nuevo archivo CSV
    guardar_matriz(nombre + "_modificado", matriz)

    return ruta


def alrededores(matriz, salida, ruta_temporal):
    analizados = []
    Y = ruta_temporal[-1][1]
    Z = ruta_temporal[-1][2]
    valor_actual = matriz[Y][Z]

    if valor_actual == NORTE:
        if Y - 1 > 0:
            valor = matriz[Y - 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y - 1, Z])
    elif valor_actual == SUR:
        try:
            valor = matriz[Y + 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y + 1, Z])
        except:
            pass
    elif valor_actual == C_LEFT:
        if Z - 1 > 0:
            valor = matriz[Y][Z - 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z - 1])
    elif valor_actual == C_RIGHT:
        try:
            valor = matriz[Y][Z + 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z + 1])
        except:
            pass
    elif valor_actual == "B":
        if Z - 1 > 0:
            valor = matriz[Y][Z - 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z - 1])
        try:
            valor = matriz[Y][Z + 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z + 1])
        except:
            pass
    elif valor_actual == "D":
        if Y - 1 > 0:
            valor = matriz[Y - 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y - 1, Z])
        try:
            valor = matriz[Y + 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y + 1, Z])
        except:
            pass
    else:
        try:
            valor = matriz[Y + 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y + 1, Z])
        except:
            pass

        if Y - 1 > 0:
            valor = matriz[Y - 1][Z]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y - 1, Z])

        try:
            valor = matriz[Y][Z + 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z + 1])
        except:
            pass

        if Z - 1 > 0:
            valor = matriz[Y][Z - 1]
            if valor not in ["T", "P", "E", "H", "Z", "J", EDIFICIO]:
                analizados.append([valor, Y, Z - 1])

    for elemento in analizados:
        if elemento not in ruta_temporal:
            ruta_temporal.append(elemento)

            if elemento[1] == salida[0] and elemento[2] == salida[1]:
                return ruta_temporal

            ruta_temporal = alrededores(matriz, salida, ruta_temporal)

            if ruta_temporal[-1][1] == salida[0] and ruta_temporal[-1][2] == salida[1]:
                return ruta_temporal
            else:
                ruta_temporal = ruta_temporal[:-1]

    return ruta_temporal


ruta = analizaralrededor([0, 0], [9, 9], "base")
print(ruta)
