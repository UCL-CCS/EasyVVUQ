import os
import pandas as pd
import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
from easyvvuq import OutputType
from .base import BaseAnalysisElement


# Author: Wouter Edeling
__license__ = "LGPL"


class SCAnalysis(BaseAnalysisElement):

    def element_name(self):
        return "SC_analysis"

    def element_version(self):
        return "0.3"

    def __init__(self, params_cols=None, sampler=None, qoi_cols=None):

        if sampler is None:
            msg = 'PCE analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.params_cols = params_cols
        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    # main analysis subroutine
    def analyse(self, data_frame=None):

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")

        qoi_cols = self.qoi_cols

        results = {'statistical_moments': {},
                   'sobol_indices': {k: {} for k in qoi_cols}}

        # Chaospy computation of 1D weights
        xi = []
        wi = []
        for dist in self.sampler.vary.get_values():
            xi_i, wi_i = cp.generate_quadrature(
                self.sampler.quad_order, dist, rule=self.sampler.quad_rule)
            xi.append(xi_i.flatten())
            wi.append(wi_i.flatten())
        self.xi = xi
        self.wi = wi

        # Compute tensor product nodes and weights
        xi_d, self.wi_d = cp.generate_quadrature(order=self.sampler.quad_order,
                                                 domain=self.sampler.joint_dist,
                                                 rule=self.sampler.quad_rule)
        self.xi_d = xi_d.T

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(values)

        self.samples = samples
        self._number_of_samples = self.sampler._number_of_samples

        # number of uncertain parameters
        self.d = self.xi_d.shape[1]

        # size of one code sample
        self.N_qoi = self.samples[qoi_cols[0]][0].size

        # Compute descriptive statistics for each quantity of interest
        for qoi_k in qoi_cols:
            mean_k, var_k = self.get_moments(qoi_k)
            std_k = var_k**0.5

            # compute statistical moments
            results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                     'var': var_k,
                                                     'std': std_k}

            # compute all Sobol indices
            results['sobol_indices'][qoi_k] = self.get_Sobol_indices(qoi_k, 'all')

        return results

    # Compute the first two statistical moments
    def get_moments(self, qoi):

        # compute the mean and variance of the code samples, using quad weights
        mean_f = np.zeros([self.N_qoi, 1])
        var_f = np.zeros([self.N_qoi, 1])

        for k in range(self._number_of_samples):
            sample_k = (self.samples[qoi][k]).values.reshape([self.N_qoi, 1])
            mean_f += sample_k * self.wi_d[k].prod()

        for k in range(self._number_of_samples):
            sample_k = (self.samples[qoi][k]).values.reshape([self.N_qoi, 1])
            var_f += (sample_k - mean_f)**2 * self.wi_d[k].prod()

        return mean_f, var_f

    # use the SC expansion as a surrogate

    def surrogate(self, qoi, x):
        # interpolated QoI
        f_int = np.zeros([self.N_qoi, 1])

        # list with the 1d collocation points of all uncertain parameters
        # [self.all_vars[param]['xi_1d'] for param in self.all_vars.keys()]
        C = self.xi

        # loop over all samples
        for k in range(self._number_of_samples):

            idx = {}
            for i in range(self.d):
                # indices of current collocation point xi_d[k] in 1d
                # collocation points
                idx[i] = (C[i] == self.xi_d[k][i]).nonzero()[0]

            L = []
            for i in range(self.d):
                # values of Lagrange polynomials at x
                L.append(LagrangePoly(x[i], C[i], idx[i]))

            # current sample
            qoi_k = self.samples[qoi][k].values.reshape([self.N_qoi, 1])  # .reshape(self.N_qoi)

            # surrogate: samples interpolated via Lagrange polynomials
            f_int += qoi_k * np.prod(L)

        return f_int

    ####################################################################
    # BEGIN SOBOL SUBROUTINES                                          #
    # Method: 'Global Sensitivity Analysis for Stocastic Collocation'  #
    #          G. Tang and G. Iaccarino, AIAA 2922, 2010               #
    ####################################################################

    def compute_tensor_prod_u(self, xi, wi, u, u_prime):
        # tensor products with dimension of u
        xi_u = {}
        wi_u = {}
        for key in u:
            xi_u[key] = xi[key]
            wi_u[key] = wi[key]

        xi_d_u = np.array(list(product(*xi_u.values())))
        wi_d_u = np.array(list(product(*wi_u.values())))

        # tensor products with dimension of u' (complement of u)
        xi_u_prime = {}
        wi_u_prime = {}
        for key in u_prime:
            xi_u_prime[key] = xi[key]
            wi_u_prime[key] = wi[key]

        xi_d_u_prime = np.array(list(product(*xi_u_prime.values())))
        wi_d_u_prime = np.array(list(product(*wi_u_prime.values())))

        return {'xi_d_u': xi_d_u, 'wi_d_u': wi_d_u,
                'xi_d_u_prime': xi_d_u_prime, 'wi_d_u_prime': wi_d_u_prime}

    #############################

    def compute_h(self, qoi, u, u_prime, xi_d_u, xi_d_u_prime, wi_d_u_prime):
        S_u = xi_d_u.shape[0]
        S_u_prime = xi_d_u_prime.shape[0]

        # coefficients h = f*w' integrated over u', so cardinality is that of u
        h = {}
        for i_u in range(S_u):
            h[i_u] = 0.
            for i_up in range(S_u_prime):

                # collocation point to be evaluated
                xi_s = np.zeros(self.d)

                # add the xi of u (at the correct location k)
                idx = 0
                for k in u:
                    xi_s[k] = xi_d_u[i_u][idx]
                    idx += 1

                # add the xi of u' (at the correct location k)
                idx = 0
                for k in u_prime:
                    xi_s[k] = xi_d_u_prime[i_up][idx]
                    idx += 1

                #
                tmp = np.prod(self.xi_d == xi_s, axis=1)
                idx = np.where(tmp == 1)[0][0]
                h[i_u] += self.samples[qoi][idx].values.flatten() * \
                    wi_d_u_prime[i_up].prod()

        return h

    #############################

    # Computes Sobol indices using Stochastic Collocation
    def get_Sobol_indices(self, qoi, typ):

        # multi indices
        U = list(range(self.d))

        if typ == 'first_order':
            P = list(powerset(U))[0:self.d + 1]
        elif typ == 'all':
            # all indices u
            P = list(powerset(U))

        # get first two moments
        mu, D = self.get_moments(qoi)
        mu = mu.flatten()
        D = D.flatten()

        # list of 1D nodes and quad weights
        xi = self.xi
        wi = self.wi

        # total variance might be zero at some locations, Sobol index not defined there
        # idx_gt0 = np.where(D > 0)[0]

        # partial variances
        D_u = {}
        # D_0 = mu**2
        D_u[P[0]] = mu**2

        sobol = {}

        for u in P[1:]:

            # complement of u
            u_prime = np.delete(U, u)

            # compute corresponding tensor products and GQ weights
            tmp = self.compute_tensor_prod_u(xi, wi, u, u_prime)
            xi_d_u = tmp['xi_d_u']
            wi_d_u = tmp['wi_d_u']
            xi_d_u_prime = tmp['xi_d_u_prime']
            wi_d_u_prime = tmp['wi_d_u_prime']

            # cardinality of u
            S_u = xi_d_u.shape[0]

            # h coefficients
            h = self.compute_h(qoi, u, u_prime, xi_d_u, xi_d_u_prime, wi_d_u_prime)

            # partial variance
            D_u[u] = 0.0
            for i_u in range(S_u):
                D_u[u] += h[i_u]**2 * wi_d_u[i_u].prod()
            D_u[u] = D_u[u].flatten()

            # all subsets of u
            W = list(powerset(u))[0:-1]

            # partial variance of u
            for w in W:
                D_u[u] -= D_u[w]

            # compute Sobol index, only include points where D > 0
            # sobol[u] = D_u[u][idx_gt0]/D[idx_gt0]
            sobol[u] = D_u[u] / D

        sort = []
        for u in P[1:]:
            #print('Sobol index ', u, ' = ', sobol[u])
            sort.append(sobol[u])

        # print('Total sum = ', np.sum(sobol.values())/self.N_qoi)

        return sobol

    #########################
    # END SOBOL SUBROUTINES #
    #########################

# https://docs.python.org/3/library/itertools.html#recipes


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# Lagrange polynomials used for interpolation


def LagrangePoly(x, x_i, j):

    l_j = 1.0

    for i in range(len(x_i)):

        if i != j:
            denom = x_i[j] - x_i[i]
            nom = x - x_i[i]

            l_j *= nom / denom

    return l_j
