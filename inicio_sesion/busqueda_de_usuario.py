import json

def analizar(nombre="",contrasena=""):

    resultado = False
    
    with open("inicio_sesion\credenciales.json","r") as datos:
        credenciales = json.load(datos)
    contando = True
    contador = 0
    while contando:
        try:
            if credenciales["usuarios"][contador]["nombre"] == nombre and credenciales["usuarios"][contador]["contrasena"] == contrasena:

                resultado = True
                
            
            contador += 1
        except:
            contando = False

    return resultado