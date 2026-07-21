#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize a Square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __lt__(self, other):
        """Compare if square area is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if square area is less than or equal to another."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Compare if square area is equal to another."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if square area is not equal to another."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if square area is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if square area is greater than or equal to another."""
        return self.area() >= other.area()
