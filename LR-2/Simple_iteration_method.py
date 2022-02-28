import numpy as np


def prime_criteria(a):
    first_criteria = []
    for i in range(a.shape[0]):
        s = 0
        for j in range(a.shape[1]):
            s += np.abs(a[i][j])
        first_criteria.append(s)

    if max(first_criteria) < 1:
        return True

    second_criteria = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            second_criteria += a[i][j] ** 2

    if second_criteria < 1:
        return True

    third_criteria = []
    for j in range(a.shape[1]):
        s = 0
        for i in range(a.shape[0]):
            s += np.abs(a[i][j])
        third_criteria.append(s)

    return max(third_criteria) < 1


def prime_iteration(a, b):
    for i in range(5):
        b[i] /= a[i][i]
        a[i] /= a[i][i]

    b = np.eye(5) - a

    if not prime_criteria(b.copy()):
        print("criteria is not satisfied")
        return None

    x = np.zeros(5)
    e = 1
    interation_count = 0

    while e > 1e-4:
        x_next = b.dot(x.T) + b
        e = np.sqrt((x_next - x).dot((x_next - x).T))
        x = x_next
        interation_count += 1

    return x, interation_count
