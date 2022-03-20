from sympy import *
import Chord_module as cm
import Half_div_module as hm
import Newton_module as nm
import Shturm_module as sm


poly = [1, -5.5796, -193.022, -633.105]
eps = 0.0001


def f(x):
    return x ** 3 - 5.5796 * x ** 2 - 193.022 * x - 633.105


def output(result_full):
    if result_full is None:
        print("Корней нет")
        print("======================================")
    else:
        result_x = result_full[1]
        result_iteration = result_full[0]
        print(f"Результат: " "%.4f" % result_x)
        print(f"\nКол-во итераций: {result_iteration}")
        print("======================================")


if __name__ == '__main__':
    x = Symbol('x')
    by_shturm = sm.shturm_function_answer(f(x), x)
    print(f"\nВычисление кол-ва корней методом Штурма: {by_shturm}")

    print("\n======================================")
    print("Метод Ньютона:\n--------------")
    output(nm.exec_newton(f(x), poly, eps))

    print("\n======================================")
    print("Метод хорд:\n--------------")
    output(cm.exec_chord_method(f(x), poly, eps, poly[1]))

    print("\n======================================")
    print("Метод половинного деления:\n--------------")
    output(hm.exec_half_div(f, eps))
