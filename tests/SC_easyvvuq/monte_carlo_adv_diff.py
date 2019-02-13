import numpy as np
import matplotlib.pyplot as plt

#import advection diffusion finite-element solver
import ADE as ade

#select range of uncertain parameters
Pe_range = [100, 200]
f_range = [0.9, 1.1]

#select number of elements in spatial discretization
nel = 100

#create solver object
ade_obj = ade.ADE(Pe_range, f_range, nel)

#generate MC samples (in standard domain [-1, 1])
n_mc = 1000
theta = np.random.rand(n_mc, 2)*2.0 - 1.0

#solution array
U = np.zeros([nel+1, n_mc])

#run finite element code at random values of Pe and f
for i in range(n_mc):
    U[:, i] = ade_obj.solve(theta[i])
    
#plot results
fig = plt.figure()
ax = fig.add_subplot(111, xlabel=r'x', ylabel=r'u(x)', title=r'MC samples')
ax.plot(ade_obj.x, U, alpha = 0.25)
plt.tight_layout()
plt.show()