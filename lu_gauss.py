import numpy as np

def lu_gauss(A, B):
    lu, piv = np.linalg.lu_factor(A)
    solusi = np.linalg.lu_solve((lu, piv), B)
    return solusi

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
B = np.array([8, -11, -3])

solusi = lu_gauss(A, B)
print("Solusi menggunakan dekomposisi LU (Gauss):", solusi)
