import numpy as np
import chaospy as cp
import easyvvuq as uq

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"


# Set to True to test with plots, False for travis
_PLOT = False


def test_validate_similarity():
    pass


def test_validate_similarity_hellinger():
    pass


def test_validate_similarity_shannon_jenson():
    pass


def test_validate_similarity_wasserstein1():
    pass


def test_validate_similarity_wasserstein2():
    pass


# Build QoI distributions to compare
def samples(x, y):
    # Vary the mean
    mu1 = (y - 50.)**2 / 500.
    sig1 = 0.2
    dist1 = cp.Normal(mu1, sig1)

    # Vary the sdtv
    mu2 = 2.5
    sig2 = 0.1 + 0.01 * y
    dist2 = cp.Normal(mu2, sig2)

    # Probabily densities
    p1 = dist1.pdf(x)
    p2 = dist2.pdf(x)

    # Cummulative distributions
    dx = x[-1] - x[0]
    c1 = dx * dist1.cdf(x)
    c2 = dx * dist2.cdf(x)

    return p1, p2, c1, c2


if __name__ == "__main__":
    # Grid for pdf and cdf evaluations
    x = np.linspace(-4.5, 7.5, 1000)

    # Grid to generate samples
    y = np.linspace(0, 100, 500)

    # Generate samples data
    pdf1 = []
    pdf2 = []
    cdf1 = []
    cdf2 = []
    for yi in y:
        p1, p2, c1, c2 = samples(x, yi)
        pdf1.append(p1)
        pdf2.append(p2)
        cdf1.append(c1)
        cdf2.append(c2)

    # Compute distances
    validater = uq.comparison.ValidateSimilarityHellinger()

    # Hellinger distance (the default one)
    dh = validater.compare(pdf1, pdf2)

    # Jensen-Shannon distance
    validater = uq.comparison.ValidateSimilarityShannonJenson()
    dj = validater.compare(pdf1, pdf2)

    # Wasserstein-1 distance
    validater = uq.comparison.ValidateSimilarityWasserstein1()
    dw1 = validater.compare(cdf1, cdf2)

    # Wasserstein-2 distance
    validater = uq.comparison.ValidateSimilarityWasserstein2()
    dw2 = validater.compare(cdf1, cdf2)

    # Visualisations
    if _PLOT:
        import pylab as plt

        # QoIs means and stdvs
        m1 = (y - 50.)**2 / 500
        s1 = 0.2 * np.ones_like(y)
        m2 = 2.5 * np.ones_like(y)
        s2 = 0.1 * np.ones_like(y) + 0.01 * y

        fig, axs = plt.subplots(2, 1)

        axs[0].plot(y, m1, "k-", label="QoI 1")
        axs[0].plot(y, m1 + s1, "k-", alpha=0.2)
        axs[0].plot(y, m1 - s1, "k-", alpha=0.2)
        axs[0].fill_between(y, m1 - s1, m1 + s1, color="k", alpha=0.15)

        axs[0].plot(y, m2, "b-", label="QoI 2")
        axs[0].plot(y, m2 + s2, "b-", alpha=0.2)
        axs[0].plot(y, m2 - s2, "b-", alpha=0.2)
        axs[0].fill_between(y, m2 - s2, m2 + s2, color="b", alpha=0.15)

        axs[0].legend()
        axs[0].grid()

        axs[1].plot(y, dh, label="Hellinger")
        axs[1].plot(y, dj, label="Shannon-Jenseen")
        axs[1].plot(y, dw1, label="Wassertein-1")
        axs[1].plot(y, dw2, label="Wassertein-2")

        axs[1].set_ylabel("distances")
        axs[1].legend()
        axs[1].grid()

        plt.show()
