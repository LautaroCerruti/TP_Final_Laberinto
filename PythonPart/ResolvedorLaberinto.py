import sys

def leerLaberinto(fileName, matrix):
    iteradorLineas = 0
    entrada = open(fileName,"r")
    lineas = entrada.readlines()
    entrada.close()
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

def nodeAnalizer(node, SumaX, SumaY, fakeQueue, solucion):
            if len(solucion[node[0]+SumaX][node[1]+SumaY]) == 0: 
                solucion[node[0]+SumaX][node[1]+SumaY] = solucion[node[0]][node[1]].copy()
                solucion[node[0]+SumaX][node[1]+SumaY].append((node[0]+SumaX, node[1]+SumaY))
                fakeQueue.append((node[0]+SumaX,node[1]+SumaY))
            elif len(solucion[node[0]+SumaX][node[1]+SumaY]) > (len(solucion[node[0]][node[1]])+1):
                solucion[node[0]+SumaX][node[1]+SumaY] = solucion[node[0]][node[1]].copy()
                solucion[node[0]+SumaX][node[1]+SumaY].append((node[0]+SumaX, node[1]+SumaY))

def BFS(matrix, puntoInicial):
    alto = len(matrix)
    largo = len(matrix[0])
    solucion = []
    iterador = 0
    while iterador < alto:
        solucion.append([[]]*largo)
        iterador+=1
    fakeQueue = [puntoInicial]
    solucion[puntoInicial[0]][puntoInicial[1]] = [puntoInicial]
    while len(fakeQueue) > 0:
        node = fakeQueue[0]
        fakeQueue.pop(0)
        if node[0] != 0 and matrix[node[0]-1][node[1]] != "1":
            nodeAnalizer(node, -1, 0, fakeQueue, solucion)
        if node[1] != 0 and matrix[node[0]][node[1]-1] != "1":
            nodeAnalizer(node, 0, -1, fakeQueue, solucion)
        if node[0] != (alto-1) and matrix[node[0]+1][node[1]] != "1":
            nodeAnalizer(node, 1, 0, fakeQueue, solucion)
        if node[1] != (largo-1) and matrix[node[0]][node[1]+1] != "1":
            nodeAnalizer(node, 0, 1, fakeQueue, solucion)
    return solucion

def buscaCamino(matrix, inicio, objetivo):
    Caminos = BFS(matrix, inicio)
    return(Caminos[objetivo[0]][objetivo[1]])

def imprimeResultado(resultado, archivoSalida):
    solucion = []
    for nodo in resultado:
        solucion.append((nodo[1]+1,nodo[0]+1))
    print(solucion)

def Main():
    archivoEntrada = sys.argv[1]
    archivoSalida = sys.argv[2]
    matrix = []
    inicio, objetivo = leerLaberinto(archivoEntrada, matrix)
    resultado = buscaCamino(matrix, inicio, objetivo)
    if len(resultado) == 0:
        print("No tiene solucion")
    else:
        imprimeResultado(resultado, archivoSalida)

if __name__ == "__main__":
    Main()