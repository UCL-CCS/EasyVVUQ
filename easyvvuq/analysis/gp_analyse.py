from easyvvuq import OutputType
from .base import BaseAnalysisElement
from sklearn.gaussian_process import GaussianProcessRegressor


class GaussianProcessSurrogate(BaseAnalysisElement):

    def __init__(self, attr_cols, target_cols):
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
        self.attr_cols = attr_cols
        self.target_cols = target_cols

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

        gp = GaussianProcessRegressor(**kwargs)
        gp.fit(x, y)
        return gp
