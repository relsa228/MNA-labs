import time

from euler_method_module import euler_method
from runge_kutta_method_module import runge_kutta_method


def function(x, y):
    return 1.1*(1 - y**2)/(2*x**2 + y**2 + 1)

print("Метод Эйлера:")
t = time.perf_counter()
euler = euler_method(function, 1000000, 0.000001, 0, 0)
t_w = time.perf_counter() - t
print(f"В точке x = {'%.6f' % euler[0]} имеет значение: {'%.6f' % euler[1]}")
print(f"Время выполнения: {'%.6f' % t_w}")

print("\nМетод Рунге-Кутта:")
t = time.perf_counter()
runge_kutta = runge_kutta_method(function, 1000000, 0.000001, 0, 0)
t_w = time.perf_counter() - t
print(f"В точке x = {'%.6f' % runge_kutta[0]} имеет значение: {'%.6f' % runge_kutta[1]}")
print(f"Время выполнения: {'%.6f' % t_w}")