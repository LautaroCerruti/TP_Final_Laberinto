import sys
import subprocess

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
    nodesToInsert = []
    while len(fakeStack) > 0:
        nodesToInsert.clear()
        node = fakeStack[0]
        fakeStack.pop(0)
        if node[0] != 0 and solucion[node[0]-1][node[1]] == (-1,-1) and matrix[node[0]-1][node[1]] != "1":
            solucion[node[0]-1][node[1]] = node
            if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > (abs(objetivo[0]-(node[0]-1)) + abs(objetivo[1]-node[1])):
                nodesToInsert.append((node[0]-1,node[1]))
            else:
                nodesToInsert.insert(0, (node[0]-1,node[1]))
        if node[1] != 0 and solucion[node[0]][node[1]-1] == (-1,-1) and matrix[node[0]][node[1]-1] != "1":
            solucion[node[0]][node[1]-1] = node
            if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > (abs(objetivo[0]-node[0]) + abs(objetivo[1]-(node[1]-1))):
                nodesToInsert.append((node[0],node[1]-1))
            else:
                nodesToInsert.insert(0, (node[0],node[1]-1))
        if node[0] != (alto-1) and solucion[node[0]+1][node[1]] == (-1,-1) and matrix[node[0]+1][node[1]] != "1":
            solucion[node[0]+1][node[1]] = node
            if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > abs((objetivo[0]-(node[0]+1)) + abs(objetivo[1]-node[1])):
                nodesToInsert.append((node[0]+1,node[1]))
            else:
                nodesToInsert.insert(0, (node[0]+1,node[1]))
        if node[1] != (largo-1) and solucion[node[0]][node[1]+1] == (-1,-1) and matrix[node[0]][node[1]+1] != "1":
            solucion[node[0]][node[1]+1] = node
            if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > (abs(objetivo[0]-node[0]) + abs(objetivo[1]-(node[1]+1))):
                nodesToInsert.append((node[0],node[1]+1))
            else:
                nodesToInsert.insert(0, (node[0],node[1]+1))
        for n in nodesToInsert:
            fakeStack.insert(0, n)
        if node[0]==objetivo[0] and node[1]==objetivo[1]:
            fakeStack.clear()
    return solucion

def buscaCamino(matrix, inicio, objetivo):
    Padres = DFS(matrix, inicio, objetivo)
    nodo = objetivo
    Resultado = [nodo]
    if Padres[objetivo[0]][objetivo[1]] != (-1,-1):
        while nodo != inicio:
            nodo = Padres[nodo[0]][nodo[1]]
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
    response = subprocess.run(["./a.out", "entradaLaberinto.txt", "laberinto.txt"])
    entrada = open(archivoEntrada,"r")
    inicio, objetivo = leerLaberinto(entrada, matrix)
    entrada.close()
    resultado = buscaCamino(matrix, inicio, objetivo)
    contador = 1
    while len(resultado) == 0:
        matrix.clear()
        response = subprocess.run(["./a.out", "entradaLaberinto.txt", "laberinto.txt"])
        contador += 1
        #print(contador)
        entrada = open(archivoEntrada,"r")
        inicio, objetivo = leerLaberinto(entrada, matrix)
        entrada.close()
        resultado = buscaCamino(matrix, inicio, objetivo)
    print(contador)
    imprimeResultado(resultado, archivoSalida)

if __name__ == "__main__":
    Main()