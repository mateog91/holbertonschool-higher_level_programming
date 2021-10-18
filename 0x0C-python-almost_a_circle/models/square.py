#!/usr/bin/python3
"""Module with Class Square"""
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Subclass Square
        Base->Rectangle->Square"""

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:
            args: cannot be keyword argument

                1st argument should be the id attribute
                2nd argument should be the size attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            kwargs: key=value pair
                key: is the name of the attribute to update
                value: the value which the attribute will be updated to
        """
        if args:
            attr_names = ["id", "size", "x", "y"]
            [setattr(self, c_attr, c_arg)
             for c_arg, c_attr in zip(args, attr_names)]
        else:
            [setattr(self, key, kwargs[key]) for key in kwargs]

    def to_dictionary(self):
        """Retrieves a dictionary representation of the instance

        Returns:
            [str]: dictionary json representation of the instance
        """
        new_keys = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in new_keys}
