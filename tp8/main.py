from utils import exercice, GREEN, ENDC


#************************************
#***** Vos fonctions ci-dessous *****
#************************************

# EXERCICE 1

def hamming(str1, str2):
    # ******************** Votre code ci-dessous ********************
    if len(str1) != len(str2):
        return -1
    
    dist = 0
    for x1, x2 in zip(str1, str2):
        if x1 != x2:
            dist += 1
    return dist
    # ******************** Votre code ci-dessus *********************

# EXERCICE 2

def recherche_mot_force_brute(mot, texte):
    # ******************** Votre code ci-dessous ********************
    m, n = len(mot), len(texte)
    for j in range(n - m + 1):
        for i in range(m):
            if mot[i] != texte[j + i]:
                break
        else:
            return j
    return -1
    # ******************** Votre code ci-dessus *********************

# EXERCICE 3

def levenshtein(a, b, verbose=False):
    dist = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, 1 + len(a)):
        dist[i][0] = i
    
    for j in range(1, 1 + len(b)):
        dist[0][j] = j
    
    for i in range(1, 1 + len(a)):
        for j in range(1, 1 + len(b)):
            if a[i - 1] == b[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(
                    dist[i - 1][j] + 1,
                    dist[i][j - 1] + 1,
                    dist[i - 1][j - 1] + 1
                )

    if verbose:
        print("\nMatrice de distance :")
        print("\n".join(map(lambda row: " ".join(map(str, row)), dist)))

    return dist[-1][-1]

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
    str1 = input("str1 = ")
    str2 = input("str2 = ")
    print(f"\nLevenshtein({str1}, {str2}) = {levenshtein(str1, str2)}.")
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":

    exercice1()
    exercice2()
    exercice3()
