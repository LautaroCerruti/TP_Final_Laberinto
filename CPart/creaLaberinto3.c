#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#define MaxLinea 100

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

void generaObstaculosAleatorios(char** matrix, int cantidadAleatorios, int dimension, char c){
    int yPunto, xPunto, iterador;
    if(c=='1'){
        for(iterador = 0; iterador < dimension*dimension-cantidadAleatorios;){
            yPunto = rand() % dimension;
            xPunto = rand() % dimension;
            if(matrix[yPunto][xPunto] == c){
                matrix[yPunto][xPunto] = '0';
                ++iterador;
            }
        }
    } else {
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

int charReplace(char* string, char c1, char c2){
    int cantidad = 0;
    for(int iterador = 0; string[iterador] != '\0'; ++iterador){
        if(string[iterador] == c1) {
            string[iterador] = c2;
            ++cantidad;
        }
    }
    return cantidad;
}

char** leeYGeneraLaberinto(FILE* entrada, int dimension){
    int iterador, yEntidad, xEntidad, cantAleatorios, valido = 1, cantFijos = 0, transformaFijos = 0;
    char **matrix, buffer[MaxLinea], relleno;
    matrix = (char**) malloc(sizeof(char*)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[iterador] = (char*) malloc(sizeof(char)*(dimension+1));
    }
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
        rewind(entrada);
        fgets(buffer, MaxLinea, entrada);
        fgets(buffer, MaxLinea, entrada);
        fgets(buffer, MaxLinea, entrada);

        while (fgetc(entrada) == '(' && valido)
        {
            fscanf(entrada, "%d,%d)\n", &yEntidad, &xEntidad);
            if(matrix[yEntidad-1][xEntidad-1]==relleno && yEntidad-1<dimension && xEntidad-1<dimension && yEntidad>0 && xEntidad>0){
                matrix[yEntidad-1][xEntidad-1]='F';
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
    if(!valido){
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