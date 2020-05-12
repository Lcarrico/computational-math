import math
from random import random, randint
import sympy as sp
from sympy.solvers import solve

def trapRule(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(1, n):
        total += f(a + i * h)
    total += (1/2)*(f(a + 0) + f(a + n * h))
    return total * h


def trapRuleError(a, b, max, tol):
    top = b - a
    bottom = ((12 * tol)/(max * (b - a)))**(1/2)
    return top/bottom


def simpson(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(1, n):
        #if even, divide the 4 by 2
        total += 4/(((i+1)%2) + 1)*f(a + i * h)
    total += f(a + 0) + f(a + n * h)
    return total * h / 3


def simpsonError(a, b, max, tol):
    top = b - a
    bottom = ((180 * tol)/(max * (b - a)))**(1/4)
    return top/bottom

def simpsonError2(a, b, max, tol):
    top = (b-a)**5*max
    bottom = 180 * tol
    return (top/bottom)**(1/4)

def forFD(f, x, h):
    return (f(x + h) - f(x)) / h


def cenFD(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def bacFD(f, x, h):
    return (f(x) - f(x - h)) / h


def cenSD(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2


def lengthOfCurve(f_expr, a, b, n, m="t"):
    x = sp.symbols("x")
    derv = sp.diff(f_expr, x)
    expr = (1 + (derv)**2)**(1/2)
    f = sp.lambdify(x, expr)

    if m == 't':
        return trapRule(f, a, b, n)
    return simpson(f, a, b, n)

def monteCarlo(f, a, b, n):
    total = sum([f(random()*(b-a)+a) for i in range(n)])
    return (b-a) * (1/n) * total

def monteCarlo2D(f_expr, a, b, c, d, n):
    x, y = sp.symbols('x y')
    exprs_x = solve(f_expr, y)
    fs = [sp.lambdify(x, i) for i in exprs_x]
    total = 0
    for i in range(n):
        rand = random()*(b-a)+a
        rand_f = fs[randint(0, len(fs)-1)]
        total += abs(rand_f(rand))
    return (b-a) * (d-c) / n * total
