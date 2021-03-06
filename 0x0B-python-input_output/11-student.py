#!/usr/bin/python3
"""Module that creates a Class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialiation of instances of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
            of a Student instance """
        if isinstance(attrs, list) and all(type(e) is list for e in attrs):
            return {e: self.e for e in attrs if hasattr(self, e)}
        else:
            return vars(self)

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
