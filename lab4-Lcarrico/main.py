from lib import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print("\nExercise 3\n")
n = [4, 8, 16, 32, 64]

x = sp.symbols("x")
f3_1_expr = sp.exp(-(x**2))
f3_2_expr = sp.cos(np.pi * (1 + x**2))
f3_3_expr = x**(1/2) * sp.exp(x)

fs = [[f3_1_expr, 0, 10], [f3_2_expr, 0, 2], [f3_3_expr, 0, 1]]

for f, a, b in fs:
    print("With f as: " + str(f))
    fl = sp.lambdify(x, f)

    realValue = sp.integrate(f, (x, a, b)).evalf()
    print("Actual value is:", realValue)

    Ytrap = []
    Ysimp = []
    for i in n:
        value = trapRule(fl, 0, b, i)
        print("Using Trapezoidal rule with n @", i, "we get:", value)
        Ytrap.append(np.abs(value - realValue))

        value = simpson(fl, 0, b, i)
        print("Using Simpson's rule with n @", i, "we get:", value)
        Ysimp.append(np.abs(value - realValue))

    plt.title("Trapezoidal and Simpson's Rule for:\n" + str(f))
    plt.plot(n, Ytrap, label="Error with Trapezoidal Rule")
    plt.plot(n, Ysimp, label="Error with Simpson's Rule")
    plt.legend(loc="upper right")
    plt.show()
    print("\n")


print("\nExercise 4")
f4_1_expr = sp.sin(sp.pi * x)
f4_2_expr = sp.exp(x)
f4_3_expr = sp.exp(x**2)

val = lengthOfCurve(f4_1_expr, 0, 5, 50)
print("Length of", f4_1_expr, "from 0 to 5 is:", val)

val = lengthOfCurve(f4_2_expr, 0, 2, 50)
print("Length of", f4_2_expr, "from 0 to 2 is:", val)

val = lengthOfCurve(f4_3_expr, 0, 2, 50)
print("Length of", f4_3_expr, "from 0 to 2 is:", val)

print("\nExercise 5")
h = 0.05

def f5_1(x): #real val is 1
    return np.exp(x)

def f5_2(x): #real val is 1/2
    return np.arctan(x**2 - x + 1)

def f5_3(x):
    return np.arctan(100*x**2 - 199*x + 100)

f = sp.lambdify(x, sp.diff(sp.atan(100*x**2 - 199*x + 100), x))
realValue = f(1)

fs = [[f5_1, 0, 1, "e^x"], [f5_2, 1, (1/2), "tan^-1(x^2 - x + 1)"], [f5_3, 1, realValue, "tan^-1(100x^2 - 199x + 100)"]]
for f,x,t,label in fs:
    print("With f as", label)

    val = forFD(f, x, h)
    print("Value from Forward First Derivative", val)
    print("Error from Forward First Derivative", np.abs(val - t), "\n")

    val = cenFD(f, x, h)
    print("Value from Center First Derivative", val)
    print("Error from Center First Derivative", np.abs(val - t), "\n")

    val = bacFD(f, x, h)
    print("Value from Backward First Derivative", val)
    print("Error from Backward First Derivative", np.abs(val - t), "\n")

print("Center was much more accurate.")

print("\nExercise 6")
# max value of the 2nd derv ''' is 1
# max value of the 4th derv of the function between 1 and 3 is 2

def f(x):
    return x * np.log(x)

a,b = 1,3
max1,max2 = 1,2
tol = 10**(-6)
n1 = int(trapRuleError(a, b, max1, tol))
n2 = int(simpsonError2(a, b, max2, tol))

print("For a tolerance of", tol, "you need a n of", n1, "for Trapezoidal Rule")
print("For a tolerance of", tol, "you need a n of", n2, "for Simpson's Rule\n")
print("Trapezoidal Rule gives us a value of:", trapRule(f, a, b, n1))
print("Simpson's gives us a value of:", simpson(f, a, b, n2))

def f(x):
    return 2 * math.sqrt(1 - x**2)
print("Monte Carlo 1D Test for PI:", monteCarlo(f, -1, 1, 20000))

x,y = sp.symbols("x y")
f_expr = x**2 + y**2 - 1
print("Monte Carlo 2D Test for PI:", monteCarlo2D(f_expr, -1, 1, -1, 1, 20000))
