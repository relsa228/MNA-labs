import numpy as np

from Gauss import gaussFunc
from MainElem import gaussPivotFunc

matrix = np.array([[3.8, 6.7, -1.2, 5.2],
                   [6.4, 1.3, -2.7, 3.8],
                   [2.4, -4.5, 3.5, -0.6]])


if __name__ == '__main__':
    result = gaussPivotFunc(matrix)

    print(result)
