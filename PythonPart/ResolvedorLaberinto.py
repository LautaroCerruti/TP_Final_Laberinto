import sys
import subprocess
import random

#   leerLaberinto: file list(list(char)) -> Tupla(int, int) Tupla(int, int)
#   Dado un archivo de entrada y una lista, lee el laberinto de la entrada y lo almacena como un array bidimensional de caractares
#   Retorna 2 tuplas, una con las coordenadas del punto de inicio, y otra con las del objetivo
def leerLaberinto(entrada, matrix):
    iteradorLineas = 0
    lineas = entrada.readlines()
    for linea in lineas:
        linea = list(linea)
        matrix.append(linea[:-1])
        if linea.count("I") != 0:
            xInicio = linea.index("I")
            yInicio = iteradorLineas
        if linea.count("X") != 0:
            xObjetivo = linea.index("X")
            yObjetivo = iteradorLineas
        iteradorLineas += 1
    return (yInicio, xInicio), (yObjetivo, xObjetivo)

def nodeAnalizer(solucion, matrix, nodesToInsert, objetivo, node, alto, largo, a, b):
    if (node[0]+a) not in {-1, alto} and (node[1]+b) not in {-1, largo} and solucion[node[0]+a][node[1]+b] == (-1,-1) and matrix[node[0]+a][node[1]+b] != "1":
        solucion[node[0]+a][node[1]+b] = node
        if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > (abs(objetivo[0]-(node[0]+a)) + abs(objetivo[1]-(node[1]+b))):
            nodesToInsert.append((node[0]+a,node[1]+b))
        else:
            nodesToInsert.insert(0, (node[0]+a,node[1]+b))

def DFS(matrix, puntoInicial, objetivo, solucion):
    alto = len(matrix)
    largo = len(matrix[0])
    iterador = 0
    while iterador < alto:
        solucion.append([(-1,-1)]*largo)
        iterador+=1
    fakeStack = [puntoInicial]
    solucion[puntoInicial[0]][puntoInicial[1]] = puntoInicial
    nodesToInsert = []
    while fakeStack:
        nodesToInsert.clear()
        node = fakeStack[0]
        fakeStack.pop(0)
        nodeAnalizer(solucion, matrix, nodesToInsert, objetivo, node, alto, largo, -1, 0)
        nodeAnalizer(solucion, matrix, nodesToInsert, objetivo, node, alto, largo, 0, -1)
        nodeAnalizer(solucion, matrix, nodesToInsert, objetivo, node, alto, largo, 1, 0)
        nodeAnalizer(solucion, matrix, nodesToInsert, objetivo, node, alto, largo, 0, 1)
        for n in nodesToInsert:
            fakeStack.insert(0, n)
        if node[0]==objetivo[0] and node[1]==objetivo[1]:
            fakeStack.clear()

def buscaCamino(matrix, inicio, objetivo):
    padres = []
    DFS(matrix, inicio, objetivo, padres)
    nodo = objetivo
    Resultado = [nodo]
    if padres[objetivo[0]][objetivo[1]] != (-1,-1):
        while nodo != inicio:
            nodo = padres[nodo[0]][nodo[1]]
            Resultado.insert(0, nodo)  
        return Resultado
    else:
        return []

def imprimeResultado(resultado, archivoSalidaName):
    salida = open(archivoSalidaName,"w")
    for nodo in resultado:
        salida.write('(' + str(nodo[0]+1) + ',' + str(nodo[1]+1)+')\n')
    salida.close()

def Main():
    #archivoEntrada = sys.argv[1]
    #archivoSalida = sys.argv[2]
    archivoEntrada = "laberinto.txt"
    archivoSalida = "solucionLaberinto.txt"
    matrix = []
    response = subprocess.run(["./a.out", "entradaLaberinto.txt", "laberinto.txt", str(random.randint(0,100000000))])
    print(response)
    if response.returncode:
        entrada = open(archivoEntrada,"r")
        inicio, objetivo = leerLaberinto(entrada, matrix)
        entrada.close()
        resultado = buscaCamino(matrix, inicio, objetivo)
        while len(resultado) == 0:
            matrix.clear()
            response = subprocess.run(["./a.out", "entradaLaberinto.txt", "laberinto.txt", str(random.randint(0,10000000))])
            print(response)
            entrada = open(archivoEntrada,"r")
            inicio, objetivo = leerLaberinto(entrada, matrix)
            entrada.close()
            resultado = buscaCamino(matrix, inicio, objetivo)
        imprimeResultado(resultado, archivoSalida)
    else:
        print("No se pudo generar un laberinto")

if __name__ == "__main__":
    Main()