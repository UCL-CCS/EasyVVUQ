"""Will create a Gaussian Process surrogate of your model. For
the sampler you can use the random sampler or the quasi-random
sampler. Don't forget to set the analysis class to GaussianProcessSurrogate
as is shown in the example below.

This uses the Gaussian Process model from sklearn.

Examples
--------
>>> campaign = uq.Campaign(name='surrogate')
>>> sampler = uq.sampling.RandomSampler(
    vary = {"Pe": cp.Uniform(100.0, 200.0), "f": cp.Uniform(0.95, 1.05)}
    max_num=100, analysis_class=uq.analysis.GaussianProcessSurrogate)
>>> campaign.add_app(name="sc", params=params, actions=actions)
>>> campaign.set_sampler(sampler)
>>> campaign.execute().collate()
>>> results = campaign.analyse(qoi_cols=output_columns)
>>> surrogate = results.surrogate()
>>> surrogate({'Pe' : 110.0, 'f': 1.0})
"""

from .base import BaseAnalysisElement
from sklearn.gaussian_process import GaussianProcessRegressor
from .results import AnalysisResults
import numpy as np


class GaussianProcessSurrogateResults(AnalysisResults):
    """Gaussian process surrogate results class. You would never
    create this manually in normal use. It is meant to be returned as the
    result of GaussianProcessSurrogate analyse method.

    Parameters
    ----------
    gps: list
        This will be one GP model for each coordinate of a vector QoI.
    parameters: list
        A list of input parameter names.
    qoi: str
        Output variable name.
    """

    def __init__(self, gp, parameters, qoi):
        self.gp = gp
        self.parameters = parameters
        self.qoi = qoi

    def surrogate(self):
        """Returns the GP surrogate model as a Python function.

        Returns
        -------
        function
            Returns a function that takes a dictionary and returns a dictionary.
            These dictionaries use the same format as Encoder and Decoder used
            to construct the surrogate.
        """
        def surrogate_fn(inputs):
            values = np.array([[inputs[key] for key in self.parameters]])
            return {self.qoi[0]: [x for x in self.gp.predict(values)[0]]}
        return surrogate_fn

    def get_params(self):
        return self.gp.kernel_.get_params()


class GaussianProcessSurrogate(BaseAnalysisElement):

    def __init__(self, sampler, qoi_cols, **kwargs):
        """An analysis class that can construct a Gaussian Process surrogate
        of your model. Based on the sklearn GaussianProgressRegressor class.

        Parameters
        ----------
        sampler : Sampler
            `Sampler` that was used to generate samples to train this surrogate model.
        qoi_cols : list
            Corresponding target values (can be vectors).
        """
        self.sampler = sampler
        self.attr_cols = list(sampler.vary.get_keys())
        self.target_cols = qoi_cols
        self.kwargs = kwargs

    def analyse(self, data_frame=None):
        """Construct a Gaussian Process surrogate based on data in `data_frame`.

        Parameters
        ----------
        data_frame : pandas.DataFrame
            Data which you want to use to fit the Gaussian Process to.
        kwargs : keyword arguments
            These arguments will be passed to sklearn's GaussianProcessRegressor.
            For details on what this could be, please see

        Returns
        -------
        easyvvuq.analysis.gp.GaussianProcessSurrogateResults
           `GaussianProcessSurrogateResults` instance. Used to interact with the surrogate
           model and to possibly access other functionality provided by the fitted model.
        """
        x = data_frame[self.attr_cols].values  # lgtm [py/hash-unhashable-value]
        y = data_frame[self.target_cols].values  # lgtm [py/hash-unhashable-value]
        gp = GaussianProcessRegressor(**self.kwargs)
        gp = gp.fit(x, y)
        return GaussianProcessSurrogateResults(gp, self.attr_cols, self.target_cols)
