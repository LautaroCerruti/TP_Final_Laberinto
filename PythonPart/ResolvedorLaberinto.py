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

def nodeAnalizer(node, SumaY, SumaX, fakeQueue, solucion):
            if len(solucion[node[0]+SumaY][node[1]+SumaX]) == 0: 
                solucion[node[0]+SumaY][node[1]+SumaX] = solucion[node[0]][node[1]].copy()
                solucion[node[0]+SumaY][node[1]+SumaX].append((node[0]+SumaY, node[1]+SumaX))
                fakeQueue.append((node[0]+SumaY,node[1]+SumaX))
            elif len(solucion[node[0]+SumaY][node[1]+SumaX]) > (len(solucion[node[0]][node[1]])+1):
                solucion[node[0]+SumaY][node[1]+SumaX] = solucion[node[0]][node[1]].copy()
                solucion[node[0]+SumaY][node[1]+SumaX].append((node[0]+SumaY, node[1]+SumaX))

def nodeAnalizerDFS(node, SumaY, SumaX, fakeStack, solucion):
    if solucion[node[0]+SumaY][node[1]+SumaX] == (-1,-1): 
        solucion[node[0]+SumaY][node[1]+SumaX] = node
        fakeStack.insert(0, (node[0]+SumaY,node[1]+SumaX))

def DFS(matrix, puntoInicial, objetivo):
    alto = len(matrix)
    largo = len(matrix[0])
    solucion = []
    iterador = 0
    while iterador < alto:
        solucion.append([(-1,-1)]*largo)
        iterador+=1
    fakeStack = [puntoInicial]
    solucion[puntoInicial[0]][puntoInicial[1]] = puntoInicial
    while len(fakeStack) > 0:
        node = fakeStack[0]
        fakeStack.pop(0)
        if node[0] != 0 and matrix[node[0]-1][node[1]] != "1":
            nodeAnalizerDFS(node, -1, 0, fakeStack, solucion)
        if node[1] != 0 and matrix[node[0]][node[1]-1] != "1":
            nodeAnalizerDFS(node, 0, -1, fakeStack, solucion)
        if node[0] != (alto-1) and matrix[node[0]+1][node[1]] != "1":
            nodeAnalizerDFS(node, 1, 0, fakeStack, solucion)
        if node[1] != (largo-1) and matrix[node[0]][node[1]+1] != "1":
            nodeAnalizerDFS(node, 0, 1, fakeStack, solucion)
        if node[0]==objetivo[0] and node[1]==objetivo[1]:
            fakeStack.clear()
    return solucion

def BFS(matrix, puntoInicial, objetivo):
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
        print(node)
        if node[0] != 0 and matrix[node[0]-1][node[1]] != "1":
            nodeAnalizer(node, -1, 0, fakeQueue, solucion)
        if node[1] != 0 and matrix[node[0]][node[1]-1] != "1":
            nodeAnalizer(node, 0, -1, fakeQueue, solucion)
        if node[0] != (alto-1) and matrix[node[0]+1][node[1]] != "1":
            nodeAnalizer(node, 1, 0, fakeQueue, solucion)
        if node[1] != (largo-1) and matrix[node[0]][node[1]+1] != "1":
            nodeAnalizer(node, 0, 1, fakeQueue, solucion)
        if node[0]==objetivo[0] and node[1]==objetivo[1]:
            fakeQueue.clear()
    return solucion

def buscaCamino(matrix, inicio, objetivo):
    Padres = DFS(matrix, inicio, objetivo)
    nodo = objetivo
    Resultado = [nodo]
    if Padres[objetivo[0]][objetivo[1]] != (-1,-1):
        while nodo != inicio:
            nodo = Padres[nodo[0]][nodo[1]]
            Resultado.insert(1, nodo)
        return Resultado
    else:
        return []

def imprimeResultado(resultado, archivoSalida):
    solucion = []
    for nodo in resultado:
        solucion.append((nodo[0]+1,nodo[1]+1))
    print(solucion)

def Main():
    #archivoEntrada = sys.argv[1]
    #archivoSalida = sys.argv[2]
    archivoEntrada = "salidaLaberinto.txt"
    archivoSalida = "salida"
    matrix = []
    inicio, objetivo = leerLaberinto(archivoEntrada, matrix)
    print(objetivo)
    resultado = buscaCamino(matrix, inicio, objetivo)
    if len(resultado) == 0:
        print("No tiene solucion")
    else:
        imprimeResultado(resultado, archivoSalida)

if __name__ == "__main__":
    Main()