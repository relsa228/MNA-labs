def gaussFunc(matrix):
    for nrow, row in enumerate(matrix):
        divider = row[nrow]
        row /= divider
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    return matrix
