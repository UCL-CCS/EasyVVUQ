"""Analysis element for Markov Chain Monte Carlo (MCMC).
"""
import chaospy as cp
import pandas as pd
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
from .qmc_analysis import QMCAnalysisResults


class MCMCAnalysisResults(AnalysisResults):
    def __init__(self, dist, samples):
        self.dist = dist
        self.samples = samples

    def get_distribution(self):
        return self.dist

class MCMCAnalysis(BaseAnalysisElement):
    def __init__(self, sampler, qoi=None):
        self.sampler = sampler
        self.qoi = qoi

    def element_name(self):
        """Name for this element"""
        return "MCMCAnalysis"

    def element_version(self):
        """Version of this element"""
        return "0.1"

    def analyse(self, data_frame):
        data = data[frame][self.sampler.inputs]
        value = data[frame][self.sampler.qoi]
        dist = cp.J(*[cp.SampleDist(row.values) for _, row in data.iterrows()])
        return MCMCAnalysisResults(dist, df[self.sampler.inputs + [self.sampler.qoi]])
