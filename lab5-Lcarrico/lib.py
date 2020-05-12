def LUFactorization(A):
    n = len(A)
    L = [[0 for i in range(n)] for i in range(n)]
    U = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1
        for j in range(i):
            total = sum([L[i][k]*U[k][j] for k in range(i)])
            L[i][j] = (A[i][j] - total) / U[j][j]
        for j in range(i,n):
            total = sum([L[i][k]*U[k][j] for k in range(j)])
            U[i][j] = A[i][j] - total

    return [L, U]


def LUx(A, b):
    n = len(b)
    L,U = LUFactorization(A)
    y = []
    for i in range(n):
        y.append(b[i] - sum([L[i][j]*y[j] for j in range(i)]))
    x = [0 for i in range(n)]
    for i in range(0,n)[::-1]:
        x[i] = round((y[i] - sum([U[i][k]*x[k] for k in range(i,n)])) / U[i][i], 6)
    return x
