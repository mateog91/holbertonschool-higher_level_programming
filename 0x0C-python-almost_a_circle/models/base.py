#!/usr/bin/python3
"""module with class Base"""


class Base:
    # creat class attribute number of objects
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
