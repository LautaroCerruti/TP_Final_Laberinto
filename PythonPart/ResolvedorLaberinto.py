def LeerLaberinto(file, matrix):
    xObjetivo = -1
    iteradorLineas = 0
    Lineas = file.readlines()
    file.close()
    for linea in Lineas:
        linea = list(linea)
        matrix.append(linea[:-1])
        if linea.count("2") != 0:
            xObjetivo = linea.index("2")
            yObjetivo = iteradorLineas
        iteradorLineas += 1
    return [yObjetivo, xObjetivo]

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
        Node = fakeQueue[0].copy()
        fakeQueue.pop(0)
        if Node[0] != 0 and matrix[Node[0]-1][Node[1]] != "1":
            if len(solucion[Node[0]-1][Node[1]]) == 0: 
                solucion[Node[0]-1][Node[1]] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]-1][Node[1]].append([Node[0]-1, Node[1]])
                fakeQueue.append([Node[0]-1,Node[1]])
            elif len(solucion[Node[0]-1][Node[1]]) > (len(solucion[Node[0]][Node[1]])+1):
                solucion[Node[0]-1][Node[1]] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]-1][Node[1]].append([Node[0]-1, Node[1]])
        
        if Node[1] != 0 and matrix[Node[0]][Node[1]-1] != "1":
            if len(solucion[Node[0]][Node[1]-1]) == 0: 
                solucion[Node[0]][Node[1]-1] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]][Node[1]-1].append([Node[0], Node[1]-1])
                fakeQueue.append([Node[0],Node[1]-1])
            elif len(solucion[Node[0]][Node[1]-1]) > (len(solucion[Node[0]][Node[1]])+1):
                solucion[Node[0]][Node[1]-1] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]][Node[1]-1].append([Node[0], Node[1]-1])

        if Node[0] != (alto-1) and matrix[Node[0]+1][Node[1]] != "1":
            if len(solucion[Node[0]+1][Node[1]]) == 0: 
                solucion[Node[0]+1][Node[1]] = (solucion[Node[0]][Node[1]]).copy()
                solucion[Node[0]+1][Node[1]].append([Node[0]+1, Node[1]])
                fakeQueue.append([Node[0]+1,Node[1]])
            elif len(solucion[Node[0]+1][Node[1]]) > (len(solucion[Node[0]][Node[1]])+1):
                solucion[Node[0]+1][Node[1]] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]+1][Node[1]].append([Node[0]+1, Node[1]])

        if Node[1] != (largo-1) and matrix[Node[0]][Node[1]+1] != "1":
            if len(solucion[Node[0]][Node[1]+1]) == 0: 
                solucion[Node[0]][Node[1]+1] = (solucion[Node[0]][Node[1]]).copy()
                solucion[Node[0]][Node[1]+1].append([Node[0],Node[1]+1])
                fakeQueue.append([Node[0],Node[1]+1])
            elif len(solucion[Node[0]][Node[1]+1]) > (len(solucion[Node[0]][Node[1]])+1):
                solucion[Node[0]][Node[1]+1] = solucion[Node[0]][Node[1]].copy()
                solucion[Node[0]][Node[1]+1].append([Node[0],Node[1]+1])
    return solucion


def BuscaCamino(matrix, objetivo):
    Caminos = BFS(matrix, [0,0])
    return(Caminos[objetivo[0]][objetivo[1]])


def Main():
    ArchivoEntrada = input("Ingrese el nombre del archivo donde se encuentra el laberinto: ")
    Entrada = open(ArchivoEntrada,"r")
    matrix = []
    objetivo = LeerLaberinto(Entrada, matrix)
    Resultado = BuscaCamino(matrix, objetivo)
    if len(Resultado) == 0:
        print("No tiene solucion")
    else:
        print(Resultado)

if __name__ == "__main__":
    Main()