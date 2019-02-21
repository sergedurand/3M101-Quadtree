#include<stdio.h> 
#include<stdlib.h> 
#include<time.h>
   
struct noeud 
{ 
    int cle; 
    struct noeud *gauche, *droite; 
}; 
   
// Fonction de création d'un noeud
struct noeud *newNoeud(int item) 
{ 
    struct noeud *temp =  (struct noeud *)malloc(sizeof(struct noeud)); 
    temp->cle = item; 
    temp->gauche = temp->droite = NULL; 
    return temp; 
} 

struct noeud * valMinNoeud(struct noeud* noeud) 
{ 
    struct noeud* current = noeud; 
  
    //Boucle pour trouver la feuille la plus à gauche
    while (current->gauche != NULL) 
        current = current->gauche; 
  
    return current; 
} 
   
// Parcours préfixe de l'arbre
void inorder(struct noeud *root) 
{ 
    if (root != NULL) 
    { 
        inorder(root->gauche); 
        printf("%d \n", root->cle); 
        inorder(root->droite); 
    } 
} 
   
/* Fonction d'insertion d'une clé dans l'arbre */
struct noeud* insertion(struct noeud* noeud, int cle) 
{ 
    /* Si l'arbre est vide, retourner un nouveau noeud */
    if (noeud == NULL) return newNoeud(cle); 
  
    /* Sinon, récursion */
    if (cle < noeud->cle) 
        noeud->gauche  = insertion(noeud->gauche, cle); 
    else if (cle > noeud->cle) 
        noeud->droite = insertion(noeud->droite, cle);    
  
    /* On retourne le pointeur inchangé sur le noeud si cle==noeud->cle */
    return noeud; 
} 


// Fonction de recherche
struct noeud* recherche(struct noeud* root, int cle) 
{ 
    // Cas de base: Racine nulle ou clé égale à la racine
    if (root == NULL || root->cle == cle) 
       return root; 
     
    if (root->cle < cle) 
       return recherche(root->droite, cle); 
  
    return recherche(root->gauche, cle); 
} 


/* Fonction de suppression d'une clé */
struct noeud* suppressionNoeud(struct noeud* root, int cle) 
{ 
    // Cas de base
    if (root == NULL) return root; 
  
    // Si la clé à supprimer est plus petite que la clé courante, on explore à gauche
    if (cle < root->cle) 
        root->gauche = suppressionNoeud(root->gauche, cle); 

    else if (cle > root->cle) 
        root->droite = suppressionNoeud(root->droite, cle); 
  
    //Si la clé est égale à la clé courante, c'est celle qu'il faut supprimer
    else
    { 
        // Noeud avec un fils ou aucun fils
        if (root->gauche == NULL) 
        { 
            struct noeud *temp = root->droite; 
            free(root); 
            return temp; 
        } 
        else if (root->droite == NULL) 
        { 
            struct noeud *temp = root->gauche; 
            free(root); 
            return temp; 
        } 
  
        // Noeud avec 2 fils: on prend le plus petit à droite
        struct noeud* temp = valMinNoeud(root->droite); 
  
        // On copie le contenu du successeur dans ce noeud
        root->cle = temp->cle; 
  
        // On supprime le successeur
        root->droite = suppressionNoeud(root->droite, temp->cle); 
    } 
    return root; 
} 

int main() 
{ 
    struct noeud *root = NULL; 
    root=insertion(root,100000);
    int i;
    for (i=0;i<200000;i++){
	if (i!=99999)
	root=insertion(root,i);
    }
  /*
    double time_spent2=0.0;
    double time_spent=0.0;
    for (i=0;i<20;i++){
	/*clock_t begin2 = clock();
        root=recherche(root,75000);
        clock_t end2 = clock();
        time_spent2+=(double) (end2-begin2)/CLOCKS_PER_SEC;
        printf("recherche: %lf\n",time_spent2);

	clock_t begin = clock();
        root = suppressionNoeud(root,75000);
        clock_t end = clock();
        time_spent+=(double) (end-begin)/CLOCKS_PER_SEC;
	printf("suppression: %lf\n",time_spent);*/
	clock_t begin = clock();
        root=insertion(root,99999);
        clock_t end = clock();
        time_spent+=(double) (end-begin)/CLOCKS_PER_SEC;
	printf("insertion: %f\n",(double) (end-begin)/CLOCKS_PER_SEC);

    }
    printf("time spent2: %lf\n",time_spent2);
    printf("insertion: %lf\n",time_spent/i);
   // printf("recherche: %lf\n",time_spent2/20.0);
    


	



    //inorder(root); 
  
    return 0; 
} 

