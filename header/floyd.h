//
// Created by patch on 05/12/22.
//

#ifndef _FLOYD_H
#define _FLOYD_H
#include <stdlib.h>
#include "graph.h"

// Initialise une matrice de taille n * n
int ** initMatrice(int n);

void grapheToMatrice(graph *g, int ** matrice);

int ** floyd(int **matriceAdj, int n);

float distanceMoyenneFloyd(int **mAdj, int n);

int diametreFloyd(int **mAdj, int n);

// Libère propement l'espace occupé par une matrice
void freeMatrice(int **matrice, int n);

#endif //_FLOYD_H
