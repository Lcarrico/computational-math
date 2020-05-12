from lib import *

# Questions 5.2 and 5.1
plot(sp.sin(x), x, [1, 3, 5], sp.pi, np.arange(0, 2*sp.pi, .1))
plot(sp.exp(-x) * sp.sin(x), x, [8, 9, 10, 11], 0, np.arange(-1, 5, .1))


# Questions 6.1, 6.2, 6.3, 6.4
plot(x**(1/2), x, [1, 2], 1, np.arange(-10, 10, .1))
plot(sp.sin(x), x, [1, 2], sp.pi/4, np.arange(-10, 10, .1))
plot(sp.exp(sp.cos(x)), x, [1, 2], 0, np.arange(-10, 10, .1))
plot(sp.log(1 + sp.exp(x)), x, [1, 2], 0, np.arange(-10, 10, .1))


# Questions 7.1 and 7.2 - See report for 7.3 and 7.4
plot(sp.exp(x), x, [1, 2, 3, 4], 0, np.arange(-10, 1, .1))

# Here is 7.2
p4exp = taylor(sp.exp(x), x, 4, 0)
fs = [1/p4exp, sp.exp(x), p4exp]
plotTaylors(fs, np.arange(-10, 1, .1))
