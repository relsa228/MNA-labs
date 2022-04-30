import numpy as np


class NewtonPoly:

    def __init__(self, x_arg, y_arg):
        self.X = np.array(x_arg)
        self.Y = np.array(y_arg)

    def get_n(self, j, xc):
        n = 1
        for i in range(j):
            n *= (xc - self.X[i])

        return n

    def get_a(self, j, l):
        if j == 0:
            return self.Y[0]
        elif j - l == 1:
            return (self.Y[j] - self.Y[l]) / (self.X[j] - self.X[l])
        else:
            return (self.get_a(j, l + 1) - self.get_a(j - 1, l)) / (self.X[j] - self.X[l])

    def interpolate(self, x_point):
        newton_res = 0
        for j in range(len(self.X)):
            newton_res += self.get_a(j, 0) * self.get_n(j, x_point)

        return newton_res
