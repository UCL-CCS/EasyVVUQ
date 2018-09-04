import easyvvuq.utils.json as json_utils


class BaseEncoder(object):
    """Baseclass for all EasyVVUQ encoders.

    Skeleton encoder which establishes the format and provides the basis of our
    contract - take in ``app_info`` and provide an ``encode``
    method to parse these and write relevant run file to a target directory.

    TODO: If we end up converting Attributed to Properties with ``@property``
    of Kristof style ``@advanced_property`` decorators then they should be
    documented in the property's getter method.

    Parameters
    ----------
    app_info    : dict, optional
        Application information. Will try interpreting as a dict or JSON
        file/stream or filename.

    Attributes
    ----------
    app_info    : dict
        Contains application information.

    """

    def __init__(self, app_info, *args, **kwargs):

        if not hasattr(app_info, 'items'):

            self.app_info = json_utils.process_json(app_info)

        else:

            self.app_info = app_info

    def encode(self, params={}, target_dir=''):
        raise NotImplementedError

