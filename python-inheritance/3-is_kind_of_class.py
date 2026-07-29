#!/usr/bin/python3
"""
This module contains a utility function for object classification.

It provides functionality to determine if an object is an instance of a class
or any class inherited from that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to inspect.
        a_class: The target class to check against.

    Returns:
        True if obj is an instance or inherited instance, otherwise False.
    """
    return isinstance(obj, a_class)
