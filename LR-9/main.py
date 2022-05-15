from euler_method_module import euler_method
from runge_kutta_method_module import runge_kutta_method


def function(x, y):
    return 1.1*(1 - y**2)/(2*x**2 + y**2 + 1)


print(euler_method(function, 10000, 0.0001, 0, 0))
print(runge_kutta_method(function, 10000, 0.0001, 0, 0))
