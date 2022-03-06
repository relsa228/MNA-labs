import numpy as np


def prime_criteria(on_proc_matrix) -> bool:
    eigenvalues = np.linalg.eigh(on_proc_matrix)[0]
    for i in eigenvalues:
        if i >= 1:
            return False
    return True


def prime_iteration(a, b_data, eps):
    for i in range(a.shape[0]):
        b_data[i] /= a[i][i]
        a[i] /= a[i][i]

    b_inproc = np.eye(a.shape[0]) - a
    if not prime_criteria(b_inproc):
        print("Нарушен необходимый критерий")
        return None

    x = np.zeros(a.shape[0])
    converge = False
    interation = 0

    while not converge:
        x_new = b_inproc.dot(x.T) + b_data
        converge = np.sqrt((x_new - x).dot((x_new - x).T)) <= eps
        x = x_new
        interation += 1

    return x, interation
