from .base import BaseSamplingElement
import numpy as np
import chaospy as cp

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
            - distribution
            - P (The orthogonal polynomials)
            - nodes
            - weights
            - sampler_number
            - parameters_number

        polynomial_order : int, optional
            The polynomial order, default is 4.

        quadrature_rule : char, optional
            The quadrature method, default is Gaussian "G".

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.

        """
        self.campaign = campaign

        # The probality distributions of uncertain parameters
        params_distribution = list(self.campaign.vars.values())
        # Multivariate distribution
        self.campaign.distribution = cp.J(*params_distribution)

        # The orthogonal polynomials corresponding to the joint disctribution
        self.campaign.P = cp.orth_ttr(
            polynomial_order, self.campaign.distribution)

        # The quadrature oder (+2 ?)
        quad_order = polynomial_order + 1

        # Nodes and weights for the integration
        self.campaign.nodes, self.campaign.weights = cp.generate_quadrature(
            quad_order, self.campaign.distribution, rule=quadrature_rule, sparse=sparse)

        # Number of samples
        self.campaign.sample_number = len(self.campaign.nodes[0])

        # Number of uncertain parameters
        self.parameters_number = len(params_distribution)

    def element_name(self):
        return "PCE_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def generate_runs(self):
        for i_val in range(self.campaign.sample_number):
            run_dict = {}
            i_par = 0
            for param_name in self.campaign.vars.keys():
                run_dict[param_name] = self.campaign.nodes.T[i_val][i_par]
                i_par += 1

            yield run_dict
