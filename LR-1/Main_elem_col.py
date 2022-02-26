import numpy as np


def gauss_pivot_func(matrix_a, b):
    for k in range(matrix_a.shape[0] - 1):
        # поиск строки с максимальным элементом
        max_elem = 0
        strng = 0
        for i in range(k, matrix_a.shape[0]):
            if abs(matrix_a[i, k]) > abs(max_elem):
                max_elem = matrix_a[i, k]
                strng = i
        # меняем местами строки квадратной матрицы
        change = np.repeat(matrix_a[k], 1)
        matrix_a[k], matrix_a[strng] = matrix_a[strng], change
        # меняем местами элементы вектора-столбца
        change = np.repeat(b[k], 1)
        b[k], b[strng] = b[strng], change
        # делим полученную строку на max_elem
        matrix_a[k] = matrix_a[k] / max_elem
        b[k] = b[k] / max_elem
        # домножаем строку на коэффициенты и вычитаем ее из остальных строк
        for i in range(k + 1, matrix_a.shape[0]):
            factor = matrix_a[i, k]
            matrix_a[i] = matrix_a[i] - matrix_a[k] * factor
            b[i] = b[i] - b[k] * factor

    # находим аргументы уравнений
    x = [b[b.shape[0] - 1] / (matrix_a[matrix_a.shape[0] - 1, matrix_a.shape[0] - 1])]
    for i in range(matrix_a.shape[0] - 2, -1, -1):
        n = b[i]
        for j in range(len(x)):
            n = n - x[j] * matrix_a[i, matrix_a.shape[0] - 1 - j]
        x.append(n)

    # переворачиваем значения в списке
    x_norm = []
    for i in reversed(x):
        x_norm.append(i)
    return x_norm, matrix_a, b
