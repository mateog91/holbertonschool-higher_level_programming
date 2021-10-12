#!/usr/bin/python3
"""Module for Task 5
    Write a function that writes an Object to a text file,
    using a JSON representation:"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
        using a JSON representation:"""
    with open(filename, mode="w", encoding="UTF-8") as myFile:
        json.dump(my_obj, myFile)
