import numpy as np

from Gauss import gauss_func
from Main_elem_col import gauss_main_col_func
from Main_elem_full import gauss_main_full_func


def val():
    d = np.array([[2.33, 0.81, 0.67, 0.92, -0.53],
                  [-0.53, 2.33, 0.81, 0.67, 0.92],
                  [0.92, -0.53, 2.33, 0.81, 0.67],
                  [0.67, 0.92, -0.53, 2.33, 0.81],
                  [0.81, 0.67, 0.92, -0.53, 2.33]])

    c = np.array([[0.2, 0, 0.2, 0, 0],
                  [0, 0.2, 0, 0.2, 0],
                  [0.2, 0, 0.2, 0, 0.2],
                  [0, 0.2, 0, 0.2, 0],
                  [0, 0, 0.2, 0, 0.2]])

    b = np.array([4.2 for _ in range(5)])
    a = 4 * c + d
    return a, b


def output(result_full):
    np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
    result_x = result_full[0]
    result_matrix_a = np.c_[result_full[1], result_full[2].T]
    print(f"Полученная матрица:\n {result_matrix_a}")
    print("\nРезультат:")
    for i in range(val()[0].shape[0]):
        print(f"x_{i + 1} = " "%.4f" % result_x[i])


if __name__ == '__main__':

    print("\nМетод Гаусса:\n-------------")
    result = gauss_func(val()[0], val()[1])
    if result is not None:
        output(result)
    print("======================================================================================")

    print("\n\nМетод Гаусса с выбором главного элемента по столбцу:\n-----------------------------"
          "-----------------------")
    result = gauss_main_col_func(val()[0], val()[1])
    output(result)
    print("======================================================================================")

    print("\n\nМетод Гаусса с выбором главного элемента по всей матрице:\n------------------------"
          "---------------------------------")
    result = gauss_main_full_func(val()[0], val()[1])
    output(result)
    print("======================================================================================")
