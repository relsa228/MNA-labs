import numpy as np


def make_identity(matrix_t):
    for nrow in range(len(matrix_t) - 1, 0, -1):
        row = matrix_t[nrow]
        for upper_row in matrix_t[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix_t


def gauss_pivot_func(matrix):
    for nrow in range(len(matrix)):
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow]
        if abs(divider) < 1e-10:
            raise ValueError(f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}")
        row /= divider
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    make_identity(matrix)
    return matrix
