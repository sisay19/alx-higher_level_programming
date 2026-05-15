#!/usr/bin/python3
"""Module containing the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a new Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x coordinate offset.
            y (int): y coordinate offset.
            id (int): ID of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x with validation."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y with validation."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of the rectangle.

        Returns:
            int: Area.
        """
        return self.width * self.height

    def display(self):
        """Print the rectangle using the `#` character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update attributes using *args (ordered) or **kwargs.

        Order for *args: id, width, height, x, y.
        """
        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the rectangle.

        Returns:
            dict: Dictionary with id, width, height, x, y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
