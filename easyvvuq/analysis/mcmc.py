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
    pass

class MCMCAnalysis(BaseAnalysisElement):
    pass
