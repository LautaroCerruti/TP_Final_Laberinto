import sys

def LeerLaberinto(fileName, matrix):
    iteradorLineas = 0
    Entrada = open(fileName,"r")
    Lineas = Entrada.readlines()
    Entrada.close()
    for linea in Lineas:
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

def nodeAnalizer(Node, SumaX, SumaY, fakeQueue, solucion):
            if len(solucion[Node[0]+SumaX][Node[1]+SumaY]) == 0: 
                solucion[Node[0]+SumaX][Node[1]+SumaY] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]+SumaX][Node[1]+SumaY].append((Node[0]+SumaX, Node[1]+SumaY))
                fakeQueue.append((Node[0]+SumaX,Node[1]+SumaY))
            elif len(solucion[Node[0]+SumaX][Node[1]+SumaY]) > (len(solucion[Node[0]][Node[1]])+1):
                solucion[Node[0]+SumaX][Node[1]+SumaY] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]+SumaX][Node[1]+SumaY].append((Node[0]+SumaX, Node[1]+SumaY))

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
        Node = fakeQueue[0]
        fakeQueue.pop(0)
        if Node[0] != 0 and matrix[Node[0]-1][Node[1]] != "1":
            nodeAnalizer(Node, -1, 0, fakeQueue, solucion)
        if Node[1] != 0 and matrix[Node[0]][Node[1]-1] != "1":
            nodeAnalizer(Node, 0, -1, fakeQueue, solucion)
        if Node[0] != (alto-1) and matrix[Node[0]+1][Node[1]] != "1":
            nodeAnalizer(Node, 1, 0, fakeQueue, solucion)
        if Node[1] != (largo-1) and matrix[Node[0]][Node[1]+1] != "1":
            nodeAnalizer(Node, 0, 1, fakeQueue, solucion)
    return solucion

def BuscaCamino(matrix, inicio, objetivo):
    Caminos = BFS(matrix, inicio)
    return(Caminos[objetivo[0]][objetivo[1]])

def ImprimeResultado(resultado, archivoSalida):
    solucion = []
    for nodo in resultado:
        solucion.append((nodo[1]+1,nodo[0]+1))
    print(solucion)

def Main():
    ArchivoEntrada = sys.argv[1]
    ArchivoSalida = sys.argv[2]
    matrix = []
    inicio, objetivo = LeerLaberinto(ArchivoEntrada, matrix)
    Resultado = BuscaCamino(matrix, inicio, objetivo)
    if len(Resultado) == 0:
        print("No tiene solucion")
    else:
        ImprimeResultado(Resultado, ArchivoSalida)

if __name__ == "__main__":
    Main()