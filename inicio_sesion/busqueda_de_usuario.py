import json

def contador(usuarios):
    contando = True
    contador = 0
    while contando:
        try:
            usuarios["usuarios"][contador]["nombre"]
            contador += 1
        except:
            contando = False

    return contador        


def analizar(nombre,contraseña):
    
    with open("inicio_sesion\credenciales.json","r") as datos:
        credenciales = json.load(datos)

    cantidad_usuarios = contador(credenciales)
    

    print(cantidad_usuarios)
    print(credenciales["usuarios"][0]["nombre"])

analizar("a","b")