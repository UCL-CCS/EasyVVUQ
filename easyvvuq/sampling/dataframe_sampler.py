"""
"""

from .base import BaseSamplingElement
import csv

__license__ = "LGPL"


class DataFrameSampler(BaseSamplingElement, sampler_name="csv_sampler"):

    def __init__(self, df, counter=0):
        """Takes a DataFrame and outputs it row by row.
        """
        self.data = df.to_dict(orient='records')
        self.counter = counter

    def is_finite(self):
        return True

    def n_samples(self):
        """Returns the number of samples in this sampler.
        Returns
        -------
        if the user specifies maximum number of samples than return that, otherwise - error
        """
        return len(self.data)

    def __next__(self):
        try:
            return self.data[self.counter]
        finally:
            if self.counter < self.n_samples():
                self.counter += 1
            else:
                raise StopIteration
