import numpy as np

def crout(A, B):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        U[i, i] = 1
        for k in range(i, n):
            sum = np.dot(L[i, :i], U[:i, k])
            L[k, i] = A[k, i] - sum
        for k in range(i + 1, n):
            sum = np.dot(L[k, :i], U[:i, i])
            U[i, k] = (A[i, k] - sum) / L[i, i]

    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        y[i] = (B[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
B = np.array([8, -11, -3])

solusi = crout(A, B)
print("Solusi menggunakan metode Crout:", solusi)
