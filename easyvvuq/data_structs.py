"""Data structures to ensure consistency during serialization for databases.

"""
import os
import logging
import json
from easyvvuq import constants
from easyvvuq.encoders import BaseEncoder
from easyvvuq.decoders import BaseDecoder

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

logger = logging.getLogger(__name__)


def check_local_dir(path, dir_type='campaign'):
    """
    Check that local path exists and if not create it.

    Parameters
    ----------
    path : str
        Directory location to check.
    dir_type : str, default='campaign'
        Type of directory we are checking (used for user and debugging
        information.)

    Returns
    -------

    """

    if not os.path.isdir(path):

        if os.path.exists(path):
            logger.critical(f'{path} specified as {dir_type} directory '
                            f'for local run but is not a directory.')
            raise IOError(f'Invalid {dir_type} directory')
        else:
            os.makedirs(path)


def check_reference(ref, run_name, ref_type='campaign'):
    """
    Validation check for a `RunInfo` reference. Checks that an integer value
    has been passed to use as a reference to another 'table' - i.e. to a
    specific campaign, app or sampler.

    Parameters
    ----------
    ref : int
        Reference to be checked.
    run_name : str
        Name of run for which the check is being performed (user info/
        debugging).
    ref_type : str, default='campaign'
        Are we checking for a campaign, sampler or app (user info/
        debugging).

    Returns
    -------

    """

    if ref is None:
        message = f'No {ref_type} id specified for run {run_name}'
        logger.critical(message)
        raise RuntimeError(message)

    if not isinstance(ref, int):
        message = (f'Invalid {ref_type} id ({ref}) specified for '
                   f'run {run_name}')
        logger.critical(message)
        raise RuntimeError(message)


class ParamsSpecification:

    def __init__(self, params, appname=None):

        if not isinstance(params, dict):
            msg = "params must be of type 'dict'"
            logger.error(msg)
            raise Exception(msg)

        if not params:
            msg = ("params must not be empty. At least one parameter "
                   "should be specified.")
            logger.error(msg)
            raise Exception(msg)

        # Check each param has a dict as a value, and that dict has a "default" defined
        for param_key, param_def in params.items():
            if not isinstance(param_def, dict):
                msg = f"Entry for param '{param_key}' must be a dictionary"
                logger.error(msg)
                raise Exception(msg)
            if "default" not in param_def:
                msg = (
                    f"Entry for param '{param_key}' must be a dictionary"
                    f"defining a 'default' value for this parameter."
                )
                logger.error(msg)
                raise Exception(msg)

        self.params_dict = params
        self.appname = appname

    def process_run(self, new_run, verify=True):

        if verify:
            # Check if parameter names match those already known for this app
            for param in new_run.keys():
                if param not in self.params_dict.keys():
                    allowed_params_str = ','.join(list(self.params_dict.keys()))
                    reasoning = (
                        f"Run dict contains extra parameter, "
                        f"{param}, which is not a known parameter name "
                        f"of app {self.appname}.\n"
                        f"The allowed param names for this app appear to be:\n"
                        f"{allowed_params_str}")
                    raise RuntimeError(reasoning)

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in self.params_dict.keys():
            if param not in new_run.keys():
                default_val = self.params_dict[param]["default"]
                new_run[param] = default_val

        return new_run

    def serialize(self):
        return json.dumps(self.params_dict)

    @staticmethod
    def deserialize(serialized_params):
        return ParamsSpecification(json.loads(serialized_params))


class RunInfo:
    """Handles information for individual application runs.

    Parameters
    ----------
    run_name : str
        Human readable name of the run.
    app : None or int
        ID of the associated application.
    params : None or dict
        Dictionary of parameter values for this run.
    sample: None or int
        ID of the sampler that created the run.
    campaign: None or int
        ID of the associated campaign.

    Attributes
    ----------
    campaign : int
        ID of the associated campaign.
    sample : int
        ID of the sampler that created the run.
    app : int
        ID of the associated application.
    run_name : str
        Human readable name of the run.
    status : enum(Status)
    """

    def __init__(self, run_name='', app=None, params=None, sample=None,
                 campaign=None, status=constants.Status.NEW):

        # TODO: Handle fixtures

        check_reference(campaign, run_name, ref_type='campaign')
        check_reference(sample, run_name, ref_type='sampler')
        check_reference(app, run_name, ref_type='app')

        self.campaign = campaign
        self.sample = sample
        self.app = app
        self.run_name = run_name

        if not params:
            message = f'No run configuration specified for run {run_name}'
            logger.critical(message)
            raise RuntimeError(message)

        self.params = params
        self.status = status

    def to_dict(self, flatten=False):
        """Convert to a dictionary (optionally flatten to single level)

        Parameters
        ----------
        flatten : bool
            Should the return dictionary be single level (i.e. should `params`
            or other dictionary variables be serialized).

        Returns
        -------
        dict
            Dictionary representing the run - if flattened then params are
            returned as a JSON format sting.
        """

        if flatten:

            out_dict = {
                'run_name': self.run_name,
                'params': json.dumps(self.params),
                'status': constants.Status(self.status),
                'campaign': self.campaign,
                'sample': self.sample,
                'app': self.app,
            }

        else:

            out_dict = {
                'run_name': self.run_name,
                'params': self.params,
                'status': constants.Status(self.status),
                'campaign': self.campaign,
                'sample': self.sample,
                'app': self.app,
            }

        return out_dict


class AppInfo:
    """Handles information for particular application.

    Parameters
    ----------
    name : str or None
        Human readable application name.
    paramsspec : ParamsSpecification or None
        Description of possible parameter values.
    fixtures : dict or None
        Description of files/assets for runs.
    encoder : :obj:`easyvvuq.encoders.base.BaseEncoder`
        Encoder element for application.
    decoder : :obj:`easyvvuq.decoders.base.BaseDecoder`
        Decoder element for application.

    Attributes
    ----------
    name : str or None
        Human readable application name.
    paramsspec : ParamsSpecification or None
        Description of possible parameter values.
    fixtures : dict or None
        Description of files/assets for runs.
    input_encoder : :obj:`easyvvuq.encoders.base.BaseEncoder`
        Encoder element for application.
    output_decoder : :obj:`easyvvuq.decoders.base.BaseDecoder`
        Decoder element for application.
    """

    def __init__(
            self,
            name=None,
            paramsspec=None,
            fixtures=None,
            encoder=None,
            decoder=None):

        self.name = name
        self.input_encoder = encoder
        self.output_decoder = decoder
        self.paramsspec = paramsspec
        self.fixtures = fixtures

    @property
    def input_encoder(self):
        return self._input_encoder

    @input_encoder.setter
    def input_encoder(self, encoder):
        if not isinstance(encoder, BaseEncoder):
            msg = f"Provided 'encoder' must be derived from type BaseEncoder"
            logger.error(msg)
            raise Exception(msg)

        self._input_encoder = encoder

    @property
    def output_decoder(self):
        return self._output_decoder

    @output_decoder.setter
    def output_decoder(self, decoder):
        if not isinstance(decoder, BaseDecoder):
            msg = f"Provided 'decoder' must be derived from type BaseDecoder"
            logger.error(msg)
            raise Exception(msg)

        self._output_decoder = decoder

    def to_dict(self, flatten=False):
        """Convert to a dictionary (optionally flatten to single level)

        Parameters
        ----------
        flatten : bool
            Should the return dictionary be single level (i.e. should `paramsspec`
            and `fixtures` variables be serialized).

        Returns
        -------
        dict
            Dictionary representing the application- if flattened then `paramsspec`,
            and `fixtures` are returned as a JSON format sting.
        """

        if self.fixtures is None:
            fixtures = {}
        else:
            fixtures = self.fixtures

        if flatten:

            out_dict = self.to_dict()

            out_dict['params'] = self.paramsspec.serialize()
            out_dict['fixtures'] = json.dumps(out_dict['fixtures'])
        else:

            out_dict = {
                'name': self.name,
                'params': self.paramsspec,
                'fixtures': fixtures,
                'input_encoder': self.input_encoder.serialize(),
                'output_decoder': self.output_decoder.serialize()
            }

        return out_dict


class CampaignInfo:
    """Handles information on Campaign.

    Parameters
    ----------
    name : str or None
        Human readable campaign name.
    easyvvuq_version : str or None
        Version of EasyVVUQ used to create the campaign.
    campaign_dir_prefix : str or None
        Prefix test for campaign directory.
    campaign_dir : str or None,
        Path to the campaign directory.
    runs_dir : str or None
        path to run directory (within the campaign directory)
    local : bool, default=False
        Is this campaign designed to be created and executed on the same
        machine?

    Attributes
    ----------
    name : str or None
        Human readable campaign name.
    easyvvuq_version : str or None
        Version of EasyVVUQ used to create the campaign.
    campaign_dir_prefix : str or None
        Prefix test for campaign directory.
    campaign_dir : str or None,
        Path to the campaign directory.
    runs_dir : str or None
        path to run directory (within the campaign directory)
    """

    def __init__(self, name=None, easyvvuq_version=None,
                 campaign_dir_prefix=None, campaign_dir=None,
                 runs_dir=None, local=False):

        if name is None:
            message = "CampaignInfo constructor must be passed a 'name'."
            logger.critical(message)
            raise RuntimeError(message)

        if campaign_dir is None:
            message = "CampaignInfo constructor must be passed 'campaign_dir'"
            logger.critical(message)
            raise RuntimeError(message)

        self.name = name
        self.campaign_dir_prefix = campaign_dir_prefix

        self.easyvvuq_version = easyvvuq_version

        # TODO: think about right location for path check for remote runs
        if local:
            check_local_dir(campaign_dir)

        self.campaign_dir = campaign_dir

        if runs_dir is None:
            runs_dir = os.path.join(campaign_dir, 'runs')

        if local:
            check_local_dir(runs_dir, 'runs')

        self.runs_dir = runs_dir
        self.collater = None

    @property
    def easyvvuq_version(self):
        return self._easyvvuq_version

    @easyvvuq_version.setter
    def easyvvuq_version(self, version_no):
        # TODO: check validity and compatibility
        self._easyvvuq_version = version_no

    def to_dict(self, flatten=False):
        """Convert this to a dictionary

        Parameters
        ----------
        flatten : bool
            Should the return dictionary be single level (always true here).

        Returns
        -------
        dict
            Dictionary representing the campaign.
        """

        out_dict = {
            'name': self.name,
            'campaign_dir': self.campaign_dir,
            'campaign_dir_prefix': self.campaign_dir_prefix,
            'runs_dir': self.runs_dir,
            'easyvvuq_version': self.easyvvuq_version,
            'collater': self.collater
        }

        return out_dict
