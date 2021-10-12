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
