#!/usr/bin/python3
''' Definitionb of Class'''


class Square:
    '''Class Square'''

    def __init__(self, size=0, position=(0, 0)):
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

        self.__position = position

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

    @property
    def position(self):
        '''Getter position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setter position'''
        if not (isinstance(value, tuple) or len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Calculates area of square'''
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        [print() for el in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
