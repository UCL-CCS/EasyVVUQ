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
    sampler = QMCSampler(vary, 128)
    samples = {('run_id', 0): [], ('a', 0): [], ('b', 0): [], ('a+b', 0): []}
    for i, sample in enumerate(sampler):
        samples[('run_id', 0)].append(i)
        samples[('a', 0)].append(sample['a'])
        samples[('b', 0)].append(sample['b'])
        samples[('a+b', 0)].append(sample['a'] + sample['b'])
    df = pd.DataFrame(samples)
    analysis = QMCAnalysis(sampler)
    results = analysis.analyse(df)


if __name__ == '__main__':
    test_analyse()
