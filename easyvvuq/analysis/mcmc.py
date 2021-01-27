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
    """The analysis results class for MCMC.

    Parameters
    ----------
    samples: ndarray of shape (nsamples, ndim)
    qoi: ndarray of shape (nsamples, 1)
    """
    def __init__(self, samples, qoi):
        self.samples = samples
        self.qoi = qoi

    def distribution(self):
        """Returns the KDE estimation of the distribution.

        Returns
        -------
        ChaosPy distribution
        """
        return cp.GaussianKDE(self.samples.values.T)


class MCMCAnalysis(BaseAnalysisElement):
    """The analysis part of the MCMC method in EasyVVUQ

    Parameters
    ----------
    sampler: MCMCSampler
       an instance of MCMCSampler used to generate MCMC samples
    qoi: str
       name of the qoi
    """
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
