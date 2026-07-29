#!/usr/bin/python3
"""
This module contains a utility function for object introspection.

It provides capability to inspect and return available attributes and
methods of any given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing strings of attribute and method names.
    """
    return dir(obj)
