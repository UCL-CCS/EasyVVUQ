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

    def element_name(self):
        """Name for this element for logging purposes"""
        return "gp_surrogate"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.1"

    def analyse(self, data_frame=None):
        """Perform the basis stats analysis on the input `data_frame`.

        Analysis is based on `pandas.Dataframe.describe` and results in
        values for: count, mean, std, min, max and 25%, 50% & 75% percentiles
        for each value in the analysis.

        The data_frame is grouped according to `self.groupby` if specified and
        analysis is performed on the columns selected in `self.qoi_cols` if set.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Summary data produced through collation of simulation output.

        Returns
        -------
        :obj:`pandas.DataFrame`
            Basic statistic for selected columns and groupings of data.
        """
        x = data_frame[self.attr_cols].values
        y = data_frame[self.target_cols].values

        gp = GaussianProcessRegressor()
        gp.fit(x, y)
        return gp
