from lib import *
import matplotlib.pyplot as plt


print("Exercise 1")

A = np.array([[10, 1, 3], [2, 30, 1], [3, 5, 25]], 'd')
b = np.array([1,1,1], 'd')
guess = np.array([2,2,2], 'd')

print("Jacobi")
x, its = jacobi(A,b,guess,10**-8,20)
print("x =", x)
print("Interations =", its, "\n")

A = np.array([[10, 1, 3], [2, 30, 1], [3, 5, 25]], 'd')
b = np.array([1,1,1], 'd')
guess = np.array([2,2,2], 'd')

# ---------------------------------------------------------------------------- #

print("\nExercise 2")

print("Gauss Seidel")
x, its = seidel(A,b,guess,10**-8,20)
print("x =", x)
print("Interations =", its, "\n")

# ---------------------------------------------------------------------------- #

print("\nExercise 3")

A = np.array([[2, 1, 0, 0, 0], [-1, 3, 1, 0, 0], [0, -1, 3, 1, 0], [0, 0, -1, 4, 1], [0, 0, 0, -1, 2]], 'd')
b = np.array([0, -4, 12, 6, 9], 'd')
guess = np.array([0, -4, 12, 6, 9], 'd')

print("Jacobi")
x, its = jacobi(A,b,guess,10**-8,200)
print(np.dot(A,x), b)
print("x =", x)
print("Interations =", its, "\n")

A = np.array([[2, 1, 0, 0, 0], [-1, 3, 1, 0, 0], [0, -1, 3, 1, 0], [0, 0, -1, 4, 1], [0, 0, 0, -1, 2]], 'd')
b = np.array([0, -4, 12, 6, 9], 'd')
guess = np.array([0, -4, 12, 6, 9], 'd')

print("Gauss Seidel")
x, its = seidel(A,b,guess,10**-8,200)
print("x =", x)
print("Interations =", its, "\n")

# ---------------------------------------------------------------------------- #

print("\nExercise 4")
A = createTridiagonal(4, 1, 100)
b = np.ones(100)
guess = np.ones(100)

print("Jacobi")
x, its = jacobi(A,b,guess,10**-8,200)
print("x =", x)
print("Interations =", its, "\n")

A = createTridiagonal(4, 1, 100)
b = np.ones(100)
guess = np.ones(100)

print("Gauss Seidel")
x, its = seidel(A,b,guess,10**-8,200)
print("x =", x)
print("Interations =", its, "\n")

# ---------------------------------------------------------------------------- #

print("\nExercise 5")
M, b = createMandB(100)
A = np.eye(100) - M
guess = np.copy(b)

print("Jacobi")
x, its_j = jacobi(A,b,guess,10**-8,200)
print("x =", x)
print("Interations =", its_j, "\n")

A = np.eye(100) - M
guess = np.copy(b)

print("Gauss Seidel")
x, its = seidel(A,b,guess,10**-8,200)
print("x =", x)
print("Interations =", its, "\n")

true_sol = np.zeros(100)
for i in range(true_sol.size):
    true_sol[i] = 1 + createT(i+1, 100)

print("True Solution")
print(true_sol)

jacobi_norms = np.zeros(10)
jacobi_ratios = np.zeros(9)
seidel_norms = np.zeros(10)
seidel_ratios = np.zeros(9)
guess_j = np.copy(b)
guess_s = np.copy(b)


for i in range(10):
    A = np.eye(100) - M
    x, its_j = jacobi(A,b,guess_j,10**-8,1)
    jacobi_norms[i] = norm(true_sol, x)
    guess_j = x

    A = np.eye(100) - M
    x, its = seidel(A,b,guess_s,10**-8,1)
    seidel_norms[i] = norm(true_sol, x)
    guess_s = x

    if i != 0:
        jacobi_ratios[i-1] = jacobi_norms[i] / jacobi_norms[i-1]
        seidel_ratios[i-1] = seidel_norms[i] / seidel_norms[i-1]

X = range(1,11)

plt.title("Error Values")
plt.plot(X,jacobi_norms,label="Jacobi")
plt.plot(X,seidel_norms,label="Gauss Seidel")
plt.legend(loc='upper right')
plt.show()


X = range(1,10)

plt.title("Convergence Rates")
plt.plot(X,jacobi_ratios,label="Jacobi")
plt.plot(X,seidel_ratios,label="Gauss Seidel")
plt.legend(loc='best')
plt.show()
