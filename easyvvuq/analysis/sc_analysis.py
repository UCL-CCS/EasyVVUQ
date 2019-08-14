"""Analysis element for Stochastic Collocation (SC).

Method: 'Global Sensitivity Analysis for Stochastic Collocation'
        G. Tang and G. Iaccarino, AIAA 2922, 2010
"""
import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
from easyvvuq import OutputType
from .base import BaseAnalysisElement

__author__ = "Wouter Edeling"
__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

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


class SCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """Analysis element for Stochastic Collocation (SC).

        Method: 'Global Sensitivity Analysis for Stocastic Collocation'
                G. Tang and G. Iaccarino, AIAA 2922, 2010

        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.stochastic_collocation.SCSampler`
            Sampler used to initiate the PCE analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'SC analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler
        self._number_of_samples = sampler._number_of_samples

    def element_name(self):
        """Name for this element for logging purposes"""
        return "SC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.3"

    def analyse(self, data_frame=None):
        """Perform PCE analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Input data for analysis.

        Returns
        -------
        dict
            Results dictionary with sub-dicts with keys:
            ['statistical_moments', 'sobol_indices'].
            Each dict has an entry for each item in `qoi_cols`.
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        results = {'statistical_moments': {},
                   'sobol_indices': {k: {} for k in self.qoi_cols}}

        if self.sampler.sparse == False:
            self.analyse_tensor_grid(results, self.qoi_cols, data_frame)
        else:
            self.analyse_sparse_grid(results, self.qoi_cols, data_frame)

        return results

        
    def analyse_tensor_grid(self, results, qoi_cols, data_frame):
        """
        Perform the post-processing analysis for a full tensor product grid
        (sparse = False)
        """
        
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
            results['sobol_indices'][qoi_k] = self.get_sobol_indices(qoi_k, 'all')

        return results
    
    def analyse_sparse_grid(self, results, qoi_cols, data_frame):
        """
        Perform the post-processing analysis for a sparse grid
        (sparse = True)
        """
        #use this above too?
        self.xi_d = self.sampler.xi_d
        self.xi_1d = self.sampler.xi_1d
        self.wi_1d = self.sampler.wi_1d

        self.L = self.sampler.q
        self.N = self.sampler.N
        
        self.Map = {}
        for level in range(self.N, self.L+1):
            self.Map[level] = self.create_map(self.N, level)

        # Extract output values for each quantity of interest from Dataframe
        idx = 0
        samples = {k: {} for k in qoi_cols}
        
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k][self.xi_d[idx].tobytes()] = values
            idx += 1
        self.samples = samples

        self.N_qoi = samples[qoi_cols[0]][self.xi_d[0].tobytes()].size

        # Extract output values for each quantity of interest from Dataframe
        samples2 = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k].values
                samples2[k].append(values)
        self.samples2 = samples2
        self.data_frame = data_frame
        
        self.test = []
        
        # Compute descriptive statistics for each quantity of interest
        for qoi_k in qoi_cols:
            mean_k, var_k = self.get_moments(qoi_k)
            std_k = var_k**0.5
            
            # compute statistical moments
            results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                     'var': var_k,
                                                     'std': std_k}
            # compute all Sobol indices
            #results['sobol_indices'][qoi_k] = self.get_sobol_indices(qoi_k, 'all')            
            
    def compute_Q_diff(self, i, qoi, mean_f = []):
    
        """
        =======================================================================
        For every multi index i = (i1, i2, ..., id), Smolyak sums over 
        tensor products difference quadrature rules:
        (Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
        Below this product is expanded into individual tensor products, each 
        of which is then computed as:
        Q^1_{k1} X ... X Q^1_{kd} = sum...sum w_{k1}*...*w{kd}*f(x_{k1},...,x_{kd}) 
        =======================================================================
        """
        #expand the multi-index indices of the tensor product
        #(Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
        diff_idx = np.array(list(product(*[[k, -(k-1)] for k in i])))
        
        #Delta will be the sum of all expanded tensor products
        #Q^1_{k1} X ... X Q^1_{kd} = sum...sum w_{k1}*...*w{kd}*f(x_{k1},...,x_{kd})
        Delta = 0.0
    
        for diff in diff_idx:
            #Q_0 = 0, so if present do not compute Q^1_{k1} X ... X Q^1_{kd} 
            if not np.in1d(0, diff):
                X_k = [self.xi_1d[n][np.abs(diff)[n]] for n in range(self.N)]
                X_k = np.array(list(product(*X_k)))
                f_k = np.array([self.samples[qoi][x.tobytes()] for x in X_k])
                W_k = [self.wi_1d[n][np.abs(diff)[n]] for n in range(self.N)]
                W_k = np.array(list(product(*W_k)))
                W_k = np.prod(W_k, axis=1)
                
                #do some reshaping to align for multiplication
                f_k = f_k.reshape([f_k.shape[0], self.N_qoi])
                W_k = W_k.reshape([W_k.shape[0], 1])                
                
                if mean_f == []:
                    Q_prod = np.sum(f_k*W_k, axis=0).T
                else:
                    Q_prod = np.sum((f_k - mean_f)**2, axis=0).T
            else:
                Q_prod = 0.0
            
            Delta += np.sign(np.prod(diff))*Q_prod
            
        return Delta

    def get_moments(self, qoi):
        """Compute the first two statistical moments.

        Parameters
        ----------
        qoi : str
            column name of quantity of interest

        Returns
        -------
        float:
            Mean of samples, using quad weights
        float:
            Variance of samples, using quad weights
        """
        
        if self.sampler.sparse == False:
            mean_f = np.zeros([self.N_qoi, 1])
            var_f = np.zeros([self.N_qoi, 1])
    
            for k in range(self._number_of_samples):
                sample_k = (self.samples[qoi][k]).values.reshape([self.N_qoi, 1])
                mean_f += sample_k * self.wi_d[k]#.prod()
    
            for k in range(self._number_of_samples):
                sample_k = (self.samples[qoi][k]).values.reshape([self.N_qoi, 1])
                var_f += (sample_k - mean_f)**2 * self.wi_d[k]#.prod()
    
            return mean_f, var_f
        else:
            
            i_norm_le_q = self.sampler.compute_sparse_multi_idx(self.L, self.N)
    
            #compute quadrature sum_i(Delta_i1 X ... X Delta__iN)
            Delta = []
            for i in i_norm_le_q:
                Delta.append(self.compute_Q_diff(i, qoi))
                
            mean_f = np.sum(Delta, axis = 0)
            
            #compute quadrature sum_i(Delta_i1 X ... X Delta__iN)
            Delta = []
            for i in i_norm_le_q:
                Delta.append(self.compute_Q_diff(i, qoi, mean_f))
                
            var_f = np.sum(Delta, axis = 0)
                
            return mean_f, var_f

    def get_sample_array(self, qoi):
        """
        Returns an array of all samples of qoi
        """
        
        tmp = np.zeros([self._number_of_samples, self.N_qoi])
        
        for k in range(self._number_of_samples):
            tmp[k, :] = (self.samples[qoi][k]).values
        
        return tmp
    
    def create_map(self, N, L):
        l_norm_le_L = self.sampler.compute_sparse_multi_idx(L, N)
        
        k = 0
        Map = {}        
        
        for l in l_norm_le_L:
            X_l = [self.xi_1d[n][l[n]] for n in range(N)]
            X_l = np.array(list(product(*X_l)))
                        
            for x in X_l:
                j = np.where((x == self.xi_d).all(axis=1))[0][0]
                Map[k] = {'l':l, 'X':x, 'f':j}
                k += 1;
                
        return Map
        
    def sparse_surrogate(self, qoi, x, N, L):
        
        if L < N:
            return 0.0

        surr = np.zeros(self.N_qoi)

        for level in range(N, L+1):       
            
            Delta = np.zeros(self.N_qoi)
            Map = self.Map[level]
            
            for k in Map.keys():
    
                q_k = self.samples2[qoi][Map[k]['f']]
                s_k = q_k - self.sparse_surrogate(qoi, Map[k]['X'], N, level-1)
     
                l = Map[k]['l']
                
                idx = {}
                for n in range(N):
                    # indices of current collocation point xi_d[k] in 1d
                    # collocation points
                    idx[n] = (self.xi_1d[n][l[n]] == Map[k]['X'][n]).nonzero()[0][0]
    
                lagrange = []
                for n in range(N):
                    # values of Lagrange polynomials at x
                    lagrange.append(lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n]))
    
                Delta += s_k*np.prod(lagrange)
            surr += Delta
        
        return surr

    def surrogate(self, qoi, x):
        """Use the SC expansion as a surrogate.

        Parameters
        ----------
        qoi : str
            Column name of quantity of interest
        x :


        Returns
        -------

        """

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
                L.append(lagrange_poly(x[i], C[i], idx[i]))

            # current sample
            qoi_k = self.samples[qoi][k].values.reshape([self.N_qoi, 1])  # .reshape(self.N_qoi)

            # surrogate: samples interpolated via Lagrange polynomials
            f_int += qoi_k * np.prod(L)

        return f_int

    # Start SC specific methods

    @staticmethod
    def compute_tensor_prod_u(xi, wi, u, u_prime):
        """Calculate tensor products with dimension of u

        Parameters
        ----------
        xi
        wi
        u
        u_prime

        Returns
        -------

        """

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

    def compute_h(self, qoi, u, u_prime, xi_d_u, xi_d_u_prime, wi_d_u_prime):
        """

        Parameters
        ----------
        qoi
        u
        u_prime
        xi_d_u
        xi_d_u_prime
        wi_d_u_prime

        Returns
        -------

        """

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

    def get_sobol_indices(self, qoi, typ):
        """Computes Sobol indices using Stochastic Collocation

        Parameters
        ----------
        qoi
        typ

        Returns
        -------

        """

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
        D_u = {P[0]: mu**2}

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

            sort.append(sobol[u])

        return sobol

    # End SC specific methods


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    Taken from: https://docs.python.org/3/library/itertools.html#recipes

    Parameters
    ----------
    iterable : iterable
        Input sequence

    Returns
    -------

    """

    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def lagrange_poly(x, x_i, j):
    """Lagrange polynomials used for interpolation

    l_j(x) = product(x - x_m / x_j - x_m) with 0 <= m <= k
                                               and m !=j

    TODO: Complete this docstring

    Parameters
    ----------
    x : float

    x_i : list or array of float

    j : int

    Returns
    -------
    float
        l_j(x) calculated as shown above.
    """

    l_j = 1.0

    for m in range(len(x_i)):

        if m != j:
            denom = x_i[j] - x_i[m]
            nom = x - x_i[m]

            l_j *= nom / denom

    return l_j
