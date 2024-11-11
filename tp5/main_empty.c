#include <stdio.h>
#include <stdlib.h>

/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/

// EXERCICE 1

int liste_est_triee(int liste[], int size) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

// EXERCICE 2

void echanger(int liste[], int i, int j) {
    int tmp = liste[i];
    liste[i] = liste[j];
    liste[j] = tmp;
    return;
}

void tri_par_selection(int liste[], int size) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

// EXERCICE 3

void tri_a_bulles(int liste[], int size) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
    return ;
}

// EXERCICE 4

void tri_cocktail(int liste[], int size) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
    return ;
}

/****************************/
/* Vos fonctions ci-dessus **/
/****************************/

void afficher_liste(int liste[], int size) {
    for (int i = 0; i < size - 1; i++) {
        printf("%d, ", *(liste + i));
    }
    printf("%d\n", *(liste + size - 1));
}

void generer_liste_aleatoire(int* p, int size) {
    for (int i = 0; i < size; i++) {
        p[i] = (int) (100.0 * (float) rand() / (float) RAND_MAX);
    }
}

void exercice1(void) {
    printf("\n\n***************************************\n");
    printf("** EXERCICE 1 - Vérifier liste triée **\n");
    printf("***************************************\n\n");
    
    int liste1[] = {13, 10, 84, 23, 1, 8, 85, 92, 8, 37, 56, 71, 49, 77, 57, 95, 34, 98, 75, 97};
    int size1 = sizeof(liste1) / sizeof(int);
    printf("%d\n", liste_est_triee(liste1, size1));
    
    int liste2[] = {1, 8, 8, 10, 13, 23, 34, 37, 49, 56, 57, 71, 75, 77, 84, 85, 92, 95, 97, 98};
    int size2 = sizeof(liste2) / sizeof(int);
    printf("%d\n", liste_est_triee(liste2, size2));
    
    return;
}

void exercice2(void) {
    printf("\n\n************************************\n");
    printf("** EXERCICE 2 - Tri par sélection **\n");
    printf("************************************\n\n");

    int sizes[3] = {1, 10, 100};
    int size;
    for (int i = 0; i < 3; i++) {
        size = sizes[i];
        int l[size];
        printf("\n=== Taille de liste : %d ===\n", size);
        generer_liste_aleatoire(l, size);
        printf("\nOriginale : ");
        afficher_liste(l, size);
        tri_par_selection(l, size);
        printf("\nTriée : ");
        afficher_liste(l, size);
        printf("\n");
    }

    return;
}

void exercice3(void) {
    printf("\n\n*******************************\n");
    printf("** EXERCICE 3 - Tri à bulles **\n");
    printf("*******************************\n\n");
    
    int sizes[3] = {1, 10, 100};
    int size;
    for (int i = 0; i < 3; i++) {
        size = sizes[i];
        int l[size];
        printf("\n=== Taille de liste : %d ===\n", size);
        generer_liste_aleatoire(l, size);
        printf("\nOriginale : ");
        afficher_liste(l, size);
        tri_a_bulles(l, size);
        printf("\nTriée : ");
        afficher_liste(l, size);
        printf("\n");
    }

    return;
}

void exercice4(void) {
    printf("\n\n*******************************\n");
    printf("** EXERCICE 4 - Tri cocktail **\n");
    printf("*******************************\n\n");
    
    int sizes[3] = {1, 10, 100};
    int size;
    for (int i = 0; i < 3; i++) {
        size = sizes[i];
        int l[size];
        printf("\n=== Taille de liste : %d ===\n", size);
        generer_liste_aleatoire(l, size);
        printf("\nOriginale : ");
        afficher_liste(l, size);
        tri_cocktail(l, size);
        printf("\nTriée : ");
        afficher_liste(l, size);
        printf("\n");
    }

    return;
}

int main(void) {

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !

    exercice1();
    exercice2();
    exercice3();
    exercice4();
    
    return 0;
}
