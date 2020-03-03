import numpy as np
import chaospy as cp
import matplotlib.pyplot as plt
from math import exp


# The exact solution
def cooling_exact(t, k, Te):
    T0 = 95.
    return Te + (T0 - Te)*exp(-k*t)

# Joint distribution of k and T_env
dist = cp.J(cp.Uniform(0.025, 0.075),cp.Uniform(15, 25))


# Get 10 measurement points
texp = np.linspace(0, 200, 10)

# For every Point we do 10 measurements

