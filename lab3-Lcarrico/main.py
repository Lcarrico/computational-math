from lib import *
import matplotlib.pyplot as plt


X = [1,2,3]
Y = [1,16,81]
print("Exercise 1, testing x^4")
print(dividedDiffApprox(X, Y))
print("\n")


def E2_1(x):
    return cos(2*x) + exp(x) + x

X = [-.25, -.1,.1,.25]
Y = [E2_1(i) for i in X]
print("Exercise 2, part 1.")
print(dividedDiffApprox(X,Y))
print("\n")
def E2_2(x):
    return log(x) + x

X = [0.1, 1, 2]
Y = [E2_2(i) for i in X]

print("Exercise 2, part 2.")
print("Value:",dividedDiffApprox(X, Y))
print("Error:",abs(dividedDiffApprox(X, Y) - (-1)))
print("\n")


X = [0.5, 1, 1.5]
Y = [E2_2(i) for i in X]

print("Exercise 2, part 3.")
print("Value:",dividedDiffApprox(X, Y))
print("Error:",abs(dividedDiffApprox(X, Y) - (-1)))

print("\nExtra Test for 2.3")
X = [0.9, 1, 1.1]
Y = [E2_2(i) for i in X]

print("Value:",dividedDiffApprox(X, Y))
print("Error:",abs(dividedDiffApprox(X, Y) - (-1)))
print("\n")

X0 = [-1, -0.5, 0.5, 1]

def f1(x):
    return np.exp(x)
Y = [f1(i) for i in X0]
lf1 = lagrange(X0, Y)

def f2(x):
    return np.sin(np.pi * x)
Y = [f2(i) for i in X0]
lf2 = lagrange(X0, Y)

def f3(x):
    return np.arctan(x)
Y = [f3(i) for i in X0]
lf3 = lagrange(X0, Y)

def f4(x):
    return np.log(1 + (x * x))
Y = [f4(i) for i in X0]
lf4 = lagrange(X0, Y)

X0 = [-2, -1, 0, 1, 2, 3]
Y = [-5, 1, 1, 1, 7, 25]
lf5 = lagrange(X0, Y)

X0 = [1695, 1330, 1248, 1233]
Y = [13, 21, 27, 30]
lf6 = lagrange(X0, Y)


print("Exercise 3.1 Plot\n")
X = [i/100 for i in range(-100,101)]
Y = [f1(i) for i in X]
plt.plot(X,Y,'--',label="e^x")

Y = [lf1(i) for i in X]
plt.plot(X,Y,label="3rd degree Lagrange")
plt.legend(loc='lower right')
plt.show()

print("Exercise 3.2 Plot\n")
Y = [f2(i) for i in X]
plt.plot(X,Y,'--',label="sin(pi*x)")

Y = [lf2(i) for i in X]
plt.plot(X,Y,label="3rd degree Lagrange")
plt.legend(loc='lower right')
plt.show()

print("Exercise 3.3 Plot\n")
Y = [f3(i) for i in X]
plt.plot(X,Y,'--',label="tan^-1(x)")

Y = [lf3(i) for i in X]
plt.plot(X,Y,label="3rd degree Lagrange")
plt.legend(loc='lower right')
plt.show()

print("Exercise 3.4 Plot\n")
Y = [f4(i) for i in X]
plt.plot(X,Y,'--',label="log(1 + x^2)")

Y = [lf4(i) for i in X]
plt.plot(X,Y,label="3rd degree Lagrange")
plt.legend(loc='lower right')
plt.show()

print("Exercise 4 Plot\n")
X = [i/10 for i in range(-20,31)]
Y = [lf5(i) for i in X]
plt.plot(X,Y,label="4th degree Lagrange on ex4")
plt.legend(loc='lower right')
plt.show()

print("Exercise 5 Plot\n")
X = [i/10 for i in range(11000,17000)]
Y = [lf6(i) for i in X]
plt.plot(X,Y,label="3th degree Lagrange on ex5")
plt.legend(loc='lower right')
print("Estimate for ex. 5 is:", lf6(1150))
plt.show()
