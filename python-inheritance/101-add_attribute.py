#!/usr/bin/python3
"""This module defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (any): The object to add the attribute to.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
