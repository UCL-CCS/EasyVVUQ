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
        self.sparse = sampler.sparse

        #determine if quadrature rule is nested, default assumption is False
        self.nested = False
        rule = self.sampler.quadrature_rule
        growth = self.sampler.growth
        
        #TODO: ARE THERE OTHERS WHICH ARE NESTED? genz_keister SHOULD BE,
        #BUT SEEMS NOT IMPLEMENTED IN MY cp VERSION (3.0.5)
        if self.sparse == True:
            if rule == 'guass_patterson':
                self.nested = True
            elif rule == 'C' or rule == 'c' or rule == 'clenshaw_curtis' and growth == True:
                self.nested = True                

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

        #the maximum level (quad order) of the (sparse) grid         
        self.L = self.sampler.L
        
        #the number of uncertain parameters
        self.N = self.sampler.N
        
        #if L < L_min: quadratures and interpolations are zero
        #For full tensor grid: there is only one level: L_min = L
        if self.sparse == False:
            self.L_min = self.L
        #For sparse grid: multiple levels, L >= N must hold
        else:            
            self.L_min = self.N    

        # Chaospy computation of 1D weights - USED IN SOBOL SUBROUTINES
        #REMOVE LATER IN FAVOUR OF xi_1D, wi_1d
        xi = []
        wi = []
        for dist in self.sampler.vary.get_values():
            xi_i, wi_i = cp.generate_quadrature(
                self.sampler.quad_order, dist, rule=self.sampler.quad_rule)
            xi.append(xi_i.flatten())
            wi.append(wi_i.flatten())
        self.xi = xi
        self.wi = wi

        self.xi_d = self.sampler.xi_d
        self.xi_1d = self.sampler.xi_1d
        self.wi_1d = self.compute_SC_weights(rule=self.sampler.quad_rule)
        
        #per level, map a unique index k to all (level multi indices, colloc points)
        #combinations. Will differ for sparse or full tensor grids.
        #All interpolation/quadrature subroutines loop over the entries in Map
        self.Map = {}
        self.surr_lm1 = {}
        
        for level in range(self.L_min, self.L+1):
            self.Map[level] = self.create_map(self.N, level)

        self.clear_surr_lm1('interpolate')
        self.clear_surr_lm1('quadrature')

        # Extract output values for each quantity of interest from Dataframe
        qoi_cols = self.qoi_cols
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k].values
                samples[k].append(values)
        self.samples = samples

        # size of one code sample
        self.N_qoi = self.samples[qoi_cols[0]][0].size

        results = {'statistical_moments': {},
                   'sobol_indices': {k: {} for k in self.qoi_cols}}
   
     # Compute descriptive statistics for each quantity of interest
        for qoi_k in qoi_cols:
            mean_k, var_k = self.get_moments(qoi_k)
            std_k = var_k**0.5

            # compute statistical moments
            results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                     'var': var_k,
                                                     'std': std_k}
#            # compute all Sobol indices
#            results['sobol_indices'][qoi_k] = self.get_sobol_indices(qoi_k, 'all')

        return results
    
    def create_map(self, N, L):
        """
        Create a map from a unique integer k to each 
        (level multi index l, collocation point X) combination. Also
        compute the index of X (f) in the global (sparse) grid xi_d
        
        Parameters
        ----------
        - N (int) = number of parameters
        - L (int) = max level of grid
        
        Returns
        --------
        - Map: a dict for level L containing k, l, X, and f
        """

        #unique index
        k = 0
        Map = {} 
        
        print('Creating multi-index map for level', L, '...')
        
        #full tensor product
        if self.sparse == False:
           
            l = (np.ones(N)*L).astype('int')
            
            for x in self.xi_d:
                Map[k] = {'l':l, 'X':x, 'f':k}
                k += 1
        #sparse grid
        else:

            #all sparse grid multi indices l with |l| <= L
            l_norm_le_L = self.sampler.compute_sparse_multi_idx(L, N)
            
            #if nested grids are used, compute the sparse grid  of |l| <= L-1
            #which constains all points that will also be present in current grid
            if self.nested == True and L > N:
                H_Lm1_N = self.sampler.sparse_grid(L-1, N)
            
            #loop over all multi indices
            for l in l_norm_le_L:
                
                #colloc point of current level index l
                X_l = [self.xi_1d[n][l[n]] for n in range(N)]
                X_l = np.array(list(product(*X_l)))
                
                #if nested, remove points from X_l which are also in the previous sparse
                #grid (|l| <= L-1)
                if self.nested == True and L > N:
                    for x in X_l:
                        if list(x) in H_Lm1_N.tolist():
                            X_l = np.delete(X_l, x, axis=0)
                            print("Grid is nested. Not using point", \
                                  ["%.4f" %xx for xx in x], "at level", L)
    
                #for each k, store level index l, collocation point x and index j of
                #the code sample / collocation point in global grid xi_d                        
                for x in X_l:
                    j = np.where((x == self.xi_d).all(axis=1))[0][0]
                    Map[k] = {'l':l, 'X':x, 'f':j}
                    k += 1;
                    
        print('done.')

        return Map
    
    def surrogate(self, qoi, x):
        """
        Use sc_expansion UQP as a surrogate

        Parameters
        ----------
        - qoi (str): name of the qoi
        
        Returns
        -------
        the interpolated value of qoi at x (float, (N_qoi,))
        
        """
        
        return self.sc_expansion(self.L, 'interpolate', self.samples[qoi], x=x)
    
    def get_moments(self, qoi):
        """
        Use sc_expansion UQP as a quadrature method
        
        Parameters
        ----------
        - qoi (str): name of the qoi
        
        Returns
        -------
        - mean and variance of qoi (float (N_qoi,))
        
        """
        goal = 'quadrature'
        #compute mean
        mean_f = self.sc_expansion(self.L, goal, self.samples[qoi])
        
        #clear the quadrature results in surr_lm1
        self.clear_surr_lm1(goal)
        
        #compute variance
        variance_samples = []
        for sample in self.samples[qoi]:
            variance_samples.append((sample - mean_f)**2)
            
        var_f = self.sc_expansion(self.L, goal, variance_samples)
        
        return mean_f, var_f
        
    def sc_expansion(self, L, goal, samples, **args):
        """
        -----------------------------------------
        This is the UQ Pattern for the SC method.
        -----------------------------------------
        
        Can perform interpolation and quadrature for both full and sparse grids.
        
        For a qoi q, it computes the following tensor product:
        
        q \approx \sum_{l\in\Lambda} \Delta_{l}[q](x)
        
        where Delta_{l} is the difference at x between surrogates / quadratues
        of level L and L-1. See e.g.:
            
        Dimitrios Loukrezis et. al., "Assessing the Performance of Leja and 
        Clenshaw-Curtis Collocation for Computational Electromagnetics with 
        Random Input Data."
        
        Parameters
        ----------
        
        - x (float (N,)): location in stochastic space at which to eval the surrogate
        - L (int): max level of the surrogate
        
        Returns
        -------
        
        surr (float, (N_qoi,)): the interpolated value of qoi at x if goal = 'interpolate'
                                the expected value of qoi if goal = 'quadrature'        
        """        
        
        #for L < L_min the surrogate is defined as zero
        if L < self.L_min:
            return 0.0

        surr = np.zeros(self.N_qoi)

        #loop over all levels
        for level in range(self.L_min, L+1):       
            
            #contains the level multi-indices (l), colloc points x and samples
            #indices f of the (sparse) grid
            Map = self.Map[level]

            Delta = np.zeros(self.N_qoi)
            for k in Map.keys():
    
                #the current code samples
                q_k = samples[Map[k]['f']]
                
                #the hierarchical surplus (s_k) between the code output q_k and the
                #previous surrogate of level L-1 evaluated at the same location.
                #Recursively computed.
                
                if k in self.surr_lm1[goal][level]:
                    #print('surrogate already computed')
                    surr_lm1 = self.surr_lm1[goal][level][k]
                else:
                    surr_lm1 = self.sc_expansion(level-1, goal, samples, x = Map[k]['X'])
                    self.surr_lm1[goal][level][k] = surr_lm1

                s_k = q_k - surr_lm1
                
                #the current level multi index (l_1,...,l_N)
                l = Map[k]['l']
                
                idx = {}
                # indices of current collocation point (Map[k]['X'][n]),
                # in corresponding 1d colloc points (self.xi_1d[n][l[n]])
                # These are the j of the 1D lagrange polynomials l_j(x), see 
                # lagrange_poly subroutine
                for n in range(self.N):
                    idx[n] = (self.xi_1d[n][l[n]] == Map[k]['X'][n]).nonzero()[0][0]
    
                weight = []
                for n in range(self.N):
                    #interpolate
                    if goal == 'interpolate':
                        x = args['x']
                        # add values of Lagrange polynomials at x
                        weight.append(lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n]))
                    #integrate
                    elif goal == 'quadrature':
                        #add quadrature weights
                        weight.append(self.wi_1d[n][l[n]][idx[n]])
                    
                #Delta is the interpolation of the hierarchical surplus
                Delta += s_k*np.prod(weight)

            surr += Delta
        
        return surr
    
    def clear_surr_lm1(self, ID):
        """
        Clears the interpolation or quadrature results in surr_lm1[ID].
        
        surr_lm1 is a dictionary used to store surrogate results at 
        previous level (l-1). Used to avoid recomputing the surrogate
        in the recursive sc_expansion subroutine.
        
        surr_lm1['interpolation'][l][k] stores the interpolation results
        of level l-1 at collocation point X_k 
        
        Parameters
        ----------
        - ID (str): either 'interpolate' or 'quadrature'
        
        """
        self.surr_lm1[ID] = {}
        for level in range(self.L_min, self.L+1):
            self.surr_lm1[ID][level] = {}
    
    def compute_SC_weights(self, rule):
        """
        Computes the 1D quadrature weights w_j of the SC expansion:
            
            w_j = int L_j(x)p(x) dx                             (1)
        
        Here L_j is a Lagrange polynomial of the SC expansion.
        
        Parameters
        ----------
        - rule ("str"): chaospy quadrature rule used to compute (1), 
                        
        
        Returns
        -------
        - wi_1d (dict): wi_1d[n][l] gives an array
          of quadrature weigths for the n-th parameter at level l.
          
          IMPORTANT:
          If rule is the same as the rule used to compute the SC 
          collocation points, these weights will equal the weights
          computed by chaospy, since L_j(x_k) = 1 when j=k and 0 
          for the rest. This is the default setting.       
        """
        
        #no need to recompute weights
        if rule == self.sampler.quadrature_rule:
            return self.sampler.wi_1d
        #recompute weights - generally not used
        else:
            wi_1d = {}
            
            params = self.sampler.params_distribution
            
            for n in range(self.N):
                #1d weights for n-th parameter
                wi_1d[n] = {}
                #loop over all level of collocation method
                for level in range(1, self.L+1):
                    #current SC nodes over dimension n and level 
                    xi_1d = self.xi_1d[n][level]
                    wi_1d[n][level] = np.zeros(xi_1d.size)
                    
                    #generate a quadrature rule to compute the SC weights
                    xi_quad, wi_quad = cp.generate_quadrature(level, params[n], rule=rule)
                    xi_quad = xi_quad[0]
                    
                    #compute integral of the lagrange polynomial through xi_1d, weighted
                    #by the input distributions: 
                    #w_j = int L_j(xi) p(xi) dxi j = 1,..,xi_1d.size
                    for j in range(xi_1d.size):
                        #values of L_i(xi_quad)
                        lagrange_quad = np.zeros(xi_quad.size)
                        for i in range(xi_quad.size):
                            lagrange_quad[i] = lagrange_poly(xi_quad[i], xi_1d, j)
                        #quadrature
                        wi_1d[n][level][j] = np.sum(lagrange_quad*wi_quad)
                        
            return wi_1d
    
    def get_sample_array(self, qoi):
        """
        Parameters
        ----------
        - qoi (str): name of quantity of interest
        
        Returns
        -------
         - array of all samples of qoi
        """
        
        tmp = np.zeros([self._number_of_samples, self.N_qoi])
        
        for k in range(self._number_of_samples):
            tmp[k, :] = (self.samples[qoi][k])
        
        return tmp
    
    def plot_grid(self):
        """
        If N = 2 or N = 3 plot the (sparse) grid
        """
        import matplotlib.pyplot as plt
        
        if self.N == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, xlabel=r'$x_1$', ylabel=r'$x_2$') 
            ax.plot(self.xi_d[:,0], self.xi_d[:,1], 'ro')
        elif self.N == 3:
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d', xlabel=r'$x_1$', \
                                 ylabel=r'$x_2$', zlabel=r'$x_3$') 
            ax.scatter(self.xi_d[:,0], self.xi_d[:,1], self.xi_d[:,2])
        else:
            print('Will only plot for N = 2 or N = 3.')
            
        plt.tight_layout()
        plt.show()

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
                xi_s = np.zeros(self.N)

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
        U = list(range(self.N))

        if typ == 'first_order':
            P = list(powerset(U))[0:self.N + 1]
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
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

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
    """
    Lagrange polynomials used for interpolation

    l_j(x) = product(x - x_m / x_j - x_m) with 0 <= m <= k
                                               and m !=j

    Parameters
    ----------
    x : (float), location at which to compute the polynomial

    x_i : list or array of float, nodes of the Lagrange polynomials

    j : int, index of node at which l_j(x_j) = 1

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