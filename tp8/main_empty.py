from utils import exercice, GREEN, ENDC


#************************************
#***** Vos fonctions ci-dessous *****
#************************************

# EXERCICE 1

def hamming(str1, str2):
    # ******************** Votre code ci-dessous ********************
    return -1
    # ******************** Votre code ci-dessus *********************

# EXERCICE 2

def recherche_mot_force_brute(mot, texte):
    # ******************** Votre code ci-dessous ********************
    return -1
    # ******************** Votre code ci-dessus *********************

# EXERCICE 3

#***********************************
#***** Vos fonctions ci-dessus *****
#***********************************

#
# EXERCICE 1
#

@exercice
def exercice1():
    str1 = input("str1 = ")
    str2 = input("str2 = ")
    print(f"\nHamming({str1}, {str2}) = {hamming(str1, str2)}.")

#
# EXERCICE 2
#

@exercice
def exercice2():
    mot = input("mot = ")
    texte = input("texte = ")
    idx = recherche_mot_force_brute(mot, texte)
    if idx == -1:
        print(f"'{mot}' n'est pas dans '{texte}'")
    else:
        print(f"'{mot}' trouvé à l'indice {idx} : {texte[:idx]}{GREEN}{texte[idx:idx+len(mot)]}{ENDC}{texte[idx+len(mot):]}")
#
# EXERCICE 3
#

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":

    exercice1()
    exercice2()
    exercice3()
