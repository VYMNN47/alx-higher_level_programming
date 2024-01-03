#!/usr/bin/python3
"""Module for add_integer method."""

def add_integer(a, b=98):
    """function that adds 2 integers.

    Args:
        a: first int
        b: second int, default 98.

    Raises:
        TypeError: if a, b are not int or float.

    Return:
        The sum of the two ints.
    """

    if type(a) is not (int, float):
        raise TypeError('a must be an integer')
    if type(b) is not (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
