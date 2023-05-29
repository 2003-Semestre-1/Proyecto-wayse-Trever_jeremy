"""
nombre: append
entrada: lista y elemento
salida: agregar un elemento a una lista
"""
def append(lista, elemento):
    lista += [elemento]
    return lista

"""
nombre: Len
entrada: lista
salida: contador de indises que existen en una lista
"""
def Len(objeto):
    contador = 0
    for elemento in objeto:
        contador += 1
    return contador
