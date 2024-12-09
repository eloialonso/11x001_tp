import random

from utils import exercice, formatter_sudoku, generer_personnes, generer_resultats, obtenir_sudoku_valide


#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    nom = input("Nom : ")
    date_naissance = input("Date de naissance : ")
    print(f"\n--> Je m'appelle {nom} et je suis né le {date_naissance}.")
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 2
#

@exercice
def exercice2():
    nombres = list(range(10))
    # ******************** Votre code ci-dessous ********************
    carres = []
    for x in nombres:
        carres.append(x ** 2)
    # Plus court : carres = [x ** 2 for x in nombres]
    print("\n".join([f"{x}: {s}" for x, s in zip(nombres, carres)]))
    # ******************** Votre code ci-dessous ********************


#
# EXERCICE 3
#

@exercice
def exercice3():
    nombres = [0, 23, 5, 61, 86, 35, 51, 79, 2, 85, 15, 41, 19, 0, 3]
    # ******************** Votre code ci-dessous ********************
    pairs, impairs = [], []
    for nombre in nombres:
        if nombre % 2 == 0:
            pairs.append(nombre)
        else:
            impairs.append(nombre)
    print(f"Pairs : {pairs}")
    print(f"Impairs : {impairs}")
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
    #return fibonacci_dyna(n, {})
    #return fibonacci_rec(n)
    return fibonacci_it(n)
    # ******************** Votre code ci-dessus *********************


# Récursion : élégant mais lent (ne fonctionne guère au delà de n > ~30)
def fibonacci_rec(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


# Récursion + memoization : rapide mais trop de récursions pour n > ~1000
# Et chercher à la rendre terminal récursive est inutile car Python ne l'optimise pas. 
def fibonacci_dyna(n, memo):
    if n not in memo: 
        memo[n] = n if n < 2 else fibonacci_dyna(n - 1, memo) + fibonacci_dyna(n - 2, memo)
    return memo[n]


# Version itérative : pas de problème
def fibonacci_it(n):
    if n < 2: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        b, a = a + b, b
    return b


#
# EXERCICE 5
#

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
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
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 6
#

@exercice
def exercice6():
    liste_de_liste = [[random.randint(0, 99) for _ in range(2, 5)] for _ in range(2, 5)]
    liste_applatie = []
    # ******************** Votre code ci-dessous ********************
    for liste in liste_de_liste:
        liste_applatie += liste
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
    # Version récursive :
    #if len(chaine) < 2: return True
    #return chaine[0] == chaine[-1] and est_palindrome_rec(chaine[1:-1])
    
    # Version itérative en une ligne :
    # return chaine == chaine[::-1]

    # Version itérative, avec une boucle :
    for i in range(len(chaine)):
        if chaine[i] != chaine[-i-1]:
            return False
    return True
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
    print("Entrer des entiers naturels :")
    while True:
        x = input()
        if not x.isdigit():
            break
        nombres.append(int(x))
    # ******************** Votre code ci-dessus *********************
    return nombres


#
# EXERCICE 9
#

@exercice
def exercice9():
    resultats = generer_resultats()
    # ******************** Votre code ci-dessous ********************
    eleves = {}
    for notes in resultats:
        for nom, note in notes.items():
            if nom not in eleves:
                eleves[nom] = []
            eleves[nom].append(note)
    
    print("\n\n>>> BILAN :\n\n")
    max_prenom_len = max([len(p) for p in eleves.keys()])
    for nom, notes in sorted(eleves.items()):
        n = len(notes)
        moyenne = sum(notes) / n
        notes_str = f"note{'s' if n > 1 else ' '}"
        print(f"{nom.rjust(max_prenom_len)} : {n} {notes_str} - {moyenne:.2f}  de moyenne.")
    # ******************** Votre code ci-dessus *********************


#
# EXERCICE 10
#

@exercice
def exercice10():
    # ******************** Votre code ci-dessous ********************
    texte = input("Entrer du texte : ")
    mots = texte.split(" ")
    for i in range(len(mots)):
        mots[i] = mots[i].lower()
    slug = "-".join(mots)
    print(f"Slug : {slug}")
    # Plus court avec une compréhension de liste : mots = [mot.lower() for mot in mots]
    # Encore plus court avec map / lambda : slug = "-".join(map(lambda x: x.lower(), texte.split(" ")))
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

    tri_a_bulles(nombres, lambda x, y: x < y)
    print(f"\nListe de nombres triée :\n{nombres}")   

    tri_a_bulles(personnes, est_superieur_personnes)
    print(f"\nListe de personnes triée :\n{formatter_personnes(personnes)}")
    

# TODO : modifier cette fonction
def tri_a_bulles(l, fonction_superieur=lambda x, y: x > y):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if fonction_superieur(l[j], l[j + 1]):
                l[j + 1], l[j] = l[j], l[j + 1]


def est_superieur_personnes(personne_1, personne_2):
    nom_1, age_1 = personne_1
    nom_2, age_2 = personne_2
    if age_1 == age_2:
        return nom_1 > nom_2
    return age_1 > age_2


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
    for i in range(9):
        l, c, b = ligne(sudoku, i), colonne(sudoku, i), bloc(sudoku, i)
        if not (verifier_bout(l) and verifier_bout(c) and verifier_bout(b)):
            return False
    return True
    # ******************** Votre code ci-dessus *********************


def verifier_bout(bout):
    return len(bout) == 9 and set(bout) == set(range(1, 10))


def ligne(sudoku, i):
    return sudoku[i * 9 : (i + 1) * 9]


def colonne(sudoku, j):
    return sudoku[j::9]


def bloc(sudoku, k):
    bloc_ids = [9 * (i + 3 * (k // 3)) + j + 3 * (k % 3) for i in range(3) for j in range(3)]
    return [sudoku[x] for x in bloc_ids]


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

