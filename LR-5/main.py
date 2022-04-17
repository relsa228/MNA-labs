import numpy as np
from jacobi_algorithm_module import jacobi

C = np.array([[0.2, 0, 0.2, 0, 0],
             [0, 0.2, 0, 0.2, 0],
             [0.2, 0, 0.2, 0, 0.2],
             [0, 0.2, 0, 0.2, 0],
             [0, 0, 0.2, 0, 0.2]])

D = np.array([[2.33, 0.81, 0.67, 0.92, -0.53],
             [0.81, 2.33, 0.81, 0.67, 0.92],
             [0.67, 0.81, 2.33, 0.81, 0.92],
             [0.92, 0.67, 0.81, 2.33, -0.53],
             [-0.53, 0.92, 0.92, -0.53, 2.33]])

matrix_A = 4*C + D

eps = 0.0001

sol = jacobi(matrix_A, eps)
print(sol[0])
print(np.linalg.eig(matrix_A)[0])
