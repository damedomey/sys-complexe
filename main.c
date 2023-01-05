
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "header/utility.h"
#include "header/graph.h"
#include "header/floyd.h"

// print help
void usage(char *c){
    fprintf(stderr,"Usage: %s -h\n",c);
    fprintf(stderr,"  -h: print current help.\n");
    fprintf(stderr,"  -i \"inputname\": input file containing the graph (default value is stdin).\n");
    fprintf(stderr,"  -o \"outputname\": output results in a file named \"outputname\" (default value is stdout).\n");
    fprintf(stderr,"  -e \"bestNode\": start computation from node with max degree (best node)\n");
    exit(-1);
}

/***************************  MAIN  ***************************/

int main(int argc, char **argv){
//////////   DECLARATIONS AND DEFAULT VALUES   ////////////

    FILE* fin=NULL;
    FILE* fout=NULL;

    int i;

////////////////   PARSE COMMAND LINE   ///////////////////

    // default values
    char name_in[100]="";
    char name_out[100]="";
    int input_file_given=0;
    int output_file_given=0;
    int bestNode = -1; // Node with max degree

    // user's values
    for (i=1; i<argc; i++) {
        if ((strcmp(argv[i],"-h")==0) || (strcmp(argv[i],"--help")==0) ) {
            usage(argv[0]);
        }
        else if ((strcmp(argv[i],"-i")==0) || (strcmp(argv[i],"--input")==0) ) {
            if (i==argc-1)
                usage(argv[0]);
            input_file_given=1;
            strcpy(name_in,argv[++i]);
        }
        else if ((strcmp(argv[i],"-o")==0) || (strcmp(argv[i],"--output")==0) ) {
            if (i==argc-1)
                usage(argv[0]);
            output_file_given=1;
            strcpy(name_out,argv[++i]);
        }
        else if ((strcmp(argv[i],"-e")==0) || (strcmp(argv[i],"--extraction")==0) ) {
            if (i==argc-1)
                usage(argv[0]);
            bestNode = atoi(argv[++i]);
        }
        else usage(argv[0]);
    }

///////////////////   OPEN FILES   ////////////////////////

    if (input_file_given==0) {
        fin=stdin;
    }
    else {
        if ( (fin=fopen(name_in,"r"))==NULL)
            report_error("name_in -- fopen: error");
    }

    if (output_file_given==0)
        fout=stdout;
    else {
        if ( (fout=fopen(name_out,"w"))==NULL)
            report_error("name_out -- fopen: error");
    }

///////////////////   TREATMENT   /////////////////////////

    graph * g = graph_from_file(fin);
    int n = g->n, m = g->m;
    fprintf(stdout,"n = %d; m = %d\n", n, m);

    if (bestNode != -1) {
        extraction(g, bestNode);
    }

    // Question 4: densité et degré
    double densite, degre;
    densite = (double)m / (((double)(n*(n-1)))/ 2.0);
    degre = (double) (2*m)/(double)n;
    fprintf(stdout,"densite = %lf; degré moyen = %lf\n", densite, degre);

    // fprintf(stdout,"distance moyenne = %f\n", distanceMoyenne(g, 200));
    // fprintf(stdout,"diametre = %d\n", diametre(g));
    distributionDistance(g);
    // J'ai préféré continuer avec python(networkx)

////////////   CLOSE FILES AND FREE MEMORY  ///////////////

    if (fin!=NULL) {
        fclose(fin);
        fprintf(stdout,"Input file closed.\n");
        fflush(stdout);
    }

    if (fout!=NULL) {
        fclose(fout);
        fprintf(stdout,"Output file closed.\n");
        fflush(stdout);
    }
    return 0;
}

/*************************  FIN MAIN  *************************/
