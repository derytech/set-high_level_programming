#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int."""


class MyInt(int):
    """A rebellious integer class with inverted equality operators."""

    def __eq__(self, other):
        """Inverts the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality operator (!=)."""
        return super().__eq__(other)
