import csv


# constantes

A_NORTE_SUR = "S"
A_SUR_NORTE = "N"
C_LEFT = "L"
C_RIGTH = "R"
INTERSECCION = "C"
DOBLE_SENTIDO = "ND"


#codigo
matriz = []

with open("matriz\Rutabase.csv", 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=';')
    print(lector_csv)
    for fila in lector_csv:
        matriz.append(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)
print(matriz)