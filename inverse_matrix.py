import numpy as np

def inverse_matrix(A, B):
    A_inv = np.linalg.inv(A)
    solusi = np.dot(A_inv, B)
    return solusi

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
B = np.array([8, -11, -3])

solusi = inverse_matrix(A, B)
print("Solusi menggunakan matriks balikan:", solusi)
