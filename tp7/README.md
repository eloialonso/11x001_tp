# [11X001] TP n°7

---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

## Exercice 1 - `input`, `print` et *f-strings*

**TODO** :
- Compléter le code de la fonction `exercice1` comme suit :
    - À l'aide de la fonction `input`, demander à l'utilisateur son nom et sa date de naissance. 
    - À l'aide de la fonction `print`, afficher une phrase du type `"Je m'appelle XXX et je suis né le XXX."`. On pourra utiliser une [chaine de caractères formatée](https://docs.python.org/fr/3/tutorial/inputoutput.html#tut-f-strings).

>**Aide** :
Comme l'utilisation de `input`, `print` et des chaines de caractères formattées est essentielle, voici un exemple d'utilisation de ces notions :
```python
texte = input("Taper du texte : ")
print(f"Vous avez entré le texte suivant : {texte}.")
x = int(input("Entrer un nombre entier : ")) # Conversion explicite en int car input retourne un str.
print(f"Le carré de {x} est {x ** 2}.")
```

---

## Exercice 2

La variable `nombres` fournie contient la liste des entiers de 0 à 9. 

**TODO** :
- Créer une liste `carres` qui contient les éléments de la liste `nombres` élevés au carré.
- Afficher chaque nombre et son carré.

>**Aide** : Exemple d'utilisation de `zip` :
```python 
l1 = [2, 3]
l2 = [4, 5]
for e1, e2 in zip(l1, l2):
    print(f'{e1}, {e2}')
# Affiche
# 2, 4
# 3, 5
```

---

## Exercice 3

La variable `nombres` fournie contient une liste de quelques nombres entiers. 

**TODO** :

- Séparer cette liste en deux listes qu'on appelera `pairs` et `impairs`, la première contenant les nombres pairs et l'autre les nombres impairs. 
- Afficher ces deux listes pour vérifier votre solution.

---

## Exercice 4 - Fibonacci

**TODO** : 
- Compléter la fonction `fibonacci` qui prend un entier naturel `n` en entrée et doit renvoyer le `n`-ème terme de la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci).
- On peut coder cette fonction de façon récursive ou itérative, vous pouvez essayer d'implémenter les deux versions.

**Remarque** : La fonction `exercice4` est déjà implémentée et se charge d'appeler votre fonction pour une valeur entrée par l'utilisateur. La boucle s'arrête lorsque l'utilisateur saisit une valeur autre qu'un entier naturel.

---

## Exercice 5

**TODO** : Qu'affiche ce code ?

```python
a = [2, 3]
b = a
print(a)
print(b)

b[0] = 1
print(a)
print(b)

a = [5, 6]
b[0] = 10
print(a)
print(b)
```

Vous pouvez copier-coller ce code dans la fonction `exercice5` pour vérifier votre raisonnement. 

**Remarque** : Il est bien plus utile de réfléchir à la question **avant** de faire le copier-coller bien sûr.

---

## Exercice 6 

La variable `liste_de_liste` contient une liste de liste de nombres aléatoires, par exemple : `[[93, 49, 71], [36, 83, 53], [66, 32, 51]]`.


**TODO** :
- Ajouter tous les nombres dans la variable `liste_applatie` en utilisant la concaténation de liste.

Dans notre exemple, on aura `liste_applatie` qui vaut `[93, 49, 71, 36, 83, 53, 66, 32, 51]`.

---

## Exercice 7 - Palindrome

Un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) est une chaine de caractères dont l'ordre reste le même qu'on le lise de gauche à droite ou de droite à gauche. 

Exemples : 
- kayak
- radar
- engagelejeuquejelegagne

**TODO** : 

- Compléter la fonction `est_palindrome` qui prend une chaine de caractères en entrée et doit renvoyer `True` si cette chaine est un palindrome, `False` sinon.
- **Facultatif** : Essayer de coder cette fonction de façon récursive.


---

## Exercice 8

**TODO** : 
- Compléter la fonction `demander_nombres()`. 
    - Cette fonction doit, en boucle, demander à l'utilisateur un nombre entier naturel et le stocker dans la liste `nombres`. Tant que l'utilisateur rentre un entier naturel, on continue.
    - On arrête quand l'utilisateur rentre autre chose qu'un entier naturel. 
    - Cette fonction doit retourner la liste `nombres` contenant tous les nombres entrés par l'utilisateur. 
- Observer le code de la fonction `exercice8`, déjà complété, qui teste votre solution.


**Indice** : Pour vérifier qu'un `str` est convertissable en entier *naturel*, vous pouvez utiliser `str.isdigit()`. Cette fonction renvoie `True` uniquement si tous les caractères sont un chiffre. Ainsi, elle renvoie `True` pour les string contenant un entier naturel et `False` pour tout le reste, en particulier pour les nombres négatifs et à virgule.


    
---

## Exercice 9 - Manipulation de `dict` et `list`

La variable `resultats` est une `list` de `dict`. Chaque `dict` contient les notes des élèves participants à un cours. 


```python
# exemple de contenu de la variable resultats
[
    {
        'Adam': 5,
        'Alice': 1,
        'Ambre': 5,
        'Arthur': 5,
    },
    {
        'Adam': 3,
        'Ambre': 4,
        'Emma': 3,
        'Maël': 1,
        'Rose': 3
    }
]
```

Dans l'exemple ci-dessus, il y a deux cours différents : le premier cours concerne 4 élèves et le deuxième cours en concerne 5.  

Le contenu de cette variable est regénéré aléatoirement à chaque fois que vous exécutez votre code.

**TODO** :

- Créer un `dict` appelé `eleves` dont les clés sont les noms des élèves. La valeur associée à une clé est la liste des notes obtenues par l'élève.
- Afficher le nom, le nombre de note et la moyenne de chaque étudiant. 

Pour notre exemple : 

```python 
# exemple de contenu de la variable eleves
{
    'Adam': [5, 3],
    'Alice': [1],
    'Ambre': [5, 4],
    'Arthur': [5],
    'Emma': [3],
    'Maël': [1],
    'Rose': [3],
}
``` 
Affichage :
```
  Adam : 2 notes - 4.00  de moyenne.
 Alice : 1 note  - 1.00  de moyenne.
 Ambre : 2 notes - 4.50  de moyenne.
Arthur : 1 note  - 5.00  de moyenne.
  Emma : 1 note  - 3.00  de moyenne.
  Maël : 1 note  - 1.00  de moyenne.
  Rose : 1 note  - 3.00  de moyenne.
```

---

## Exercice 10 - Slugify

**TODO** :
- Demander un texte à l'utilisateur. 
- Afficher ce texte tout en minuscule et en remplaçant les espaces par des tirets (`-`).
- **Facultatif (plus avancé)** : Essayer de coder la conversion du texte en une seule ligne (par exemple à l'aide de `map` et d'une fonction anonyme).

**Exemple** : 

Le texte :

`Ce procédé est parfois appelé slugify car on convertit notre texte en son équivalent limace` 

sera convertit en : 

`ce-procédé-est-parfois-appelé-slugify-car-on-convertit-notre-texte-en-son-équivalent-limace` 

Pour information, une version complète comme [celle-ci](https://blog.tersmitten.nl/slugify/) se charge également d'enlever les accents et les caractères spéciaux.

**Aide** :

- Conversion en minuscule : voir le cours 5.2.

- Exemple d'utilisation de `split` :

```python 
texte = "Exemple de texte."
mots = texte.split(" ") # mots est une liste ["Exemple", "de", "texte."]
```

- Exemple d'utilisation de `join` :

```python 
mots = ["Exemple", "de", "texte."]
texte = "XXX".join(mots) # texte est un str : "ExempleXXXdeXXXtexte."
```


## Exercice 11 - Trier selon des critères variables 

La fonction `tri_a_bulles`, déjà codée, implémente une méthode de tri appelée [tri à bulles](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles).

**TODO** : 
- Observer le code de cette fonction pour comprendre son fonctionnement.
- Dans la fonction `exercice11`, observer son appel pour trier d'abord une liste de nombres, puis une liste de personnes.

**Remarque** : On représente une personne par un `tuple`(nom, age). Par exemple : Michel, 18 ans, sera représenté par le tuple `("Michel", 18)`.

**TODO** :
- Modifier la fonction `tri_a_bulles` comme suit :
    - Ajouter un argument `fonction_superieur`, qu'on suppose être une fonction de deux variables et qui renvoie un booléen.
    - Remplacer la comparaison `l[j] > l[j + 1]` par un appel à `fonction_superieur(l[j], l[j+1])`.
- En définissant différentes fonctions de comparaison, utiliser `tri_a_bulles` pour : 
    - Trier la liste de nombres par ordre décroissant.
    - Trier la liste de personnes par ordre d'âge croissant (et à âge égal, par ordre alphabétique).  


---

## Exercice 12 - Vérifier un sudoku

Le but de cet exercice est de vérifier si un [Sudoku](https://fr.wikipedia.org/wiki/Sudoku) complété est valide ou non. 

On représente un Sudoku par une liste de 81 nombres, ajoutés dans l'ordre ligne par ligne.

La fonction `exercice12` est déjà complétée : 
- La variable `sudoku_valide` contient un Sudoku valide.
- La variable `sudoku_invalide` contient un Sudoku invalide.
- On affiche les deux Sudoku ainsi que leur validité.

**TODO** : Modifier la fonction `verifier_sudoku` afin qu'elle vérifie la validité du Sudoku passé en argument. 

**Remarque** : Il peut être intéressant d'implémenter d'autres fonctions auxiliaires afin d'avoir un code clair et sans répétition.
