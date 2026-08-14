#!/usr/bin/python3
"""
Module for Square class.
Inherits from Rectangle and manages square attributes.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes of the Square instance."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == "size":
                        self.size = arg
                    else:
                        setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
