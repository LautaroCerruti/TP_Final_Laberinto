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

void generaObstaculosAleatorios(char** matrix, int cantidadAleatorios, int cantidadLibres, int dimension){
    int iterador, iterador2, librerand, contadorBlancos, x, y;
    printf("ENTRE\n");
    for(iterador = 0;iterador<cantidadAleatorios;++iterador){
        librerand = rand() % (cantidadLibres-iterador);
        contadorBlancos=0;
        for(y = 0; y < dimension && contadorBlancos < librerand; ++y){
            for(x = 0; x < dimension && contadorBlancos < librerand; ++x){
                if(matrix[y][x]=='0'){
                ++contadorBlancos;
                }
            }
        }
        matrix[y][x]='1';
    }
    printf("SALI\n");
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
                generaObstaculosAleatorios(matrix, cantAleatorios, (dimension*dimension-2-cantFijos), dimension);
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