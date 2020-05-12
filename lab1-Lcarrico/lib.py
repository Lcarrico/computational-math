import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')


def plot(f, x, n, a, xInt):
    for i in n:
        expr = taylor(f, x, i, a)
        print(expr)

        expr_eval = sp.lambdify(x, expr, "numpy")
        yInt = np.zeros(xInt.size, 'd')

        for j in range(xInt.size):
            yInt[j] = expr_eval(xInt[j])

        plt.plot(xInt, yInt, label="Degree %d" % i)
        plt.legend(loc='best')
    plt.show()


def plotTaylors(fs, xInt):
    for expr in fs:
        expr_eval = sp.lambdify(x, expr, "numpy")
        yInt = np.zeros(xInt.size, 'd')

        for j in range(xInt.size):
            yInt[j] = expr_eval(xInt[j])

        plt.plot(xInt, yInt, label=expr)
        plt.legend(loc='best')
    plt.show()


def taylor(expr, x, n, a):
    p = expr.subs(x, a)
    for count in range(1, n+1):
        expr = sp.diff(expr, x)
        p += ((x-a)**count/sp.factorial(count)) * expr.subs(x, a)
    return(p)
