import sympy as sp
import numpy as np
from scipy.sparse.linalg import gmres
from numpy.linalg import norm


def gradient2d(fs,n):
    F = [[0 for j in range(len(fs))] for i in range(len(fs))]
    for i in range(len(fs)):
        f = fs[i]
        for j in range(n + 1):
            d = sp.diff(f, sp.Symbol('x'+str(j)))
            F[i][j] = d
    return F


def gradient(f,n):
    F = []
    for i in range(n):
        d = sp.diff(f, sp.Symbol('x'+str(i+1)))
        F.append(d)
    return F


def gradientDesc(f, n, a, guess, tol, maxit):
    grad = gradient(f,n)
    grad_sol = np.array(calcVector(grad, guess))
    guess = np.array(guess)

    guess = guess - a * grad_sol
    count = 1
    while norm(calcVector(grad, guess)) > tol and count < maxit:
        grad = gradient(f,n)
        grad_sol = np.array(calcVector(grad, guess))
        guess = guess - a * grad_sol
        count += 1
    return guess, count


def newtons(fs, guess, a, tol, maxit):
    grad = gradient2d(fs,2)
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


def calcVector(fs, x):
    sol = []
    syms = [sp.Symbol('x'+str(i+1)) for i in range(len(x))]
    for i in range(len(fs)):
        f = fs[i]
        lam_f = sp.lambdify(syms, f, 'numpy')
        sol.append(lam_f(*x))
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
