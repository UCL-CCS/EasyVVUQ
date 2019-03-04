import os
import numpy   as np
import pandas  as pd
import chaospy as cp
from easyvvuq import OutputType
from .base    import BaseAnalysisElement


class PCEAnalysis(BaseAnalysisElement):

    def element_name(self):
        return "PCE_basic_stats"

    def element_version(self):
        return "0.1"

    def __init__(self, data_src, params_cols=[], value_cols=[],
                 *args, **kwargs):

        # TODO: Fix this to allow more flexibility - basically pass through
        # available options to `pd.DataFrame.describe()`

        # Handles creation of `self.data_src` attribute (dict)
        super().__init__(data_src, *args, **kwargs)

        data_src = self.data_src

        if data_src:
            if 'files' in data_src:
                if len(data_src['files']) != 1:
                    raise RuntimeError("Data source must contain a SINGLE file path for this UQP")
                else:
                    self.data_frame = pd.read_csv(data_src['files'][0], sep='\t')

        self.value_cols = value_cols

        if self.campaign is not None:
            if not params_cols:
                self.params_cols = list(self.campaign.params_info.keys())
            self.value_cols = self.campaign.decoder.output_columns
        else:
            self.params_cols = params_cols
        self.output_type = OutputType.SUMMARY

    def _apply_analysis(self):

        if self.data_frame is None:
            raise RuntimeError("UQP needs a data frame to analyse")

        df = self.data_frame

        output_dir = self.output_dir
        output_file = os.path.join(output_dir, 'pce_basic_stats.tsv')

        grouped_data = df.groupby(self.params_cols)

        # Get summary statistics
        results = grouped_data.describe()

        # PCE nodes, weights and Polynomial
        nodes = self.campaign.nodes
        w = self.campaign.weights
        P = self.campaign.P

        # extract code output, per run, from Dataframe
#        samples = {}
#        for i in range(self.campaign.n_samples):
#            samples[i] = df.loc[df['run_id'] == 'Run_' + str(i)][self.value_cols]
#
        # Approximation solver
#        fit = cp.fit_quadrature(P, nodes, w, samples)
#
#        # Statistical infos
#        mean = cp.E(fit, dist)
#        var  = cp.Var(fit, dist)
#        std  = cp.Std(fit, dist)
#
#        # Store results in pandas Dataframe
#        results = pd.DataFrame({'mean':mean, 'var':var, 'std':std })
#        results.to_csv(output_file, sep='\t')

        self.output_file = output_file

        return results, output_file





