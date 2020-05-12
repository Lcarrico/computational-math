import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


def removeNegatives(n):
    copy = n.copy()
    mask = copy < 0
    copy[mask] = 0
    return copy

test = np.arange(-5, 5)
print(test)
test = removeNegatives(test)
print(test)

t = np.arange(-1, 11, .1)
x = sy.symbols('x')
f = sy.lambdify(x, x**2 - 3)
plt.plot(t, f(t))
plt.show()
plt.clf()

f1 = sy.lambdify(x, x / (x**2 + 2*x + 1))
f2 = sy.integrate(f1(x), x)
print(f2)
f2 = sy.lambdify(x, f2)

f2 = sy.diff(f1(x), x)
f2 = sy.lambdify(x, f2)
t = np.arange(0, 1, .001)
plt.plot(t, f2(t))
plt.show()
