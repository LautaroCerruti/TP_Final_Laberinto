import resolvedorLaberinto
from pytest import *
# Casos de test (pytest) para el trabajo final. 

# Testeamos la funcion leerLaberinto
# Se testea el retorno del inicio y el objetivo de los laberintos leidos, y la matriz modificada por referencia
# Por test, en el archvo de los resultados tenemos el inicio como una tupla de int, el objetivo como una tupla de int y el laberinto como una lista de lista de chars
def test_leerLaberinto():
    laberinto1 = []
    laberinto2 = []
    laberinto3 = []
    laberintoTest1 = open("tests/laberintoTest1.txt","r")
    laberintoTest2 = open("tests/laberintoTest2.txt","r")
    laberintoTest3 = open("tests/laberintoTest3.txt","r")
    Entrada1 = open("tests/test1-1.txt", "r")
    lineas = Entrada1.readlines()
    inicio1 = eval(lineas[0])
    objetivo1 = eval(lineas[1])
    matriz1 = eval(lineas[2])
    inicio2 = eval(lineas[3])
    objetivo2 = eval(lineas[4])
    matriz2 = eval(lineas[5])
    inicio3 = eval(lineas[6])
    objetivo3 = eval(lineas[7])
    matriz3 = eval(lineas[8])
    assert resolvedorLaberinto.leerLaberinto(laberintoTest1, laberinto1) == (inicio1, objetivo1)
    assert laberinto1 == matriz1
    assert resolvedorLaberinto.leerLaberinto(laberintoTest2, laberinto2) == (inicio2, objetivo2)
    assert laberinto2 == matriz2
    assert resolvedorLaberinto.leerLaberinto(laberintoTest3, laberinto3) == (inicio3, objetivo3)
    assert laberinto3 == matriz3

# Testeamos la funcion buscaCamino
# Se testea el camino del inicio al objetivo retornado por esta funcion
# En el archivo de entrada test2-1.txt, tenemos una linea con el inicio, una linea con el fin, y una linea con el laberinto como es devuelto por leer archivo, por test
# Y en test2-2.txt, por test, tenemos una linea con una lista con las tuplas que forman el camino del inicio al objetivo
# una lista vacia en caso de que no haya un camino
def test_buscaCamino():
    Entrada1 = open("tests/test2-1.txt", "r")
    Entrada2 = open("tests/test2-2.txt", "r")
    lineasParametros = Entrada1.readlines()
    lineasResultados = Entrada2.readlines()
    inicio1 = eval(lineasParametros[0])
    objetivo1 = eval(lineasParametros[1])
    matriz1 = eval(lineasParametros[2])
    inicio2 = eval(lineasParametros[3])
    objetivo2 = eval(lineasParametros[4])
    matriz2 = eval(lineasParametros[5])
    inicio3 = eval(lineasParametros[6])
    objetivo3 = eval(lineasParametros[7])
    matriz3 = eval(lineasParametros[8])
    inicio4 = eval(lineasParametros[9])
    objetivo4 = eval(lineasParametros[10])
    matriz4 = eval(lineasParametros[11])
    resultado1 = eval(lineasResultados[0])
    resultado2 = eval(lineasResultados[1])
    resultado3 = eval(lineasResultados[2])
    resultado4 = eval(lineasResultados[3])
    assert resolvedorLaberinto.buscaCamino(matriz1, inicio1, objetivo1) == resultado1
    assert resolvedorLaberinto.buscaCamino(matriz2, inicio2, objetivo2) == resultado2
    assert resolvedorLaberinto.buscaCamino(matriz3, inicio3, objetivo3) == resultado3
    assert resolvedorLaberinto.buscaCamino(matriz4, inicio4, objetivo4) == resultado4

# Testeamos la funcion DFS
# Se testea la lista de lista de tuplas de ints que representan los padres de cada nodo luego del bfs, que se modifica por referencia
# En test3-1.txt, por test, tenemos una linea con el inicio, una linea con el fin, y una linea con el laberinto como es devuelto por leer archivo
# En test3-2.txt, por test, tenemos una lista de listas de tuplas de 2 ints, donde para cada nodo, guardamos el padre, que seria el nodo de donde se llego, o (-1,-1) si no fue revisado o es una pared
def test_DFS():
    Entrada1 = open("tests/test3-1.txt", "r")
    Entrada2 = open("tests/test3-2.txt", "r")
    lineasParametros = Entrada1.readlines()
    lineasResultados = Entrada2.readlines()
    solucion1 = []
    solucion2 = []
    inicio1 = eval(lineasParametros[0])
    objetivo1 = eval(lineasParametros[1])
    matriz1 = eval(lineasParametros[2])
    inicio2 = eval(lineasParametros[3])
    objetivo2 = eval(lineasParametros[4])
    matriz2 = eval(lineasParametros[5])
    resultado1 = eval(lineasResultados[0])
    resultado2 = eval(lineasResultados[1])
    resolvedorLaberinto.DFS(matriz1, inicio1, objetivo1, solucion1)
    resolvedorLaberinto.DFS(matriz2, inicio2, objetivo2, solucion2)
    assert solucion1 == resultado1
    assert solucion2 == resultado2
