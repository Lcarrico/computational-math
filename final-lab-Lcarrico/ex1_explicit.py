import matplotlib.pyplot as plt
import numpy as np
import math as mt
import imageio

def u0(x):
    return np.sin(np.pi * x)


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
        us[k][j] = h * us[k-1][j-1] + (1 - 2 * h) * us[k-1][j] + h * us[k-1][j+1]

count = 4

images = []
for i in range(count + 1):
    plt.title("One Dimensional Heat Equation - Explicit Method\nTime at " + str(int(m* (i/count))))
    plt.xlabel("Position on Line")
    plt.ylabel("Relative Temperature")

    plt.ylim((0,1.05))
    plt.plot(xs, us[int(m* (i/count)),:])
    plt.savefig("figures/explicit_fig" + str(i) + ".png")
    images.append(imageio.imread("figures/explicit_fig" + str(i) + ".png"))
    plt.clf()
imageio.mimsave('euler_explicit.gif', images)
