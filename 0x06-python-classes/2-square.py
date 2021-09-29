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
        if size < 0:
            print("size must be >= 0")
            raise ValueError
        elif not isinstance(size, int):
            print("size must be an integer")
            raise TypeError
        else:
            self.__size = size
