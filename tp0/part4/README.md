Dans cette partie optionnelle, on vous montre comment faire
des multiplications matricielles et organiser des images.


## Multiplication matricielle

Dans le code `matrix_multiplication.py`, on vous montre comment faire des multiplications matricielles
avec des listes en Python ou avec des tableaux (array) `numpy`.

Les boucles `for` suivent la méthode de multiplication matricielle qu'on aurait faite à la main:

![alt text](image.png)

Et donc on général, pour multiplier une matrice $A \in \mathbb{R}^{m \times n}$ avec une autre $B \in \mathbb{R}^{n \times p}$ et obtenir $C \in \mathbb{R}^{m \times p}$, on peut utiliser la formule ci-dessous

![alt text](image-1.png)

On aurait donc $3$ boucles, deux pour avoir $m \times p$ éléments et une pour la somme. 

## Organiser des images (optionnel / plus avancé, si vous avez déjà un peu d'expérience)


Nous allons maintenant voir comment organiser et renommer des milliers images, sans avoir à la faire à la main !

Si vous voulez essayer le code, vous pouvez télécharger le zip [ici](https://drive.google.com/file/d/17ND8oB7AkGjvfVFjNvcGliGLSNdQ_MS2/view?usp=sharing), l'extraire et le placer comme ceci
```
.
├── images/
└── main.py
```

Chaque image est nommée comme suit : `entierarbitraire_mois_jour_objet_indice.extension` avec `extension` étant soit `jpg`, soit `jpeg`.

Le but est de créer des nouveaux dossiers dans lesquels ranger les images, et d'uniformiser les extensions (jpg pour tous).

Exemples:

- `8752_08_27_deer_32.jpeg` doit être rangé dans `./08/deer/8752_08_27_deer_32.jpg`.
- `12_07_07_truck_47.jpg` doit être rangé dans `./07/truck/12_07_07_truck_47.jpg`

Le but de cet exercice plus dur est aussi de vous apprendre à chercher par vous-même sur Google ;)
