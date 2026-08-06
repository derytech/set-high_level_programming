#!/usr/bin/python3
"""
This module contains the `add_integer` function.

The function adds two numbers (integers or floats) together
after casting floats to integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: First integer or float.
        b: Second integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
