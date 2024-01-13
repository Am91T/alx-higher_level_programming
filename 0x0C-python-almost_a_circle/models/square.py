#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square, which is a special case of a rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        if args:
            args_list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
