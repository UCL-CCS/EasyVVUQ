import pytest
from easyvvuq.analysis.qmc_analysis import QMCAnalysis
from easyvvuq.sampling.qmc import QMCSampler
import chaospy as cp
import pandas as pd

def test_analyse():
    # we will use a simple model where there are two uniformly distributed
    # parameters and the model evaluates to the sum of them
    vary =  {
        "a": cp.Uniform(0.0, 1.0),
        "b": cp.Uniform(0.0, 1.0)
    }
    sampler = QMCSampler(vary, 100)
    analysis = QMCAnalysis(sampler)

if __name__ == '__main__':
    test_analyse()
