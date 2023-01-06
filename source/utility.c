
#include "../header/utility.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

///////////////////////////////////////////////////////////
////////////////   UTILITY FUNCTIONS   ////////////////////
///////////////////////////////////////////////////////////
bool inArray(const int *array, int value, int length){
    bool  inArray = false;

    for (int j = 0; j < length; j++) {
        if (array[j] == value){
            inArray = true;
            break;
        }
    }

    return inArray;
}

int* randomNodes(int max, int length) {
    srand(time(NULL));
    int *choices = (int*) malloc(length * sizeof(int));
    int i, choice;

    if (length == max) { // Pas de choix aléatoire
        for (i = 0; i < length; ++i) {
            choices[i] = i;
        }
    } else {
        for (i = 0; i < length; ++i) {
            choices[i] = -1;
        }

        i = 0;
        while (i < length){
            choice = rand() % max;
            if (!inArray(choices, choice, i)){
                choices[i] = choice;
                i++;
            }
        }

    }

    return choices;
}

int* bfs(graph *g, int root, int *distance){
    int *pere = (int*) malloc(g->n * sizeof(int));
    int *visited = (int*) malloc(g->n * sizeof(int));
    nodl *l = (nodl *)malloc(sizeof(nodl));
    cell *p, *itr;

    for (int i = 0; i < g->n; ++i) {
        distance[i] = 0;
        visited[i]=false;
    }

    init_vide(l);
    inserer_si_absent(root, l);
    visited[root]=true;
    pere[root] = root;

    while (!is_empty(l)){
        itr = l->prem;

        p = g->links[itr->node]->prem;
        while (p != NULL){
            if (visited[p->node]==false){
                visited[p->node]=true;
                inserer_si_absent(p->node, l);
                distance[p->node] = distance[itr->node] + 1;
                pere[p->node] = itr->node;
            }
            p = p->suiv;
        }

        supprimer(itr, l);
    }

    return pere;
}

double distanceMoyenne(graph *g, int tailleEchantillon){
    double somme = 0; int max = 0;
    int *choices = randomNodes(g->n, tailleEchantillon);
    int *distance = (int*) malloc(g->n * sizeof(int));

    for (int i = 0; i < tailleEchantillon; ++i) {
        fprintf(stdout,"noeud bfs actuel %d sur %d\n", i, tailleEchantillon);
        bfs(g, choices[i], distance);

        for (int j = 0; j < g->n; ++j) {
            somme += (double) distance[j];

            // Ajouter ici pour avoir de diametre de suite et éviter de recalculer une deuxième fois pour le diametre
            if (max < distance[j]) {
                max = distance[j];
            }

            // supprimer les doublons
            if (j >= choices[i]){
                if (inArray(choices, j, tailleEchantillon)){
                    somme -= (double) distance[j];
                }
            }
        }
    }

    double den = (double)(tailleEchantillon * (g->n - 1));
    den -= ((double) (tailleEchantillon * (tailleEchantillon - 1))) / 2;

    fprintf(stdout,"diametre = %d\n", max);

    return somme / den;
}

int diametre(graph *g) {
    int max = 0;
    int *choices = randomNodes(g->n, g->n);
    int *distance = (int *) malloc(g->n * sizeof(int));

    for (int i = 0; i < g->n; ++i) {
        bfs(g, choices[i], distance);

        for (int j = 0; j < g->n; ++j) {
            if (max < distance[j]) {
                max = distance[j];
            }
        }
    }

    return max;
}

void report_error(char *s){
  fprintf(stderr,"%s\n",s);
  exit(-1);
}

void extraction(graph *g, int bestNode){
    FILE *dataOut, *correspondOut;
    dataOut = fopen("data/data.txt", "w");
    correspondOut = fopen("data/correspondence.txt", "w");

    int i, *visited, *comp;
    nodl *l = NULL;

    if( (l=(nodl *)malloc(sizeof(nodl))) == NULL )
        report_error("graph_from_file: malloc() error 3");
    if( (visited=(int*)malloc(g->n*sizeof(int))) == NULL )
        report_error("graph_from_file: malloc() error 3");
    if( (comp=(int*)malloc(g->n*sizeof(int))) == NULL )
        report_error("graph_from_file: malloc() error 3");

    for (i=0;i<g->n;i++){
        visited[i]=false;
    }

    int nb=0;
    cell *p, *itr;

    init_vide(l);
    inserer_si_absent(bestNode, l);
    visited[bestNode]=true;
    comp[nb]=bestNode;
    nb++;

    while (!is_empty(l)){
        itr = l->prem;

        p = g->links[itr->node]->prem;
        while (p != NULL){
            if (visited[p->node]==false){
                visited[p->node]=true;
                inserer_si_absent(p->node, l);

                comp[nb]=p->node;
                nb++;
            }
            p = p->suiv;
        }

        supprimer(itr, l);
    }

    fprintf(correspondOut,"newname lastname\n");
    for (i=0;i<nb;i++){
        fprintf(correspondOut,"%d %d\n", i, comp[i]);
    }

    int* corres;
    if( (corres=(int*)malloc(g->n*sizeof(int))) == NULL )
        report_error("graph_from_file: malloc() error 3");

    for (i=0;i<nb;i++){
        corres[comp[i]]=i;
    }

    fprintf(dataOut,"%d\n",nb);
    for (i=0;i<nb;i++){
        p=g->links[comp[i]]->prem;
        while (p!=NULL) {
            if (visited[p->node]==1) {
                if (i < corres[p->node])
                    fprintf(dataOut,"%d %d\n", i, corres[p->node]);
            }
            p=p->suiv;
        }
    }
}

void distributionDistance(graph *g){
    FILE *dataOut;
    char filename[500];
    double p = 0;
    int *choices = randomNodes(g->n, g->n);
    int *distance = (int*) malloc(g->n * sizeof(int));
    int *output = (int*) malloc(20 * sizeof(int)); // Le diametre max des réseaux étudiés est 17, donc pas besoin d'un plus grand tableau
    for (int i = 0; i < 20; ++i) {
        output[i] = 0;
    }
    for (int i = 0; i < g->n; ++i) {
        fprintf(stdout,"noeud bfs actuel %d sur %d\n", i, g->n); // utile de le savoir lorsqu'on fait des calculs sur un réseau énorme
        bfs(g, choices[i], distance);

        for (int j = 0; j < g->n; ++j) {
            if (i < j) {
                output[distance[j]] += 1;
                p++;
            }
        }

        // Ecriture dans le fichier de sortie à chaque 1000 noeuds pour suivre l'évolution
        if (i % 1000 == 0) {
            sprintf( filename,"data/distribution_distance_%d.txt", i);
            dataOut = fopen(filename, "w");
            for (int j = 0; j < 20; j++){
                if (output[j] > 0) {
                    fprintf(dataOut,"%d %d %lf\n", j, output[j],  output[j]/p);
                }
            }
            fclose(dataOut);
        }
    }

    // Ecriture dans le fichier de sortie si tous les calculs ont été faits
    dataOut = fopen("data/distribution_distance.txt", "w");
    for (int i=0; i<20; i++){
        if (output[i] > 0) {
            fprintf(dataOut,"%d %d %lf\n", i, output[i],  output[i]/p);
        }
    }
    fclose(dataOut);
}