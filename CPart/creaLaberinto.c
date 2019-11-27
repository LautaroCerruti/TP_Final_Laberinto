#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#define MaxLinea 200

void setDefaultMatrix(char **matrix, int dimension){
    int iterador = 0;
    char *arrayCeros = (char*) malloc(sizeof(char)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        arrayCeros[iterador] = '0';
    }
    for(iterador = 0; iterador < dimension; ++iterador){
        strcpy(matrix[iterador], arrayCeros);
    }
}

void generaObstaculosAleatorios(char** matrix, int cantidadAleatorios, int dimension){
    int yPunto, xPunto;
    for(int iterador = 0; iterador < cantidadAleatorios;){
        yPunto = rand() % dimension;
        xPunto = rand() % dimension;
        if(matrix[yPunto][xPunto] == '0'){
            matrix[yPunto][xPunto] = '1';
            ++iterador;
        }
    }
}

char** leeYGeneraLaberinto(FILE* entrada, int dimension){
    int iterador, yEntidad, xEntidad, cantAleatorios, noValido = 1;
    char **matrix, buffer[MaxLinea];
    matrix = (char**) malloc(sizeof(char*)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[iterador] = (char*) malloc(sizeof(char)*dimension);
    }
    setDefaultMatrix(matrix, dimension);
    fgets(buffer, MaxLinea, entrada);
    while (fgetc(entrada) == '(' && noValido)
    {
        fscanf(entrada, "%d,%d)\n", &yEntidad, &xEntidad);
        if(matrix[yEntidad-1][xEntidad-1]=='0' && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
            matrix[yEntidad-1][xEntidad-1]='1';
        } else{
            noValido = 0;
        }
    }
    if(noValido){
        fgets(buffer, MaxLinea, entrada);
        fscanf(entrada, "%d\n", &cantAleatorios);
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
            for(iterador2 = 0; iterador2 < dimension; ++iterador2){
                fputc(matrix[iterador][iterador2], salida);
            }
            fputc('\n', salida);
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