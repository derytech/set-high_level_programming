#!/usr/bin/python3
"""
This module contains a function that checks object types.

It provides functionality to verify if an object is strictly an exact
instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to inspect.
        a_class: The class to match against.

    Returns:
        True if obj is strictly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
