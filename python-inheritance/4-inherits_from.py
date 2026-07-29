#!/usr/bin/python3
"""
This module contains a function that checks for subclass inheritance.

It provides functionality to verify if an object is an instance of a class
that inherited (directly or indirectly) from a specified class, excluding
exact matches of the specified class itself.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a subclass of a specified class.

    Args:
        obj: The object to inspect.
        a_class: The class to check inheritance against.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
