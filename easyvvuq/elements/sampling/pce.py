from .base import BaseSamplingElement
import numpy    as np
import chaospy  as cp

# author: Jalal Lakhlili

class PCESampler(BaseSamplingElement):

    def __init__(self,
                 campaign,
                 polynomial_order=4,
                 sparse=False):
        """
        Create the sampler for the Polynomial Chaos Expansion method.

        Parameters
        ----------
        campaign :

        polynomial_order : int, optional
            The polynomial order, default is 4.

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.

        """
        self.campaign = campaign

        # Get the list of probalities distribution
        distribution = list(self.campaign.vars.values())

        # Multivariate distribution
        self.campaign.dist = cp.J(*distribution)

        # The orthogonal polynomials corresponding to the joint disctribution
        self.campaign.P = cp.orth_ttr(polynomial_order, self.campaign.dist)

        # The quadrature oder
        quad_order = polynomial_order + 1

        # Nodes and weights for the integration
        # TODO: Use other rules for the quadrature (in args) and optimal order (Leja?).
        self.campaign.nodes, self.campaign.weights = \
                cp.generate_quadrature(quad_order, self.campaign.dist, rule="G", sparse=sparse)

        # Number of samples
        self.campaign.n_samples = len(self.campaign.nodes[0])

    def element_name(self):
        return "PCE_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def generate_runs(self):
        run_dict = {}
        for i_val in range(self.campaign.n_samples):
            i_par = 0
            for param_name in self.campaign.vars.keys():
                run_dict[param_name] = self.campaign.nodes.T[i_val][i_par]
                i_par += 1

            yield run_dict
