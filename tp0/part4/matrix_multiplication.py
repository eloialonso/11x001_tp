import numpy as np  # librairie pour l'algèbre linéaire

# On peut définir les matrices A, B et C
# sous forme de listes imbriqués.
A = [[1, 2, 3, 4]]  # 1 x 4
B = [[1], [2], [3], [4]]    # 4 x 1

C = [[0]]

# On peut calculer C = AB comme on l'aurait fait
# à la main.
for i in range(1):
    for j in range(1):
        for k in range(4):
            C[i][j] = C[i][j] + A[i][k]*B[k][j]

print(C)

# On peut vérifier que notre résultat est correct
# en utilisant la librairie NumPy
A_np = np.array(A)
B_np = np.array(B)
C_np = A_np @ B_np

print(C_np)
