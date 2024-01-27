#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """Adds two integers.
<<<<<<< HEAD
    Args:
        a: the first integer.
        b: the second integer, default 98.
    Raises:
        TypeError: if a, b are not int, float.
=======

    Args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

>>>>>>> 17f87994f4272a33af9d9c966e9e0f628f718f28
    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
