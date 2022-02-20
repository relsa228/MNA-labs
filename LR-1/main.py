def make_identity(matrix):
    for nrow in range(len(matrix) - 1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix


if __name__ == '__main__':
    print("Kill me, please!!!")
