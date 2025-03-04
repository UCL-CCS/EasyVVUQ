#!/usr/bin/env python3

def f(x):
    """
    Discontinuous test function

    Parameters
    ----------
    x : array
        input parameters
    Returns
    -------
    float
        f(x)

    """
    
    if x[1] <= -0.6 * x[0] + 0.8:
        return np.sum(x[0:n_xi]) - 1
    else:
        return x[0] ** 3 + np.cos(np.sum(x[1:n_xi] ** 2)) + 1

import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm

# load inputs
inputs = np.genfromtxt('input.csv', delimiter=',')
n_xi = int(inputs[-1])

output = f(inputs)

np.savetxt('output.csv', np.array([output]), header=r"f", comments='')

# uncomment to make a plot
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