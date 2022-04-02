import sympy as sp
import Iteration_module
import Newton_module

if __name__ == '__main__':
    (x, y) = sp.symbols('x y')
    eps = 0.0001
    f1 = sp.tan(x * y + 0.2) - x
    f2 = 0.8 * x ** 2 + 2 * y ** 2 - 1

    plots = sp.plot_implicit(sp.Eq(f1, 0), (x, -2, 2), (y, -2, 2), line_color="blue", show=False)
    plots.extend(sp.plot_implicit(sp.Eq(f2, 0), (x, -2, 2), (y, -2, 2), line_color="red", show=False))
    plots.show()

    first_approximation = [0.35, 0.65]
    print("1. Simple iterations method: ")
    Iteration_module.print_result(first_approximation, eps)
    print("2. Newton method: ")
    Newton_module.print_result(first_approximation, eps)
