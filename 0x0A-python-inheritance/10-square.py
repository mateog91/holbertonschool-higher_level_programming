#!/usr/bin/python3
"""Geometry Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Geometric figure"""

    def __init__(self, width, height):
        """
        Initializing Rectange

        Attritutes:
            width (int): width of rectangle, must be int greater than 0
            height (int): height of rectangle, must be int greater than 0
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """finds area of the geometric figure"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square:
    """subclass square"""

    def __init__(self, size):
        """initialization size of square

        Attributes:
            size (int): Square's size, must be and integer greater or equal
            than cero
        """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self, size):
        return self.__size * self.__size
