#!/usr/bin/python3
"""Module containing the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a new Square.

        Args:
            size (int): Size of the square (width & height).
            x (int): x coordinate offset.
            y (int): y coordinate offset.
            id (int): ID of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Get size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size (and width/height) with validation.

        Args:
            value (int): New size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using *args (ordered) or **kwargs.

        Order for *args: id, size, x, y.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the square.

        Returns:
            dict: Dictionary with id, size, x, y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
