#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#define MaxLinea 100

void setDefaultMatrix(char **matrix, int dimension){
    int iterador = 0;
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[0][iterador] = '0';
    }
    matrix[0][dimension] = '\0';
    for(iterador = 1; iterador < dimension; ++iterador){
        strcpy(matrix[iterador], matrix[0]);
    }
}

void swapCoordinates(int ***arrayCoordenadas, int yNumero, int xNumero, int yUltimoNumero, int xUltimoNumero){
    int x, y;
    y = arrayCoordenadas[yNumero][xNumero][0];
    x = arrayCoordenadas[yNumero][xNumero][1];
    arrayCoordenadas[yNumero][xNumero][0] = arrayCoordenadas[yUltimoNumero][xUltimoNumero][0];
    arrayCoordenadas[yNumero][xNumero][1] = arrayCoordenadas[yUltimoNumero][xUltimoNumero][1];
    arrayCoordenadas[yUltimoNumero][xUltimoNumero][0] = y;
    arrayCoordenadas[yUltimoNumero][xUltimoNumero][1] = x;
}

void generaObstaculosAleatorios(char** matrix, int cantidadAleatorios, int dimension){
    int numeroRandom, iterador, yPunto, xPunto, ***arrayCoordenadas, iteradorSwaps=0, iterador2 = 0, random1, random2;
    arrayCoordenadas = (int***) malloc(sizeof(int**)*dimension);

    for(iterador = 0; iterador < dimension; ++iterador){
        arrayCoordenadas[iterador] = (int**) malloc(sizeof(int*)*dimension);
        for(iterador2 = 0; iterador2 < dimension; ++iterador2){
            arrayCoordenadas[iterador][iterador2] = (int*) malloc(sizeof(int)*2);
            arrayCoordenadas[iterador][iterador2][0] = iterador;
            arrayCoordenadas[iterador][iterador2][1] = iterador2;
        }
    }
    for(iterador = 0; iterador < cantidadAleatorios;){
        random1 = rand() % (dimension-(iteradorSwaps/dimension));
        if(random1 == (dimension-(iteradorSwaps/dimension)-1)){
            random2 = rand() % (dimension-(iteradorSwaps%dimension));
        }
        else
        {
            random2 = rand() % dimension;
        }
        yPunto = arrayCoordenadas[random1][random2][0];
        xPunto = arrayCoordenadas[random1][random2][1];
        if(matrix[yPunto][xPunto] == '0'){
            matrix[yPunto][xPunto] = '1';
            ++iterador;
        }
        swapCoordinates(arrayCoordenadas, random1, random2, (dimension-(iteradorSwaps/dimension)-1), (dimension-(iteradorSwaps%dimension))-1);
        iteradorSwaps++;
    }
}

char** leeYGeneraLaberinto(FILE* entrada, int dimension){
    int iterador, yEntidad, xEntidad, cantAleatorios, noValido = 1, cantFijos = 0;
    char **matrix, buffer[MaxLinea];
    matrix = (char**) malloc(sizeof(char*)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[iterador] = (char*) malloc(sizeof(char)*(dimension+1));
    }
    setDefaultMatrix(matrix, dimension);
    fgets(buffer, MaxLinea, entrada);
    while (fgetc(entrada) == '(' && noValido)
    {
        fscanf(entrada, "%d,%d)\n", &yEntidad, &xEntidad);
        if(matrix[yEntidad-1][xEntidad-1]=='0' && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
            matrix[yEntidad-1][xEntidad-1]='1';
            ++cantFijos;
        } else{
            noValido = 0;
        }
    }
    if(noValido){
        fgets(buffer, MaxLinea, entrada);
        fscanf(entrada, "%d\n", &cantAleatorios);
        if(cantAleatorios > (dimension*dimension-2-cantFijos)){
            noValido = 0;
        }
        fgets(buffer, MaxLinea, entrada);
        fscanf(entrada, "(%d,%d)\n", &yEntidad, &xEntidad);
        if(matrix[yEntidad-1][xEntidad-1]=='0' && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
            matrix[yEntidad-1][xEntidad-1]='I';
        } else{
            noValido = 0;
        }
        if(noValido){
            fgets(buffer, MaxLinea, entrada);
            fscanf(entrada, "(%d,%d)\n", &yEntidad, &xEntidad);
            if(matrix[yEntidad-1][xEntidad-1]=='0' && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
                matrix[yEntidad-1][xEntidad-1]='X';
                generaObstaculosAleatorios(matrix, cantAleatorios, dimension);
            } else{
                noValido = 0;
            }
        }
    }
    if(!noValido){
        for(iterador = 0; iterador < dimension; ++iterador){
            free(matrix[iterador]);
        }
        free(matrix);
        return NULL;
    } else
    {
        return matrix;
    }
}

void imprimeLaberinto(FILE* salida, char** matrix, int dimension){
    int iterador, iterador2;
    if(matrix == NULL){
        fprintf(salida, "No se pudo generar el laberinto\n");
    } else {
        for(iterador = 0; iterador < dimension; ++iterador){
            fprintf(salida, "%s\n", matrix[iterador]);
        }
    }
}

int main(){
    int iterador, dimension;
    char **matrix, buffer[MaxLinea];
    srand(time(NULL));
    FILE *entrada, *salida;
    entrada = fopen("Entrada.txt","r");
    fgets(buffer, MaxLinea, entrada);
    fscanf(entrada, "%d\n", &dimension);
    matrix = leeYGeneraLaberinto(entrada, dimension);
    fclose(entrada);
    salida = fopen("salidaLaberinto.txt","w+");
    imprimeLaberinto(salida, matrix, dimension);
    fclose(salida);
    for(iterador = 0; iterador < dimension; ++iterador){
        free(matrix[iterador]);
    }
    free(matrix);
    return 0;
}