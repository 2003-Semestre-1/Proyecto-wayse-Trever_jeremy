import csv


# constantes
LEER = "r"
A_NORTE_SUR = "S"
A_SUR_NORTE = "N"
C_LEFT = "L"
C_RIGTH = "R"
INTERSECCION = "C"
DOBLE_SENTIDO = "ND"
EDIFICIO = "0"


#variables

rutas_guardadas = []


#codigo
def sacarmatriz(nombre):
    CSV = ".csv"
    RUTAS = 'rutas\ '
    
    RUTAENTERA = RUTAS[:-1] + nombre + CSV
    matriz = []
    #print(RUTAENTERA)
    with open(RUTAENTERA, LEER) as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        #print(lector_csv)
        for fila in lector_csv:
            matriz.append(fila)

    # Imprimir la matriz
    for fila in matriz:
        print(fila)
    print("--------")
    print(matriz)
    return matriz

sacarmatriz("todoceros")
#analizar la ruta de la matriz

def listaconcoords(nombre):
    print("a")

def analizaralrededor(inicio,salida,nombre):
    Y = inicio[0]
    Z = inicio[1]
    matriz = sacarmatriz(nombre)
    ruta_temportal = []
    ruta_temportal = ruta_temportal + [[matriz[Y][Z],Y , Z]]
    
    for elemento in ruta_temportal:
        analizados = []
        error = 0
        try:
            analizados = analizados + [[matriz[Y+1][Z],Y+1,Z]]
        except:
            error +1
            
        
        if Y-1 > 0:
            analizados = analizados + [[matriz[Y-1][Z],Y-1,Z]]
                  
        
        try:
            analizados = analizados + [[matriz[Y][Z+1],Y,Z+1]]
        except:
            error +1
            
        if Z-1 > 0:
            analizados = analizados + [[matriz[Y][Z-1],Y,Z-1]]
            
        if error == 4:
            continue
    
    print(analizados)
    print(ruta_temportal)
        
#analizaralrededor([0,0],[0,0],"base")