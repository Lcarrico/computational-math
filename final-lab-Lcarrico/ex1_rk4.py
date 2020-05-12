import matplotlib.pyplot as plt
import numpy as np
import math as mt
import imageio


# def f(x,t):
#     #use this to solve for the next values of u
#     pass

def u0(x):
    return np.sin(np.pi * x)

# def g0(t):
#     return 0
#
# def gL(t):
#     return 0

m = 2500
n = 25 # num of xs

L = 1.0
T = 1.0

delta_x = L/n
delta_t = T/m

alpha = .60

us = np.zeros([m+1,n+1])

for i in range(1, len(us[0,:])):
    us[0,i] = us[0,i-1] + delta_x

xs = np.copy(us[0,:])

for i in range(len(us[0, :])):
    us[0, i] = u0(us[0, i])

h = (alpha * delta_t / (delta_x * delta_x))

for k in range(1,m+1,1):
    for j in range (1,n,1):
        # us[k][j] = h * us[k-1][j-1] + (1 - 2 * h) * us[k-1][j] + h * us[k-1][j+1]
        k1 = h * (us[k-1][j+1] - 2*us[k-1][j] + us[k-1][j-1])
        k2 = h * ((us[k-1][j+1]+ 0.5*k1)-2*(us[k-1][j]+0.5*k1)+(us[k-1][j-1]+0.5*k1))
        k3 = h * ((us[k-1][j+1]+0.5*k2)-2*(us[k-1][j]+0.5*k2)+(us[k-1][j-1]+0.5*k2))
        k4 = h * ((us[k-1][j+1]+k3)-2*(us[k-1][j]+k3)+(us[k-1][j-1]+k3))
        us[k][j] = us[k-1][j] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
count = 4
images = []

for i in range(count + 1):
    plt.title("One Dimensional Heat Equation - Runge Kutta 4\nTime at " + str(int(m* (i/count))))
    plt.xlabel("Position on Line")
    plt.ylabel("Relative Temperature")

    plt.ylim((0,1.05))
    plt.plot(xs, us[int(m* (i/count)),:])
    plt.savefig("figures/rk4_fig" + str(i) + ".png")
    images.append(imageio.imread("figures/rk4_fig" + str(i) + ".png"))
    plt.clf()
imageio.mimsave('runge_kutta4.gif', images)
