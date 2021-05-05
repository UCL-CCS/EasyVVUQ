from easyvvuq import OutputType
from .base import BaseAnalysisElement
from sklearn.gaussian_process import GaussianProcessRegressor
from .results import AnalysisResults
import numpy as np


class GaussianProcessSurrogateResults(AnalysisResults):
    def __init__(self, gps, parameters, qoi):
        self.gps = gps
        self.parameters = parameters
        self.qoi = qoi

    def surrogate(self):
        def surrogate_fn(inputs):
            values = np.array([[inputs[key] for key in self.parameters]])
            results = [gp.predict(values) for gp in self.gps][0][0]
            return {self.qoi[0]: [x for x in results]}
        return surrogate_fn


class GaussianProcessSurrogate(BaseAnalysisElement):

    def __init__(self, sampler, qoi_cols):
        """Element to calculate basic stats for `qoi_cols` values.

        This results in values for: count, mean, std, min, max and 25%, 50% &
        75% percentiles for each value in the analysis.

        Parameters
        ----------
        attr_cols : list
            Attributes used to train the gaussian process regressor.
        target_cols : list
            Corresponding target values (can be vectors).
        """
        self.sampler = sampler
        self.attr_cols = list(sampler.vary.get_keys())
        self.target_cols = qoi_cols

    def analyse(self, data_frame=None, **kwargs):
        """Perform the basis stats analysis on the input `data_frame`.

        Analysis is based on `pandas.Dataframe.describe` and results in
        values for: count, mean, std, min, max and 25%, 50% & 75% percentiles
        for each value in the analysis.

        The data_frame is grouped according to `self.groupby` if specified and
        analysis is performed on the columns selected in `self.qoi_cols` if set.

        Parameters
        ----------
        data_frame : pandas.DataFrame
            Summary data produced through collation of simulation output.
        kwargs : keyword arguments
            These arguments will be passed to sklearn's GaussianProcessRegressor

        Returns
        -------
        easyvvuq.analysis.gp.GaussianProcessSurrogateResults
           GaussianProcessSurrogateResults instance
        """
        x = data_frame[self.attr_cols].values
        y = data_frame[self.target_cols].values
        gps = []
        for _ in y:
            gp = GaussianProcessRegressor(**kwargs)
            gps.append(gp.fit(x, y))
        return GaussianProcessSurrogateResults(gps, self.attr_cols, self.target_cols)
