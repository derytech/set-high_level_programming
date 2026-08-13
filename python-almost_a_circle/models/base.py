#!/usr/bin/python3
"""
Module for Base class.
"""


class Base:
    """Base class for managing id attributes across future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
