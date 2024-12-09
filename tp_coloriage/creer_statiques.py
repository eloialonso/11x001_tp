from utils import afficher_coloriage, charger_coloriage, creer_coloriage_aleatoire, obtenir_couleur_aleatoire, sauvegarder_coloriage


BLANC = (255, 255, 255)


def colorier_pixel(image, i, j, couleur):
    if image[i][j] != BLANC: # on ne veut colorier le pixel (i, j) seulement s'il est blanc
        return
    image[i][j] = couleur    # on colorie le pixel (i, j) avec la couleur demandée


def colorier_compartiment(image, i, j, couleur):
    if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != BLANC:
        return
    image[i][j] = couleur
    colorier_compartiment(image, i - 1, j, couleur)
    colorier_compartiment(image, i + 1, j, couleur)
    colorier_compartiment(image, i, j - 1, couleur)
    colorier_compartiment(image, i, j + 1, couleur)


def exercice():
    afficher_coloriage([[(255, 255, 255), (0, 0, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (120, 120, 120)]], "png/0_exemple_2x3.png")
    recreer_image = False
    if recreer_image:
        image = creer_coloriage_aleatoire()
        sauvegarder_coloriage(image, "image.txt")
    else:
        image = charger_coloriage("image.txt")

    afficher_coloriage(image, "png/1_coloriage_vide.png")

    copie1 = [x.copy() for x in image]
    copie2 = [x.copy() for x in image]
    copie3 = [x.copy() for x in image]
    
    for x in range(len(image)):
        for y in range(len(image[0])):
            if copie1[x][y] == BLANC:
                couleur = obtenir_couleur_aleatoire()
                colorier_compartiment(copie1, x, y, couleur)

    colorier_pixel(copie2, 20, 25, (255, 0, 0))
    colorier_compartiment(copie3, 20, 25, (0, 255, 0))

    afficher_coloriage(copie2, "png/2_coloriage_pixel_rouge.png")
    afficher_coloriage(copie3, "png/3_coloriage_compartiment_vert.png")
    afficher_coloriage(copie1, "png/4_coloriage_voulu.png")

if __name__ == "__main__":
    exercice()
