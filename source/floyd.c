//
// Created by patch on 05/12/22.
//

#include "../header/floyd.h"
const int MAX_INT = 99999999;

int ** initMatrice(int n){
    int ** m = (int**) malloc(n*sizeof(int*));

    for(int i = 0; i < n; i++)
    {
        m[i] = (int*) malloc(n*sizeof(int));
        for (int j = 0; j < n; ++j) {
            if(i == j)
                m[i][j] = 0;
            else
                m[i][j] = MAX_INT;
        }
    }

    return m;
}
void grapheToMatrice(graph *g, int ** matrice){
    cell *p;
    for (int i = 0; i < g->n; ++i) {
        p = g->links[i]->prem;
        while (p != NULL){
            matrice[i][p->node] = 1;
            p = p->suiv;
        }
    }
}

int ** floyd(int **matriceAdj, int n){
    int sum_ik_kj = 0;

    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                sum_ik_kj = matriceAdj[i][k] + matriceAdj[k][j];

                if (sum_ik_kj < matriceAdj[i][j]){
                    matriceAdj[i][j] = sum_ik_kj;
                }
            }

        }
    }
    return matriceAdj;
}

float distanceMoyenneFloyd(int **mAdj, int n){
    float somme = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i < j){
                somme += (float) mAdj[i][j];
            }
        }
    }

    float den = ((float)(n* (n - 1)))/2;
    return somme / den;
}

int diametreFloyd(int **mAdj, int n){
    int max = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (max < mAdj[i][j]){
                max = mAdj[i][j];
            }
        }
    }
    return max;
}

void freeMatrice(int **matrice, int n){
    for(int i = 0; i < n; i++)
    {
        free(matrice[i]);
    }
    free(matrice);
}