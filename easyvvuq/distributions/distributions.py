import numpy as np
import csv
from chaospy import Dist

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
__license__ = "LGPL"


def options(choices):
    """
    Generator to repeatedly provide one of a list of options (in order)

    Parameters
    ----------
    choices:    list
        Set of choices to be used in simulations

    Yields
    -------
    object:
        Selection from input choices
    """

    while True:
        for choice in choices:
            yield choice


# A discrete distribution (integers only) for use with random seeds.
class uniform_integer(Dist):
    def __init__(self, lo, up):
        """
        Initializer.
        """
        Dist.__init__(self, lo=lo, up=up)
        self.lo = lo
        self.up = up

    def cdf(self, x_data):
        """
        Cumulative distribution function.
        """
        return (x_data - self.lo) / (self.up - self.lo)

    def bnd(self):
        """
        Lower and upper bounds.
        """

        return self.lo, self.up

    def pdf(self):
        """
        Probability density function.
        """
        return 1. / (self.up - self.lo)

    def ppf(self, q_data):
        """
        Point percentile function.
        """
        return q_data * (self.up - self.lo) + self.lo

    def sample(self, size=()):
        """
        Produces random integer values i, uniformly distributed on the closed
        interval [lo, up], that is, distributed according to the discrete
        probability function P(i/lo,up)=1/(up-lo).

        Parameters
        ----------
        size (numpy.ndarray):
            The size of the samples to generate.

        Returns
        -------
        (numpy.ndarray):
            Random samples with shape ``size``.
        """

        return np.random.randint(self.lo, self.up, size)


# TODO: Convert this to a chaospy style distribution
def custom_histogram(filename):
    """
    Create a generator from histogram read from a CSV file
    TODO: Test this properly

    Parameters
    ----------
    filename:  str
        Path to file containing histogram

    Yields
    -------

    """

    # Read in the list of values and their associated probabilities
    # (1st and 2nd column, respectively)
    with open(filename, "r") as infile:
        probabilities = []
        values = []
        csvreader = csv.reader(infile)
        for row in csvreader:
            if '#' in row[0]:  # skip comment line
                continue
            values.append(float(row[0]))
            probabilities.append(float(row[1]))
        probabilities = np.array(probabilities)
        values = np.array(values)

        # Force normalization
        probabilities /= probabilities.sum()

    while True:
        yield np.random.choice(values, p=probabilities)

# TODO: This is deprecated. Chaospy version should be used from now on.
# Remove once nothing depends on this.


def legendre(m):
    """
    Returns the m-th order 1D legendre rules for uniformly distributed variables.
    To be used for stochastic collocation method.
    """
    xi_1d, wi_1d = np.polynomial.legendre.leggauss(m)

    return {'xi_1d': xi_1d, 'wi_1d': 0.5 * wi_1d}
