#! /usr/bin/python
# -*- coding: utf-8 -*-
u"""
Cubic Spline library
author Atsushi Sakai
license: MIT
"""
import numpy as np
import math
import matplotlib.pyplot as plt

from spline_module import Spline


def calc_xy_curvature(s, sx, sy):
    u"""
    Calc curvature x-y spline curve
    """
    dx = sx.__calc__D(s)
    ddx = sx.calcdd(s)
    dy = sy.__calc__D(s)
    ddy = sy.calcdd(s)
    k = (ddy * dx - ddx * dy) / (dx ** 2 + dy ** 2)
    return k


def calc_yaw(s, sx, sy):
    u"""
    calc yaw of x-y spline curve
    """
    dx = sx.__calc__D(s)
    dy = sy.__calc__D(s)
    yaw = math.atan2(dy, dx)
    return yaw


if __name__ == '__main__':
    # input
    #  x = [-1.0, 0.0, 1.0, 2.0, 3.0]
    #  x = [-0.5, 0.0, 0.5, 1.0, 1.5]
    x = [1, 1.25, 1.5, 1.75, 2]
    #  y = [3.2, 2.7, 6, 5, 6.5]
    y = [1, 0.8, 0.6, 0.5, 0.5]

    # 3d spline interporation
    spline = Spline(x, y)
    rx = np.arange(1, 2, 0.01)
    ry = [spline.calc(i) for i in rx]

    plt.plot(x, y, "xb", color='b')
    plt.plot(rx, ry, "-r", color='r')
    plt.plot(x, np.divide(1, x), color='g')
    plt.grid(True)
    plt.axis("equal")
    plt.show()
