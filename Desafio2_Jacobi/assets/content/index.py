import numpy as np


def clean_diagonal(A, B):
    n = len(A)
    M = np.zeros((n, n))
    C = np.zeros(n)
    for i in range(n):
        C[i] = B[i] / A[i][i]
        for j in range(n):
            if i != j:
                M[i][j] = -A[i][j] / A[i][i]
    return M, C


def jacobi(A, B, tolerance, max_iter=100000):
    x = np.zeros(len(B))
    M, C = clean_diagonal(A, B)
    for _ in range(max_iter):
        x_new = np.zeros(len(x))
        for i in range(len(x_new)):
            x_new[i] = np.dot(M[i], x) + C[i]
        errors = np.abs(x_new - x)
        max_error = np.max(errors)
        x = x_new
        if max_error < tolerance:
            break
    return x


A = [[52, 20, 25], [30, 50, 20], [18, 30, 52]]  # Matriz de coeficientes
B = [4800, 5810, 5690]  # Vector de términos independientes

tolerance = 1e-10  # Tolerancia de error para la solución

print(jacobi(A, B, tolerance))
