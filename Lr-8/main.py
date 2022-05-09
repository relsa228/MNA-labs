import numpy as np
from simpsons_rule_module import simpson
from riemann_sum_module import rimemann
from trapezoidal_rule_module import trapezoidal


def f(x):
    return np.sqrt(x)


a = 0
b = 4
n = 100

if __name__ == '__main__':
    print(simpson(f, a, b, n))
    print(rimemann(f, a, b, n))
    print(trapezoidal(f, a, b, n))
