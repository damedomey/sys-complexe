#include "../header/nodelist.h"
#include "../header/utility.h"

void init_vide (nodl* l) {
    l->prem=NULL;
    l->dern=NULL;
}
bool is_empty(nodl *l){
    if (l->prem==NULL && l->dern==NULL) {
        return true;
    } else return false;
}
void inserer_en_tete (int u, nodl* l) {

    cell* q;
    if( (q=(cell *)malloc(sizeof(cell))) == NULL )
        report_error("graph_from_file: malloc() error 1");
    q->node=u;

    if (l->dern==NULL) l->dern=q;

    q->suiv=l->prem;
    if (l->prem!=NULL) l->prem->prec=q;
    q->prec=NULL;
    l->prem=q;

}

void inserer_apres (int u, nodl* l, cell* p) {
	
	cell* q;
	if( (q=(cell *)malloc(sizeof(cell))) == NULL )
    report_error("graph_from_file: malloc() error 1");
	q->node=u;
  
	if (p->suiv==NULL) l->dern=q;
	else p->suiv->prec=q;  
    
	q->suiv=p->suiv;
	q->prec=p;
	p->suiv=q;
	
}

void inserer_si_absent(int u, nodl* l){

    cell *itr = l->prem;

    while (itr != NULL){
        if (itr->node == u) {
            return;
        }
        itr = itr->suiv;
    }
    inserer_en_queue(u, l);
}

void inserer_en_queue (int u, nodl* l) {
	
	if (l->dern!=NULL) inserer_apres (u, l, l->dern);
	else inserer_en_tete (u, l);
}

void supprimer (cell* p, nodl* l){

	if (p->prec==NULL) {
		l->prem=p->suiv;
	}
	else {
		p->prec->suiv=p->suiv;
	}
	if (p->suiv==NULL) {
		l->dern=p->prec;
	}
	else {
		p->suiv->prec=p->prec;
	}

	free(p);

}

void free_nodl(nodl* l) {
	if (l!=NULL){
		while (l->prem!=NULL) {
			supprimer(l->prem,l);
		}
		free(l);
	}	
}
