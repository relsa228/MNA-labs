import numpy as np


def seidel_criteria(matrix) -> bool:
    on_proc_matrix = matrix.copy()

    diag = np.diagonal(on_proc_matrix)
    for i in range(0, on_proc_matrix.shape[0]):
        for j in range(0, on_proc_matrix.shape[0]):
            if i != j:
                on_proc_matrix[i][j] = on_proc_matrix[i][j] / diag[i]
    for i in range(0, on_proc_matrix.shape[1]):
        on_proc_matrix[i][i] = 0

    f = np.zeros(on_proc_matrix.shape)
    for i in range(0, on_proc_matrix.shape[0]):
        for j in range(i, on_proc_matrix.shape[0]):
            f[i][j] = on_proc_matrix[i][j]

    h = on_proc_matrix - f
    e = np.eye(on_proc_matrix.shape[0])
    lambd = np.linalg.eigh(on_proc_matrix)[0]

    for i in lambd:
        res = f + i*h - i*e
        if int(np.linalg.det(res)) == 0 and abs(i) >= 1:
            return False

    return True


def seidel_method(a, b, eps):
    n = len(a)
    x = np.zeros(n)
    iterations = 0

    if not seidel_criteria(a):
        print("Нарушен необходимый критерий")
        return None

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(a[i][j] * x_new[j] for j in range(i))
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / a[i][i]

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
        iterations += 1

    return x, iterations
