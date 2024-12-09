from pathlib import Path
import random

import matplotlib.pyplot as plt


BLACK, WHITE = (0, 0, 0), (255, 255, 255)


def creer_coloriage_aleatoire(size_x=50, size_y=50, nb_points=1000, black_frame=True):
    bitmap = [[WHITE if ((0 < i < size_x - 1 and 0 < j < size_y - 1) or not black_frame) else BLACK for i in range(size_y)] for j in range(size_x)]
    count = 0
    point = (random.randint(0, size_x - 1), 0)
    length = 0
    while count < nb_points or (count >= nb_points and not (point[0] == 0 or point[1] == 0 or point[0] == size_x - 1 or point[1] == size_y - 1)):
        x, y = point
        bitmap[x][y] = BLACK
        count += 1
        if length == 0:
            length = random.randint(min(size_x, size_y) // 4, min(size_x, size_y) // 2)
            direction = random.randint(0, 7)
        if direction == 0:
            point = (x + 1, y)
        if direction == 1:
            point = (x - 1, y)
        if direction == 2:
            point = (x, y + 1)
        if direction == 3:
            point = (x -1, y - 1)
        if direction == 4:
            point = (x + 1, y + 1)
        if direction == 5:
            point = (x + 1, y - 1)
        if direction == 6:
            point = (x - 1, y - 1)
        if direction == 7:
            point = (x - 1, y + 1)
        length -= 1
        if point[0] < 0 or point[1] < 0 or point[0] >= size_x or point[1] >= size_y:
            length = 0
            point = (x, y)
    return bitmap


def afficher_coloriage(image, fname=None):
    plt.imshow(image)
    plt.axis("off")
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname, bbox_inches="tight", pad_inches=0)
    

def obtenir_couleur_aleatoire():
    couleur = tuple([random.randint(0, 255) for _ in range(3)])
    return couleur if couleur not in (WHITE, BLACK) else obtenir_couleur_aleatoire()


def sauvegarder_coloriage(image, fname):
    with Path(fname).open('w') as f:
        f.write("\n".join(map(lambda row: " ".join(map(lambda rgb: ",".join(map(lambda x: str(x), rgb)), row)), image)))


def charger_coloriage(fname):
    with Path(fname).open('r') as f:
        raw = f.readlines()
    image = [[tuple(map(lambda x: int(x), rgb.split(","))) for rgb in line.split(" ")] for line in raw]
    return image

