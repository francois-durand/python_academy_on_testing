def my_get(lst, index, default=None):
    """Get an element in a list by position, with a default value.

    Parameters
    ----------
    lst : list
    index : int
    default : object

    Returns
    -------
    object
        The element of position `index` in the list `lst`. If the position does not exist, return  `default`.

    Examples
    --------
    If the position `index` exists, return the corresponding element:

        >>> my_get(['a', 'b', 'c'], 2, 'z')
        'c'

    Otherwise, return `default`:

        >>> my_get(['a', 'b', 'c'], 42, 'z')
        'z'
    """
    try:
        return lst[index]
    except IndexError:
        return default
