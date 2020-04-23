from ast import literal_eval

def multi_index_tuple_parser(lst):
    """
    Parses a list of strings to tuples if they represent tuples, otherwise
    leaves them as is.

    Parameters
    __________
    lst : list of strings

    Returns
    _______
    a tuple consisting of a list of tuples and/or strings and a bool indicating if
    the lst contains any tuples
    """
    if not lst:
        raise RuntimeError('multi_index_tuple_parser needs a non-empty list of strings')
    for name in lst:
        if not isinstance(name, str):
            raise RuntimeError('multi_index_tuple_parser needs a list of strings')
    return [], False
