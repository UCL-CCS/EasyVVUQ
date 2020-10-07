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
    contains_tuples = True
    if len(lst) == 0:
        raise RuntimeError('multi_index_tuple_parser needs a non-empty list of strings')
    for name in lst:
        if not isinstance(name, str):
            raise RuntimeError('multi_index_tuple_parser needs a list of strings')
    result = []
    for name in lst:
        if name.strip()[0] == '(' and name.strip()[-1] == ')':
            name = literal_eval(name)
        else:
            contains_tuples = False
        result.append(name)
    return result, contains_tuples


def remove_start_of_file(filename, delimiter):
    """Overwrite a file leaving only the portion of it after the
    delimiter string.

    Parameters
    ----------
    filename : str
       the name (and path) of the file to processs

    delimiter : str
       the string after which the file is copied over
    """
    with open(filename, 'r') as fd:
        lines = fd.readlines()
    remaining = []
    after_delimiter = False
    for line in lines:
        if after_delimiter:
            remaining.append(line)
        if line.strip() == delimiter:
            after_delimiter = True
    with open(filename, 'w') as fd:
        for line in remaining:
            fd.write(line)
