import numpy as np

from Seidel import saidel_method


def val():
    d = np.array([[1.33, 0.21, 0.17, 0.12, -0.13],
                  [-0.13, -1.33, 0.11, 0.17, 0.12],
                  [0.12, -0.13, -1.33, 0.11, 0.17],
                  [0.17, 0.12, -0.13, -1.33, 0.11],
                  [0.11, 0.67, 0.12, -0.13, -1.33]])

    c = np.array([[0.01, 0, -0.02, 0, 0],
                  [0.01, 0.01, -0.02, 0, 0],
                  [0, 0.01, 0.01, 0, -0.02],
                  [0, 0, 0.01, 0.01, 0],
                  [0, 0, 0, 0.01, 0.01]])

    b = np.array([1.2, 2.2, 4.0, 0.0, -1.2])
    a = 4 * c + d
    return a, b


def output(result_full):
    np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
    result_x = result_full[0]
    result_iteration = result_full[1]
    print("Результат:")
    for i in range(val()[0].shape[0]):
        print(f"x_{i + 1} = " "%.4f" % result_x[i])
    print(f"\nКол-во итераций: {result_iteration}")
    print("======================================")


if __name__ == '__main__':
    print("\n======================================")
    print("Метод Зейделя:\n--------------")
    result = saidel_method(val()[0], val()[1])
    output(result)
