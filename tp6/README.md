# [11X001] TD n°6

---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

**Remarque générale** :

Pour les exercices de ce TD, implémenter vos fonctions dans le fichier `main.c` dans la zone indiquée :

```
/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/



/****************************/
/* Vos fonctions ci-dessus **/ 
/****************************/
```

car le compilateur va vérifier qu'elles sont bien déclarées avant leur appel.

---

**Remarque** : Dans tout le TD, on considèrera la liste d'entiers suivante :

`13, 10, 84, 23, 1, 8, 85, 92, 8, 37, 56, 71, 49, 77, 57, 95, 34, 98, 75, 97`.

---

**Remarque** : Copier également le fichier `algorithmes_td5.c`.

---


## Exercice 1 - Complexité

**TODO** : 

- Évaluer la complexité temporelle des extraits de code ci-dessous:

```
int a = 0, b = 0;
for (i = 0; i < N; i++) {
    a = a + rand();
}
for (j = 0; j < M; j++) {
    b = b + rand();
}
```

```
int a = 0;
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}
```

```
int a = 0, i = N;
while (i > 1) {
    a += i;
    i /= 2;
}
```

```
int i, j, k = 0;
for (i = n / 2; i <= n; i++) {
    for (j = 2; j <= n; j = j * 2) {
        k = k + n / 2;
    }
}
```

---

## Exercice 2 - Tri rapide

Voici un pseudo-code pour le tri rapide:

```
partitionner(tableau T, entier premier, entier dernier, entier pivot)
    échanger T[pivot] et T[dernier]  // échange le pivot avec le dernier du tableau , le pivot devient le dernier du tableau
    j := premier
    pour i de premier à dernier - 1 // la boucle se termine quand i = (dernier-1).
        si T[i] <= T[dernier] alors
            échanger T[i] et T[j]
            j := j + 1
    échanger T[dernier] et T[j]
    renvoyer j

tri_rapide(tableau T, entier premier, entier dernier)
        si premier < dernier alors
            pivot := choix_pivot(T, premier, dernier)
            pivot := partitionner(T, premier, dernier, pivot)
            tri_rapide(T, premier, pivot-1)
            tri_rapide(T, pivot+1, dernier)
```

**TODO** :

- À la main, trier la liste fournie en utilisant le tri rapide décrit dans le pseudocode ci-dessus.
- Implémenter la fonction `void tri_rapide(int liste[], int size)` dans le fichier `main.c`. 

La fonction `exercice2`, déjà implémentée, teste votre fonction sur la liste fournie dans cet énoncé.

---

## Exercice 3 - Tri fusion

Voici un pseudo-code pour le tri fusion:

```
tri_fusion(T: liste à trier)
    n = length(T)

    if n =< 1
        return T

    cutoff = n / 2
    left = T[:cutoff]
    right = T[cutoff:]

    left = tri_fusion(left)
    right = tri_fusion(right)

    return fusion(left, right)

fusion(left: liste, right: liste)
    result = []

    while length(left) > 0 and length(right) > 0
        if first(left) =< first(right)
            append first(left) to result
            left = rest(left)
        else
            append first(right) to result
            right = rest(right)

    if length(left) > 0
        append rest(left) to result
    if length(right) > 0
        append rest(right) to result

    return result
```

**TODO** :

- À la main, trier la liste fournie en utilisant le tri fusion décrit dans le pseudocode ci-dessus.
- Implémenter la fonction `void tri_fusion(int liste[], int size)` dans le fichier `main.c`.

La fonction `exercice3`, déjà implémentée, teste votre fonction sur la liste fournie dans cet énoncé.

---

## Exercice 4 - Benchmarking

**Information :** 
- La fonction `generer_liste` vous permet de générer aléatoirement une liste de `size` valeurs.
- À l'aide de `<time.h>`, l'extrait de code ci-dessous permet de calculer le temps d'exécution d'un programme.
```
clock_t debut = clock();
// Mon programme 
clock_t fin = clock();
double temps_ecoule = (double)(fin - debut) / CLOCKS_PER_SEC;
```

**TODO** :
- Utiliser le code de benchmarking fourni dans l'exercice 4 pour génerer 100 listes de taille 100, 1000 et 10000 et pour chaque cas calculer la moyenne du temps d'exécution des algorithmes de tri suivants:
    - Tri par sélection
    - Tri à bulles
    - Tri fusion
    - Tri rapide

- Comparer le temps d'exécution en fonction de la taille de l'entrée avec la complexité théorique de ces algorithmes.

---

## Exercice 5 - Sort me if you can

**TODO** :
- Ordonner des liste de nombres allant de 1 à 16 de manière à ce que l'application des tris suivants soit la plus lente possible:
    - Tri par sélection
    - Tri à bulles
    - Tri fusion
