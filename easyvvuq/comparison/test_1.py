import numpy as np
import chaospy as cp
import matplotlib.pylab as plt
from easyvvuq.comparison.validate import Validate_Similarity

# vary std
sig = [i*0.5 for i in range(2, 21)]
# xgrid
x = np.linspace(-4.*sig[-1], 4.*sig[-1], int(1e3))

# Normal distribtion with same mean
p = []
c = []
for s in sig:
    Ni = cp.Normal(0, s)
    pi = Ni.pdf(x)
    ci = Ni.cdf(x)
    p.append(pi)
    c.append(ci)

fig = plt.figure()

# plot densitie
ax1 = fig.add_subplot(121)
ax1.plot(x, c[0], label=r"$\mathcal{N}(0,1)$")
ax1.plot(x, c[9], label=r"$\mathcal{N}(0,4.5)$")
ax1.plot(x, c[-1],label=r"$\mathcal{N}(0,10)$")
ax1.set_title("Cumulative densities", fontsize=16)
ax1.grid()
ax1.legend()

# Compute distance
v = Validate_Similarity()
v.set_metric("W1")
#pref = [p[0]]*19
#d = v.compare(pref, p)

cref = [c[9]]*19
d = v.compare(cref, c)

ax2 = fig.add_subplot(122)
ax2.plot(sig, d, '.-')
ax2.set_xlabel(r"$\sigma_i$", fontsize=16)
ax2.set_title(r"W2 distance between $\mathcal{N}(0, 1)$ and" +
              "$\mathcal{N}(0, \sigma_i)$", fontsize=16)
ax2.set_xticks(np.arange(0, 11, 1))
ax2.grid()

plt.show()
