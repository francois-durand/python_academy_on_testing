import numpy as np


def my_np_array(lst):
    """Convert list to numpy array.

    Parameters
    ----------
    lst : list

    Returns
    -------
    ndarray
        The corresponding numpy array.

    Examples
    --------
        >>> my_np_array([1, 2, 3642])  # doctest: +NORMALIZE_WHITESPACE
        array([ 1, 2, 3642])
    """
    return np.array(lst)
