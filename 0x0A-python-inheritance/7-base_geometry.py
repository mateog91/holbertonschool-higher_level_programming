#!/usr/bin/python3
"""Module with an empty Class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """finds area of the geometric figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
