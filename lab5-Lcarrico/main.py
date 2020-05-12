from lib import *

print("\nExercise 1, testing LU Function")
test_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L,U = LUFactorization(test_A)
print(L)
print(U)

print("\nExercie 3, testing Ax=b, solving for x")
test_A = [[2,1,1],[1,2,1],[1,1,2]]
test_B = [7, 8, 9]

x = LUx(test_A, test_B)
print(x)

print("\nExercise 5, solving the first system")
test_A = [[2, 1, 0, 0, 0],
        [-1, 2, 1, 0, 0],
        [0, -1, 2, 1, 0],
        [0, 0, -1, 2, 1],
        [0, 0, 0, -1, 2]]

test_b = [3, 2, 2, 2, 1]

x = LUx(test_A, test_b)
print(x)

print("\nExercise 6, solving the second system")
test_A = [[2, 1, 1, 0, 0],
        [1, -1, 2, 0, 0],
        [3, 2, 10, 2, 0],
        [0, 0, -1, 2, 1],
        [0, 0, 2, 3, 0]]

test_b = [3, 2, 2, 2, 1]

x = LUx(test_A, test_b)
print(x)

print("\nExercise 7, solving the tridiagonal system")
n = 100
test_A = [[0 for i in range(n)] for i in range(n)]
test_b = [1 for i in range(n)]

for i in range(len(test_A)):
    test_A[i][i]=4
for i in range(1,len(test_A)):
    test_A[i][i-1]=1
for i in range(len(test_A)-1):
    test_A[i][i+1]=1

x = LUx(test_A, test_b)
print(x)
