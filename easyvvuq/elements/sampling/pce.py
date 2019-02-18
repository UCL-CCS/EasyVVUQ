from .base import BaseSamplingElement
import numpy    as np
import chaospy  as cp

# TODO
# Change self.campagn using a new design => check with the easyvvuq team.
# Use other rules for the quadrature (in arguments ?) and optimal order (Leja?).
# Optimase generate_runs routine.

class PCESampler(BaseSamplingElement):

    def __init__(self,
                 campaign,
                 distribution,
                 polynomial_order=4,
                 sparse=False):
        """
        Create the polynomial chaos expansion Sampler.

        Parameters
        ----------
        distribution : list of chaospy.Dist
            List of the probability distribution for the given parameters.

        polynomial_order : int, optional
            The polynomial order, default is 4.

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.

        """

        self.campaign = campaign

        # Multivariate distribution
        self.campaign.dist = cp.J(*distribution)

        # The orthogonal polynomials corresponding to the joint disctribution
        self.campaign.P = cp.orth_ttr(polynomial_order, self.campaign.dist)

        # The quadrature oder
        quad_order = polynomial_order + 1

        # Nodes and weights for the integration
        self.campaign.nodes, self.campaign.weights = \
                cp.generate_quadrature(quad_order, self.campaign.dist, rule="G", sparse=sparse)


        self.campaign.number_of_samples = len(self.campaign.nodes[0])

    def element_name(self):
        return "PCE_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def generate_runs(self):

        # each run_dict[i] will caintan nparams
        for i in range(self.campaign.number_of_samples):
            run_dict = {"c":self.campaign.nodes.T[i]}

            yield run_dict
