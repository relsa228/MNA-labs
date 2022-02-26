import numpy as np

from Gauss import gauss_func
from Main_elem_col import gauss_pivot_func

D = np.array([[2.33, 0.81, 0.67, 0.92, -0.53],
              [-0.53, 2.33, 0.81, 0.67, 0.92],
              [0.92, -0.53, 2.33, 0.81, 0.67],
              [0.67, 0.92, -0.53, 2.33, 0.81],
              [0.81, 0.67, 0.92, -0.53, 2.33]])

C = np.array([[0.2, 0, 0.2, 0, 0],
              [0, 0.2, 0, 0.2, 0],
              [0.2, 0, 0.2, 0, 0.2],
              [0, 0.2, 0, 0.2, 0],
              [0, 0, 0.2, 0, 0.2]])

b = np.array([4.2 for i in range(5)])


def output(result):
    result_x = result[0]
    result_b = result[2]
    result_matrix_a = np.c_[result[1], result_b.T]
    print(f"\nПолученная матрица:\n {result_matrix_a}")
    print("\nРезультат:")
    for i in range(A.shape[0]):
        print(f"x[{i + 1}] =" "%.4f" % result_x[i])


if __name__ == '__main__':
    A = 4 * C + D
    print("Метод Гаусса:")
    result = gauss_func(A, b)
    if result is not None:
        output(result)

    print("Метод Гаусса с выбором главного элемента по столбцу:")
    result = gauss_pivot_func(A, b)
    output(result)
