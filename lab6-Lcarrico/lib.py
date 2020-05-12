import numpy as np


def accuracyScore(x, b):
    return round(100 - norm(x, b), 2)

def norm(x, b):
    return np.sum(np.absolute(np.subtract(x,b)))


def jacobi(A, b, x1, tol, maxit):
    A = np.copy(A)
    size = x1.size
    x2 = np.zeros(size)
    count = 0
    norm = np.sum(np.absolute(np.subtract(np.dot(A,x2),b)))
    while count < maxit and norm > tol:
        count += 1
        for i in range(size):
            total = 0
            for j in range(i):
                total += A[i, j] * x1[j]
            for j in range(i+1, size):
                total += A[i, j] * x1[j]
            x2[i] = (b[i] - total) / A[i, i]
        norm = np.sum(np.absolute(np.subtract(np.dot(A,x2),b)))
        x1[:] = x2[:]
    return x1, count


def seidel(A, b, x, tol, maxit):
    A = np.copy(A)
    size = x.size
    count = 0
    norm = np.sum(np.absolute(np.subtract(np.dot(A,x),b)))
    while count < maxit and norm > tol:
        count += 1
        for i in range(size):
            total = 0
            for j in range(i):
                total += A[i, j] * x[j]
            for j in range(i+1, size):
                total += A[i, j] * x[j]
            x[i] = (b[i] - total) / A[i, i]
        norm = np.sum(np.absolute(np.subtract(np.dot(A,x),b)))
    return x, count


def createTridiagonal(inner, outer, n):
    A = np.zeros((n,n))
    A[0, 0] = inner

    for i in range(1, n):
        A[i, i] = inner
        A[i, i-1] = outer
        A[i-1, i] = outer

    return A


def createT(i, n):
    return ((2 * i) - 1) / (2 * n)

def createB(tj):
    return 1/4 + tj - ((1/2) * tj**3)

def createMandB(n):
    M = np.zeros((n,n))
    b = np.zeros(n)
    for i in range(n):
        ti = createT(i+1, n)
        b[i] = createB(ti)
        for j in range(n):
            tj = createT(j+1, n)
            M[i,j] = (1/(2 * n)) * ((ti**3/(1 + tj)) + 1)
    return M, b
