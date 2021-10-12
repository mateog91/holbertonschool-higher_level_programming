#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class ;
    otherwise False."""


def inherits_from(obj, a_class):
    """returns ture if is instance of a class inhereted otherwise False"""
    if issubclass(type(obj), a_class):
        if type(obj) is a_class:
            return False
        else:
            return True
