# [11X001] TD n°1
---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

## Consignes générales (pour tous les TD)

- La **consigne** de chaque exercice est dans le fichier `README.md`. Les **TODO** indiquent des consignes à suivre.
- Le **code** des exercices est dans le fichier `main.c`. Chaque exercice correspond à une fonction dans ce fichier, nommée `exercice1` pour l'exercice 1, `exercice2` pour l'exercice 2 etc.
- L'endroit où vous êtes supposés écrire votre code est délimité comme suit : 

```c 
/******************** Votre code ci-dessous ********************/
    


/******************** Votre code ci-dessus *********************/
```

- Pour compiler et exécuter votre programme, vous pouvez taper `clang <nom_fichier>.c -o <nom_executable>` puis `./<nom_executable>`. 
- Les **solutions** seront fournies une semaine après le TD. 


---


## Exercice 1

L'exercice 1 est déjà implémenté, il affiche simplement :  

```
Bonjour monde !
```

**TODO** : Observer le code de cet exercice, en particulier l'usage de `printf` que vous utiliserez dans l'exercice suivant. 

---

## Exercice 2

**TODO**: Écrire un programme qui affiche votre nom, date de naissance et adresse e-mail. Par exemple, il affichera : 

```
Nom     : Michel LAMBDA
Né le   : 31.10.2001
Contact : michel.lambda@unige.ch
```

---


## Exercice 3
    
**TODO** : Afficher la première lettre de votre prénom avec des #.

Par exemple, pour la lettre A, votre programme pourrait afficher : 

```
     #     
    # #    
   #   #   
  #######  
 #       # 
#         #
```

**Indice** : Utiliser la fonction `printf`.

---


## Exercice 4

**TODO** : Déclarer et affecter cinq variables de type `char` correspondant aux cinq caractères qui composent le mot *UNIGE*.

**TODO** : Afficher le mot *UNIGE* caractère par caractère, d'abord à l'endroit, puis à l'envers, en utilisant `printf` et ces cinq variables.

> **Astuce** : Pour injecter une variable dans l'affichage de `printf`, utiliser : 
- `%c` pour une variable de type `char`
- `%d` pour une variable de type `int`
- `%f` pour une variable de type `float`

> Par exemple : 
```c 
printf("Première lettre = %c", 'a');            // Affiche "Première lettre = a"
printf("2 x 6 = %d x %d = %d", 3, 4, 6 + 6);    // Affiche "2 x 6 = 3 x 4 = 12"
printf("Racine de 2 vaut environ %f", 1.41421); // Affiche "Racine de 2 vaut environ 1.41421"
```

---



## Exercice 5

**TODO** : Calculer et afficher le périmètre et l'aire d'un cercle.  

**Astuce** : L'astuce de l'exercice 2 est utile ici aussi.

**Remarques** :

- Pour la valeur de Pi, utiliser la variable `PI`, définie au début de l'exercice : 

```c
const float PI = 3.1415926535;
```

- Le rayon du cercle est un `float` demandé à l'utilisateur lors de l'exécution du programme, grâce à la fonction `scanf`. **/!\ Cette partie est déjà implémentée pour vous !** Comme on fera beaucoup appel à `scanf` dans les prochains TD, pour demander à l'utilisateur d'entrer une valeur, nous vous conseillons de commencer à observer son fonctionnement :

```c
float radius;  // déclaration de la variable
printf("Entrer le rayon du cercle (en m) : ");  // message d'invitation (facultatif mais plus user-friendly)
scanf("%f", &radius);  // lecture de la valeur entrée par l'utilisateur
```


---


## Exercice 6

**TODO** : Calculer son âge en jours et stocker le résultat dans la variable `age_in_day`. Pour faire simple, on ignore les années bissextiles et on considère qu'un mois fait toujours 30 jours, et donc qu'un an fait 360 jours.

**Remarque** : 
- Similairement à l'exercice 3, on utilise la fonction `scanf` pour demander la date de naissance et la date du jour à l'utilisateur lors de l'exécution. **/!\ Partie déjà implémenté pour vous**. À nouveau, nous vous conseillons d'observer / de jouer avec la syntaxe pour vous familiariser avec l'utilisation de `scanf` :

```c
int birth_year, birth_month, birth_day;  // Déclaration des variables 
printf("Entrer votre date de naissance (format dd/mm/yyyy) : ");  // Message d'invitation
scanf("%d/%d/%d", &birth_day, &birth_month, &birth_year);  // Lecture de la date entrée
```


---


## Exercice 7

**TODO** : Convertir en jours, semaines, années le nombre de jours stocké dans la variable `nb_of_days` (dont la valeur est demandée à l'utilisateur avec la fonction `scanf`, similairement aux exercices précédents). Vous pouvez considérer qu'un an fait toujours 365 jours.

**Exemple** : Si l'utilisateur entre le nombre 2153, on veut afficher : 

```
2153 jours font 5 année(s), 46 semaine(s) et 6 jour(s).
```

---


## Exercice 8

**TODO** : Observer le code de l'exercice : 

```c 
int a = 7, b = 2;
float c, d;  

c = a / b; // Ne modifier que cette ligne

printf("%d / %d = %f \n", a, b, c); 
```

Il affiche : 
```
7 / 2 = 3.000000
```

**TODO** : Utiliser une conversion explicite en `float` pour que votre code affiche : 
```
7 / 2 = 3.500000
```

**Remarque**: Ne modifier que la ligne indiquée. En particulier, ne pas changer les types de `a`, `b` et `c` lors de leur déclaration.


---


## Exercice 9

Le but de cet exercice est de comprendre la représentation en mémoire d'un nombre entier et d'illustrer la limitation dite de *dépassement d'entier*, ou **integer overflow** en anglais.

--- 

### Principe

#### Rappel sur les bases 

- Nous avons l'habitude de considérer les nombres en **décimal** (base 10). Prenons quelques exemples : 
    - Le nombre 42 : les chiffres '4' et '2' signifient **4** x 10 + **2** x 1, qu'on écrira **4** x 10^1 + **2** x 10^0
    - Le nombre 591 : les chiffres '5', '9' et '1' signifient **5** x 10^2 + **9** x 10^1 + **1** x 10^0
- Mais on peut en fait représenter les nombres dans la base que l'on veut. Par exemple : 
    - Le nombre 42 en base 8 se décompose comme **5** x 8^1 + **2** x 8^0 et s'écrit donc '52'
    - Le nombre 591 en base 5 se décompose comme **4** x 5^3 + **3** x 5^2 + **3** x 5^1 + **1** x 5^0 et s'écrit donc '4331'
- Dans un ordinateur, les nombres sont représentés en **binaire** (base 2). Par exemple : 
    - Le nombre 42 en base 2 se décompose comme **1** x 2^5 + **0** x 2^4 + **1** x 2^3 + **0** x 2^2 + **1** x 2^1 + **0** x 2^0 et s'écrit donc '101010'
    - Le nombre 591 en base 2 se décompose comme **1** x 2^9 + **0** x 2^8 + **0** x 2^7 + **1** x 2^6 + **0** x 2^5 + **0** x 2^4 + **1** x 2^3 + **1** x 2^2 + **1** x 2^1 + **1** x 2^0 et s'écrit donc '1001001111'

#### Stockage d'un entier 

Comme la mémoire d'un ordinateur n'est pas infinie, il faut décider combien de bits on utilise au maximum pour stocker un nombre entier.

Par exemple : 
- Si on décide d'utiliser 1 bit, on pourra stocker les nombres '0' et '1'
- Si on décide d'utiliser 2 bits, on pourra stocker les nombres '00', '01', '10' et '11' (correspondants en décimal à 0, 1, 2 et 3).
- Si on décide d'utiliser 3 bits, on pourra stocker les nombres '000', '001', '010', '011', '100', '101', '110', '111',  (correspondants en décimal à 0, 1, 2, 3, 4, 5, 6 et 7).

On voit qu'à chaque fois qu'on rajoute un bit, on double le nombre d'entiers que l'on peut représenter. Ainsi, si on décide d'utiliser **n** bits, on pourra représenter **2^n** entiers.

Par exemple, avec 8 bits, on peut stocker 2^8 entiers (les nombres de 0 à 255) : 
- 0 s'écrit '00000000'
- 1 s'écrit '00000001'
- 27 s'écrit '00011011'
- 254 s'écrit '11111110'
- 255 s'écrit '11111111'

#### Dépassement d'entier / integer overflow

Mais alors, comment stocker 256 avec 8 bits ? En binaire, 256 s'écrit '100000000' (un '1' suivi de huit '0'). Comme on ne dispose que de 8 bits, on tronque le 9ème bit et on obtient donc '00000000', ce qui correspond au nombre 0. On ne peut donc pas représenter un nombre supérieur ou égal à 256 avec seulement 8 bits.

De même, 259 s'écrit '100000011'. On tronque le 9ème bit et on obtient '00000011', ce qui correspond au nombre 3.

Ce phénomène s'appelle un **integer overflow** : quand un nombre est trop grand pour rentrer dans le nombre de bits dont on dispose, on tronque les bits en trop et on obtient donc un autre nombre. Ceci est la plupart du temps indésirable et constitue une source de bug à surveiller !

**Remarque** : On obtient en fait le nombre de départ modulo 2^n (avec n le nombre de bits utilisés). Par exemple, avec 8 bits, 259 % 2^8 = 3. 

---

### Mise en pratique

- **TODO**: Observer / comprendre / jouer avec le code fourni dans la fonction `exercice7`. 

**Remarque** : On utilise le type `unsigned char` car il permet de stocker des nombres entiers sur 8 bits, comme dans l'explication précédente.

- **TODO (plus avancé)** : Reproduire le même exemple mais avec le type `int`. En particulier, vous pouvez : 
    - Déclarer une nouvelle variable de type `int`.
    - Utiliser la fonction `sizeof` sur cette variable, pour savoir sur combien d'octets est stocké un `int` (multiplier par 8 pour avoir le résultat en bits).
    - Créer un overflow en affectant un nombre supérieur à la capacité maximale du type `int`. 

**Remarque** : Le type `int` est **signé**, ce qui veut dire qu'il permet de représenter des nombres entiers négatifs. Avec n bits, on garde un bit pour représenter le signe et les bits restants servent à encoder la valeur. Ainsi, avec 8 bits, on représentera les entiers de -128 à +127 si notre type est signé, et les entiers de 0 à 255 si notre type n'est pas signé. **Cela explique pourquoi l'overflow apparait dès 2^31 et non à 2^32.**

**Pour aller plus loin** : Pour que l'addition des représentations binaires soit en accord avec ce que l'on attend (addition classique d'entiers relatifs), on représente les entiers négatifs avec leur complément à 2^n : voir [cet article Wikipédia sur le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) pour en savoir plus.

