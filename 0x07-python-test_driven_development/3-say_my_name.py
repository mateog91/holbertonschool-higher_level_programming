#!/usr/bin/python3
''' This module has only one function: ''say_my_name''

    Description:
    Prints first and last name
    If no last name is given, it will asume an empty string
'''


def say_my_name(first_name, last_name=""):
    ''' returns nothing
    Args:
        first_name (str): First name
        last_name (str): Last name. If no argument is given, asumes an empty string

    Description:
        Prints first and las name
        If first_name or last_name are not empty, raises a value error
    '''

    if type(first_name) is not str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
