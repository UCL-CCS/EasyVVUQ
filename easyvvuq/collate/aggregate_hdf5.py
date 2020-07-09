"""Provides an element for aggregation of results from all complete runs.
"""

import os
from .base import BaseCollationElement
from easyvvuq import OutputType, constants
import h5py

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


class AggregateHDF5(BaseCollationElement, collater_name="aggregate_hdf5"):
    """
    Aggregate the results of all completed simulations described by the
    Campaign. Will simply concatenate all simulation data into one big
    HDF5 DataFrame. This dataframe is stored in the campaign directory.

    """

    def collate(self, campaign, app_id):
        """
        Collected the decoded run results for all completed runs with ENCODED status

        Parameters
        ----------
        campaign : :obj:`easyvvuq.campaign.Campaign`
            EasyVVUQ coordination object from which to get information on runs
            to be collated.

        Returns
        -------
        `int`:
            The number of new data rows added during collation
        """

        decoder = campaign._active_app_decoder

        if decoder.output_type != OutputType.SAMPLE:
            raise RuntimeError('Can only aggregate sample type data')

        # Aggregate any uncollated runs into a dataframe (for appending to existing full df)
        new_data = {}
        qoi_cols = campaign._active_app_decoder.output_columns

        # Loop through all runs with status ENCODED (and therefore not yet COLLATED)
        processed_run_IDs = []
        for run_id, run_info in campaign.campaign_db.runs(
                status=constants.Status.ENCODED, app_id=app_id):

            # Use decoder to check if run has completed (in general application-specific)
            if decoder.sim_complete(run_info=run_info):

                run_data = decoder.parse_sim_output(run_info=run_info)
                new_data[run_id] = {}
                for qoi in qoi_cols:
                    new_data[run_id][qoi] = run_data[qoi].values
                processed_run_IDs.append(run_id)

        print('a')
        self.append_data(campaign, new_data)
        print('b')
        campaign.campaign_db.set_run_statuses(processed_run_IDs, constants.Status.COLLATED)
        print('c')

        return len(processed_run_IDs)

    def append_data(self, campaign, new_data):
        """

        Parameters
        ----------
        campaign : EasyVVUQ campaign object
        new_data : a dictionary containing the new simulation results for
        each quantity of interest. The results are appended to the HDF5 file
        samples.hdf5, located in the Campaign work directory

        Returns
        -------
        None.

        """
        hdf5_file = os.path.join(campaign.campaign_dir, 'samples.hdf5')
        #retrieve the names of the quantities of interest
        qoi_cols = campaign._active_app_decoder.output_columns

        h5f = h5py.File(hdf5_file, 'a')
        for qoi in qoi_cols:
            #Each QoI is stored in a separate group
            if not qoi in h5f.keys():
                h5f.create_group(qoi)
            #Each QoI sample is stored in a dataset qoi/run_id
            for run_id in new_data.keys():
                h5f.create_dataset(qoi + '/' + run_id, data=new_data[run_id][qoi])
        h5f.close()

    def get_collated_dataframe(self, campaign, app_id):
        """
        Read the samples from the HDF5 file samples.hdf5, and store them in
        a dictionary to be used in the analysis classes.

        Parameters
        ----------
        campaign : EasyVVUQ Campaign object
        app_id : the EasyVVUQ app id.

        Returns
        -------
        data : the simulation samples stored in a dictionary. Format of the
        dict is data[qoi][run_id], e.g. data['velocity']['Run_1']

        """

        hdf5_file = os.path.join(campaign.campaign_dir, 'samples.hdf5')
        qoi_cols = campaign._active_app_decoder.output_columns
        h5f = h5py.File(hdf5_file, 'r')
        data = {}
        for qoi in qoi_cols:
            data[qoi] = {}
            for run_id in h5f[qoi].keys():
                data[qoi][run_id] = h5f[qoi + '/' + run_id][()]
        h5f.close()
        return data

    def element_version(self):
        return "0.1"

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        """Return dict required for restart from serlialized form.

        Returns
        -------
        dict:
            Only parameter needed for restart is location of hdf5 file
        """
        return {}
