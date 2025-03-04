#!/usr/bin/env python3

import numpy as np


def f(x1, x2):

    if x2 <= -0.6 * x1 + 0.8:
        return x1 + x2 - 1
    else:
        return x1 ** 3 + x2 ** 2 + 1


# load inputs
inputs = np.genfromtxt('input.csv', delimiter=',')

output = f(inputs[0], inputs[1])

np.savetxt('output.csv', np.array([output]), header=r"f", comments='')

# uncomment to make a plot

# import matplotlib.pyplot as plt
# from matplotlib import cm
# xx = np.linspace(0,1,20)
# X1,X2 = np.meshgrid(xx, xx)

# F = np.zeros([20,20])

# for i in range(20):
#     for j in range(20):
#         F[i, j] = f(X1[i, j], X2[i, j])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X1, X2, F, linewidth=0, antialiased=False, cmap=cm.coolwarm)
# plt.savefig('test_function.png')
