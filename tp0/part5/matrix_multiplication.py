import numpy as np

A = [[1, 2, 3, 4]]  # 1 x 4
B = [[1], [2], [3], [4]]    # 4 x 1

C = [[0]]

for i in range(1):
    for j in range(1):
        for k in range(4):
            C[i][j] = C[i][j] + A[i][k]*B[k][j]

print(C)

A_np = np.array(A)
B_np = np.array(B)
C_np = A_np @ B_np

print(C_np)
