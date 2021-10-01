#!/usr/bin/python3
"""define empty rectangle"""


class Rectangle:
    """Make a Rectangle"""

    def __init__(self, width=0, height=0):
        '''
        Initializing Rectangle

        Attributes:
        width (int): Width of rectangle
        height (int): Height of recantle
        Must be integer greater or equal than cero
        '''
        self.width = width
        self.height = height

    @property  # getter
    def width(self):
        '''getter of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property  # getter
    def height(self):
        '''getter of width'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
