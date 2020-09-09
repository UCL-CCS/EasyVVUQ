from . import RandomSampler
import logging


class MCSampler(RandomSampler, sampler_name='mc_sampler'):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        #the number of uncertain inputs
        self.n_params = len(vary)
        #joint distribution
        self.joint = cp.J(*list(vary.values()))

    def __next__(self):
        for idx, param_name in enumerate(self.vary.get_keys()):
            run_dict[param_name] = self.xi_mc[self.sobol_count][idx]
        self.sobol_count += 1

    def generate_sobol_samples(self, n_mc):
        """
        Generates the n_mc*(n_params + 2) input samples needed to compute the
        Sobol indices. Stored in MCAnalysis.xi_mc.

        Method: A. Saltelli, Making best use of model evaluations to compute
        sensitivity indices, Computer Physics Communications, 2002.

        Parameters
        ----------
        n_mc : the number of Monte Carlo samples per input matrix. The total
        number of samples is n_mc*(n_params + 2)

        Returns
        -------
        None.

        """
        logging.debug('Drawing input samples for Sobol index computation.')
        # set the flag to True
        # the index in the dataframe of the first sobol sample
        self.sobol_start = self.count
        # a counter for the sobol samples. Used in __next__
        self.sobol_count = 0
        # the number of MC samples required to compute the Sobol indices
        self.max_num = n_mc * (self.n_params + 2)
        logging.debug('Generating {} input samples spread over {} sample matrices.'.format(
            self.max_num, self.n_params + 2))
        # Matrix M1, the sample matrix
        M_1 = self.joint.sample(n_mc).T
        # Matrix M2, the resample matrix (see reference above)
        M_2 = self.joint.sample(n_mc).T
        # xi_mc will stores all input samples
        self.xi_mc = []
        self.xi_mc.append(M_1)
        self.xi_mc.append(M_2)
        # Compute the N_i matrices (see again reference above)
        for i in range(self.n_params):
            N_i = np.array(M_2)
            # N_i = M2 with i-th colum from M1
            N_i[:, i] = M_1[:, i]
            self.xi_mc.append(N_i)
        # turn into array of size n_mc*(n_params + 2) x n_params
        self.xi_mc = np.array(self.xi_mc).reshape([self.max_num, self.n_params])
        logging.debug('Done.')
