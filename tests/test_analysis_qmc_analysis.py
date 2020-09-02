import pytest
from easyvvuq.analysis.qmc_analysis import QMCAnalysis
from easyvvuq.sampling.qmc import QMCSampler
import chaospy as cp
import pandas as pd
import numpy as np


def test_analyse():
    # we will use a simple model where there are two uniformly distributed
    # parameters and the model evaluates to the sum of them
    vary = {
        "a": cp.Uniform(0.0, 1.0),
        "b": cp.Uniform(0.0, 1.0)
    }
    sampler = QMCSampler(vary, 100)
    samples = []
    for i, sample in enumerate(sampler):
        samples.append(
            [i, sample['a'], sample['b'], sample['a'] + sample['b']])
    df = pd.DataFrame(samples, columns=['run_id', 'a', 'b', 'a+b'])
    analysis = QMCAnalysis(sampler)
    results = analysis.analyse(df)


if __name__ == '__main__':
    test_analyse()
