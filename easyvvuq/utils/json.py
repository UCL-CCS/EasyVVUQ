import json


def process_json(src):
    """Interpret JSON input (given as stream/file or filename), return dict

        Parameters
        ----------
        src
            Source stream/file or filename.

        Returns
        -------
        dict
            The result of interpreting input as JSON.

    """

    if hasattr(src, 'read'):

        json_stream = src

    else:

        try:
            json_stream = open(src, 'r')

        except Exception as e:

            reasoning = (
                f"\nInputs to Wrapper must be dict or valid JSON (stream "
                f"or read from filename) but received {type(src)} {src}"
            )

            raise Exception(str(e) + reasoning)

    return json.load(json_stream)
