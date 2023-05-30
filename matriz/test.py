def analizaralrededor(inicio, salida, nombre):
    Y = inicio[0]
    Z = inicio[1]
    matriz = sacarmatriz(nombre)
    rutas_posibles = []
    ruta_temporal = []
    ruta_temporal = append(ruta_temporal, [matriz[Y][Z], Y, Z])
    visitados = []
    visitados.append((Y, Z))
    alrededores(matriz, salida, ruta_temporal, visitados, rutas_posibles)

    return rutas_posibles


def alrededores(matriz, salida, ruta_temporal, visitados, rutas_posibles):
    analizados = []
    error = 0
    Y = ruta_temporal[-1][1]
    Z = ruta_temporal[-1][2]

    # Columna abajo
    try:
        analizados = append(analizados, [matriz[Y + 1][Z], Y + 1, Z])
    except:
        error += 1

    # Columna arriba
    if Y - 1 >= 0:
        analizados = append(analizados, [matriz[Y - 1][Z], Y - 1, Z])

    # Fila derecha
    try:
        analizados = append(analizados, [matriz[Y][Z + 1], Y, Z + 1])
    except:
        error += 1

    # Fila izquierda
    if Z - 1 >= 0:
        analizados = append(analizados, [matriz[Y][Z - 1], Y, Z - 1])

    for elementos in analizados:
        coord = (elementos[1], elementos[2])
        if coord not in visitados and matriz[coord[0]][coord[1]] not in EDIFICIO:
            ruta_temporal = append(ruta_temporal, elementos)
            visitados.append(coord)

            if Len(ruta_temporal) > 1:
                if ruta_temporal[-1][1] == salida[0] and ruta_temporal[-1][2] == salida[1]:
                    rutas_posibles.append(ruta_temporal[:])

            alrededores(matriz, salida, ruta_temporal, visitados, rutas_posibles)

            if ruta_temporal[-1][1] == salida[0] and ruta_temporal[-1][2] == salida[1]:
                rutas_posibles.append(ruta_temporal[:])
            else:
                ruta_temporal = ruta_temporal[:-1]

    return rutas_posibles

rutas = analizaralrededor([0, 0], [4, 5], "base")
