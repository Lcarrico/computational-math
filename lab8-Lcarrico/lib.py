import sympy as sp
import numpy as np
from numpy.linalg import norm
from scipy.sparse.linalg import gmres
import matplotlib.pyplot as plt


def graph(vals, labels, title):
    plt.title(title)
    for i in range(len(vals)):
        plt.plot(vals[i][0], vals[i][1], label=labels[i])
    plt.legend(loc='best')
    plt.show()


def eulerExplicit(f_exprs, n, h, t0, y0s, var_count=None):
    if var_count == None:
        var_count = len(f_exprs)

    t = [t0]
    ys = [[y0s[i]] for i in range(len(y0s))]

    x = []
    for i in range(var_count + 1):
        x.append(sp.Symbol('x' + str(i)))

    fs = []
    for f in f_exprs:
        fs.append(sp.lambdify(x, f))

    for i in range(1, n+1):
        t.append(t[-1] + h)
        cur_y = [y[-1] for y in ys]
        for j in range(len(ys)):
            ys[j].append(ys[j][-1] + h * fs[j](t[-1], *cur_y))

    return t, ys


def rungeKutta2(f_exprs, n, h, t0, y0s):
    t = [t0]
    t = np.array(t)
    # print(t)
    ys = [[y0s[i]] for i in range(len(y0s))]

    x = []
    for i in range(len(f_exprs) + 1):
        x.append(sp.Symbol('x' + str(i)))

    fs = []
    for f in f_exprs:
        fs.append(sp.lambdify(x, f))

    for i in range(1, n+1):
        t = np.append(t, t[-1] + h)
        cur_y = np.array([y[-1] for y in ys])

        for j in range(len(ys)):
            k2 = cur_y[j] + h * fs[j](t[-1] + (h/2), *(cur_y + (h/2) * fs[j](t[-1], *cur_y)))
            ys[j].append(k2)

    return t, ys

def rungeKutta4(f_exprs, n, h, t0, y0s):
    t = [t0]
    t = np.array(t)
    # print(t)
    ys = [[y0s[i]] for i in range(len(y0s))]

    x = []
    for i in range(len(f_exprs) + 1):
        x.append(sp.Symbol('x' + str(i)))

    fs = []
    for f in f_exprs:
        fs.append(sp.lambdify(x, f))

    for i in range(1, n+1):
        t = np.append(t, t[-1] + h)
        cur_y = np.array([y[-1] for y in ys])

        for j in range(len(ys)):
            k1 = h * fs[j](t[-1], *cur_y)
            k2 = h * fs[j](t[-1] + (h/2), *(cur_y + k1/2))
            k3 = h * fs[j](t[-1] + (h/2), *(cur_y + k2/2))
            k4 = h * fs[j](t[-1] + h, *(cur_y + k3))

            ys[j].append(cur_y[j] + (1/6)*(k1 + 2*k2 + 2*k3 + k4))

    return t, ys



def newtons(fs, symbols, guess, a, tol, maxit):
    grad = gradient2d(fs,symbols)
    grad_sol = np.matrix(calcGradient2d(grad, guess))
    vector_sol = np.matrix(calcVector(fs, guess))
    guess = np.matrix(guess)

    x = np.matrix(gmres(grad_sol, vector_sol.T, tol=10E-8)[0])
    guess = np.asarray(guess - a*x)[0]

    count = 1
    while norm(calcVector(fs, guess)) > tol and count < maxit:
        grad_sol = np.matrix(calcGradient2d(grad, guess))
        vector_sol = np.matrix(calcVector(fs, guess))
        guess = np.matrix(guess)

        x = np.matrix(gmres(grad_sol, vector_sol.T, tol=10E-8)[0])
        guess = np.asarray(guess - a*x)[0]
        count += 1
    return guess, count


def newtons_lambdafied(fs, grad, constants, symbols, guess, a, tol, maxit):
    grad_sol = np.matrix(calcGradient2d_lambdafied(grad, guess))
    vector_sol = np.matrix(calcVector_lambdafied(fs, guess))

    guess = np.matrix(guess)

    x = np.matrix(gmres(grad_sol, vector_sol.T, tol=10E-8)[0])
    guess = np.asarray(guess - a*x)[0]

    count = 1
    while norm(calcVector_lambdafied(fs, guess)) > tol and count < maxit:
        grad_sol = np.matrix(calcGradient2d_lambdafied(grad, guess))
        vector_sol = np.matrix(calcVector_lambdafied(fs, guess))
        guess = np.matrix(guess)

        x = np.matrix(gmres(grad_sol, vector_sol.T, tol=10E-8)[0])
        guess = np.asarray(guess - a*x)[0]
        count += 1
    return guess, count


def calcVector(fs, x):
    sol = []
    syms = [sp.Symbol('x'+str(i+1)) for i in range(len(x))]
    for i in range(len(fs)):
        f = fs[i]
        lam_f = sp.lambdify(syms, f, 'numpy')
        sol.append(lam_f(*x))
    return sol

def calcVector_lambdafied(fs, x):
    sol = []
    for i in range(len(fs)):
        f = fs[i]
        sol.append(f(*x))
    return sol

def calcGradient2d(gradient, x):
    syms = [sp.Symbol('x'+str(i+1)) for i in range(len(x))]
    sol = [[0 for j in range(len(x))] for i in range(len(x))]
    for i in range(len(gradient)):
        for j in range(len(gradient)):
            f = gradient[i][j]
            lam_f = sp.lambdify(syms, f, 'numpy')
            sol[i][j] = lam_f(*x)
    return sol

def calcGradient2d_lambdafied(gradient, x):
    sol = [[0 for j in range(len(x))] for i in range(len(x))]
    for i in range(len(gradient)):
        for j in range(len(gradient)):
            f = gradient[i][j]
            sol[i][j] = f(*x)
    return sol

def gradient2d(fs,symbols):
    F = [[0 for j in range(len(fs))] for i in range(len(fs))]
    for i in range(len(fs)):
        f = fs[i]
        for j in range(len(symbols)):
            d = sp.diff(f, symbols[j])
            F[i][j] = d
    return F


def eulerImplicit(f_exprs, n, h, t0, y0s, itmax=100, tol=10E-8, alpha=1):
    t = [t0]
    ys = [[y0s[i]] for i in range(len(y0s))]
    t = np.array(t)
    ys = np.array(ys)

    x = []
    for i in range(len(f_exprs) + 1):
        x.append(sp.Symbol('x' + str(i)))

    y_sym = []
    for i in range(len(f_exprs), len(f_exprs) * 2):
        y_sym.append(sp.Symbol('x' + str(i+1)))

    # n = 1
    for i in range(1, n+1):

        t = np.append(t, t[-1] + h)
        cur_y = ys[:, -1]

        # Newton's method for nonlinear systems of equations
        it = 0
        guess = cur_y

        f_newtons = [i for i in f_exprs]
        for i in range(len(f_newtons)):
            f_newtons[i] = str(cur_y[i]) + " + " + str(h) + " * (" + f_exprs[i] + ") - x" + str(i+1)

        # print(f_newtons)
        grad_newtons = gradient2d(f_newtons, x[1:])

        for i in range(len(f_newtons)):
            f_newtons[i] = sp.lambdify(x[1:], f_newtons[i])

        for i in range(len(grad_newtons)):
            for j in range(len(grad_newtons[i])):
                grad_newtons[i][j] = sp.lambdify(x[1:], grad_newtons[i][j])

        y_n1 = newtons_lambdafied(f_newtons, grad_newtons, [], x[1:], guess, alpha, tol, itmax)
        new_ys = ys.tolist()
        for i in range(len(y_n1[0])):
            new_ys[i].append(y_n1[0][i])

        ys = np.array(new_ys)

    return t, ys
