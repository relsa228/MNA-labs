import time

from runge_kutt_module import runge_kutta_method
from adams_module import adams_bash


def function(x, y):
    return 1.1 * (1 - y ** 2) / (2 * x ** 2 + y ** 2 + 1)


print("\nМетод Рунге-Кутта:")
t = time.perf_counter()
runge_kutta = runge_kutta_method(function, 1000000, 0.000001, 0, 0)
t_w = time.perf_counter() - t
print(f"В точке x = {'%.6f' % runge_kutta[0]} имеет значение: {'%.6f' % runge_kutta[1]}")
print(f"Время выполнения: {'%.6f' % t_w}")

print("\nМетод Адамса:")
t = time.perf_counter()
adams_bash = adams_bash(function, 1000000, 0, 1, 0)
t_w = time.perf_counter() - t
print(f"В точке x = {'%.6f' % adams_bash[0]} имеет значение: {adams_bash[1]}")
print(f"Время выполнения: {'%.6f' % t_w}")
