import json
from .campaign import Campaign
from .populate_runs_dir import populate_runs_dir
from .apply_for_each_run import apply_for_each_run
from .execute import execute_local
from . import uqp
from . import reader
import pkg_resources

DEFAULT_ENCODERS = pkg_resources.resource_filename(__name__, 'default_app_encoders.json')

with open(DEFAULT_ENCODERS) as fin:
    app_encoders = json.load(fin)

# TODO: Search for user specified encoders list
user_encoders = ''

if user_encoders:
    with open(user_encoders) as fin:
        app_encoders.update(json.load(fin))