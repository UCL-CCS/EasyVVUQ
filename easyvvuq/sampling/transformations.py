import chaospy as cp
import numpy as np

__author__ = "Juraj Kardos"
__copyright__ = """

    Copyright 2022 Juraj Kardos

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class Transformations:
    def __init__(self):
        pass

    # Applies Rosenblatt transformation
    # to the independent nodes.
    # Returns: The transformed nodes or transformed (weights, nodes)
    # Args:
    #   @Nodes - Independent nodes to be transformed
    #   @Distribution - PDF of the independent nodes
    #   @Distribution_dep - PDF of the correlated nodes
    #   @regression - see PCESampler(regression) parameter
    @staticmethod
    def rosenblatt(nodes, distribution, distribution_dep, regression=True):

        # Input nodes are expected to be in sape (ndim x nsamples),
        # but user might have have provided the transposed array
        do_transpose = False
        if not nodes.shape[0] == len(distribution):
            do_transpose = True
            nodes = nodes.T
            if not nodes.shape[0] == len(distribution):
                raise ValueError("Input nodes have wrong shape.")
        
        transformed_nodes = []

        transformed_nodes = distribution_dep.inv(distribution.fwd(nodes))

        if do_transpose:
            transformed_nodes = transformed_nodes.T
            nodes = nodes.T # need to transpose back (args. are passed by reference)

        # Transform node weights in the pseudo-spectral method
        if not regression:
            # The transformed weights are not used
            transformed_weights = None
            # TODO: need to add weights argument
            # transformed_weights = weights * distribution_dep.pdf(transformed_nodes)/distribution.pdf(nodes)
            return (transformed_weights, transformed_nodes)

        return transformed_nodes

    # Applies Cholesky transformation
    # to the independent nodes.
    # Returns: The transformed nodes or transformed (weights, nodes)
    # Args:
    #   @Nodes - Independent nodes to be transformed
    #   @vary - Vary object containing the PDF of the parameters
    #   @correlation - correlation matrix
    #   @regression - see PCESampler(regression) parameter
    @staticmethod
    def cholesky(nodes, vary, correlation, regression=True):

        if str(type(vary)) == "<class 'dict'>":
            items = vary.items() # simple dictionary
        else:
            items = vary.get_items() # Vary object
        nparams = len(items)

        # Input nodes are expected to be in shape (ndim x nsamples),
        # but user might have have provided the transposed array
        do_transpose = False
        if not nodes.shape[0] == nparams:
            do_transpose = True
            nodes = nodes.T
            if not nodes.shape[0] == nparams:
                raise ValueError("Input nodes have wrong shape.")

        # Shift and stretch the nodes to a unit normal distribution
        # Until now we have samples from a general non-unit normal distribution
        nodes_unit = np.zeros(nodes.shape)
        for i, (param, distribution) in enumerate(items):
            if type(distribution).__name__ == "Uniform":
                a = distribution._parameters['lower'] #lower
                b = distribution._parameters['upper'] #upper
                nodes_unit[i] = (nodes[i] - a) / (b-a)
            elif type(distribution).__name__ == "Normal":
                a = distribution._parameters['shift'] #mu
                b = distribution._parameters['scale'] #sigma
                nodes_unit[i] = (nodes[i] - a) / b

        transformed_nodes = []
        L = np.linalg.cholesky(correlation)
        transformed_nodes = np.matmul(L, nodes_unit)

        # Shift and stretch the transformed nodes to the target distr.
        # Until now we had samples from unit uniform (or normal) distributions
        for i, (param, distribution) in enumerate(items):
            if type(distribution).__name__ == "Uniform":
                a = distribution._parameters['lower'] #lower
                b = distribution._parameters['upper'] #upper
                transformed_nodes[i] = a + (b-a)*transformed_nodes[i]
            elif type(distribution).__name__ == "Normal":
                a = distribution._parameters['shift'] #mu
                b = distribution._parameters['scale'] #sigma
                transformed_nodes[i] = a + b*transformed_nodes[i]

        if do_transpose:
            transformed_nodes = transformed_nodes.T
            nodes = nodes.T # need to transpose back (args. are passed by reference)

        # Tested & implemented only with the point collocation!
        # For spectral projection we need to work also with
        # the node weights, which requires some additional care
        # assert(regression)
        if not regression:
            transformed_weights = None
            return (transformed_weights, transformed_nodes)

        return transformed_nodes