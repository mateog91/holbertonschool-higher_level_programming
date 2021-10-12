#!/usr/bin/python3
"""Geometry Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of """

    def __init__(self, size):
        """initialization size of square

        Attributes:
            size (int): Square's size, must be and integer greater or equal
            than cero
        """

        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self, size):
        return self.__size * self.__size
