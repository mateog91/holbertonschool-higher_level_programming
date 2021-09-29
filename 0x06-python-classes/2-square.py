#!/usr/bin/python3
''' Definitionb of Class'''


class Square:
    '''Class Square'''

    def __init__(self, size=0):
        '''
        Initializing  size of square

        Attributes:
            size (int): Square's size, must be and integer greater or equal
            than cero
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
