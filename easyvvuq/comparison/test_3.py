"""Comparison of density-divergences: Assymetric Gaussian"""
import numpy as np
import chaospy as cp
import easyvvuq as uq
import pylab as plt
import time


time0 = time.time()

# CDF1
def c1(x, y):
    m = (y-50.)**2/500.
    sa = 0.2
    sb = 1.
    xa = x[x>=m]
    da = cp.Normal(m, sa)
    xb = x[x<m]
    db = cp.Normal(m, sb)
    dx = x[-1]-x[0]
    return dx*np.concatenate((db.cdf(xb), da.cdf(xa)))

# CDF2
def c2(x, y):
    m = 2.5
    sa = 0.2
    sb = 0.1+0.01*y
    xa = x[x>=m]
    da = cp.Normal(m, sa)
    xb = x[x<m]
    db = cp.Normal(m, sb)
    dx = x[-1]-x[0]
    return dx*np.concatenate((db.cdf(xb), da.cdf(xa)))

# PDF1
def d1(x, y):
    m = (y-50.)**2/500.
    sa = 0.2
    sb = 1.
    xa = x[x>=m]
    da = cp.Normal(m, sa)
    xb = x[x<m]
    db = cp.Normal(m, sb)
    return np.concatenate((db.pdf(xb), da.pdf(xa)))

# PDF2
def d2(x, y):
    m = 2.5
    sa = 0.2
    sb = 0.1+0.01*y
    xa = x[x>=m]
    da = cp.Normal(m, sa)
    xb = x[x<m]
    db = cp.Normal(m, sb)
    return np.concatenate((db.pdf(xb), da.pdf(xa)))

# Grid for pdf and cdf evaluations
x = np.linspace(-4.5, 7.5, int(1e3))

# Grid for "UQ"
y = np.linspace(0, 100, 500)

# To plot UQ functions
m1 = (y-50.)**2/500
m2 = 2.5*np.ones_like(y)
sa1 = 0.2*np.ones_like(y)
sa2 = 0.2*np.ones_like(y)
sb1 = np.ones_like(y)
sb2 = 0.1*np.ones_like(y) + 0.01*y

# Sampling from PDF
p1 = []
p2 = []
for yi in y:
    p1.append(d1(x, yi))
    p2.append(d2(x, yi))

# Sampling fron CDF
p3 = []
p4 = []
for yi in y:
    p3.append(c1(x, yi))
    p4.append(c2(x, yi))

# Compute distances
vs = uq.comparison.Validate_Similarity()
dh = vs.compare(p1, p2)

vs.set_metric("JS")
djs = vs.compare(p1, p2)

vs.set_metric("W1")
dw1 = vs.compare(p3, p4)

vs.set_metric("W2")
dw2 = vs.compare(p3, p4)

print("time = ", time.time()-time0)

# PLOTS
fig, axs = plt.subplots(2, 1)
axs[0].set_title("Comparison of density-divergences: Assymetric Gaussian")
axs[0].plot(y, m1, "k-")
axs[0].plot(y, m1+sa1, "k-", alpha=0.2)
axs[0].plot(y, m1-sb1, "k-", alpha=0.2)
axs[0].fill_between(y, m1-sb1, m1+sa1, color="k", alpha=0.15)

axs[0].plot(y, m2, "b-")
axs[0].plot(y, m2+sa2, "b-", alpha=0.2)
axs[0].plot(y, m2-sb2, "b-", alpha=0.2)
axs[0].fill_between(y, m2-sb2, m2+sa2, color="b", alpha=0.15)
axs[0].grid()

axs[1].plot(y, dh, label="Hellinger")
axs[1].plot(y, djs, label="Shannon-Jenseen")
axs[1].plot(y, dw1, label="Wassetein-1")
axs[1].plot(y, dw2, label="Wassetein-2")
axs[1].set_ylabel("distances")
axs[1].legend()
axs[1].grid()

plt.show()
