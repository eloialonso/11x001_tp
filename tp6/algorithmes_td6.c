#include <stdio.h>

int liste_est_triee(int liste[], int size) {
    for (int i = 0; i < size - 1; i++) {
        if (liste[i] > liste[i + 1]) {
            return 0;
        }
    }
    return 1;
}

void echanger_td6(int liste[], int i, int j) {
    int tmp = liste[i];
    liste[i] = liste[j];
    liste[j] = tmp;
    return;
}

void tri_par_selection(int liste[], int size) {
    for(int i = 0; i < size - 1; i++) {
        int min = i;

        for(int j = i + 1; j < size; j++) {
            if(liste[min] > liste[j]) {
                min = j;
            }
        }

        if(min != i) {
            echanger_td6(liste, i, min);
        }
    }
}

void tri_a_bulles(int liste[], int size) {
    int swap;
    do {
        swap = 0;
        for (int i = 1; i < size; i++) {
            if (liste[i - 1] > liste[i]) {
                echanger_td6(liste, i - 1, i);
                swap = 1;
            }
        }
    } while (swap);
    return ;
}

void tri_cocktail(int liste[], int size) {
    int swap;
    do {
        swap = 0;
        for (int i = 1; i < size; i++) {
            if (liste[i - 1] > liste[i]) {
                echanger_td6(liste, i - 1, i);
                swap = 1;
            }
        }
        if (!swap) {
            break;
        }
        swap = 0;
        for (int i = size - 1; i > 0; i--) {
            if (liste[i - 1] > liste[i]) {
                echanger_td6(liste, i - 1, i);
                swap = 1;
            }
        }
    } while (swap);
    return ;
}
