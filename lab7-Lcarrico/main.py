from lib import *

print("Exercise 1\n")
x1, x2 = sp.symbols('x1 x2')
f_exprs = [x1**2+x1*x2-16, x2*sp.exp(x1)+sp.sin(x2)-4]
print(f_exprs)
xs = [1, 1]

print("Testing Newtons:")
sols, it = newtons(f_exprs, xs, 1, 10E-8, 200)
print("Solutions:",sols)
print("Iterations:",it)

print("\nTesting Gradient Descent:")
f = x1**3 + x1*x2 + (1 + x2)**2
print(f)
n=2
guess = [.5,-1]

sols, it = gradientDesc(f, n, .1, guess, 10E-8, 500)
print("Solutions:",sols)
print("Iterations:",it)

print("\n\nExercise 2\n")
f_exprs = [x1**2 + x2**2 - 4, x1**2 - x2**2 - 1]
print(f_exprs)
xs = [[-1, 1], [-1,-1], [1,1], [1,-1]]


for x in xs:
    print("Testing Newtons:")
    sols, it = newtons(f_exprs, x, 1, 10E-8, 200)
    print("Solutions:",sols)
    print("Iterations:",it)

print("\n\nExercise 3\n")
f_exprs = [x1**2 + x1*x2**3 - 9, 3*x1**2*x2 - x2**3 - 4]
print(f_exprs)
xs = [[-3,0],[-1,-2],[1,2],[3,0]]

for x in xs:
    print("Testing Newtons:")
    sols, it = newtons(f_exprs, x, 1, 10E-8, 200)
    print("Solutions:", sols)
    print("Iterations:", it)

print("\n\nExercise 4\n")
f_exprs = [5 * x1 * x2 - x1 * (1 + x2), -x1 * x2 + (1 - 5)*(1 + x2)]

print(f_exprs)
print("Testing Newtons:")

xs = [[15,15],[-15,-15]]

sols, it = newtons(f_exprs, xs[0], 1, 10E-8, 500)
print("Solutions:",sols)
print("Iterations:",it)

sols, it = newtons(f_exprs, xs[1], 1, 10E-8, 500)
print("Solutions:",sols)
print("Iterations:",it)


print("\n\nExercise 5\n")
print("Testing Gradient Descent:")
f = x1**4 + x1*x2 + (1 + x2)**2
print(f)
n=2

guess = [.7,-1.4]
sols, it = gradientDesc(f, n, .1, guess, 10E-8, 500)
print("Solutions:",sols)
print("Iterations:",it)


print("\n\nExercise 6\n")
print("Testing Gradient Descent:")
f = (1 - x1)**2 + 100 * (x2 - x1**2)**2
print(f)
n=2
guess = [0.5,1.5]

sols, it = gradientDesc(f, n, .001, guess, 10E-8, 200)
print("Solutions:",sols)
print("Iterations:",it)


print("\n\nExercise 7\n")
print("Testing Gradient Descent:")
f = sp.sin((1/2)*x1**2 - (1/4)*x2**2 + 3) * sp.cos(2*x1 + 1 - sp.exp(x2))
print(f)
n=2
guess = [1,1]

sols, it = gradientDesc(f, n, .0001, guess, 10E-8, 1000)
print("Solutions:",sols)
print("Iterations:",it)
