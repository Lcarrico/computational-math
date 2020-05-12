from lib import *
import math

# Exercise 1
f = lambda x: x**6 - x - 1.0 # root at about -0.75
sol = bisect(f, 1, 2, 5*10**-4, 1000)
print("Root for exercise 1: ", sol[0], end="\n")
print("Iterations for exercise 1: ", sol[1], end="\n\n")


# Exercise 2
# Estimated roots at -1, -0.75, -0.25, 0.25 0.75, 1
g = lambda x: 32*x**6 - 48*x**4 + 18*x**2 - 1
graph(g, 100, [-100, 100])

# List of ranges for roots
lst = [[-1.2, -0.8], [-0.95, -0.55], [-0.45, -0.05],
        [0.05, 0.45], [0.55, 0.95], [0.8, 1.2]]

print("Roots for exercise 2: ")
for i in range(len(lst)):
    sol = bisect(g, lst[i][0], lst[i][1], 10**-10, 1000)
    print("Root Number ", i+1, ":\t", sol[0], sep="")
    print("Iterations for exercise 2: ", sol[1])

print()

# Exercise 3
h = lambda x: exp(x) - x - 2
sol = bisect(h, 1, 1.3, 5*10**-8, 1000)
print("Root for exercise 3:", sol[0], end="\n")
print("Iterations for exercise 3: ", sol[1], end="\n\n")
# Extra Credit Solution in Notes


#Exercise 4
f = lambda x: x**6 - x - 1.0
fprime = lambda x: 6*x**5 - 1
sol = newtons(f, fprime, 1.0, 10**-10, 1000)
print("Root for exercise 4:", sol[0], end="\n")
print("Iterations for exercise 4: ", sol[1], end="\n\n")

#Exercise 5
B = [1, 5, 10, 25, 50]
xs = [-0.5, -0.4, -0.3, -0.2, -0.15]

x = sp.symbols('x')
gs = [x + sp.exp(-i * x**2) * sp.cos(x) for i in B]
gPrimes = [sp.lambdify(x, sp.diff(i)) for i in gs]
gs = [sp.lambdify(x, g) for g in gs]

print("Roots for exercise 5: ")
lst = [newtons(g, gPrime, x, 10**-2, 100) for g, gPrime, x in zip(gs, gPrimes, xs)]
for i in range(len(lst)):
    print("Root Number ", i+1, ":\t", lst[i][0], sep="")
    print("Iteration Number for Root ", i+1, ":\t", lst[i][1], sep="", end="\n\n")
print()

print("Exercise 5 Explanations")
print("A good choice for x0 is -0.5 since it is close to the actual 0")
print("As the values of B increases, the roots of the functions decrease while approaching 0")
print()


#Exercise 6
h = lambda x: x**3 - 3*x**2 + 3*x - 1
hPrime = lambda x: 3*x**2 - 6*x + 3
sol = newtons(h, hPrime, 1.2, 10**-16, 100)
print("Root for exercise 6:", sol[0], end="\n")
print("Iterations for exercise 6: ", sol[1], end="\n\n")


# Exercise 7 x**m - a = 0
sol = solveRoot(3, 2, 1)
print("Root for exercise 7:", sol[0], end="\n")
print("Iterations for exercise 7: ", sol[1], end="\n\n")

# Exercise 8
f = lambda x: x**3 - 3*x**2 + 3*x - 1
sol = secant(f, 0.8, 1.1, 10**-15, 100)
print("Root for exercise 8:", sol[0], end="\n")
print("Iterations for exercise 8: ", sol[1], end="\n\n")

# Exercise 9
g = lambda x: x + 0.2238*(x**2 - 5)
sol = fixedPoint(g, 1.5, 10**-16, 1000)
print("Negative Root for exercise 9:", [0], end="\n")
print("Iterations for exercise 9.1: ", sol[1], end="\n\n")

g = lambda x: x + (-0.4*(x**2 - 5))
sol = fixedPoint(g, 2.4, 10**-16, 1000)
print("Positive Root for exercise 9:", sol[0], end="\n")
print("Iterations for exercise 9.2: ", sol[1], end="\n\n")

# Exercise 10
f = lambda x: x**6 - x - 1
fprime = lambda x: 6*x**5 -1

addToPlot(newtons, [f, fprime, 2.0, 10**-16], "Newtons")
addToPlot(bisect, [f, 1.0, 2.0, 5*10**-16], "Bisection")
addToPlot(secant, [f, 1.0, 2.0, 5*10**-16], "Secant")
plt.title("Convergence Comparison")
plt.show()
