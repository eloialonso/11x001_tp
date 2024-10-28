# [11X001] TD n°4

---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

## Exercice 1

**TODO** : 
- Lire un entier naturel `n` et créer un tableau de `n` entiers.
- À l'aide de l'arithmétique de pointeurs, itérer à travers le tableau afin d'affecter à chaque entrée `i` la valeur `i`*`i`.

---

## Exercice 2

**TODO** : Le fichier `ma_liste.dat` contient des valeurs que nous souhaitons lire et stocker dans une liste:
- Implémenter une liste chaînée ainsi que les fonctions permettant de créer une liste chaînée et d'y insérer une valeur.
- Créer une liste chaînée et y insérer les valeurs lues lors du parcours de `ma_liste.txt`
- Parcourir la liste chaînée afin de calculer la moyenne de ses valeurs et écrire le résultat dans le fichier `ma_moyenne.dat`.

---

## Exercice 3

Cette exercice consiste à étendre l'implémentation d'un vecteur vue dans le cours au cas d'une matrice.

**TODO** : 
- Implémenter une structure `matrice` composée des champs: `int num_lignes`, `int num_colonnes` et `float **index_lignes`. `index_lignes` est un pointeur vers des pointeurs de `float`.  
Le `i`-ème pointeur pointe vers la ligne `i` de la matrice et la `j`-ème valeur pointée par ce pointeur correspond à l'entrée `i, j` de la matrice. Par exemple, `index_lignes[2][3]` est l'entrée de la deuxième ligne, troisième colonne de la matrice.
- Implémenter la fonction : `cree_matrice`.
- De la même manière, implémenter les fonctions : `randomize_matrice`, `affiche_matrice`, `norme_l2_matrice`, `insere_valeur_matrice` et `detruit_matrice`.  
- Implémenter la fonction `redimensionne_matrice` permettant d'augmenter le nombre de lignes et de colonnes d'une matrice.

---




