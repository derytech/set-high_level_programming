#!/usr/bin/python3
"""
This module defines a custom list class that extends the built-in list.

It provides functionality to display elements in sorted order without
modifying the original list instance state.
"""


class MyList(list):
    """
    A custom list class inheriting from the built-in list object.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
