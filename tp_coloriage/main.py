from utils import afficher_coloriage, charger_coloriage, creer_coloriage_aleatoire, obtenir_couleur_aleatoire


BLANC = (255, 255, 255)


def colorier_pixel(image, i, j, couleur):
    if image[i][j] != BLANC: # on ne veut colorier le pixel (i, j) seulement s'il est blanc
        return
    image[i][j] = couleur    # on colorie le pixel (i, j) avec la couleur demandée
    # Remarque : cette fonction ne retourne rien car on modifie directement la variable image
    # (En Python, une liste est passée par référence à une fonction)


def colorier_compartiment(image, i, j, couleur):
    # ******************** Votre code ci-dessous ********************
    if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != BLANC:
        return
    image[i][j] = couleur
    colorier_compartiment(image, i - 1, j, couleur)
    colorier_compartiment(image, i + 1, j, couleur)
    colorier_compartiment(image, i, j - 1, couleur)
    colorier_compartiment(image, i, j + 1, couleur)
    # ******************** Votre code ci-dessus *********************


def exercice1():
    image = charger_coloriage("image.txt")
    # ******************** Votre code ci-dessous ********************
    colorier_pixel(image, i=20, j=25, couleur=(255, 0, 0))
    # ******************** Votre code ci-dessus *********************
    afficher_coloriage(image)


def exercice2():
    image = charger_coloriage("image.txt")
    colorier_compartiment(image, i=20, j=25, couleur=(0, 255, 0))
    afficher_coloriage(image)


def exercice3():
    image = charger_coloriage("image.txt")
    #image = creer_coloriage_aleatoire() # Décommenter cette ligne pour avoir un coloriage aléatoire à la place
    # ******************** Votre code ci-dessous ********************
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == BLANC:
                couleur = obtenir_couleur_aleatoire()
                colorier_compartiment(image, i, j, couleur)
    # ******************** Votre code ci-dessus *********************
    afficher_coloriage(image)


if __name__ == "__main__":
    exercice1()
    exercice2()
    exercice3()
