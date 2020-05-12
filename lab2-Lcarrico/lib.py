import matplotlib.pyplot as plt
from math import exp, log
import sympy as sp


def graph(f, div, iter):
    x = [i/div for i in range(iter[0],iter[1])]
    y = [f(i) for i in x]
    plt.plot(x, y)
    plt.title("Graph of 32*x^6 - 48*x^4 + 18*x^2 - 1")
    plt.show()


def bisect(f, a, b, tol, itmax):
    count = 0
    while abs(b - a) >= tol and abs(f((a + b)/2)) >= tol and count < itmax:
        c = (a + b)/2
        if f(c) == 0:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        count += 1
    return c, count


def newtons(f, fprime, x, tol, itmax, its=1):
    if abs(f(x)) < tol or its > itmax:
        return x, its
    x = x - f(x)/fprime(x)
    return newtons(f, fprime, x, tol, itmax, its+1)


def solveRoot(m, a, guess):
    x = sp.symbols('x')

    f1 = x**m - a
    f1prime = sp.diff(f1)
    f1 = sp.lambdify(x, f1)
    f1prime = sp.lambdify(x, f1prime)

    return newtons(f1, f1prime, guess, 10**-16, 100)


def secant(f, x0, x1, tol, itmax, its=1):
    if abs(f(x1)) < tol or its > itmax or abs(x1-x0) < tol:
        return x1, its
    remainder = f(x1) * (x1 - x0)/(f(x1) - f(x0))
    x0 = x1
    x1 = x1 - remainder
    return secant(f, x0, x1, tol, itmax, its+1)


def fixedPoint(g, x0, tol, itmax):
    x1 = g(x0)
    it = 0

    while abs(g(x1) - x1) >= tol and abs(x1 - x0) >= tol and it < itmax:
        x0, x1 = x1, g(x1)
        it += 1
    return x1, it


def addToPlot(f, params, name):
    dct={}
    for i in range(1, 21):
        dct[i] = log(abs(f(params[0], params[1], params[2], params[3], i)[0] - 1.13472))
    import matplotlib.pyplot as plt
    x = list(dct.keys())
    y = list(dct.values())
    plt.plot(x, y)
    plt.legend(["Newtons", "Bisection", "Secant"])
