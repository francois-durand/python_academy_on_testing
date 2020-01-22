from random import randint


def my_randint(a, b):
    """Random integer.

    Returns
    -------
    int
        A random integer between `a` and `b` (both included).

    Examples
    --------
        >>> my_randint(0, 0)
        0
        >>> my_randint(0, 10)  # doctest: +SKIP
        7
    """
    return randint(a, b)
