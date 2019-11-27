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

char** leeYGeneraLaberinto(FILE* entrada){
    int dimension, iterador;
    char **matrix, buffer[MaxLinea];
    fgets(buffer, MaxLinea, entrada);
    fscanf(entrada, "%d\n", &dimension);
    matrix = (char**) malloc(sizeof(char*)*dimension);
    for(iterador = 0; iterador < dimension; ++iterador){
        matrix[iterador] = (char*) malloc(sizeof(char)*dimension);
    }
    setDefaultMatrix(matrix, dimension);
    
}

int main(){
    int iterador;
    char **matrix;
    srand(time(NULL));
    FILE *entrada, *salida;
    entrada = fopen("Entrada.txt","r");
    matrix = leeYGeneraLaberinto(entrada);
    fclose(entrada);
    return 0;
}