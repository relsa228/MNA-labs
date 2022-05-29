import time
import matplotlib.pyplot as plt

from runge_kutt_module import runge_kutta_method
from adams_module import adams_bash


def function(x, y):
    return 0.9 * (1 - y ** 2) / (2.5 * x ** 2 + y ** 2 + 1)

print("\nМетод Адамса:")
t = time.perf_counter()
adams_bash = adams_bash(function, 30, 0, 1, 0)
t_w = time.perf_counter() - t
print(f"В точке x = {'%.6f' % adams_bash[0]} имеет значение: {adams_bash[1]}")
print(f"Время выполнения: {'%.6f' % t_w}")

x_str = [0]
for i in range(30, 0, -1):
    x_str.append(x_str[30 - i] + 1/30)
plt.plot(x_str, adams_bash[1], "xb")
plt.grid(True)
plt.axis("equal")
plt.show()
