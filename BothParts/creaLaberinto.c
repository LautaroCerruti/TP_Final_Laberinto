#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MaxLinea 100

/*
    charReplace: char* char char -> int
    Toma un array de char, un caracter c1 y un caracter c2
    Reemplaza todas las apariciones en el array de c1 con c2
    Retorna la cantidad de apariciones de c1
*/
int charReplace(char* string, char c1, char c2){
    int cantidad = 0, iterador;
    for(iterador = 0; string[iterador] != '\0'; ++iterador){
        if(string[iterador] == c1) {
            string[iterador] = c2;
            ++cantidad;
        }
    }
    return cantidad;
}

/*
    setDefaultMatrix: char** int char
    Toma un array bidimensional de char que representa el laberinto, el tamaño de cada dimension de la matriz y un caracter C
    Guarda en todos los caracteres de la matriz, el caracter ingresado
*/
void setDefaultMatrix(char **matrix, int dimension, char c){
    int iterador = 0;
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[0][iterador] = c;
    }
    matrix[0][dimension] = '\0';
    for(iterador = 1; iterador < dimension; ++iterador){
        strcpy(matrix[iterador], matrix[0]);
    }
}

/*
    generaObstaculosAleatorios: char** int int char
    Toma un array bidimensional de char, la cantidad de obstaculos a generar, el tamaño de cada dimension de la matriz y un caracter C
    Modifica la matriz, para que tenga la cantidad de obstaculos aleatorios requridos
    El caracter que se ingresa tiene que ser el que se uso para la matriz predeterminada
    Si el caracter ingresado es '1', se completa la matriz con lugares libres '0'
    Si el caracter ingresado es '0', se completa la matriz con obstaculos'1'
*/
void generaObstaculosAleatorios(char** matrix, int cantidadAleatorios, int dimension, char c){
    int yPunto, xPunto, iterador;
    if(c=='1'){ // Si se requerian poner mas obstaculos que lugares libres, se lleno la matriz de 1 y se generan 0 randoms
        for(iterador = 0; iterador < dimension*dimension-cantidadAleatorios;){
            yPunto = rand() % dimension;
            xPunto = rand() % dimension;
            if(matrix[yPunto][xPunto] == c){
                matrix[yPunto][xPunto] = '0';
                ++iterador;
            }
        }
    } else {    // Si no, se lleno la matriz de 0 y se generan los obstaculos de forma random
        for(iterador = 0; iterador < cantidadAleatorios;){
            yPunto = rand() % dimension;
            xPunto = rand() % dimension;
            if(matrix[yPunto][xPunto] == c){
                matrix[yPunto][xPunto] = '1';
                ++iterador;
            }
        }
    }
}

/*
    leeYGeneraLaberinto: FILE* int char** -> int
    Toma un archivo, la dimension del laberinto y el array bidimensional donde se esta almacenando
    Esta funcion lee el archivo, y genera el laberinto con todas las cosas que alli se especifican
    Tambien valida algunas cosas como que no se pidan mas numeros aleatorios que el tamaño del laberinto, que no se repitan las posiciones
    ya sean de obstaculos, inicio o objetivo
    Retorna un int, que es 0 si no fue valida la entrada del archivo, 1 si lo fue
*/
int leeYGeneraLaberinto(FILE* entrada, int dimension, char **matrix){
    int iterador, yEntidad, xEntidad, cantAleatorios, valido = 1, cantFijos = 0, transformaFijos = 0;
    char buffer[MaxLinea], relleno;
    fgets(buffer, MaxLinea, entrada);
    while (fgetc(entrada) == '(' && valido)
    {
        fgets(buffer, MaxLinea, entrada);
        ++cantFijos;
    }
    fgets(buffer, MaxLinea, entrada);
    fscanf(entrada, "%d\n", &cantAleatorios);
    if(cantAleatorios > (dimension*dimension-2-cantFijos)) valido = 0;
    if(valido){
        if(cantAleatorios <= ((dimension*dimension)/2)) relleno = '0';
        else relleno='1';
        setDefaultMatrix(matrix, dimension, relleno);
        rewind(entrada);    //Hacemos un rewind, ya que lee hasta la cantidad de aleatorios para saber con que rellenar la matriz
        fgets(buffer, MaxLinea, entrada);
        fgets(buffer, MaxLinea, entrada);
        fgets(buffer, MaxLinea, entrada);

        while (fscanf(entrada, "(%d,%d)\n", &yEntidad, &xEntidad) && valido)
        {
            if(matrix[yEntidad-1][xEntidad-1]==relleno && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
                matrix[yEntidad-1][xEntidad-1]='F'; // Los fijos los guardamos momentaneamente como una F, luego los cambiamos por 1
            } else{
                valido = 0;
            }
        }
        if(valido){
            fgets(buffer, MaxLinea, entrada);
            fgets(buffer, MaxLinea, entrada);
            fgets(buffer, MaxLinea, entrada);
            fscanf(entrada, "(%d,%d)\n", &yEntidad, &xEntidad);
            if(matrix[yEntidad-1][xEntidad-1]==relleno && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
                matrix[yEntidad-1][xEntidad-1]='I';
            } else{
                valido = 0;
            }
            if(valido){
                fgets(buffer, MaxLinea, entrada);
                fscanf(entrada, "(%d,%d)\n", &yEntidad, &xEntidad);
                if(matrix[yEntidad-1][xEntidad-1]==relleno && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
                    matrix[yEntidad-1][xEntidad-1]='X';
                    generaObstaculosAleatorios(matrix, cantAleatorios, dimension, relleno);
                    for(iterador = 0; transformaFijos < cantFijos && iterador < dimension; ++iterador){
                        transformaFijos += charReplace(matrix[iterador], 'F', '1');
                    }
                } else{
                    valido = 0;
                }
            }
        }
    }
    return valido;
}

/*
    imprimeLaberinto: FILE* char** int
    Toma un archivo, un array bidimensional que representa el laberinto y la dimension del mismo
    Imprime en el archivo el laberinto
*/
void imprimeLaberinto(FILE* salida, char** matrix, int dimension){
    int iterador, iterador2;
    for(iterador = 0; iterador < dimension; ++iterador){
        fprintf(salida, "%s\n", matrix[iterador]);
    }
}

int main(int argc, char *argv[]){
    int iterador, dimension, generoBandera;
    char **matrix, buffer[MaxLinea];
    srand(atoi(argv[3]));
    FILE *entrada, *salida;
    entrada = fopen(argv[1],"r");
    fgets(buffer, MaxLinea, entrada);
    fscanf(entrada, "%d\n", &dimension);
    matrix = (char**) malloc(sizeof(char*)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[iterador] = (char*) malloc(sizeof(char)*(dimension+1));
    }
    generoBandera = leeYGeneraLaberinto(entrada, dimension, matrix);
    fclose(entrada);
    if(generoBandera){
        salida = fopen(argv[2],"w+");
        imprimeLaberinto(salida, matrix, dimension);
        fclose(salida);
    } else {
        printf("No se pudo generar el laberinto, entrada invalida\n");
    }
    for(iterador = 0; iterador < dimension; ++iterador){
        free(matrix[iterador]);
    }
    free(matrix);
    return generoBandera;
}