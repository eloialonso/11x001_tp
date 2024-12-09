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
    return
    # ******************** Votre code ci-dessus *********************


def exercice1():
    image = charger_coloriage("image.txt")
    # ******************** Votre code ci-dessous ********************

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

    # ******************** Votre code ci-dessus *********************
    afficher_coloriage(image)


if __name__ == "__main__":
    exercice1()
    exercice2()
    exercice3()
