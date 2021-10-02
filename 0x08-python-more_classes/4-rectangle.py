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

    def area(self):
        '''Calculates the area'''
        return self.__height * self.__width

    def perimeter(self):
        '''Calculates the perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")

        rows = "#" * self.__width
        drawing = ""
        for i in range(0, self.__height):
            drawing = drawing + rows
            if (i < self.__height - 1):
                drawing = drawing + "\n"

        return drawing

    def __repr__(self):
        return 'Rectangle('+str(self.__width)+', '+str(self.__height)+')'
