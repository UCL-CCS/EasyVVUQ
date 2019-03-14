import numpy as np
import math
"""
SIMPLE FINITE ELEMENT SOLVER FOR u_x + 1/Pe*u_xx = f, USING LINEAR SHAPE FUNCTIONS
"""


class ADE:

    def __init__(self, range_Pe, range_f, nel):

        # PARAMETERS
        self.nel = nel
        self.x = np.linspace(0, 1, nel + 1)
        self.h = 1 / np.double(self.nel)
        self.Pe_a = range_Pe[0]
        self.Pe_b = range_Pe[1]
        self.f_a = range_f[0]
        self.f_b = range_f[1]

    def solve(self, theta):

        # theta is in [-1, 1], map to physical domain as given by the range
        # in Pe and f
        Pe = 0.5 * (self.Pe_b - self.Pe_a) * \
            theta[0] + 0.5 * (self.Pe_b + self.Pe_a)
        f = 0.5 * (self.f_b - self.f_a) * \
            theta[1] + 0.5 * (self.f_b + self.f_a)

        print('Solving advection diffusion equation at Pe = ', Pe, ' and f = ', f)

        nel = self.nel
        h = self.h

        K = np.zeros([nel + 1, nel + 1])
        F = np.zeros(nel + 1)

        # GQ RULES
        Q = 2
        eps_i = np.array([-1 / math.sqrt(3.0), 1 / math.sqrt(3.0)])
        wi = np.ones(2)

        # assumble K matrix and F vector
        for e in range(nel):

            XA1 = e * h
            XA2 = (e + 1) * h

            x = (h * eps_i + XA1 + XA2) / 2

            [N1x, N2x] = der_shape(h, Q)
            [N1, N2] = shape(x, XA1, XA2)

            # diffusive term
            k11 = 1.0 / Pe * N1x * N1x * wi - N1x * N1 * wi
            k11 = k11.sum()
            k12 = 1.0 / Pe * N1x * N2x * wi - N1x * N2 * wi
            k12 = k12.sum()
            k21 = 1.0 / Pe * N2x * N1x * wi - N2x * N1 * wi
            k21 = k21.sum()
            k22 = 1.0 / Pe * N2x * N2x * wi - N2x * N2 * wi
            k22 = k22.sum()

            # forcing term
            f1 = N1 * f
            f1 = f1.sum()
            f2 = N2 * f
            f2 = f2.sum()

            # local element matrices
            if e > 0 and e < int(nel - 1):
                K[e, e] = K[e, e] + k11
                K[e, e + 1] = K[e, e + 1] + k12
                K[e + 1, e] = K[e + 1, e] + k21
                K[e + 1, e + 1] = K[e + 1, e + 1] + k22

                F[e] = F[e] + f1
                F[e + 1] = F[e + 1] + f2
            elif e == 0:
                K[e + 1, e] = K[e + 1, e] + k21
                K[e + 1, e + 1] = K[e + 1, e + 1] + k22

                F[e + 1] = F[e + 1] + f2
            else:
                K[e, e] = K[e, e] + k11
                K[e, e + 1] = K[e, e + 1] + k12

                F[e] = F[e] + f1

        K[0, 0] = 1.0
        K[nel, nel] = 1.0

        return np.linalg.solve(K, F)

# Finite element linear shape functions and their derivatives


def der_shape(h, Q):
    N1x = -1 / h * np.ones(Q)
    N2x = 1 / h * np.ones(Q)

    return [N1x, N2x]


def shape(x, XA1, XA2):

    if np.max(x) < 1.0:
        eps = (2.0 * x - XA1 - XA2) / (XA2 - XA1)
    else:
        eps = (2.0 * x - XA1 - XA2) / (XA2 - XA1)
        eps[-1] = -1

    # value shape function
    N1 = 0.5 * (1 - eps)
    N2 = 0.5 * (1 + eps)
    return [N1, N2]
