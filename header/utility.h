

#ifndef TD_UTILITY_

#define TD_UTILITY_
#include "graph.h"


///////////////////////////////////////////////////////////
////////////////   UTILITY FUNCTIONS   ////////////////////
///////////////////////////////////////////////////////////

// Recheche un entier dans un tableau d'entier
bool inArray(const int *array, int value, int length);

int* randomNodes(int max, int length);

// precondition: graph et distance* initialisé
// postcondition: écrit les distance dans le tableau distance, retourne la liste des pères
int* bfs(graph *g, int root, int *distance);

// Calcule la distance moyenne à partir d'un échantillon
// precondition: graph *g initialisé, et la taille d'échantillonnage (le nombre de noeuds)
double distanceMoyenne(graph *g, int tailleEchantillon);

int diametre(graph *g);

void distributionDistance(graph *g);

// Extraction de la plus grande composante connexe est enregistrement du graphe dans
// data/data.txt et les correspondance dans le graphe non connecté (peut être)
// dans data/correspondence.txt
void extraction(graph *g, int bestNode);

// SORTIR DU PROGRAMME AVEC UNE ERREUR
// precondition: s pointe sur une chaine de caractere valide
// postcondition: ecrit la chaine de caractere pointee par s sur la sortie d'erreur standard et sort du programme avec le code d'erreur -1
void report_error(char *s);
#endif
