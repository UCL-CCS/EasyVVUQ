import os
import logging
import json
import easyvvuq as uq
from easyvvuq.constants import __easyvvuq_version__

logger = logging.getLogger(__name__)


def check_local_dir(path, dir_type='campaign'):
    """
    Check that local path exists and if not create it.

    Parameters
    ----------
    path : str
        Directory location to check.
    dir_type :
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
    ref_type : str
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


class RunInfo:

    def __init__(self, run_name='', app=None, params=None, sample=None,
                 campaign=None):

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

        self.status = 'created'

    def to_dict(self, flatten=False):

        if flatten:

            out_dict = {
                'run_name': self.run_name,
                'params': json.dumps(self.params),
                'status': self.status,
                'campaign': self.campaign,
                'sample': self.sample,
                'app': self.app,
            }

        else:

            out_dict = {
                'run_name': self.run_name,
                'params': self.params,
                'status': self.status,
                'campaign': self.campaign,
                'sample': self.sample,
                'app': self.app,
            }

        return out_dict


class AppInfo:

    def __init__(self, name=None, params=None, encoder=None, decoder=None, collation=None):

        self.name = name
        self.input_encoder = encoder
        self.output_decoder = decoder
        self.collation = collation
        self.params = params

    @property
    def input_encoder(self):
        return self._input_encoder

    @input_encoder.setter
    def input_encoder(self, encoder):
        available_encoders = uq.encoders.base.AVAILABLE_ENCODERS

        # TODO: Fix/relocate check. Problem is with live/serialized encoder info.
#        if encoder not in available_encoders:
#            message = (f"Encoder not found. Looking for {encoder}.\n"
#                       f"Available encoders are {available_encoders}.")
#            logging.critical(message)
#            raise RuntimeError(message)

        self._input_encoder = encoder

    @property
    def output_decoder(self):
        return self._output_decoder

    @output_decoder.setter
    def output_decoder(self, decoder):
        available_decoders = uq.decoders.base.AVAILABLE_DECODERS

        # TODO: Fix/relocate check. Problem is with live/serialized encoder info.
#        if decoder not in available_decoders:
#            message = (f"Decoder not found. Looking for {decoder}.\n"
#                       f"Available decoders are {available_decoders}.")
#            logging.critical(message)
#            raise RuntimeError(message)

        self._output_decoder = decoder

    def to_dict(self, flatten=False):

        if flatten:

            out_dict = self.to_dict()

            for field in ['params', 'input_encoder', 'output_decoder', 'collation']:
                out_dict[field] = json.dumps(out_dict[field])

        else:

            out_dict = {
                'name': self.name,
                'params': self.params,
                'input_encoder': self.input_encoder.serialize(),
                'output_decoder': self.output_decoder.serialize(),
                'collation': self.collation.serialize()
            }

        return out_dict


class CampaignInfo:

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

    @property
    def easyvvuq_version(self):
        return self._easyvvuq_version

    @easyvvuq_version.setter
    def easyvvuq_version(self, version_no):
        # TODO: check validity and compatibility
        self._easyvvuq_version = version_no

    def to_dict(self, flatten=False):

        out_dict = {
            'name': self.name,
            'campaign_dir': self.campaign_dir,
            'campaign_dir_prefix': self.campaign_dir_prefix,
            'runs_dir': self.runs_dir,
            'easyvvuq_version': self.easyvvuq_version,
        }

        return out_dict
