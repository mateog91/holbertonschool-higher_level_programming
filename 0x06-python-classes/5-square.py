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

    @property  # getter
    def size(self):
        '''getter of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Calculates area of square'''
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return

        for row in range(0, self.__size):
            for column in range(0, self.__size):
                print("#", end="")
            print("")
