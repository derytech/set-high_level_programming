#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square using Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance with validated size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
