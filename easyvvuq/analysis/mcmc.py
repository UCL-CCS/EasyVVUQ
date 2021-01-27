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
    def __init__(self, samples, qoi):
        self.samples = samples
        self.qoi = qoi

    def distribution(self):
        return cp.GaussianKDE(self.samples.values.T)


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

    def analyse(self, df):
        samples = df[self.sampler.inputs]
        qoi = df[self.sampler.qoi]
        return MCMCAnalysisResults(samples, qoi)
