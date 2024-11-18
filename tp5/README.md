# [11X001] TD n°5

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

**Remarque** : Dans tout le TD, vous pouvez utiliser la liste d'entiers suivante pour faire les tris manuellement :

`13, 10, 84, 23, 1, 8, 85, 92, 8, 37, 56, 71, 49, 77, 57, 95, 34, 98, 75, 97`.

---

## Exercice 1 - Vérifier si une liste est triée

**TODO** :

- Implémenter une fonction `int liste_est_triee(int liste[], int size)` qui renvoie `1` si `liste` est correctement triée, `0` sinon.
- On passe l'entier `size` en argument car on a besoin de la taille du tableau pour pouvoir itérer à travers ses éléments.

La fonction `exercice1`, déjà implémentée, teste votre fonction sur une liste non triée et une liste triée.

---

## Exercice 2 - Tri par sélection

Voici le pseudo-code donné dans le cours pour le tri par sélection :

```
procedure tri_selection(T : liste à trier)
    n = length(T)
    for i = 0 to n - 2 do
        min = i
        for j = i + 1 to n - 1 do
            if T[j] < T[min] then
                min = j
            end if
        end for
        if min != i then
            swap(T[i], T[min])
        end if
    end for
end procedure
```

**TODO** :

- À la main, trier la liste fournie en utilisant le tri par sélection décrit dans le pseudocode ci-dessus.
- Implémenter la fonction `void tri_par_selection(int liste[], int size)` dans le fichier `main.c`.

La fonction `exercice2`, déjà implémentée, teste votre fonction sur des listes d'entiers aléatoires.

---

## Exercice 3 - Tri à bulles

Voici le pseudo-code donné dans le cours pour le tri à bulles :

```
procedure tri_a_bulle(T : liste à trier)
    n = length(T)
    do
        echange = false
        for i = 1 to n-1 do
            if T[i-1] > T[i] then
                swap(T[i-1], T[i])
                echange = true
            end if
        end for
    while echange
end procedure
```

**TODO** :

- À la main, trier la liste fournie en utilisant le tri à bulles décrit dans le pseudocode ci-dessus.
- Implémenter la fonction `void tri_a_bulles(int liste[], int size)` dans le fichier `main.c`. 
- **CONSEIL IMPORTANT** : Ce code est fourni dans le cours, en C, mais nous vous conseillons de vous entrainer à implémenter cet algorithme en vous basant *uniquement sur le pseudo-code ci-dessus*.

La fonction `exercice3`, déjà implémentée, teste votre fonction sur des listes d'entiers aléatoires.

---

## Exercice 4 - Tri cocktail

Voici le pseudo-code donné dans le cours pour le tri cocktail :

```
procedure tri_cocktail(T : liste à trier)
    n = length(T)
    do
        echange = false
        for i = 0 to n - 2 do:
            if T[i] > T[i + 1] then
                swap(T[i], T[i + 1])
                echange = true
            end if
        end for
        if not echange then
            break do-while loop
        end if
        echange = false
        for i = n - 2 to 0 do:
            if T[i] > T[i + 1] then
                swap(T[i], T[i + 1])
                echange = true
            end if
        end for
    while echange
end procedure
```

**TODO** :

- À la main, trier la liste fournie en utilisant le tri cocktail décrit dans le pseudocode ci-dessus.
- Implémenter la fonction `void tri_cocktail(int liste[], int size)` dans le fichier `main.c`.

La fonction `exercice4`, déjà implémentée, teste votre fonction sur des listes d'entiers aléatoires.
