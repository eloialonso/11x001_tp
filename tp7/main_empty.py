import random

from utils import exercice, formatter_sudoku, generer_personnes, generer_resultats, obtenir_sudoku_valide


#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 2
#

@exercice
def exercice2():
    nombres = list(range(10))
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessous ********************


#
# EXERCICE 3
#

@exercice
def exercice3():
    nombres = [0, 23, 5, 61, 86, 35, 51, 79, 2, 85, 15, 41, 19, 0, 3]
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 4
#

@exercice
def exercice4():
    while True:
        n = input("Calcul du n-ème terme de la suite de Fibonacci, n = ")
        if not n.isdigit(): break
        n = int(n)
        print(f"--> fibonacci({n}) = {fibonacci(n)}\n")


def fibonacci(n):
    # ******************** Votre code ci-dessous ********************
    return 0
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 5
#

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 6
#

@exercice
def exercice6():
    liste_de_liste = [[random.randint(0, 99) for _ in range(2, 5)] for _ in range(2, 5)]
    liste_applatie = []
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************
    print(f"Liste de liste : {liste_de_liste}")
    print(f"Liste applatie : {liste_applatie}")


#
# EXERCICE 7
#

@exercice
def exercice7():
    while True:
        chaine = input("Entrer une chaine de caractères (presser 'Entrée' pour sortir) : ")
        if chaine == "":
            break
        pal = est_palindrome(chaine)
        verbe = "est" if pal else "n'est pas"
        print(f"'{chaine}' {verbe} un palindrome.\n")


def est_palindrome(chaine):
    # ******************** Votre code ci-dessous ********************
    return False
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 8
#

@exercice
def exercice8():
    # Cette fonction est déjà complétée. Vous devez compléter la fonction `demander_nombres`
    nombres = demander_nombres()
    print(f"Vous avez entré les nombres suivants : {nombres}")


def demander_nombres():
    nombres = []
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************
    return nombres


#
# EXERCICE 9
#

@exercice
def exercice9():
    resultats = generer_resultats()
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 10
#

@exercice
def exercice10():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 11
#

@exercice
def exercice11():
    nombres = [random.randint(0, 100) for _ in range(random.randint(3, 20))]
    print(f"\nListe de nombres aléatoires :\n{nombres}")

    personnes = generer_personnes()
    formatter_personnes = lambda personnes: "\n".join(map(lambda personne: f"{personne[0]} ({personne[1]})", personnes))
    print(f"\nListe de personnes aléatoires :\n{formatter_personnes(personnes)}")

    tri_a_bulles(nombres)  # TODO : modifier cette ligne
    print(f"\nListe de nombres triée :\n{nombres}")   

    tri_a_bulles(personnes)  # TODO : modifier cette ligne
    print(f"\nListe de personnes triée :\n{formatter_personnes(personnes)}")
    

# TODO : modifier cette fonction
def tri_a_bulles(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]


#
# EXERCICE 12
#

@exercice
def exercice12():
    sudoku_valide = obtenir_sudoku_valide()
    sudoku_invalide = sudoku_valide.copy()
    sudoku_invalide[0], sudoku_invalide[1] = sudoku_invalide[1], sudoku_invalide[0] 

    for i, sudoku in enumerate([sudoku_valide, sudoku_invalide]):
        print(f"\nSudoku n°{i  +1}\n")
        print(formatter_sudoku(sudoku))
        print("--> " + ("VALIDE" if verifier_sudoku(sudoku) else "INVALIDE"))


def verifier_sudoku(sudoku):
    # ******************** Votre code ci-dessous ********************
    return False
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":

    exercice1()
    exercice2()
    exercice3()
    exercice4()
    exercice5()
    exercice6()
    exercice7()
    exercice8()
    exercice9()
    exercice10()
    exercice11()
    exercice12()


