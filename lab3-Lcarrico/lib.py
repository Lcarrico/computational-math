import numpy as np
import sympy as sp
from math import *


def dividedDiffApprox(x, y):
    if len(x) > 1:
        return dividedDiff(x, y) * factorial(len(x) - 1)
    return dividedDiff(x, y)


def dividedDiff(x, y):
    if len(x) != len(y):
        print("x and y aren't the same length")
        return
    if len(x) == 1:
        return y[0]
    if len(x) == 2:
        return (y[1] - y[0])/(x[1] - x[0])
    return (dividedDiff(x[1:],y[1:]) - dividedDiff(x[:-1],y[:-1])) / (x[-1] - x[0])


def lagrange(X, Y):
    x = sp.symbols('x')
    expr = 0
    for i in range(len(X)):
        if i == len(X) - 1:
            X0 = X[:-1]
        else:
            X0 = X[:i] + X[i+1:]
        top = np.prod([x-j for j in X0])
        bottom = np.prod([X[i] - j for j in X0])
        val = Y[i]
        expr += (top / bottom) * val
    expr = sp.simplify(expr)
    print("\n",expr,"\n")
    return sp.lambdify(x, expr, 'numpy')
