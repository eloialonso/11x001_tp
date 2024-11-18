#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "algorithmes_td6.c"

/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/

// EXERCICE 2

void echanger(int liste[], int i, int j) {
    int tmp = liste[i];
    liste[i] = liste[j];
    liste[j] = tmp;
    return;
}

int partitionner(int liste[], int premier, int dernier, int pivot) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

void tri_rapide_(int liste[], int premier, int dernier) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

void tri_rapide(int liste[], int size) {
    tri_rapide_(liste, 0, size - 1);
}

// EXERCICE 3

void fusion(int liste[], int low, int mid, int high) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

void tri_fusion_(int liste[], int low, int high) {
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus ********************/
}

void tri_fusion(int liste[], int size) {
    tri_fusion_(liste, 0, size - 1);
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

void copier_liste(int* src, int* dst, int size) {
    for (int i = 0; i < size; i++) {
        dst[i] = src[i];
    }
}

void exercice2(void) {
    printf("\n\n*****************************\n");
    printf("** EXERCICE 2 - Tri rapide **\n");
    printf("*****************************\n\n");
    
    int sizes[3] = {1, 10, 100};
    int size;
    for (int i = 0; i < 3; i++) {
        size = sizes[i];
        int l[size];
        printf("\n=== Taille de liste : %d ===\n", size);
        generer_liste_aleatoire(l, size);
        printf("\nOriginale : ");
        afficher_liste(l, size);
        tri_rapide(l, size);
        printf("\nTriée : ");
        afficher_liste(l, size);
        printf("\n");
    }

    return;
}

void exercice3(void) {
    printf("\n\n*****************************\n");
    printf("** EXERCICE 3 - Tri fusion **\n");
    printf("*****************************\n\n");
    
    int sizes[3] = {1, 10, 100};
    int size;
    for (int i = 0; i < 3; i++) {
        size = sizes[i];
        int l[size];
        printf("\n=== Taille de liste : %d ===\n", size);
        generer_liste_aleatoire(l, size);
        printf("\nOriginale : ");
        afficher_liste(l, size);
        tri_fusion(l, size);
        printf("\nTriée : ");
        afficher_liste(l, size);
        printf("\n");
    }

    return;
}

void exercice4(void) {
    printf("\n\n*******************************\n");
    printf("** EXERCICE 4 - Benchmarking **\n");
    printf("*******************************\n\n");
    
    // Paramétrage du benchmark
    int sizes[] = {100, 1000, 10000};
    int nb_repetition = 100;
    int nb_algos = 4;

    int nb_sizes = sizeof(sizes) / sizeof(int);
    int size;
    double temps_ecoule[nb_sizes][nb_algos][nb_repetition]; 
    clock_t debut, fin;

    for (int s = 0; s < nb_sizes; s++) {
        size = sizes[s];
        int l1[size], l2[size];
        printf("\n\n==== Taille de liste : %d ====\n\n", size);
        printf("Répétition n° : ");
        for (int i = 0; i < nb_repetition; i++) {
            printf("%d ", i + 1);
            fflush(stdout);
            generer_liste_aleatoire(l1, size);
            for (int j = 0; j < nb_algos; j++) {
                copier_liste(l1, l2, size);
                debut = clock();
                switch (j) {
                    case 0:
                        tri_par_selection(l2, size);
                        break;
                    case 1:
                        tri_a_bulles(l2, size);
                        break;
                    case 2:
                        tri_fusion(l2, size);
                        break;
                    case 3:
                        tri_rapide(l2, size);
                        break;
                    default:
                        break;
                };
                fin = clock();
                if (!liste_est_triee(l2, size)) {
                    printf("Erreur, liste non triée (algo %d, run %d).", j, i);
                    return;
                };
                temps_ecoule[s][j][i] = (double)(fin - debut) / CLOCKS_PER_SEC;
            };
        };
    }
    
    // Affichage des résultats du benchmark
    printf("\n\n========= RÉSULTATS =========\n\n");
    for (int s = 0; s < nb_sizes; s++) {
        size = sizes[s];
        printf("\nTemps moyen pour trier une liste de %d entiers (sur %d répétitions) :\n\n", size, nb_repetition);
        double moyenne;
        for (int j = 0; j < nb_algos; j++) {
            moyenne = 0.0;
            for (int i = 0; i < nb_repetition; i++) {
                moyenne += temps_ecoule[s][j][i];
            }
            moyenne /= nb_repetition;

            printf("- ");
            switch (j) {
                case 0:
                    printf("Tri par sélection");
                    break;
                case 1:
                    printf("Tri à bulles");
                    break;
                case 2:
                    printf("Tri fusion");
                    break;
                case 3:
                    printf("Tri rapide");
                    break;
                default:
                    break;
            };
            printf(" : %.2f ms.\n", moyenne * 1000);
        }
    }

    return;
}


int main(void) {

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !

    exercice2();
    exercice3();
    exercice4();
    
    return 0;
}
