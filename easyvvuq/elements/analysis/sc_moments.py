import os
import pandas as pd
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement

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


class SCMoments(BaseAnalysisElement):

    def element_name(self):
        return "basic_stats"

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
        
        #SC quad weights
        wi_d = self.campaign.wi_d
        
        number_of_samples = wi_d.shape[0]
        
        #extract code output, per run, from Dataframe
        samples = {}
        for i in range(number_of_samples):
            samples[i] = df.loc[df['run_id'] == 'Run_' + str(i)][self.value_cols]
        
        #size of one code sample
        N_qoi = samples[0].size
        
        #compute the mean and variance of the code samples, using quad weights
        mean_f = np.zeros([N_qoi, 1])
        var_f = np.zeros([N_qoi, 1])    
    
        for k in range(number_of_samples):
            mean_f += samples[k]*wi_d[k].prod()
    
        for k in range(number_of_samples):
            var_f += (samples[k] - mean_f)**2*wi_d[k].prod()
    
        #store results in pandas Dataframe
        results = pd.DataFrame({'mean_f':mean_f.flatten(), 'var_f':var_f.flatten()})
  
        #write result to csv file
        output_dir = self.output_dir
        output_file = os.path.join(output_dir, 'sc_moments.tsv')
        results.to_csv(output_file, sep='\t')
        self.output_file = output_file

        return results, output_file
