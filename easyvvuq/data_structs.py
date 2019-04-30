import os
import logging
import json
import easyvvuq as uq
from .constants import version

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

    if not isinstance(ref, 'int'):
        message = (f'Invalid {ref_type} id ({ref}) specified for '
                   f'run {run_name}')
        logger.critical(message)
        raise RuntimeError(message)


class RunInfo:

    def __init__(self, run_name='', app=None, params={}, sample=None,
                 campaign=None):

        # TODO: Handle fixtures

        check_reference(campaign, run_name, ref_type='campaign')
        check_reference(sample, run_name, ref_type='sampler')
        check_reference(app, run_name, ref_type='app')

        self.campaign = campaign
        self.sample = sample
        self.run_name = run_name

        if not params:
            message = f'No run configuration specified for run {run_name}'
            logger.critical(message)
            raise RuntimeError(message)

        self.params = params

        self.status = 'created'

    def to_dict(self):

        out_dict = {
            'run_name': self.run_name,
            'params': self.params,
            'status': self.status,
            'campaign': self.campaign,
            'sample': self.sample,
            'app': self.app,
        }

        return out_dict

    def dict_for_db(self):

        db_dict = {
            'run_name': self.run_name,
            'params': json.dumps(self.params),
            'status': self.status,
            'campaign': self.campaign,
            'sample': self.sample,
            'app': self.app,
        }

        return db_dict


class AppInfo:

    def __init__(self, name='app', input_encoder=None, encoder_options={},
                 output_decoder=None, decoder_options=None, execution={},
                 params={}, fixtures={}, collation={}, variable=[],
                 ):

        self.name = name
        self.input_encoder = input_encoder
        self.output_decoder = output_decoder
        self.encoder_options = encoder_options
        self.decoder_options = decoder_options
        self.execution = execution
        self.params = params
        self.fixtures = fixtures
        self.collation = collation
        # TODO: check that variable is subset of keys of params dict
        self.variable = variable

    @property
    def input_encoder(self):
        return self._input_encoder

    @input_encoder.setter
    def input_encoder(self, encoder):
        available_encoders = uq.encoders.base.available_encoders
        if encoder not in available_encoders:
            message = (f"Encoder not found. Looking for {encoder}.\n"
                       f"Available encoders are {available_encoders}.")
            logging.critical(message)
            raise RuntimeError(message)

        self._input_encoder = encoder

    @property
    def output_decoder(self):
        return self._output_decoder

    @output_decoder.setter
    def output_decoder(self, decoder):
        available_decoders = uq.decoders.base.available_decoders
        if decoder not in available_decoders:
            message = (f"Decoder not found. Looking for {decoder}.\n"
                       f"Available decoders are {available_decoders}.")
            logging.critical(message)
            raise RuntimeError(message)

        self._output_decoder = decoder

    def to_dict(self):

        out_dict = {
            'name': self.name,
            'input_encoder': self.input_encoder,
            'encoder_options': self.encoder_options,
            'output_decoder': self.output_decoder,
            'decoder_options': self.decoder_options,
            'execution': self.execution,
            'params': self.params,
            'fixtures': self.fixtures,
            'collation': self.collation,
            'variable': self.variable,
        }

        return out_dict

    def dict_for_db(self):

        db_dict = self.to_dict()

        for field in ['params', 'fixtures',
                      'execution', 'collation',
                      'encoder_options', 'decoder_options']:
            db_dict[field] = json.dumps(db_dict[field])

        return db_dict


class CampaignInfo:

    def __init__(self, name='default', easyvvuq_version=version,
                 campaign_dir_prefix='EasyVVUQ_Campaign_', campaign_dir='.',
                 runs_dir=None, local=False):

        self.name = name
        self.campaign_dir_prefix = campaign_dir_prefix

        self.easyvvuq_version = easyvvuq_version,

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

    def to_dict(self):

        out_dict = {
            'campaign_dir': self.campaign_dir,
            'campaign_dir_prefix': self.campaign_dir_prefix,
            'runs_dir': self.runs_dir,
            'easyvvuq_version': self.easyvvuq_version,
        }

        return out_dict

    def dict_for_db(self):

        return self.to_dict()
