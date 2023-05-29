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
    #for fila in matriz:
        #print(fila)
    #print("--------")
    #print(matriz)
    #print("--------")
    return matriz


#analizar la ruta de la matriz

def listaconcoords(nombre):
    print("a")

def analizaralrededor(inicio,salida,nombre):
    Y = inicio[0]
    Z = inicio[1]
    matriz = sacarmatriz(nombre)
    ruta_temporal = []
    ruta_temporal = ruta_temporal + [[matriz[Y][Z],Y , Z]]
    ruta = alrededores(matriz,salida,ruta_temporal)
    print(ruta)
    #print(ruta_temportal)

def alrededores(matriz,salida,ruta_temporal):   
        #print(ruta_temporal)
        analizados = []
        error = 0
        Y = ruta_temporal[-1][1]
        Z = ruta_temporal[-1][2]
        #columna abajo
        try:
            analizados = analizados + [[matriz[Y+1][Z],Y+1,Z]]
        except:
            error +1    
        #columna arriba
        if Y-1 > 0:
            analizados = analizados + [[matriz[Y-1][Z],Y-1,Z]]
            
        #fila derecha
        try:
            analizados = analizados + [[matriz[Y][Z+1],Y,Z+1]]
        except:
            error +1
        
        #fila izquierda
        if Z-1 > 0:
            analizados = analizados + [[matriz[Y][Z-1],Y,Z-1]]
            
        print("Analizados")
        print(analizados) 
        for elementos in analizados:
               
            ruta_temporal = ruta_temporal + [elementos]
            print("Ruta_temporal")
            print(ruta_temporal)
            print("largo de ruta")
            print(len(ruta_temporal))
            if len(ruta_temporal) > 1:
                if ruta_temporal[-1][1] == salida[0] and ruta_temporal[-1][2] == salida[1]:
                    return ruta_temporal
                
            ruta_temporal = alrededores(matriz,salida,ruta_temporal)
                
            if ruta_temporal[-1][1] == salida[0] and ruta_temporal[-1][2] == salida[1]:
                return ruta_temporal
            else:
                ruta_temporal = ruta_temporal[:-1]
        
        return ruta_temporal
            
    
        

analizaralrededor([0,0],[4,5],"base")