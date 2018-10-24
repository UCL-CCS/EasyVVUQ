import numpy as np
import csv

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


def normal(mean, sigma):
    """
    Generator returning samples picked from the specified normal distribution

    Parameters
    ----------
    mean:   float
        Mean of the normal distribution
    sigma:  float
        Standard deviation of the normal distribution

    Yields
    -------
    float
        Number drawn from provided distribution
    """

    while True:
        yield np.random.normal(mean, sigma)


def uniform(min_val, max_val):
    """
    Generator returning values picked from the specified uniform distribution

    Parameters
    ----------
    min_val:    float
        Minimum value covered by the distribution
    max_val:    float
        Maximum value covered by the distribution

    Yields
    -------
    float
        Number drawn from provided distribution

    """
    while True:
        yield np.random.uniform(min_val, max_val)

def uniform_integer(min_val, max_val):
    """
    Generator returning integer values picked from the specified uniform distribution

    Parameters
    ----------
    min_val:    int
        Minimum value covered by the distribution
    max_val:    int
        Maximum value covered by the distribution

    Yields
    -------
    int
        Number drawn from provided distribution

    """
    while True:
        yield np.random.randint(min_val, max_val)


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
            if '#' in row[0]: # skip comment line
                    continue
            values.append(float(row[0]))
            probabilities.append(float(row[1]))
        probabilities = np.array(probabilities)
        values = np.array(values)

        # Force normalization
        probabilities /= probabilities.sum()

    while True:
        yield np.random.choice(values, p=probabilities) 

