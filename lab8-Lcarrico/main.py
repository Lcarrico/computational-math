from lib import *
from mpl_toolkits.mplot3d import Axes3D



""" Exercise 2 """

f1_expr = '2/3 * x1 - 4/3 * x1 * x2'
f2_expr = '1 * x1 * x2 - 1. * x2'
f_exprs = [f1_expr, f2_expr]
n = 100
h = 1E-1
t0 = 0
y0s = [0.9,1]

t, ys = eulerExplicit(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Explicit Prey vs Predator Relationship Given Values")

t, ys = eulerImplicit(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Implicit Prey vs Predator Relationship Given Values")

t, ys = rungeKutta2(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Runge Kutta 2 Prey vs Predator Relationship Given Values")

t, ys = rungeKutta4(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Runge Kutta 4 Prey vs Predator Relationship Given Values")



f1_expr = '1.1 * x1 - 0.4 * x1 * x2'
f2_expr = '0.1 * x1 * x2 - 0.4 * x2'
f_exprs = [f1_expr, f2_expr]
n = 200
h = 1E-1
t0 = 0
y0s = [10,10]

t, ys = eulerExplicit(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Explicit Prey vs Predator Relationship Other Cool Values")

t, ys = eulerImplicit(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Implicit Prey vs Predator Relationship Other Cool Values")

t, ys = rungeKutta2(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Runge Kutta 2 Prey vs Predator Relationship Other Cool Values")

t, ys = rungeKutta4(f_exprs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
graph(vals, ["Prey", "Predator"], "Runge Kutta 4 Prey vs Predator Relationship Other Cool Values")


""" Exercise 3 """

# Create functions
r = [1, 0.72, 1.53, 1.27]
a = [[1,    1.09, 1.52, 0   ],
     [0,    1,    0.44, 1.36],
     [2.33, 0,    1,    0.47],
     [1.21, 0.51, 0.35, 1   ]]

fs = []
for i in range(4):
    total = []
    for j in range(4):
        total.append(str(a[i][j]) + " * x" + str(j + 1))
    total = " + ".join(total)
    fs.append(str(r[i]) + " * x" + str(i+1) + " * (1 - " + total + ")")

print(fs)


n = 100
h = 1E-4
t0 = 0
y0s = [20,30,40,50]


t, ys = eulerExplicit(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Explicit Competitive Lotka–Volterra With Given Values")

t, ys = eulerImplicit(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Implicit Competitive Lotka–Volterra With Given Values")

t, ys = rungeKutta2(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Runge Kutta 2 Competitive Lotka–Volterra With Given Values")

t, ys = rungeKutta4(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Runge Kutta 4 Competitive Lotka–Volterra With Given Values")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Species 1')
ax.set_ylabel('Species 2')
ax.set_zlabel('Species 3')
plt.title("3D Relationship Between All Species Population with Given Values");

img = ax.scatter(*ys[:3], c=ys[3], cmap=plt.hot())
cbar = fig.colorbar(img)
cbar.ax.set_ylabel('Species 4')
plt.show()



# Create functions
r = [0.43, 0.23, .54, 1.1]
a = [[1,    0,    4.12, 1.64],
     [0,    1,    0,    1.36],
     [2.33, 0,    1,    0   ],
     [1.23, 0.71, 0,    1   ]]

fs = []
for i in range(4):
    total = []
    for j in range(4):
        total.append(str(a[i][j]) + " * x" + str(j + 1))
    total = " + ".join(total)
    fs.append(str(r[i]) + " * x" + str(i+1) + " * (1 - " + total + ")")

print(fs)

n = 25
h = 1E-4
t0 = 0
y0s = [200,300,400,500]

t, ys = eulerExplicit(fs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
labels = ["Species " + str(i + 1) for i in range(len(ys))]
graph(vals, labels, "Explicit Competitive Lotka–Volterra With Other Cool Values")

t, ys = eulerImplicit(fs, n, h, t0, y0s)
vals = [[t, y] for y in ys]
labels = ["Species " + str(i + 1) for i in range(len(ys))]
graph(vals, labels, "Implicit Competitive Lotka–Volterra With Other Cool Values")

t, ys = rungeKutta2(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Runge Kutta 2 Competitive Lotka–Volterra With Other Cool Values")

t, ys = rungeKutta4(fs, n, h, t0, y0s)
labels = ["Species " + str(i + 1) for i in range(len(ys))]
vals = [[t, y] for y in ys]
graph(vals, labels, "Runge Kutta 4 Competitive Lotka–Volterra With Other Cool Values")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Species 1')
ax.set_ylabel('Species 2')
ax.set_zlabel('Species 3')
plt.title("3D Relationship Between All Species Population with Other Cool Values");

img = ax.scatter(*ys[:3], c=ys[3], cmap=plt.hot())
cbar = fig.colorbar(img)
cbar.ax.set_ylabel('Species 4')
plt.show()
