import numpy as np
import chaospy as cp
from .base import BaseSamplingElement

# author: Jalal Lakhlili

class PCESampler(BaseSamplingElement):
    def __init__(self,
                 campaign,
                 polynomial_order=4,
                 quadrature_rule="G",
                 sparse=False):
        """
        Create the sampler for the Polynomial Chaos Expansion method.

        Parameters
        ----------
        campaign : Campaign
            To stores informations about the PCE element.
            - Multivariate distribution
            - The orthogonal polynomials P
            - The quadrature informations: order, rule and sparsity
            - Number of samples

        polynomial_order : int, optional
            The polynomial order, default is 4.

        quadrature_rule : char, optional
            The quadrature method, default is Gaussian "G".

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.

        """
        self.campaign = campaign

        # List of the probality distributions of uncertain parameters
        params_distribution = list(self.campaign.vars.values())

        # Multivariate distribution
        self.campaign.distribution = cp.J(*params_distribution)

        # The orthogonal polynomials corresponding to the joint distribution
        self.campaign.P = cp.orth_ttr(
            polynomial_order, self.campaign.distribution)

        # The quadrature informations: order, rule and sparsity
        self.campaign.quad_order = polynomial_order + 1
        self.campaign.quad_rule = quadrature_rule
        self.campaign.quad_sparse = sparse

        # Nodes and weights for the integration
        self._nodes, _ = cp.generate_quadrature(order=self.campaign.quad_order,
                                                domain=self.campaign.distribution,
                                                rule=quadrature_rule,
                                                sparse=sparse)

        # Number of samples
        self.campaign.number_of_samples = len(self._nodes[0])

    def element_name(self):
        return "PCE_sampler"

    def element_version(self):
        return "0.2"

    def is_finite(self):
        return True

    def generate_runs(self):
        for i_val in range(self.campaign.number_of_samples):
            run_dict = {}
            i_par = 0
            for param_name in self.campaign.vars.keys():
                run_dict[param_name] = self._nodes.T[i_val][i_par]
                i_par += 1

            yield run_dict
