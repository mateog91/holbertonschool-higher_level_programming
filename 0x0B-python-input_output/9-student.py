#!/usr/bin/python3
"""Module that creates a Class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialiation of instances of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation
            of a Student instance """
        return vars(self)
