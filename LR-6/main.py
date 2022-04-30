import time

import matplotlib.pyplot as plt
import numpy as np

from lagrange_module import LagrangePoly
from newton_module import NewtonPoly

k = 4
m = 2
X = np.linspace(0, 1, 11)
p = [0, 0.41, 0.79, 1.13, 1.46, 1.76, 2.04, 2.3, 2.55, 2.79, 3.01]
Y = [p_i + (-1) ** k * m for p_i in p]

x = [-1.5, -0.75, 0, 0.75, 1.5]
y = [-14.10141, -0.93159, 0, 0.93159, 14.10141]
yy = [-14.10141, -3.00956, -1.55740, -0.93159, -0.54630, -0.25534, 0, 0.25534, 0.54630, 0.93159, 1.55740, 3.00956,
      14.10141]
xx = [-1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]

lp = LagrangePoly(X, Y)
nw = NewtonPoly(X, Y)

t = time.perf_counter()
res = nw.interpolate(0.47)
t_w = time.perf_counter() - t

print(f"Интерполяция в точке 0.47: {'%.5f' % res}")
print(f"Время выполнения: {'%.5f' % t_w}")

for i in range(0, 10):
    print(lp.basis(0.47, i))
# plt.plot(xx, )
# plt.plot(xx, lp.basis(xx, 1))
# plt.plot(xx, lp.basis(xx, 2))
# plt.plot(xx, lp.basis(xx, 3))
# plt.plot(X, nw.interpolate(X), linestyle=':')
# plt.plot(xx, np.tan(xx), linestyle=':')
# plt.show()
