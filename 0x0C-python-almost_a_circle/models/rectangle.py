#!/usr/bin/python3
""" Module for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    # Initialization
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing Rectangle

        Args:
            width ([int]): [width of Rectangle]
            height ([int]): [height of Rectangle]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): []. Defaults to 0.
            id ([type], optional): []. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Over riding private methods
    def __str__(self):
        string = f"[{self.__class__.__name__}]({self.id}) {self.x}/{self.y} - \
{self.width}"
        if self.__class__.__name__ == "Rectangle":
            string += f"/{self.height}"
        return string

    # Private fields

    @property  # getter
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        super().integer_validator("width", value)
        self.__width = value

    @property  # getter
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        super().integer_validator("height", value)
        self.__height = value

    @property  # getter x
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        super().integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        super().integer_validator("y", value)
        self.__y = value

    # Public Methods
    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.height

    def display(self):
        """Prints to stdout the Rectangle instance  with the char '#'"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            row_print = (" " * self.__x) + ("#" * self.width)
            print(row_print)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:
            args: cannot be keyword argument

                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            kwargs: key=value pair
                key: is the name of the attribute to update
                value: the value which the attribute will be updated to
        """
        if args:
            attr_names = ["id", "width", "height", "x", "y"]
            [setattr(self, c_attr, c_arg)
             for c_arg, c_attr in zip(args, attr_names)]
        else:
            [setattr(self, key, kwargs[key]) for key in kwargs]

    def to_dictionary(self):
        """Retrieves a dictionary representation of the instance

        Returns:
            [str]: dictionary json representation of the instance
        """
        new_keys = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in new_keys}
