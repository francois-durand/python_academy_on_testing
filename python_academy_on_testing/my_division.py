def my_division(x, y):
    """Divide.

    Parameters
    ----------
    x : Number
    y : Number

    Returns
    -------
    Number
        The division of `x` by `y`.

    Examples
    --------
    Even if arguments are integers, the result is a float:

        >>> my_division(42, 6)
        7.0

    If `y` is zero, it raises a ZeroDivisionError:

        >>> my_division(42, 0)
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
    """
    return x / y
