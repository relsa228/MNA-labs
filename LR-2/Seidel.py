import numpy as np


def saidel_method(matrix_a, b):
    max_elem = len(matrix_a)
    x = [.0 for i in range(max_elem)]
    iteration = 0
    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(max_elem):
            s1 = sum(matrix_a[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix_a[i][j] * x[j] for j in range(i + 1, max_elem))
            x_new[i] = (b[i] - s1 - s2) / matrix_a[i][i]
            pogr = sum(abs(x_new[i] - x[i]) for i in range(max_elem))
            converge = pogr < 1e-6
        iteration += 1
        x = x_new
    return x, iteration
