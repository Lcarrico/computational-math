import matplotlib.pyplot as plt
import numpy as np
import math as mt
import imageio



def f(x,t):
    return 2 * (np.e ** (- t)) * np.sin(x)

def u0(x):
    return np.sin(x)

def v0(x):
    return -np.sin(x)

# def g0(t):
#     return 0
#
# def gL(t):
#
# def gL(t):
#     return 0

m = 1000
n = 100

L = np.pi
T = 50

delta_x = L/n
delta_t = T/m

alpha = 0.01

us = np.zeros([m+1,n+1]) #initializes all to zero, including boundaries

for i in range(1, len(us[0,:])):
    us[0,i] = us[0,i-1] + delta_x

# print(us[0, :])

xs = np.copy(us[0,:])

us[0,-1] = 0

for i in range(len(us[0, :]) - 1):
    us[0, i] = u0(us[0, i])

# print(us[0, :])


h = (alpha * delta_t * delta_t / (delta_x * delta_x))
# print(h, delta_t, delta_x)
# exit()
#initialize second row
for i in range(len(us[1, :]) - 1):
    us[1, i] = us[0,i] + v0(xs[i]) * delta_t

# print(us[0, :])
# print(us[1, :])

# for k in range(2,m+1):
#     for j in range (1,n):
#         # print(us[k][j], end="\t")
#         print(k, k * delta_x, j, j * delta_t)
#         us[k][j] = h * (us[k-1][j-1] - 2 * us[k-1][j] + us[k-1][j+1]) + delta_t**2 * f(xs[j], k * delta_t) + 2*us[k-1][j] - us[k-2,j]
#         # print(us[k][j])



for k in range(2,m+1):
    for j in range (1,n):
        us[k,j] = -us[k-2,j] + 2 * us[k-1,j] + h * (us[k-1,j+1] - 2 * (us[k-1,j]) + us[k-1,j-1]) + delta_t**2 * f(xs[j], k * delta_t)
    us[k,0], us[k,-1] = 0, 0



# print(us[2, :])

# plt.xlim(0, 3)
# plt.ylim(-1,1)
# # plt.ylim((0,1.05))
# plt.plot(xs, us[0,:])
# # print(us[int(0),:])
# plt.savefig("figures/explicit_fig" + str(i) + ".png")
# # images.append(imageio.imread("figures/explicit_fig" + str(i) + ".png"))
# plt.show()
# plt.clf()
#
# plt.xlim(0, 3)
# plt.ylim(-1,1)
# plt.plot(xs, us[1,:])
# # print(us[int(1),:])
# plt.savefig("figures/explicit_fig" + str(i) + ".png")
# # images.append(imageio.imread("figures/explicit_fig" + str(i) + ".png"))
# plt.show()
# plt.clf()

count = 4
images = []

for i in range(count + 1):
    plt.xlim(0, np.pi)
    plt.ylim(-20,20)
    plt.title("One Dimensional Wave Equation - Explicit Method\nTime at " + str(int(m* (i/count))))
    plt.xlabel("Position on Line")
    plt.ylabel("Relative Temperature")

    # plt.ylim((0,1.05))
    plt.plot(xs, us[int(m* (i/count)),:])
    # print(us[int(m* (i/count)),:])
    plt.savefig("figures/wave_explicit_fig" + str(i) + ".png")
    images.append(imageio.imread("figures/wave_explicit_fig" + str(i) + ".png"))
    # plt.show()
    plt.clf()
imageio.mimsave('euler_explicit_1d_wave.gif', images)
