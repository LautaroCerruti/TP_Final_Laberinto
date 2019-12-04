import sys
import subprocess
import random

# La forma a representar al laberinto es una lista de lista de caracteres, Donde I es el inicio, X el objetivo, 0 un camino libre y 1 una pared
# List(List(char))

#   leerLaberinto: file list(list(char)) -> Tupla(int, int) Tupla(int, int)
#   Dado un archivo de entrada y una lista, lee el laberinto de la entrada y lo almacena como un array bidimensional de caractares
#   Retorna 2 tuplas, una con las coordenadas del punto de inicio, y otra con las del objetivo
def leerLaberinto(entrada, matriz):
    iteradorLineas = 0
    lineas = entrada.readlines()
    for linea in lineas:
        linea = list(linea)
        matriz.append(linea[:-1])
        if linea.count("I") != 0:
            xInicio = linea.index("I")
            yInicio = iteradorLineas
        if linea.count("X") != 0:
            xObjetivo = linea.index("X")
            yObjetivo = iteradorLineas
        iteradorLineas += 1
    return (yInicio, xInicio), (yObjetivo, xObjetivo)

#   nodeAnalizer: list(list(tupla(int,int))) list(list(char)) list(tupla(int,int)) tupla(x,y) tupla(x,y) int int int int
#   Dado una lista de listas de tuplas, donde se alacenan los padres de cada nodo, el laberinto, 
#   una lista de tuplas donde se guardan los nodos con determinado orden para luego meterlos en el stack, 
#   una tupla que es el nodo objetivo, otra tupla que es el nodo actual, un int que es la dimension del laberinto
#   y finalmente 2 ints que indican que nodo aledaño al nodo actual estamos tratando de analizar,
#   Realiza una serie de validaciones, como que este nodo exista, que no sea una pared 
#   y que ya no tenga un padre almacenado (lo que indicaria que ya fue ingresado en el stack)
#   Y en caso que ninguna de estas se cumpla, almacena el nodo actual como su padre, 
#   y segun la distancia manhattan con el objetivo, decide en que orden tiene que ser introducido en el stack
def nodeAnalizer(padres, matriz, nodesToInsert, objetivo, node, dimension, a, b):
    if (node[0]+a) not in {-1, dimension} and (node[1]+b) not in {-1, dimension} and padres[node[0]+a][node[1]+b] == (-1,-1) and matriz[node[0]+a][node[1]+b] != "1":
        padres[node[0]+a][node[1]+b] = node
        if (abs(objetivo[0]-node[0]) + abs(objetivo[1]-node[1])) > (abs(objetivo[0]-(node[0]+a)) + abs(objetivo[1]-(node[1]+b))):
            nodesToInsert.append((node[0]+a,node[1]+b))
        else:
            nodesToInsert.insert(0, (node[0]+a,node[1]+b))

#   DFS: lista(lista(char)) tupla(int, int) tupla(int, int) list(list(tupla(int,int)))
#   Esta funcion toma el laberinto, el punto en el que inicia el laberinto, el objetivo, y una list(list(tupla(int,int))) donde guardamos los padres por referencia
#   Esta funcion implementa un DFS con algunas mejoras como el orden en el que metemos los nodos al stack
#   El stack lo implementamos con una lista
def DFS(matriz, puntoInicial, objetivo, padres):
    dimension = len(matriz[0])
    iterador = 0
    while iterador < dimension:
        padres.append([(-1,-1)]*dimension)
        iterador+=1
    stack = [puntoInicial]
    padres[puntoInicial[0]][puntoInicial[1]] = puntoInicial
    nodesToInsert = []
    while stack:
        nodesToInsert.clear()
        node = stack[0]
        stack.pop(0)
        nodeAnalizer(padres, matriz, nodesToInsert, objetivo, node, dimension, -1, 0)
        nodeAnalizer(padres, matriz, nodesToInsert, objetivo, node, dimension, 0, -1)
        nodeAnalizer(padres, matriz, nodesToInsert, objetivo, node, dimension, 1, 0)
        nodeAnalizer(padres, matriz, nodesToInsert, objetivo, node, dimension, 0, 1)
        for n in nodesToInsert:
            stack.insert(0, n)
        if node[0]==objetivo[0] and node[1]==objetivo[1]:
            stack.clear()

#   buscaCamino: lista(lista(char)) tupla(int, int) tupla(int, int) -> list(tuplas(int,int))
#   Toma el laberinto, el inicio y el objetivo
#   Ejecuta el DFS y retorna una lista que contiene el caminp desde el inicio hasta el nodo, que la forma recorriendo los padres
#   En caso de no poder resolver el laberinto, retorna una lista vacia
def buscaCamino(matriz, inicio, objetivo):
    padres = []
    DFS(matriz, inicio, objetivo, padres)
    nodo = objetivo
    Resultado = [nodo]
    if padres[objetivo[0]][objetivo[1]] != (-1,-1):
        while nodo != inicio:
            nodo = padres[nodo[0]][nodo[1]]
            Resultado.insert(0, nodo)  
        return Resultado
    else:
        return []

#   imprimeResultado list(tuplas(int,int)) str
#   Imprime en el archivo la solucion del laberinto
def imprimeResultado(resultado, archivoSalidaName):
    salida = open(archivoSalidaName,"w+")
    for nodo in resultado:
        salida.write('(' + str(nodo[0]+1) + ',' + str(nodo[1]+1)+')\n')
    salida.close()

def Main():
    archivoEntradaC = sys.argv[1]
    laberinto = sys.argv[2]
    archivoSolucion = sys.argv[3]
    matriz = []
    response = subprocess.run(["./a.out", archivoEntradaC, laberinto, str(random.randint(0,1000000000))])
    if response.returncode:
        entrada = open(laberinto,"r")
        inicio, objetivo = leerLaberinto(entrada, matriz)
        entrada.close()
        resultado = buscaCamino(matriz, inicio, objetivo)
        while len(resultado) == 0:
            matriz.clear()
            response = subprocess.run(["./a.out", archivoEntradaC, laberinto, str(random.randint(0,100000000))])
            entrada = open(laberinto,"r")
            inicio, objetivo = leerLaberinto(entrada, matriz)
            entrada.close()
            resultado.clear()
            resultado = buscaCamino(matriz, inicio, objetivo)
        imprimeResultado(resultado, archivoSolucion)
    else:
        print("No se pudo generar un laberinto")

if __name__ == "__main__":
    Main()