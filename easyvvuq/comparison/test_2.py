import numpy as np
import chaospy as cp
import matplotlib.pylab as plt
from easyvvuq.comparison.validate import Validate_Similarity

# vary std
mu = [i*0.5 for i in range(0, 21)]
print(len(mu))
# xgrid
x = np.linspace(-10, 12, int(1e4))

# Normal distribtion with same mean
p = []
for m in mu:
    Ni = cp.Normal(m, 2)
    pi = Ni.pdf(x)
    p.append(pi)

fig = plt.figure()

# plot densitie
ax1 = fig.add_subplot(121)
ax1.plot(x, p[0], "r-", label=r"$\mathcal{N}(0, 2)$")
ax1.plot(x, p[4], "--")
ax1.plot(x, p[8], "--")
ax1.plot(x, p[10], "--", label=r"$\mathcal{N}(\mu_i, 2)$")
ax1.set_title("Densities", fontsize=16)
ax1.grid()
ax1.legend()

# Compute distance
v = Validate_Similarity()
pref = [p[0]]*21
d = v.compare(pref, p)

ax2 = fig.add_subplot(122)
ax2.plot(mu, d, '.-')
ax2.set_xlabel(r"$\mu_i$", fontsize=16)
ax2.set_title(r"Hellinger distance between $\mathcal{N}(0, 2)$ and" +
              "$\mathcal{N}(\mu_i, 2)$", fontsize=16)
ax2.set_xticks(np.arange(0, 11, 1))
ax2.grid()

plt.show()
